from string import Template
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

opt_passes = {  "Optimize1qGates": Optimize1qGates(), "Optimize1qGatesDecomposition":Optimize1qGatesDecomposition(),
                "Collect1qRuns": Collect1qRuns(), "Collect2qBlocks": Collect2qBlocks(),
                "CollectMultiQBlocks":CollectMultiQBlocks(),"CollectLinearFunctions":CollectLinearFunctions(),
                "CollectCliffords":CollectCliffords(),"ConsolidateBlocks":ConsolidateBlocks(),
                "InverseCancellation":InverseCancellation([XGate()]),
                "CommutationAnalysis":CommutationAnalysis(),"CommutativeCancellation":CommutativeCancellation(),
                "CommutativeInverseCancellation":CommutativeInverseCancellation(),
                "Optimize1qGatesSimpleCommutation":Optimize1qGatesSimpleCommutation(),
                "RemoveDiagonalGatesBeforeMeasure":RemoveDiagonalGatesBeforeMeasure(),
                "RemoveResetInZeroState":RemoveResetInZeroState(),"RemoveFinalReset":RemoveFinalReset(),
                "HoareOptimizer":HoareOptimizer(),"TemplateOptimization":TemplateOptimization(),
                "ResetAfterMeasureSimplification":ResetAfterMeasureSimplification(), #"EchoRZXWeylDecomposition":EchoRZXWeylDecomposition(),
                "OptimizeCliffords":OptimizeCliffords(),"ElidePermutations":ElidePermutations(),
                "OptimizeAnnotated":OptimizeAnnotated()
            }

