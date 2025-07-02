from string import Template
import re
import os
import ast
import random
from cirq_gates_generator import gate_generator
import subprocess
import sys
from code_fuzzer.result_analysis import cirq_probability_checker, remove_cr
from qiskit_api import generate_random_append_statement
from code_fuzzer.qasm_execution import QasmExecution
import uuid

opt_passes = """
circuit = transformers.drop_empty_moments(circuit)
circuit = transformers.defer_measurements(circuit)
circuit = transformers.expand_composite(circuit)
circuit = transformers.merge_single_qubit_gates_to_phxz(circuit)
circuit = transformers.stratified_circuit(circuit)
circuit = transformers.eject_phased_paulis(circuit)
circuit = transformers.drop_negligible_operations(circuit)
circuit = transformers.eject_z(circuit)
circuit = transformers.optimize_for_target_gateset(circuit)
"""


class CirqGenerator:
    def __init__(self, qubit_num, measure_num=1, gate_num_upper=5, measure_times=10000, transplie=None, backend="aer",
                 use_pass=None, cond_qubit=2, structure="odi", fuzz_type="while_break"):
        self.qnum = qubit_num
        self.cnum = cond_qubit
        self.code = ""
        self.fuzzing_code = ""

        # without_exec part are for qasm
        self.code_without_exec = ""
        self.fuzzing_code_without_exec = ""

        self.qreg = "q"
        self.creg = "creg"
        self.qc = "circuit"
        self.cond_creg = "cond_creg"
        self.gate_list = []
        self.code_structure = "odi"
        self.backend = backend
        self.max_measure_times = measure_times
        self.measure_times = 500
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

        # if transplie:
        #     self.transpile = transplie
        # else:
        #     self.transpile_choice()
        #
        # if use_pass:
        #     self.use_pass = use_pass
        # else:
        #     self.pass_choice()

        self.filename = "fuzzing_cirq/temp_test.py"
        self.fuzzing_filename = "fuzzing_cirq/fuzzing_test.py"

        self.integrate_combine(fuzz_type=fuzz_type)


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

        # dead code generation
        self.code += f"sub_circuit = cirq.Circuit() \n"
        self.fuzzing_code += f"sub_circuit = cirq.Circuit() \n"
        for sub in range(5):
            self.fuzzing_code += gate_generator(qubits_num=self.qnum, cir_name="sub_circuit") + "\n"

        self.fuzzing_code += f"sub_op = cirq.CircuitOperation(sub_circuit.freeze()) \n"

        self.code += f"{self.qc}.append(cirq.measure({self.qreg}[{self.qnum}], key=\"c\")) \n"
        self.fuzzing_code += f"{self.qc}.append(cirq.measure({self.qreg}[{self.qnum}], key=\"c\")) \n"

        self.fuzzing_code += f"{self.qc}.append(sub_op.with_classical_controls(\"c\")) \n"

        # 添加后续的量子门操作
        self.code += self.gate_list[3]
        self.code_without_exec += self.gate_list[3]
        self.fuzzing_code += self.gate_list[3]
        self.fuzzing_code_without_exec += self.gate_list[3]

        # 添加 measure 语句
        self.code += f"{self.qc}.append(cirq.measure({self.qreg}, key=\"m\")) \n"
        self.code_without_exec += f"{self.qc}.append(cirq.measure({self.qreg}, key=\"m\")) \n"

        self.fuzzing_code += f"{self.qc}.append(cirq.measure({self.qreg}, key=\"m\")) \n"
        self.fuzzing_code_without_exec += f"{self.qc}.append(cirq.measure({self.qreg}, key=\"m\")) \n"

        self.code += opt_passes
        self.fuzzing_code += opt_passes

        # 为 code 和fuzzing code添加模拟器，对于qasm则不需要
        self.code += self.final_part(show_type="simulator")
        self.fuzzing_code += self.final_part(show_type="simulator")


    def write_import(self):
        # 最基本的import语句
        code_line = ""
        code_line += "import cirq\n"
        code_line += "from cirq import transformers\n"
        code_line += "\n"
        return code_line

    def basic_set(self):
        # 声明QuantumCircuit， QuantumRegister， ClassicalRegister语句
        code_line = ""
        code_line += f"{self.qreg} = cirq.LineQubit.range({self.qnum+1}) \n"
        code_line += f"{self.qc} = cirq.Circuit()\n"
        # code_line += f"{self.cond_creg} = cirq.LineQubit.range(1) \n"
        code_line += "\n"
        return code_line

    def gate_generation(self, indent):
        # 随机量子门操作的构建
        gate_code = ""
        for i in range(self.gate_num_upper):
            flag = random.uniform(0.5, 1)
            if flag > 0.5:
                gate_code += "\t" * indent + gate_generator(qubits_num=self.qnum, cir_name=self.qc) + "\n"
        return gate_code

    def final_part(self, show_type):
        # QuantumCircuit构建后的实验结果
        # 提供生成matplotlib生成电路图，和模拟器调用执行的代码
        code_line = "\n"
        if show_type == "draw":
            code_line += f"print({self.qc}) \n"
        elif show_type == "simulator":
            code_line += "simulator = cirq.Simulator() \n"
            code_line += f"result = simulator.run({self.qc}, repetitions={self.measure_times}) \n"
            code_line += "print(result.histogram(key='m'))"
        return code_line

    def output_postprocess(self, dis):
        dis = dis.replace("Counter(", "").replace(")", "").replace("\x1b[0m", "")
        check_list = [f'{num:0{self.qnum}b}' for num in range(pow(2, self.qnum))]
        target = remove_cr(eval(dis), self.qnum)
        dict_target = {}
        for i in check_list:
            dict_target[i] = target.get(i, 0)
        return dict_target

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

        tr_stdout = truth_result.stdout.replace("Counter(", "").replace(")", "").replace("\x1b[0m", "")
        fz_stdout = fuzzing_result.stdout.replace("Counter(", "").replace(")", "").replace("\x1b[0m", "")


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

        # 通过对hellinger距离进行判断，对于超过0.1的样本进行异常的储存
        elif not cirq_probability_checker(eval(tr_stdout), eval(fz_stdout), shot=self.measure_times,
                                     qnum=self.qnum):
            max_measure = 0
            truth_rst = self.output_postprocess(truth_result.stdout)
            fuzzing_rst = self.output_postprocess(fuzzing_result.stdout)
            total_measure = self.measure_times
            while max_measure < self.max_measure_times:
                max_measure += self.measure_times
                if not cirq_probability_checker(truth_rst, fuzzing_rst, shot=total_measure, qnum=self.qnum):
                    break

                temp_truth_result = subprocess.run([sys.executable, self.filename], capture_output=True, text=True, timeout=600)
                temp_fuzzing_result = subprocess.run([sys.executable, self.fuzzing_filename], capture_output=True, text=True, timeout=600)

                for i in truth_rst.keys():
                    truth_rst[i] += self.output_postprocess(temp_truth_result.stdout).get(i, 0)
                    fuzzing_rst[i] += self.output_postprocess(temp_fuzzing_result.stdout).get(i, 0)
            else:
                # 说明while语句并没有通过break结束
                # 也说明程序是一直不满足hellinger < 0.1 的要求， 而是取样次数超出限制
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


    def check_code(self):
        # 检查truth代码和fuzzing代码
        print(self.code)
        print("####################################")
        print(self.fuzzing_code)


if __name__ == "__main__":
    a = CirqGenerator(5, 1)

    # a.check_code()
    a.run()
