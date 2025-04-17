from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.circuit import Parameter, ParameterVector
from qiskit.circuit.library import XGate
from qiskit.transpiler.passes import *
import z3
from qiskit.transpiler import PassManager, generate_preset_pass_manager
from math import pi

qreg = QuantumRegister(5)
creg = ClassicalRegister(5)
qc = QuantumCircuit(qreg, creg)

# qc.ccz(4, 3, 1)
# qc.cx(3, 2)
# qc.p(1.5707963267948966, 4)
# qc.cswap(4, 2, 1)
# qc.ccx(4, 2, 0)
# qc.t(0)
# qc.cz(2, 3)
# qc.iswap(2, 0)
# qc.iswap(3, 2)
# qc.z(1)


# a = 1.7976931348623157e+3
# if a == 1.7976931348623157e+3 -1:
# 	qc.h(0)
# def create_oracle(qreg):
#     oracle = QuantumCircuit(qreg, name='Oracle')
#     oracle.h(qreg[1])
#     oracle.mcx([qreg[0]], qreg[1])
#     oracle.h(qreg[1])
#     return oracle.to_gate(label='Oracle')
#
#
# def create_diffuser(qreg):
#     diffuser = QuantumCircuit(qreg, name='Diffuser')
#     diffuser.h(qreg)
#     diffuser.x(qreg)
#     diffuser.h(qreg[1])
#     diffuser.mcx([qreg[0]], qreg[1])
#     diffuser.h(qreg[1])
#     diffuser.x(qreg)
#     diffuser.h(qreg)
#     return diffuser.to_gate(label='Diffuser')
#
#
# oracle_gate = create_oracle(QuantumRegister(2))
# diffuser_gate = create_diffuser(QuantumRegister(2))
# results = []
# grdc_qreg = QuantumRegister(2)
# grdc_creg = ClassicalRegister(2)
# grdc_qc = QuantumCircuit(grdc_qreg, grdc_creg)
# grdc_qc.h(grdc_qreg)
# for _ in range(1):
#     grdc_qc.append(oracle_gate, qargs=grdc_qreg)
#     grdc_qc.append(diffuser_gate, qargs=grdc_qreg)
#     grdc_qc.measure(grdc_qreg, grdc_creg)

# transpiled_qc = transpile(grdc_qc, backend=backend, optimization_level=1)
#
# # 运行电路
# job = backend.run(transpiled_qc)
#
# # 获取结果
# result = job.result()
# counts = result.get_counts()
# print(counts)

grdc_qreg = QuantumRegister(2)
grdc_creg = ClassicalRegister(2)
grdc_qc = QuantumCircuit(grdc_qreg, grdc_creg)
grdc_qc.x(0)
grdc_qc.x(1)
grdc_qc.measure(grdc_qreg, grdc_creg)

# backend = Aer.get_backend('aer_simulator')
# transpiled_qc = transpile(grdc_qc, backend=backend, optimization_level=1)
#
# # 运行电路
# job = backend.run(transpiled_qc, shots=100000)
#
# # 获取结果
# result = job.result()
# counts = result.get_counts()
# print(counts)

with grdc_qc.if_test((grdc_creg, 0b11)) as else_1:
    pass
with else_1:
    qc.h(0)

# qc.measure(qreg[0], creg[0])
# with qc.if_test((creg[0], 0b0)) as else_1:
#     qc.swap(4, 1)
#     qc.ccz(2, 1, 0)
#     qc.iswap(1, 0)
#     qc.h(0)
#     qc.y(3)
#     qc.h(4)
#     qc.ry(1.5707963267948966, 4)
#     qc.rz(0.7853981633974483, 0)
#     qc.iswap(4, 2)
#     qc.ry(1.5707963267948966, 1)
# with else_1:
#     qc.h(1)
#     qc.swap(3, 0)
#     qc.rz(0.39269908169872414, 3)
#     qc.t(1)
#     qc.t(1)
#     qc.crz(1.5707963267948966, 2, 1)
#     qc.ccz(3, 1, 0)
#     qc.rz(1.5707963267948966, 1)
#     qc.cswap(4, 1, 0)
#     qc.cry(0.7853981633974483, 1, 3)
#
# qc.tdg(2)
# qc.cry(0.39269908169872414, 4, 2)
# qc.rx(1.5707963267948966, 1)
# qc.cx(2, 1)
# qc.ry(0.39269908169872414, 4)
# qc.crz(1.5707963267948966, 1, 0)
# qc.z(1)
# qc.cz(1, 3)
# qc.cswap(4, 3, 2)
# qc.cx(4, 1)


qc.measure(qreg, creg)

simulator = Aer.get_backend("aer_simulator")

p = PassManager(Optimize1qGates())
qc = p.run(qc)

compiled_circuit = transpile(qc, backend=simulator, optimization_level=3, routing_method="sabre",
                             layout_method="noise_adaptive", approximation_degree=1)
job = simulator.run(compiled_circuit, shots=100000)
result = job.result().get_counts()
print(result)
