from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, transpile, execute 
from qiskit.circuit import Parameter, ParameterVector 
from math import pi 

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.rz(1.5707963267948966, 4)
qc.h(4)
qc.cx(1, 0)
qc.cry(1.5707963267948966, 0, 4)
qc.t(1)
qc.measure(qreg[0], creg[0])
with qc.if_test((creg[0], 0)) as else_1: 
	qc.tdg(2)
	qc.cry(1.5707963267948966, 2, 3)
	qc.cry(1.5707963267948966, 0, 1)
	qc.cswap(4, 3, 0)
	qc.cz(1, 2)
with else_1: 
	qc.ccz(3, 1, 0)
	qc.crz(1.5707963267948966, 3, 0)
	qc.cz(1, 2)
	qc.y(4)
	qc.t(1)

qc.cz(1, 4)
qc.x(4)
qc.cry(1.5707963267948966, 0, 1)
qc.crz(1.5707963267948966, 0, 1)
qc.x(3)
qc.measure(qreg, creg) 
simulator = Aer.get_backend("aer_simulator") 
compiled_circuit = transpile(qc, simulator) 
job = execute(compiled_circuit, simulator, shots=1024) 
result = job.result().get_counts() 
print("results:", result)