class QiskitGenerator:
    def __init__(self, qubit_num, measure_num = 1, gate_num_upper = 5, measure_times = 10000, transplie = None, backend = "aer", use_pass = None, cond_qubit = 2):
        self.qnum = qubit_num
        self.cnum = cond_qubit
        self.code = ""
        self.fuzzing_code = ""
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


        self.combine()
        self.fuzzing_combine()

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
        routing_method = ['basic', 'lookahead', 'sabre']
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
        code_line += f"compiled_circuit = transpile({self.qc}, backend = simulator, optimization_level = {optimization_level}, routing_method = \"{routing_method}\", layout_method = \"{layout_method}\", approximation_degree = {approximation_degree} ) \n"
        return code_line


    def combine(self):
        # 未fuzzing的程序生成

        # 添加基本的import函数
        self.code += self.write_import()
        self.code_without_exec += self.write_import()

        # 添加基本的QuantumCircuit， QuantumRegister， ClassicalRegister的声明语句
        self.code += self.basic_set()
        self.code_without_exec += self.basic_set()

        # 添加声明后的第一组量子门操作
        self.code += self.gate_list[0]
        self.code_without_exec += self.gate_list[0]

        # 添加最基本的dynamic circuit的逻辑语句
        self.code += self.only_dynamic_if()
        self.code_without_exec += self.only_dynamic_if()

        # 添加if_test语句结束后的量子门操作
        self.code += self.gate_list[3]
        self.code_without_exec += self.gate_list[3]

        # 添加实现优化和模拟器调用的代码
        for i in range(self.qnum):
            self.code += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"
            self.code_without_exec += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"
        self.code += self.final_part(show_type="simulator")

    def fuzzing_combine(self):
        dcf = DeadCodeFuzzer(qubit_num=self.cnum)
        self.fuzzing_code += self.write_import()
        self.fuzzing_code += self.basic_set()
        self.fuzzing_code += self.gate_list[0]

        # 在if_test语句前添加dead code进行fuzzing
        self.fuzzing_code += dcf.classical_dead()
        oracle, deadcode, deadqc= dcf.quantum_dead()
        self.fuzzing_code += deadcode
        self.fuzzing_code += f"{self.qc}.compose({deadqc}, inplace = True, qubits = {[self.qnum+i for i in range(self.cnum)]}) \n"
        # self.fuzzing_code += dcf.if_test_dead(oracle = oracle, qc=self.qc, qreg=self.qreg,
        #                                       cond_reg=self.cond_creg, qnum=self.qnum, cnum=self.cnum)

        while_gate = self.gate_generation(indent=1)
        self.fuzzing_code += dcf.while_dead(oracle = oracle, qc=self.qc, qreg=self.qreg,
                                              cond_reg=self.cond_creg, qnum=self.qnum, cnum=self.cnum, gate_list=while_gate)

        self.fuzzing_code += self.only_dynamic_if()
        self.fuzzing_code += self.gate_list[3]
        for i in range(self.qnum):
            self.fuzzing_code += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"
        self.fuzzing_code += self.final_part(show_type="simulator")

        self.fuzzing_code_without_exec += self.write_import()
        self.fuzzing_code_without_exec += self.basic_set()
        self.fuzzing_code_without_exec += self.gate_list[0]

        # 在if_test语句前添加dead code进行fuzzing
        self.fuzzing_code_without_exec += dcf.classical_dead()
        oracle, deadcode, deadqc= dcf.quantum_dead()
        self.fuzzing_code_without_exec += deadcode
        self.fuzzing_code_without_exec += f"{self.qc}.compose({deadqc}, inplace = True, qubits = {[self.qnum+i for i in range(self.cnum)]}) \n"
        # if dead
        # self.fuzzing_code_without_exec += dcf.if_test_dead(oracle = oracle, qc=self.qc, qreg=self.qreg,
        #                                       cond_reg=self.cond_creg, qnum=self.qnum, cnum=self.cnum)

        # while dead
        while_gate = self.gate_generation(indent=1)
        self.fuzzing_code_without_exec += dcf.while_dead(oracle=oracle, qc=self.qc, qreg=self.qreg,
                                            cond_reg=self.cond_creg, qnum=self.qnum, cnum=self.cnum,
                                            gate_list=while_gate)

        self.fuzzing_code_without_exec += self.only_dynamic_if()
        self.fuzzing_code_without_exec += self.gate_list[3]
        for i in range(self.qnum):
            self.fuzzing_code_without_exec += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}]) \n"


    def only_dynamic_if(self):
        # 最基本的dynamic circuit
        # 只使用if_test执行的单次控制流嵌套
        code_line = ""
        # for i in self.measure_index:
        #     code_line += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}])\n"
        # code_line += f"with {self.qc}.if_test(({self.creg}{self.measure_index}, 0b{self.result})) as else_1: \n"
        # code_line += self.gate_list[1]
        # code_line += f"with else_1: \n"
        # code_line += self.gate_list[2]
        # code_line += "\n"
        return code_line


    def write_import(self):
        # 最基本的import语句
        code_line = ""
        code_line += "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile \n"
        code_line += "from qiskit_aer import Aer \n"
        code_line += "from qiskit.providers.fake_provider import GenericBackendV2 \n"
        code_line += "from qiskit.providers.fake_provider import GenericBackendV2 \n"
        code_line += "from qiskit.circuit import Parameter, ParameterVector \n"
        code_line += "from qiskit.circuit.library import XGate \n"
        code_line += "from qiskit.transpiler.passes import * \n"
        code_line += "import z3 \n"
        code_line += "from qiskit.transpiler import PassManager, generate_preset_pass_manager \n"
        # code_line += "from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator \n"
        # code_line += "from pathlib import Path \n"
        code_line += "from math import pi \n"
        code_line += "\n"
        return code_line

    def basic_set(self):
        # 声明QuantumCircuit， QuantumRegister， ClassicalRegister语句
        code_line = ""
        code_line += f"{self.qreg} = QuantumRegister({self.qnum + self.cnum}) \n"
        code_line += f"{self.creg} = ClassicalRegister({self.qnum}) \n"
        code_line += f"{self.cond_creg} = ClassicalRegister({self.cnum}) \n"
        code_line += f"{self.qc} = QuantumCircuit({self.qreg}, {self.creg}, {self.cond_creg}) \n"
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
            gate_code += "\t"* indent + gate_generator(qubits_num=self.qnum, cir_name=self.qc) + "\n"
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
            code_line += f"job = simulator.run(compiled_circuit, shots={self.measure_times}) \n"
            code_line += f"result = job.result().get_counts() \n"
            code_line += f"print(result)"
            code_line += "\n"
        return code_line

    def run(self):
        # 运行原始ground truth程序，和经过dead code fuzzing的程序
        with open(self.filename, "w") as file:
            file.write(self.code)

        truth_result = subprocess.run([sys.executable, self.filename], capture_output=True, text=True)
        # truth_result = subprocess.Popen([sys.executable, self.filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        #                                 text=True)

        with open(self.fuzzing_filename, "w") as file:
            file.write(self.fuzzing_code)

        fuzzing_result = subprocess.run([sys.executable, self.fuzzing_filename], capture_output=True, text=True)

        # print("truth_result:", truth_result.stdout)
        # print(truth_result.stderr == "")
        # print("fuzzing_result:", fuzzing_result.stdout)
        # print(fuzzing_result.stderr == "")

        if (truth_result.stderr == "" and fuzzing_result.stderr != "") or (truth_result.stderr != "" and fuzzing_result.stderr == ""):
            print("Found crash!!!")
            directory = "fuzzing/buggy_program/crash"

            files = sorted(f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)))

            if files:
                pre, post = files[-1][:-3].split("_")
                truth_file = directory + f"/truth_{str(int(post)+1)}.py"
                fuzzing_file = directory + f"/fuzzing_{str(int(post) + 1)}.py"
            else:
                truth_file = directory + "/truth_0.py"
                fuzzing_file = directory + "/fuzzing_0.py"

            with open(truth_file, "w") as file:
                file.write(self.code)

            with open(fuzzing_file, "w") as file_f:
                file_f.write(self.fuzzing_code)
        elif (truth_result.stderr != "" and fuzzing_result.stderr != ""):
            pass

        elif not probability_checker(eval(truth_result.stdout), eval(fuzzing_result.stdout), shot=self.measure_times, qnum=self.qnum):
            print("Found wrong!!!")
            directory = "fuzzing/buggy_program/probability"

            files = sorted(f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)))

            if files:
                pre, post = files[-1][:-3].split("_")
                truth_file = directory + f"/truth_{str(int(post) + 1)}.py"
                fuzzing_file = directory + f"/fuzzing_{str(int(post) + 1)}.py"
            else:
                truth_file = directory + "/truth_0.py"
                fuzzing_file = directory + "/fuzzing_0.py"

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

        if qc:
            # 转换为 OpenQASM 3.0
            qasm_code = qiskit.qasm3.dumps(qc)
        else:
            raise Exception("QuantumCircuit Objects not exist")

        qasm_file = "qasm_code/code.qasm3"
        with open(qasm_file, "w") as file:
            file.write(qasm_code)

        fuzzing_qc = self.extract_qc_from_code(self.fuzzing_code_without_exec)

        if fuzzing_qc:
            # 转换为 OpenQASM 3.0
            fuzzing_qasm_code = qiskit.qasm3.dumps(fuzzing_qc)
        else:
            raise Exception("Fuzzing QuantumCircuit Objects not exist")

        fuzzing_qasm_file = "qasm_code/fuzzing_code.qasm3"
        with open(fuzzing_qasm_file, "w") as fuzzing_file:
            fuzzing_file.write(fuzzing_qasm_code)




    def check_code(self):
        # 检查truth代码和fuzzing代码
        print(self.fuzzing_code_without_exec)

if __name__ == "__main__":
    a = QiskitGenerator(5,1)
    # a.check_code()
    a.run()