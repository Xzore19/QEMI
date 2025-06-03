from string import Template
import re
import os
import ast
import random
from qiskit_gates_generator import gate_generator
import subprocess
import sys
import numpy as np
from qiskit import QuantumCircuit
import qiskit.qasm3
from qiskit.circuit.library import XGate
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager, generate_preset_pass_manager
from code_fuzzer.dead_code_fuzzer import DeadCodeFuzzer
from code_fuzzer.result_analysis import probability_checker
from qiskit_api import generate_random_append_statement
from code_fuzzer.qasm_execution import QasmExecution

opt_passes = {"Optimize1qGates": Optimize1qGates(), "Optimize1qGatesDecomposition": Optimize1qGatesDecomposition(),
              "Collect1qRuns": Collect1qRuns(), "Collect2qBlocks": Collect2qBlocks(),
              "CollectMultiQBlocks": CollectMultiQBlocks(), "CollectLinearFunctions": CollectLinearFunctions(),
              "CollectCliffords": CollectCliffords(), "ConsolidateBlocks": ConsolidateBlocks(),
              "InverseCancellation": InverseCancellation([XGate()]),
              "CommutationAnalysis": CommutationAnalysis(), "CommutativeCancellation": CommutativeCancellation(),
              "CommutativeInverseCancellation": CommutativeInverseCancellation(),
              "Optimize1qGatesSimpleCommutation": Optimize1qGatesSimpleCommutation(),
              "RemoveDiagonalGatesBeforeMeasure": RemoveDiagonalGatesBeforeMeasure(),
              "RemoveResetInZeroState": RemoveResetInZeroState(), "RemoveFinalReset": RemoveFinalReset(),
              "HoareOptimizer": HoareOptimizer(), "TemplateOptimization": TemplateOptimization(),
              "ResetAfterMeasureSimplification": ResetAfterMeasureSimplification(),
              # "EchoRZXWeylDecomposition":EchoRZXWeylDecomposition(),
              "OptimizeCliffords": OptimizeCliffords(), "ElidePermutations": ElidePermutations(),
              "OptimizeAnnotated": OptimizeAnnotated()
              }


