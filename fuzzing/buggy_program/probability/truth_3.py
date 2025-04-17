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

qc.cry(0.7853981633974483, 1, 0)
qc.cry(1.5707963267948966, 3, 2)
qc.z(2)
qc.swap(4, 3)
qc.p(1.5707963267948966, 3)
qc.ccx(3, 2, 0)
qc.p(0.7853981633974483, 0)
qc.z(2)
qc.swap(3, 1)
qc.iswap(4, 1)
qc.measure(qreg[3], creg[3])
with qc.if_test((creg[3], 0b0)) as else_1: 
	qc.cswap(4, 3, 1)
	qc.cry(1.5707963267948966, 4, 0)
	qc.t(0)
	qc.p(1.5707963267948966, 4)
	qc.rz(1.5707963267948966, 3)
	qc.cswap(4, 2, 1)
	qc.ry(0.39269908169872414, 4)
	qc.ch(3, 2)
	qc.cx(4, 3)
	qc.cp(0.7853981633974483, 4, 1)
with else_1: 
	qc.ry(0.7853981633974483, 1)
	qc.crz(0.39269908169872414, 3, 1)
	qc.t(1)
	qc.iswap(4, 3)
	qc.ry(0.7853981633974483, 0)
	qc.swap(3, 2)
	qc.x(4)
	qc.tdg(0)
	qc.cz(0, 3)
	qc.z(2)

qc.cx(3, 0)
qc.ccx(3, 2, 0)
qc.cswap(3, 1, 0)
qc.ch(2, 0)
qc.tdg(0)
qc.cry(0.39269908169872414, 3, 0)
qc.iswap(3, 2)
qc.x(2)
qc.rx(1.5707963267948966, 3)
qc.h(3)
qc.measure(qreg, creg) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
