from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, transpile, execute
from qiskit.circuit import Parameter, ParameterVector
from math import pi

qreg = QuantumRegister(5)
creg = ClassicalRegister(5)
qc = QuantumCircuit(qreg, creg)

qc.h(0)
qc.measure(qreg[0], creg[0])
with qc.if_test((creg[0], 0)) as else_1:
	qc.x(1)
with else_1:
	qc.x(2)

qc.x(3)
qc.measure(qreg, creg)
simulator = Aer.get_backend("aer_simulator")
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result().get_counts()
print("results:", result)
