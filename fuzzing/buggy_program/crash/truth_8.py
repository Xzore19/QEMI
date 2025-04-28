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

qreg = QuantumRegister(7) 
creg = ClassicalRegister(5) 
cond_creg = ClassicalRegister(2) 
qc = QuantumCircuit(qreg, creg, cond_creg) 

qc.cswap(3, 2, 1)
qc.y(4)
qc.crz(0.39269908169872414, 4, 2)
qc.ry(1.5707963267948966, 0)
qc.y(4)
qc.ccz(4, 1, 0)
qc.ccz(3, 2, 1)
qc.rx(1.5707963267948966, 3)
qc.cp(0.7853981633974483, 4, 1)
qc.t(1)
qc.measure(qreg[3], creg[3])
with qc.if_test((creg[3], 0b1)) as else_1: 
	qc.ccz(4, 3, 1)
	qc.ch(4, 1)
	qc.t(1)
	qc.tdg(2)
	qc.z(2)
	qc.ry(0.39269908169872414, 3)
	qc.iswap(4, 1)
	qc.cry(0.7853981633974483, 4, 3)
	qc.iswap(4, 3)
	qc.cswap(3, 1, 0)
with else_1: 
	qc.ccx(4, 2, 0)
	qc.ry(0.39269908169872414, 3)
	qc.swap(3, 1)
	qc.rx(0.7853981633974483, 0)
	qc.rz(0.39269908169872414, 2)
	qc.swap(1, 0)
	qc.swap(4, 0)
	qc.cry(0.39269908169872414, 4, 0)
	qc.cx(1, 0)
	qc.ccx(4, 3, 1)

qc.tdg(4)
qc.h(3)
qc.swap(2, 0)
qc.rz(0.7853981633974483, 3)
qc.rz(1.5707963267948966, 2)
qc.rx(0.39269908169872414, 2)
qc.rz(0.7853981633974483, 0)
qc.ccx(4, 2, 1)
qc.p(0.7853981633974483, 0)
qc.ry(1.5707963267948966, 2)
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
