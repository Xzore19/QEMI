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

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.iswap(4, 2)
qc.cswap(4, 3, 2)
qc.cz(0, 1)
qc.ccz(4, 3, 2)
qc.y(1)
qc.t(1)
qc.rz(0.39269908169872414, 1)
qc.t(4)
qc.iswap(1, 0)
qc.ry(0.39269908169872414, 1)
qc.measure(qreg[4], creg[4])
with qc.if_test((creg[4], 0b0)) as else_1: 
	qc.swap(3, 1)
	qc.cry(0.7853981633974483, 2, 1)
	qc.crz(1.5707963267948966, 0, 1)
	qc.h(3)
	qc.tdg(4)
	qc.x(1)
	qc.ccx(4, 2, 1)
	qc.x(1)
	qc.swap(3, 1)
	qc.crz(1.5707963267948966, 1, 0)
with else_1: 
	qc.ch(3, 2)
	qc.z(2)
	qc.cx(4, 0)
	qc.rx(0.7853981633974483, 0)
	qc.crx(0.7853981633974483, 4, 2)
	qc.x(0)
	qc.cswap(4, 2, 0)
	qc.cry(0.39269908169872414, 3, 4)
	qc.cswap(4, 2, 1)
	qc.rz(0.7853981633974483, 4)

qc.p(1.5707963267948966, 2)
qc.p(0.7853981633974483, 1)
qc.swap(3, 0)
qc.tdg(0)
qc.rz(0.7853981633974483, 1)
qc.h(2)
qc.y(0)
qc.rx(0.39269908169872414, 2)
qc.z(4)
qc.cry(0.7853981633974483, 3, 2)
qc.measure(qreg, creg) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
