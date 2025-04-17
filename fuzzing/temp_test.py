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

qc.cz(2, 3)
qc.h(4)
qc.ch(3, 1)
qc.t(1)
qc.rz(1.5707963267948966, 2)
qc.p(0.39269908169872414, 3)
qc.ccx(3, 1, 0)
qc.cry(0.7853981633974483, 4, 0)
qc.ry(0.39269908169872414, 2)
qc.swap(3, 0)
qc.measure(qreg[2], creg[2])
with qc.if_test((creg[2], 0b1)) as else_1: 
	qc.ch(2, 1)
	qc.p(0.39269908169872414, 1)
	qc.ccz(4, 1, 0)
	qc.crx(1.5707963267948966, 1, 4)
	qc.x(3)
	qc.cswap(3, 2, 1)
	qc.iswap(4, 2)
	qc.ry(1.5707963267948966, 4)
	qc.iswap(2, 0)
	qc.ch(4, 0)
with else_1: 
	qc.cswap(3, 2, 0)
	qc.p(0.39269908169872414, 2)
	qc.cry(1.5707963267948966, 4, 0)
	qc.z(1)
	qc.ccx(3, 2, 0)
	qc.ccx(4, 3, 1)
	qc.ccz(3, 2, 0)
	qc.cry(0.7853981633974483, 1, 3)
	qc.x(4)
	qc.ch(2, 1)

qc.cswap(4, 3, 1)
qc.crx(0.7853981633974483, 4, 3)
qc.h(1)
qc.rx(1.5707963267948966, 1)
qc.z(1)
qc.iswap(4, 2)
qc.ry(1.5707963267948966, 3)
qc.cp(0.7853981633974483, 4, 3)
qc.swap(2, 0)
qc.ch(3, 2)
qc.measure(qreg, creg) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
