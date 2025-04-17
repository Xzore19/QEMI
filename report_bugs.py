from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager

qreg = QuantumRegister(5)
creg = ClassicalRegister(5)
qc = QuantumCircuit(qreg, creg)

temp_qreg = QuantumRegister(2)
temp_creg = ClassicalRegister(2)
temp_qc = QuantumCircuit(temp_qreg, temp_creg)
temp_qc.x(0)
temp_qc.x(1)
temp_qc.measure(temp_qreg, temp_creg)

with temp_qc.if_test((temp_creg, 0b11)) as else_1:
    qc.x(0)
with else_1:
    qc.h(0)

qc.measure(qreg, creg)
#
# simulator = Aer.get_backend("aer_simulator")
#
# p = PassManager(Optimize1qGates())
# qc = p.run(qc)
#
# compiled_circuit = transpile(qc, backend=simulator, optimization_level=3)
# job = simulator.run(compiled_circuit, shots=100000)
# result = job.result().get_counts()
# print(result)

import matplotlib as plt

qc.draw("mpl")

plt.pyplot.show()