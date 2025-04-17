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

qc.ry(0.39269908169872414, 4)
qc.swap(3, 2)
qc.tdg(2)
qc.ry(0.39269908169872414, 2)
qc.tdg(4)
qc.cx(3, 2)
qc.z(3)
qc.ch(1, 0)
qc.tdg(2)
qc.cry(0.7853981633974483, 1, 2)
qc.measure(qreg[3], creg[3])
with qc.if_test((creg[3], 0b1)) as else_1: 
	qc.p(0.7853981633974483, 1)
	qc.cx(4, 0)
	qc.z(2)
	qc.cswap(4, 3, 2)
	qc.cp(0.39269908169872414, 3, 1)
	qc.crz(0.39269908169872414, 2, 0)
	qc.rz(0.39269908169872414, 2)
	qc.rz(0.39269908169872414, 1)
	qc.h(0)
	qc.ccx(4, 3, 1)
with else_1: 
	qc.y(0)
	qc.rx(0.39269908169872414, 2)
	qc.cp(0.39269908169872414, 4, 1)
	qc.t(4)
	qc.ccx(3, 1, 0)
	qc.ccx(4, 3, 1)
	qc.cz(1, 3)
	qc.ccx(4, 1, 0)
	qc.rx(0.39269908169872414, 4)
	qc.cswap(4, 3, 2)

qc.h(0)
qc.iswap(4, 1)
qc.cx(1, 0)
qc.ry(0.7853981633974483, 2)
qc.cx(4, 0)
qc.cswap(4, 2, 0)
qc.swap(4, 1)
qc.x(0)
qc.x(2)
qc.cry(1.5707963267948966, 3, 4)
qc.measure(qreg, creg) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
