from dc_cond_gen.gr_generator import generate_grover_code
from qiskit_gates_generator import gate_generator
import random
from qiskit_api import generate_random_append_statement
import uuid

class DeadCodeFuzzer():
    # 用于生成明确的dead code
    def __init__(self, qubit_num = 2):
        self.qubit_num = qubit_num
        self.uid = uuid.uuid4().hex[:6]
        self.qr_name = f"qr_{self.uid}"
        self.cr_name = f"cr_{self.uid}"


    def classical_dead(self):
        # append dead code for classical condition
        code_line = "\n"
        code_line += "a = 1.7976931348623157e+3 \n"
        code_line += "if a == 1.7976931348623157e+3 -1:\n"
        code_line += "\tqc.h(0) \n"
        return code_line

    def quantum_dead(self, mode="normal"):
        if mode == "grover":
            oracle, code = generate_grover_code(num_qubits=self.qubit_num)
        elif mode == "normal":
            oracle = "11"
            code = f"""
{self.qr_name} = QuantumRegister(2)
{self.cr_name} = ClassicalRegister(2)
qc.add_register({self.qr_name})
qc.add_register({self.cr_name})
qc.x({self.qr_name}[0])
qc.x({self.qr_name}[1])
"""

        return oracle, code, None


    def if_test_dead(self, qc, qreg, qnum, cond_reg,gate_list):
        code_line, unfuzz_line = "", ""
        oracle, deadcode, _ = self.quantum_dead()
        code_line += deadcode
        # code_line += f"{qc}.compose({deadqc}, inplace = True, qubits = {[qnum + i for i in range(self.qubit_num)]}) \n"
        for i in range(self.qubit_num):
            code_line += f"{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"

        code_line += f"with {qc}.if_test(({self.cr_name}, 0b{oracle})) as else_1: \n"
        code_line += "\tpass\n"
        code_line += f"with else_1: \n"
        code_line += gate_list
        code_line += "\n"
        return code_line, unfuzz_line

    def if_test_else(self, qc, qreg, qnum, cond_reg, gate_list, dead_list):
        code_line, unfuzz_line = "", ""
        oracle, deadcode, _ = self.quantum_dead()
        code_line += deadcode
        unfuzz_line += deadcode
        # code_line += f"{qc}.compose({deadqc}, inplace = True, qubits = {[qnum + i for i in range(self.qubit_num)]}) \n"
        # unfuzz_line += f"{qc}.compose({deadqc}, inplace = True, qubits = {[qnum + i for i in range(self.qubit_num)]}) \n"

        for i in range(self.qubit_num):
            code_line += f"{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"
            unfuzz_line += f"{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"

        code_line += f"with {qc}.if_test(({self.cr_name}, 0b{oracle})) as else_1: \n"
        unfuzz_line += f"with {qc}.if_test(({self.cr_name}, 0b{oracle})) as else_1: \n"
        code_line += gate_list
        unfuzz_line += gate_list
        code_line += f"with else_1: \n"
        unfuzz_line += f"with else_1: \n"
        code_line += dead_list
        unfuzz_line +="\tpass \n"
        unfuzz_line += "\n"
        code_line += "\n"
        return code_line, unfuzz_line

    def dynamic_for_continue(self, qc, gate_list, dead_list):
        code_line, unfuzz_line = "", ""
        code_line += f"with {qc}.for_loop(range(3)) as i:\n"
        unfuzz_line += f"with {qc}.for_loop(range(3)) as i:\n"
        code_line += gate_list
        unfuzz_line += gate_list
        code_line += f"\tqc.continue_loop()\n"
        unfuzz_line += f"\tqc.continue_loop()\n"
        code_line += dead_list
        return code_line, unfuzz_line

    def dynamic_for_break(self, qc, gate_list, dead_list):
        code_line, unfuzz_line = "", ""
        code_line += f"with {qc}.for_loop(range(3)) as i:\n"
        unfuzz_line += f"with {qc}.for_loop(range(3)) as i:\n"
        code_line += gate_list
        unfuzz_line += gate_list
        code_line += f"\tqc.break_loop()\n"
        unfuzz_line += f"\tqc.break_loop()\n"
        code_line += dead_list
        return code_line, unfuzz_line

    def dynamic_for_zero(self, qc, gate_list):
        code_line = "a = 0\n"
        code_line += f"with {qc}.for_loop(range(a)) as i:\n"
        code_line += gate_list
        return code_line, ""

    def while_dead(self, qc, qreg, cond_reg, qnum, gate_list):
        oracle, deadcode, _ = self.quantum_dead()
        if oracle[-1] == "0":
            oracle = oracle[:-1] + "1"
        else:
            oracle = oracle[:-1] + "0"

        code_line= ""
        code_line += deadcode
        # code_line += f"{qc}.compose({deadqc}, inplace = True, qubits = {[qnum + i for i in range(self.qubit_num)]}) \n"

        for i in range(self.qubit_num):
            code_line += f"{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"

        code_line += f"with {qc}.while_loop(({self.cr_name}, 0b{oracle})): \n"
        code_line += gate_list
        for i in range(self.qubit_num):
            code_line += f"\t{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"
        code_line += "\n"
        return code_line, ""

    def while_break(self, qc, qreg, cond_reg, qnum, gate_list, dead_list):
        oracle, deadcode, _ = self.quantum_dead()
        code_line, unfuzz_line = "", ""
        code_line += deadcode
        unfuzz_line += deadcode
        # code_line += f"{qc}.compose({deadqc}, inplace = True, qubits = {[qnum + i for i in range(self.qubit_num)]}) \n"
        # unfuzz_line += f"{qc}.compose({deadqc}, inplace = True, qubits = {[qnum + i for i in range(self.qubit_num)]}) \n"

        for i in range(self.qubit_num):
            code_line += f"{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"
            unfuzz_line += f"{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"

        code_line += f"with {qc}.while_loop(({self.cr_name}, 0b{oracle})): \n"
        unfuzz_line += f"with {qc}.while_loop(({self.cr_name}, 0b{oracle})): \n"
        for i in range(self.qubit_num):
            code_line += f"\t{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"
            unfuzz_line += f"\t{qc}.measure({self.qr_name}[{i}], {self.cr_name}[{i}]) \n"
        code_line += gate_list
        unfuzz_line += gate_list
        code_line += f"\t{qc}.break_loop()\n"
        unfuzz_line += f"\t{qc}.break_loop()\n"
        code_line += dead_list
        return code_line, unfuzz_line


    def gate_generation(self, indent):
        # 随机量子门操作的构建
        gate_code = ""
        for i in range(self.gate_num_upper):
            flag = random.uniform(0, 1)
            if flag > 0.75:
                gate_code += "\t" * indent + gate_generator(qubits_num=self.qnum, cir_name=self.qc) + "\n"
            else:
                qc, code = generate_random_append_statement(max_qubits=self.qnum, qc_var=self.qc, qr_var=self.qreg)
                code_frag = code.split("\n")
                for cf in code_frag:
                    gate_code += "\t" * indent + cf + "\n"
        return gate_code
