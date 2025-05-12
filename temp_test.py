from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager

qreg = QuantumRegister(7)
creg = ClassicalRegister(5)
cond_creg = ClassicalRegister(2)
qc = QuantumCircuit(qreg, creg, cond_creg)

qc.measure(qreg[4], creg[4])
with qc.if_test((creg[4], 0b1)) as else_1:
	qc.cx(2, 0)
	qc.iswap(4, 2)
with else_1:
	qc.cx(2, 0)

qc.measure(qreg[0], creg[0])
qc.measure(qreg[1], creg[1])
qc.measure(qreg[2], creg[2])
qc.measure(qreg[3], creg[3])
qc.measure(qreg[4], creg[4])


simulator = Aer.get_backend("aer_simulator")

p = PassManager(CollectCliffords())
qc = p.run(qc)

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 )
job = simulator.run(compiled_circuit, shots=10000)
result = job.result().get_counts()
print(result)