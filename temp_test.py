# from qiskit import QuantumCircuit
#
# from qiskit import QuantumCircuit
#
# def circuit_to_qiskit_code(circuit: QuantumCircuit, circuit_name="qc") -> str:
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
#
#
# from qiskit import QuantumCircuit
# qc = QuantumCircuit(2, 2)
# qc.h(0)
# qc.cx(0, 1)
# qc.measure(0, 0)
# qc.measure(1, 1)
#
# print(circuit_to_qiskit_code(qc))
#


from qiskit import QuantumCircuit

qc1 = QuantumCircuit(2, 2)
qc1.h(0)
qc1.cx(0, 1)

qc2 = QuantumCircuit(2, 2)
qc2.x(1)
qc2.measure(0, 0)

# 合并 qc2 到 qc1 的后面
qc3 = qc1.compose(qc2)
print(qc3.draw())
