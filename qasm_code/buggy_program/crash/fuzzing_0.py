from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.qasm3 import dumps

qreg = QuantumRegister(1)
creg = ClassicalRegister(1)
qc = QuantumCircuit(qreg, creg) 

for i in range(3):
	qc.h(0)

with qc.for_loop(range(3)) as i:
	qc.z(0)

qc.measure(qreg[0], creg[0])

qasm3_code = dumps(qc)
print(qasm3_code)




