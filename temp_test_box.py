from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager

qreg = QuantumRegister(7)
creg = ClassicalRegister(5)
qc = QuantumCircuit(qreg, creg)

qc.measure(qreg[4], creg[4])
# with qc.if_test((creg[4], 0b1)) as else_1:

# with else_1:
# 	pass

with qc.box():
	pass

simulator = Aer.get_backend("aer_simulator")

compiled_circuit = transpile(qc, backend = simulator)
job = simulator.run(compiled_circuit, shots=10000)
result = job.result().get_counts()
print(result)
