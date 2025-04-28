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

qc.ry(0.7853981633974483, 4)
qc.t(2)
qc.crz(0.39269908169872414, 1, 0)
qc.cp(0.39269908169872414, 3, 4)
qc.crz(1.5707963267948966, 3, 2)
qc.cswap(3, 2, 1)
qc.cswap(3, 2, 0)
qc.cswap(4, 3, 0)
qc.ry(0.39269908169872414, 2)
qc.tdg(3)
qc.measure(qreg[3], creg[3])
with qc.if_test((creg[3], 0b0)) as else_1: 
	qc.cp(0.7853981633974483, 2, 1)
	qc.y(0)
	qc.x(1)
	qc.cswap(3, 2, 1)
	qc.ccz(3, 2, 0)
	qc.x(0)
	qc.cswap(4, 3, 0)
	qc.rz(0.39269908169872414, 0)
	qc.rz(1.5707963267948966, 4)
	qc.rx(0.7853981633974483, 4)
with else_1: 
	qc.tdg(1)
	qc.p(1.5707963267948966, 3)
	qc.cp(0.39269908169872414, 3, 2)
	qc.h(3)
	qc.crx(0.7853981633974483, 4, 2)
	qc.cz(1, 3)
	qc.cx(4, 2)
	qc.iswap(4, 0)
	qc.x(0)
	qc.tdg(1)

qc.cswap(3, 1, 0)
qc.ccz(3, 2, 1)
qc.swap(3, 2)
qc.p(0.7853981633974483, 1)
qc.ccx(3, 2, 0)
qc.x(0)
qc.rz(0.39269908169872414, 2)
qc.cry(1.5707963267948966, 2, 0)
qc.rx(0.7853981633974483, 4)
qc.crx(0.7853981633974483, 0, 3)
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