class QiskitGenerator:
    def __init__(self, qubit_num, measure_num=1, gate_num_upper=5, measure_times=10000, transplie=None, backend="aer",
                 use_pass=None, cond_qubit=2, structure="odi", fuzz_type="while_break"):
        self.qnum = qubit_num
        self.cnum = cond_qubit
        self.code = ""
        self.fuzzing_code = ""

        # without_exec part are for qasm
        self.code_without_exec = ""
        self.fuzzing_code_without_exec = ""

        self.qreg = "qreg"
        self.creg = "creg"
        self.qc = "qc"
        self.cond_creg = "cond_creg"
        self.gate_list = []
        self.code_structure = "odi"
        self.backend = backend
        self.measure_times = measure_times
        self.measure_qubit_num = measure_num
        self.gate_num_upper = gate_num_upper
        self.measure_index = random.sample(range(self.qnum), self.measure_qubit_num)
        self.result = random.choice(range(pow(2, len(self.measure_index))))
        self.transpile = {}
        self.use_pass = None
        self.code_structure = structure

        if self.code_structure == "odi":
            self.gate_list.append(self.gate_generation(0))
            self.gate_list.append(self.gate_generation(1))
            self.gate_list.append(self.gate_generation(1))
            self.gate_list.append(self.gate_generation(0))

        if transplie:
            self.transpile = transplie
        else:
            self.transpile_choice()

        if use_pass:
            self.use_pass = use_pass
        else:
            self.pass_choice()

        self.filename = "fuzzing/temp_test.py"
        self.fuzzing_filename = "fuzzing/fuzzing_test.py"

        self.integrate_combine(fuzz_type=fuzz_type)

    def simulator_option(self):
        # 指定使用的模拟器，默认使用的aer
        code_line = "\n"
        if self.backend == "aer":
            code_line += f"simulator = Aer.get_backend(\"aer_simulator\") \n"
        elif self.backend == "GenericBackendV2":
            # 这个模拟器好像并不支持if_test语句
            code_line += f"simulator = GenericBackendV2(num_qubits={self.qnum}, seed=1234, noise_info=False) \n"
        return code_line

    def pass_choice(self):
        # 对于pass优化未指定的情况下，随机从opt_passes中选择优化方法
        pass_list = opt_passes.keys()
        self.use_pass = random.choice(list(pass_list))

    def pass_option(self):
        # 对于指定的pass优化方法，在程序中添加对应的代码
        # 使用pass优化方法的执行，使用PassManager
        code_line = "\n"
        if isinstance(self.use_pass, list):
            code_line += "p = PassManager() \n"
            for i in self.use_pass:
                code_line += f"p.append({i}()) \n"
        elif isinstance(self.use_pass, str):
            code_line += f"p = PassManager({self.use_pass}()) \n"
        code_line += f"{self.qc} = p.run({self.qc}) \n"
        return code_line

    def transpile_choice(self):
        # 对于未指定transpile函数中的参数时，随机指定以下的参数
        optimization_level = [0, 1, 2, 3]
        routing_method = ['none', 'stochastic', 'sabre', 'default']
        layout_method = ["trivial", "dense", "noise_adaptive"]
        scheduling_method = ["asap", "alap"]
        basis_gates = []

        self.transpile["optimization_level"] = random.choice(optimization_level)
        self.transpile["routing_method"] = random.choice(routing_method)
        self.transpile["layout_method"] = random.choice(layout_method)
        # self.transpile["scheduling_method"] = random.choice(scheduling_method)
        # self.transpile["approximation_degree"] = random.choice(np.linspace(0, 1, num=100000))
        self.transpile["approximation_degree"] = 1

    def transpile_option(self):
        # 对于指定的transpile函数的参数，在qiskit程序中添加对应的参数
        code_line = "\n"

        optimization_level = self.transpile["optimization_level"]
        routing_method = self.transpile["routing_method"]
        layout_method = self.transpile["layout_method"]
        # scheduling_method = self.transpile["scheduling_method"]
        approximation_degree = self.transpile["approximation_degree"]

        # 使用的参数是 optimizatio_level, routing_method, layout_method, approximation_degree
        # code_line += f"compiled_circuit = transpile({self.qc}, backend = simulator, optimization_level = {optimization_level}, routing_method = \"{routing_method}\", layout_method = \"{layout_method}\", approximation_degree = {approximation_degree},basis_gates=[\"cx\", \"h\", \"id\", \"t\"] ) \n"

        code_line += f"compiled_circuit = transpile({self.qc}, backend = simulator, optimization_level = {optimization_level}, routing_method = \"{routing_method}\", layout_method = \"{layout_method}\", approximation_degree = {approximation_degree}) \n"
        return code_line

    def integrate_combine(self, fuzz_type):
        # basic information of quantum program for qiskit
        # 添加基本的import函数
        self.code += self.write_import()
        self.code_without_exec += self.write_import()
        self.fuzzing_code += self.write_import()
        self.fuzzing_code_without_exec += self.write_import()

        # 添加基本的QuantumCircuit， QuantumRegister， ClassicalRegister的声明语句
        self.code += self.basic_set()
        self.code_without_exec += self.basic_set()
        self.fuzzing_code += self.basic_set()
        self.fuzzing_code_without_exec += self.basic_set()

        # 添加声明后的第一组量子门操作
        self.code += self.gate_list[0]
        self.code_without_exec += self.gate_list[0]
        self.fuzzing_code += self.gate_list[0]
        self.fuzzing_code_without_exec += self.gate_list[0]

        ###################################### fuzzing areas #############################################
        if fuzz_type == "for_break":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            gate_list = self.gate_generation(1)
            dead_list = self.gate_generation(1)
            dead_code, unfuzz = dcf.dynamic_for_break(qc=self.qc, gate_list=gate_list, dead_list=dead_list)
            self.code += unfuzz
            self.code_without_exec += unfuzz

            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "for_continue":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            gate_list = self.gate_generation(1)
            dead_list = self.gate_generation(1)
            dead_code, unfuzz = dcf.dynamic_for_continue(qc=self.qc, gate_list=gate_list, dead_list=dead_list)
            self.code += unfuzz
            self.code_without_exec += unfuzz

            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "for_zero":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            gate_list = self.gate_generation(1)
            dead_code, unfuzz = dcf.dynamic_for_zero(qc=self.qc, gate_list=gate_list)
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "while_dead":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            while_gate = self.gate_generation(indent=1)
            dead_code, unfuzz = dcf.while_dead(qc=self.qc, qreg=self.qreg, cond_reg=self.cond_creg, qnum=self.qnum, gate_list=while_gate)

            self.code += unfuzz
            self.code_without_exec += unfuzz
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "while_break":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)

            while_gate = self.gate_generation(indent=1)
            while_gate2 = self.gate_generation(indent=1)
            dead_code, unfuzz = dcf.while_break(qc=self.qc, qreg=self.qreg, cond_reg=self.cond_creg, qnum=self.qnum, gate_list=while_gate, dead_list=while_gate2)

            self.code += unfuzz
            self.code_without_exec += unfuzz
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code


        elif fuzz_type == "if_test_dead":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            if_gate = self.gate_generation(indent=1)
            dead_code, unfuzz = dcf.if_test_dead(qc=self.qc, qreg=self.qreg, qnum=self.qnum, cond_reg=self.cond_creg, gate_list=if_gate)

            self.code += unfuzz
            self.code_without_exec += unfuzz
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "if_test_else":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            if_gate = self.gate_generation(indent=1)
            else_gate = self.gate_generation(indent=1)
            dead_code, unfuzz = dcf.if_test_else(qc=self.qc, qreg=self.qreg, qnum=self.qnum, cond_reg=self.cond_creg, gate_list=if_gate, dead_list=else_gate)

            self.code += unfuzz
            self.code_without_exec += unfuzz
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "switch_dead":
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            gate_list = self.gate_generation(indent=2)
            dead_list = self.gate_generation(indent=2)

            dead_code, unfuzz = dcf.switch_dead(qc=self.qc, gate_list=gate_list, dead_list=dead_list)
            self.code += unfuzz
            self.code_without_exec += unfuzz
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "nest":
            dc_list = ["fb", "fz", "fc", "wd", "wb", "itd", "ite", "sd"]
            dc_indent = {"sd":2}
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)

            dc1 = random.choice(dc_list)
            dc2 = random.choice(dc_list)
            dc3 = random.choice(dc_list)

            dc1i, dc2i, dc3i = dc_indent.get(dc1, 1), dc_indent.get(dc2, 1), dc_indent.get(dc3, 1)


            dc2_gate1 = self.gate_generation(dc2i)
            dc2_gate2 = self.gate_generation(dc2i)
            temp1, temp2 = self.dcf_code(dc=dc2, dcf=dcf, gate_list=dc2_gate1, dead_list=dc2_gate2)
            dc2_code, dc2_unfuzz = self.code_indent(indent=dc1i, code1=temp1, code2=temp2)
            del(dcf)

            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            dc3_gate1 = self.gate_generation(dc3i)
            dc3_gate2 = self.gate_generation(dc3i)
            temp1, temp2 = self.dcf_code(dc=dc3, dcf=dcf, gate_list=dc3_gate1, dead_list=dc3_gate2)
            dc3_code, dc3_unfuzz = self.code_indent(indent=dc1i, code1=temp1, code2=temp2)

            dead_code, unfuzz = self.dcf_code(dc=dc1, dcf=dcf, gate_list= dc2_code, dead_list=dc3_code)

            self.code += unfuzz
            self.code_without_exec += unfuzz
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        elif fuzz_type == "nest_dead":
            dc_list = ["fb", "fz", "fc", "wd", "wb", "itd", "ite","sd"]
            dc_indent = {"sd": 2}
            dcf = DeadCodeFuzzer(qubit_num=self.cnum)

            dc1 = random.choice(dc_list)
            dc2 = random.choice(dc_list)
            dc3 = random.choice(dc_list)
            dc1i, dc2i, dc3i = dc_indent.get(dc1, 1), dc_indent.get(dc2, 1), dc_indent.get(dc3, 1)

            dc2_gate1 = self.gate_generation(dc2i)
            dc2_gate2 = self.gate_generation(dc2i)
            temp1, temp2 = self.dcf_code(dc=dc2, dcf=dcf, gate_list=dc2_gate1, dead_list=dc2_gate2)
            dc2_code, dc2_unfuzz = self.code_indent(indent=dc1i, code1=temp1, code2=temp2)
            del (dcf)

            dcf = DeadCodeFuzzer(qubit_num=self.cnum)
            dc3_gate1 = self.gate_generation(dc3i)
            dc3_gate2 = self.gate_generation(dc3i)
            temp1, temp2 = self.dcf_code(dc=dc3, dcf=dcf, gate_list=dc3_gate1, dead_list=dc3_gate2)
            dc3_code, dc3_unfuzz = self.code_indent(indent=dc1i, code1=temp1, code2=temp2)
            dead_code, _ = self.dcf_code(dc=dc1, dcf=dcf, gate_list=dc2_code, dead_list=dc3_code)
            # del dcf
            _, unfuzz = self.dcf_code(dc=dc1, dcf=dcf, gate_list=dc2_unfuzz, dead_list=dc3_unfuzz)

            self.code += unfuzz
            self.code_without_exec += unfuzz
            self.fuzzing_code += dead_code
            self.fuzzing_code_without_exec += dead_code

        ##################################################################################################

        # 添加后续的量子门操作
        self.code += self.gate_list[3]
        self.code_without_exec += self.gate_list[3]
        self.fuzzing_code += self.gate_list[3]
        self.fuzzing_code_without_exec += self.gate_list[3]

        # 添加 measure 语句
        for i in range(self.qnum):
            self.code += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"
            self.code_without_exec += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"

        for i in range(self.qnum):
            self.fuzzing_code += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"
            self.fuzzing_code_without_exec += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"

        framework = """
qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})
"""
        self.code += framework
        self.code_without_exec += framework
        self.fuzzing_code += framework
        self.fuzzing_code_without_exec += framework

        # 为 code 和fuzzing code添加模拟器，对于qasm则不需要
        self.code += self.final_part(show_type="simulator")
        self.fuzzing_code += self.final_part(show_type="simulator")

    def code_indent(self, indent, code1, code2):
        new1, new2 = "", ""
        for line in code1.split("\n"):
            new1 += "\t"*indent + line + "\n"

        for line in code2.split("\n"):
            new2 += "\t"*indent + line + "\n"

        return new1, new2

    def dcf_code(self, dc, dcf, gate_list, dead_list):
        if dc == "fb":
            code, unfuzz = dcf.dynamic_for_break(qc=self.qc, gate_list=gate_list, dead_list=dead_list)
        elif dc == "fz":
            code, unfuzz = dcf.dynamic_for_zero(qc=self.qc, gate_list=gate_list)
        elif dc == "fc":
            code, unfuzz = dcf.dynamic_for_continue(qc=self.qc, gate_list=gate_list, dead_list=dead_list)
        elif dc == "ite":
            code, unfuzz = dcf.if_test_else(qc=self.qc, qreg=self.qreg, qnum=self.qnum, cond_reg=self.cond_creg, gate_list=gate_list, dead_list=dead_list)
        elif dc == "wd":
            code, unfuzz = dcf.while_dead(qc=self.qc, qreg=self.qreg, cond_reg=self.cond_creg, qnum=self.qnum, gate_list=gate_list)
        elif dc == "wb":
            code, unfuzz = dcf.while_break(qc=self.qc, qreg=self.qreg, cond_reg=self.cond_creg, qnum=self.qnum, gate_list=gate_list, dead_list=dead_list)
        elif dc == "itd":
            code, unfuzz = dcf.if_test_dead(qc=self.qc, qreg=self.qreg, qnum=self.qnum, cond_reg=self.cond_creg, gate_list=gate_list)
        elif dc == "sd":
            code, unfuzz = dcf.switch_dead(qc=self.qc, gate_list=gate_list, dead_list=dead_list)
        else:
            code = "pass \n"
            unfuzz = code
        return code, unfuzz

    def write_import(self):
        # 最基本的import语句
        code_line = ""
        code_line += "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, AncillaRegister \n"
        code_line += "from qiskit_aer import Aer \n"
        code_line += "from qiskit.providers.fake_provider import GenericBackendV2 \n"
        code_line += "from qiskit.providers.fake_provider import GenericBackendV2 \n"
        code_line += "from qiskit.circuit import Parameter, ParameterVector \n"
        code_line += "from qiskit.circuit.library import XGate \n"
        code_line += "from qiskit.transpiler.passes import * \n"
        code_line += "from qiskit.circuit.library import * \n"
        code_line += "from qiskit.transpiler import PassManager, generate_preset_pass_manager \n"
        # code_line += "from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator \n"
        # code_line += "from pathlib import Path \n"
        code_line += "from math import pi \n"
        code_line += "import numpy as np \n"
        code_line += "np.random.seed(42) \n"
        code_line += "\n"
        return code_line

    def basic_set(self):
        # 声明QuantumCircuit， QuantumRegister， ClassicalRegister语句
        code_line = ""
        code_line += f"{self.qreg} = QuantumRegister({self.qnum}) \n"
        code_line += f"{self.creg} = ClassicalRegister({self.qnum}) \n"
        code_line += f"{self.qc} = QuantumCircuit({self.qreg}, {self.creg}) \n"
        # q_mindx = ",".join([f"{self.qreg}[{i}]" for i in self.measure_index])
        # c_mindx = ",".join([f"{self.creg}[{i}]" for i in self.measure_index])
        # code_line += f"({q_mindx}) = {self.qreg} \n"
        # code_line += f"({c_mindx}) = {self.creg} \n"
        code_line += "\n"
        return code_line

    def gate_generation(self, indent):
        # 随机量子门操作的构建
        gate_code = ""
        for i in range(self.gate_num_upper):
            flag = random.uniform(0.8, 1)
            if flag > 0.75:
                gate_code += "\t" * indent + gate_generator(qubits_num=self.qnum, cir_name=self.qc) + "\n"
            else:
                qc, code = generate_random_append_statement(max_qubits=self.qnum, qc_var=self.qc, qr_var=self.qreg)
                code_frag = code.split("\n")
                for cf in code_frag:
                    gate_code += "\t" * indent + cf + "\n"
        return gate_code

    def final_part(self, show_type):
        # QuantumCircuit构建后的实验结果
        # 提供生成matplotlib生成电路图，和模拟器调用执行的代码
        code_line = "\n"
        if show_type == "draw":
            circuit_draw = "mpl"
            code_line += "import matplotlib as plt \n"
            code_line += f"{self.qc}.draw(\"{circuit_draw}\") \n"
            code_line += "plt.pyplot.show() \n"
        elif show_type == "simulator":
            code_line += self.simulator_option()
            code_line += self.pass_option()
            code_line += self.transpile_option()

            ############################## decompose ########################################
            framework = """
qc = qc.decompose(reps=10)\n
"""
            code_line += framework

            #################################################################################
            code_line += f"job = simulator.run(compiled_circuit, shots={self.measure_times}) \n"
            code_line += f"result = job.result().get_counts() \n"
            code_line += f"print(result)"
            code_line += "\n"
        return code_line

    def run(self):
        # 运行原始ground truth程序，和经过dead code fuzzing的程序
        with open(self.filename, "w") as file:
            file.write(self.code)

        with open(self.fuzzing_filename, "w") as file:
            file.write(self.fuzzing_code)

        try:
            truth_result = subprocess.run([sys.executable, self.filename], capture_output=True, text=True, timeout=600)
        except subprocess.TimeoutExpired:
            print("truth timeout")
            directory = "fuzzing/buggy_program/timeout"
            pattern = re.compile(r"(truth|fuzzing)_(\d+)\.py")
            max_index = -1

            for f in os.listdir(directory):
                match = pattern.fullmatch(f)
                if match:
                    index = int(match.group(2))
                    if index > max_index:
                        max_index = index

            next_index = max_index + 1
            truth_file = os.path.join(directory, f"truth_{next_index}.py")
            fuzzing_file = os.path.join(directory, f"fuzzing_{next_index}.py")

            with open(truth_file, "w") as file:
                file.write(self.code)

            with open(fuzzing_file, "w") as file_f:
                file_f.write(self.fuzzing_code)

            return None

        try:
            fuzzing_result = subprocess.run([sys.executable, self.fuzzing_filename], capture_output=True, text=True, timeout=600)
        except subprocess.TimeoutExpired:
            print("fuzzing timeout")
            directory = "fuzzing/buggy_program/timeout"
            pattern = re.compile(r"(truth|fuzzing)_(\d+)\.py")
            max_index = -1

            for f in os.listdir(directory):
                match = pattern.fullmatch(f)
                if match:
                    index = int(match.group(2))
                    if index > max_index:
                        max_index = index

            next_index = max_index + 1
            truth_file = os.path.join(directory, f"truth_{next_index}.py")
            fuzzing_file = os.path.join(directory, f"fuzzing_{next_index}.py")

            with open(truth_file, "w") as file:
                file.write(self.code)

            with open(fuzzing_file, "w") as file_f:
                file_f.write(self.fuzzing_code)

            return None

        if (truth_result.stderr == "" and fuzzing_result.stderr != "") or (
                truth_result.stderr != "" and fuzzing_result.stderr == ""):
            print("Found crash!!!")
            directory = "fuzzing/buggy_program/crash"


            pattern = re.compile(r"(truth|fuzzing)_(\d+)\.py")
            max_index = -1

            for f in os.listdir(directory):
                match = pattern.fullmatch(f)
                if match:
                    index = int(match.group(2))
                    if index > max_index:
                        max_index = index

            next_index = max_index + 1
            truth_file = os.path.join(directory, f"truth_{next_index}.py")
            fuzzing_file = os.path.join(directory, f"fuzzing_{next_index}.py")

            with open(truth_file, "w") as file:
                file.write(self.code)

            with open(fuzzing_file, "w") as file_f:
                file_f.write(self.fuzzing_code)
        elif (truth_result.stderr != "" and fuzzing_result.stderr != ""):
            pass

        elif not probability_checker(eval(truth_result.stdout), eval(fuzzing_result.stdout), shot=self.measure_times,
                                     qnum=self.qnum):
            print("Found wrong!!!")
            directory = "fuzzing/buggy_program/probability"

            pattern = re.compile(r"(truth|fuzzing)_(\d+)\.py")
            max_index = -1

            for f in os.listdir(directory):
                match = pattern.fullmatch(f)
                if match:
                    index = int(match.group(2))
                    if index > max_index:
                        max_index = index

            next_index = max_index + 1
            truth_file = os.path.join(directory, f"truth_{next_index}.py")
            fuzzing_file = os.path.join(directory, f"fuzzing_{next_index}.py")

            with open(truth_file, "w") as file:
                file.write(self.code)

            with open(fuzzing_file, "w") as file_f:
                file_f.write(self.fuzzing_code)

    def extract_qc_from_code(self, qiskit_code):
        tree = ast.parse(qiskit_code)
        namespace = {}
        exec(compile(tree, filename="<ast>", mode="exec"), namespace)
        for var in namespace.values():
            if isinstance(var, QuantumCircuit):
                return var
        return None

    def qasm_convertor(self):
        # 解析 Qiskit 代码并获取 QuantumCircuit
        qc = self.extract_qc_from_code(self.code_without_exec)
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(self.code_without_exec)

        if qc:
            # 转换为 OpenQASM 3.0
            qasm_code = qiskit.qasm3.dumps(qc)
        else:
            raise Exception("QuantumCircuit Objects not exist")

        qasm_file = "qasm_code/code.qasm3"
        with open(qasm_file, "w") as file:
            file.write(qasm_code)
        # print(qasm_code)

        fuzzing_qc = self.extract_qc_from_code(self.fuzzing_code_without_exec)

        if fuzzing_qc:
            # 转换为 OpenQASM 3.0
            fuzzing_qasm_code = qiskit.qasm3.dumps(fuzzing_qc)
        else:
            raise Exception("Fuzzing QuantumCircuit Objects not exist")

        fuzzing_qasm_file = "qasm_code/fuzzing_code.qasm3"
        with open(fuzzing_qasm_file, "w") as fuzzing_file:
            fuzzing_file.write(fuzzing_qasm_code)

    def qasm_run(self):
        try:
            truth_result = QasmExecution(file="qasm_code/code.qasm3").qiskit_simulator()
            except1 = None
        except Exception as e1:
            truth_result = ""
            except1 = e1
            print(f"truth crash:{e1}")

        try:
            fuzzing_result = QasmExecution(file="qasm_code/fuzzing_code.qasm3").qiskit_simulator()
            except2 = None
        except Exception as e2:
            fuzzing_result = ""
            except2 = e2
            print(f"fuzzing crash:{e2}")

        print("+++++++++++++ truth:", truth_result)
        print("------------- fuzzing:", fuzzing_result)



        if (except1 == None and except2 != None) or (except1 != None and except2 == ""):
            print("Found crash!!!")
            directory = "qasm_code/buggy_program/crash"


            pattern = re.compile(r"(truth|fuzzing)_(\d+)\.py")
            max_index = -1

            for f in os.listdir(directory):
                match = pattern.fullmatch(f)
                if match:
                    index = int(match.group(2))
                    if index > max_index:
                        max_index = index

            next_index = max_index + 1
            truth_file = os.path.join(directory, f"truth_{next_index}.py")
            fuzzing_file = os.path.join(directory, f"fuzzing_{next_index}.py")

            with open(truth_file, "w") as file:
                file.write(self.code)

            with open(fuzzing_file, "w") as file_f:
                file_f.write(self.fuzzing_code)

        elif (except1 != None and except2 != None):
            pass

        elif not probability_checker(eval(truth_result), eval(fuzzing_result), shot=self.measure_times,
                                     qnum=self.qnum):
            print("Found wrong!!!")
            directory = "qasm_code/buggy_program/probability"

            pattern = re.compile(r"(truth|fuzzing)_(\d+)\.py")
            max_index = -1

            for f in os.listdir(directory):
                match = pattern.fullmatch(f)
                if match:
                    index = int(match.group(2))
                    if index > max_index:
                        max_index = index

            next_index = max_index + 1
            truth_file = os.path.join(directory, f"truth_{next_index}.py")
            fuzzing_file = os.path.join(directory, f"fuzzing_{next_index}.py")

            with open(truth_file, "w") as file:
                file.write(self.code)

            with open(fuzzing_file, "w") as file_f:
                file_f.write(self.fuzzing_code)

    def check_code(self):
        # 检查truth代码和fuzzing代码
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(self.code)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(self.fuzzing_code)


if __name__ == "__main__":
    a = QiskitGenerator(5, 1, fuzz_type="if_test_else")
    a.qasm_convertor()
    # a.check_code()
    # a.run()
