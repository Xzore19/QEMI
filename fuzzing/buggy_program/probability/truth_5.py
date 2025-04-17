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

qc.cry(0.7853981633974483, 2, 1)
qc.cx(3, 0)
qc.crz(0.7853981633974483, 2, 4)
qc.cry(0.7853981633974483, 2, 3)
qc.rx(0.39269908169872414, 3)
qc.ccx(3, 2, 1)
qc.ccz(4, 3, 1)
qc.cx(4, 3)
qc.ry(0.7853981633974483, 3)
qc.rz(0.7853981633974483, 2)
qc.measure(qreg[0], creg[0])
with qc.if_test((creg[0], 0b1)) as else_1: 
	qc.rz(0.7853981633974483, 3)
	qc.tdg(1)
	qc.x(1)
	qc.tdg(1)
	qc.crx(0.39269908169872414, 3, 2)
	qc.cp(1.5707963267948966, 1, 3)
	qc.crz(1.5707963267948966, 3, 1)
	qc.crx(0.7853981633974483, 1, 0)
	qc.ry(1.5707963267948966, 0)
	qc.cz(1, 3)
with else_1: 
	qc.crz(0.39269908169872414, 3, 0)
	qc.iswap(3, 2)
	qc.cry(0.7853981633974483, 1, 3)
	qc.y(0)
	qc.ch(3, 2)
	qc.ch(4, 1)
	qc.cswap(4, 2, 1)
	qc.cz(0, 4)
	qc.ccx(3, 1, 0)
	qc.cz(0, 3)

qc.p(1.5707963267948966, 4)
qc.t(3)
qc.iswap(1, 0)
qc.x(1)
qc.y(1)
qc.crx(0.7853981633974483, 0, 3)
qc.cp(0.7853981633974483, 1, 3)
qc.rx(0.39269908169872414, 1)
qc.iswap(4, 2)
qc.swap(3, 0)
qc.measure(qreg, creg) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
