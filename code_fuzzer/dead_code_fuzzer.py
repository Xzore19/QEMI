from dc_cond_gen.gr_generator import generate_grover_code
from qiskit_gates_generator import gate_generator
class DeadCodeFuzzer():
    # 用于生成明确的dead code
    def __init__(self, qubit_num = 2):
        self.qubit_num = qubit_num


    def classical_dead(self):
        # append dead code for classical condition
        code_line = "\n"
        code_line += "a = 1.7976931348623157e+3 \n"
        code_line += "if a == 1.7976931348623157e+3 -1:\n"
        code_line += "\tqc.h(0) \n"
        return code_line

    def quantum_dead(self, mode="grover"):
        if mode == "grover":
            oracle, code = generate_grover_code(num_qubits=self.qubit_num)
            qc, qreg, creg = "grdc_qc","grdc_qreg","grdc_creg"

        return oracle, code, qc


    def if_test_dead(self, oracle, qc, qreg, cond_reg, qnum, cnum, gate_list=None):
        code_line = ""
        for i in range(cnum):
            code_line += f"{qc}.measure({qreg}[{qnum+i}], {cond_reg}[{i}]) \n"

        code_line += f"with {qc}.if_test(({cond_reg}, 0b{oracle})) as else_1: \n"
        code_line += "    pass\n"
        code_line += f"with else_1: \n"
        code_line += gate_list
        code_line += "\n"
        return code_line

    def dynamic_for_continue(self, qc, gate_list):
        code_line = ""
        code_line += f"with {qc}.for_loop(range(5)) as i:\n"
        code_line += f"\tqc.continue_loop()\n"
        code_line += gate_list
        return code_line

    def dynamic_for_break(self, qc, gate_list):
        code_line = ""
        code_line += f"with {qc}.for_loop(range(5)) as i:\n"
        code_line += f"\tqc.break_loop()\n"
        code_line += gate_list
        return code_line

    def dynamic_for_zero(self, qc, gate_list):
        code_line = "a = 0\n"
        code_line += f"with {qc}.for_loop(range(a)) as i:\n"
        code_line += gate_list
        return code_line

    def while_dead(self, oracle, qc, qreg, cond_reg, qnum, cnum, gate_list):
        if oracle[-1] == "0":
            oracle = oracle[:-1] + "1"
        else:
            oracle = oracle[:-1] + "0"

        code_line = ""
        for i in range(cnum):
            code_line += f"{qc}.measure({qreg}[{qnum+i}], {cond_reg}[{i}]) \n"

        code_line += f"with {qc}.while_loop(({cond_reg}, 0b{oracle})): \n"
        code_line += gate_list
        for i in range(cnum):
            code_line += f"\t{qc}.measure({qreg}[{qnum + i}], {cond_reg}[{i}]) \n"
        code_line += "\n"
        return code_line

    def while_break(self, oracle, qc, qreg, cond_reg, qnum, cnum, gate_list, fuzz=None, gate_list2=None):

        code_line = ""
        for i in range(cnum):
            code_line += f"{qc}.measure({qreg}[{qnum+i}], {cond_reg}[{i}]) \n"

        code_line += f"with {qc}.while_loop(({cond_reg}, 0b{oracle})): \n"
        for i in range(cnum):
            code_line += f"\t{qc}.measure({qreg}[{qnum + i}], {cond_reg}[{i}]) \n"
        code_line += f"\t{qc}.break_loop()\n"
        if fuzz:
            code_line += gate_list
        return code_line

    from qiskit import QuantumCircuit

    # def circuit_to_qiskit_code(self, circuit: QuantumCircuit, circuit_name="dc_qc") -> str:
    #     lines = []
    #     num_qubits = circuit.num_qubits
    #     num_clbits = circuit.num_clbits
    #     lines.append(f"from qiskit import QuantumCircuit\n")
    #     lines.append(f"{circuit_name} = QuantumCircuit({num_qubits}, {num_clbits})\n")
    #
    #     for inst in circuit.data:
    #         instr = inst.operation
    #         qargs = inst.qubits
    #         cargs = inst.clbits
    #
    #         # 获取量子比特索引
    #         q_str = ", ".join(f"{circuit_name}.qubits[{circuit.qubits.index(q)}]" for q in qargs)
    #         # 获取经典比特索引
    #         c_str = ", ".join(f"{circuit_name}.clbits[{circuit.clbits.index(c)}]" for c in cargs)
    #
    #         # 参数处理
    #         if instr.params:
    #             param_str = ", ".join([repr(p) for p in instr.params])
    #             line = f"{circuit_name}.{instr.name}({param_str}, {q_str})"
    #         else:
    #             line = f"{circuit_name}.{instr.name}({q_str})"
    #
    #         if cargs:
    #             line = line[:-1] + ", " + c_str + ")"
    #
    #         lines.append(line)
    #
    #     return "\n".join(lines)
