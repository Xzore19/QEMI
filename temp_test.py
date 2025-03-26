from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile 
from qiskit_aer import Aer 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.circuit import Parameter, ParameterVector 
from math import pi 

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.ccx(2, 1, 0)
qc.ccz(4, 2, 1)
qc.ry(1.5707963267948966, 2)
qc.z(3)
qc.x(1)
qc.measure(qreg[1], creg[1])
with qc.if_test((creg[1], 1)) as else_1: 
	qc.cz(2, 3)
	qc.t(1)
	qc.swap(4, 2)
	qc.p(0.7853981633974483, 1)
	qc.y(3)
with else_1: 
	qc.t(4)
	qc.h(1)
	qc.h(0)
	qc.cp(0.7853981633974483, 2, 4)
	qc.tdg(4)

qc.ccx(4, 2, 0)
qc.cry(0.7853981633974483, 3, 1)
qc.y(0)
qc.t(0)
qc.rz(1.5707963267948966, 0)

qc.measure(qreg, creg) 

simulator = Aer.get_backend("aer_simulator") 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 1, routing_method = "none", layout_method = "trivial", approximation_degree = 0.26134261342613424 ) 
job = simulator.run(compiled_circuit, shots=2000) 
result = job.result().get_counts() 
print("results:", result)
