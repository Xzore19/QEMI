from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile 
from qiskit_aer import Aer 
from qiskit.circuit import Parameter, ParameterVector 
from math import pi 

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.cswap(3, 1, 0)
qc.iswap(2, 1)
qc.ccz(3, 1, 0)
qc.z(1)
qc.tdg(1)
qc.measure(qreg[1], creg[1])
with qc.if_test((creg[1], 1)) as else_1: 
	qc.crz(0.7853981633974483, 3, 0)
	qc.z(2)
	qc.tdg(4)
	qc.crx(0.39269908169872414, 2, 3)
	qc.cx(4, 2)
with else_1: 
	qc.crz(1.5707963267948966, 2, 3)
	qc.y(4)
	qc.z(3)
	qc.y(0)
	qc.rx(0.7853981633974483, 3)

qc.ccz(4, 2, 1)
qc.tdg(4)
qc.ccx(2, 1, 0)
qc.cx(3, 1)
qc.p(0.39269908169872414, 0)
qc.measure(qreg, creg) 
simulator = Aer.get_backend("aer_simulator") 
compiled_circuit = transpile(qc, simulator) 
job = simulator.run(compiled_circuit, shots=1024) 
result = job.result().get_counts() 
print("results:", result)
