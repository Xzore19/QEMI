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
qc.rz(1.5707963267948966, 1)
qc.rz(0.39269908169872414, 3)
qc.ccz(3, 2, 1)
qc.ch(1, 0)
qc.cswap(3, 2, 0)
qc.ch(3, 1)
qc.t(2)
qc.cz(1, 4)
qc.z(0)
qc.measure(qreg[4], creg[4])
with qc.if_test((creg[4], 0b1)) as else_1: 
	qc.rz(1.5707963267948966, 3)
	qc.crx(0.7853981633974483, 3, 0)
	qc.crz(0.7853981633974483, 4, 3)
	qc.ccx(2, 1, 0)
	qc.rx(0.7853981633974483, 4)
	qc.ch(4, 3)
	qc.t(4)
	qc.cx(3, 0)
	qc.cry(0.39269908169872414, 0, 1)
	qc.ccz(3, 1, 0)
with else_1: 
	qc.x(2)
	qc.iswap(2, 0)
	qc.crz(0.7853981633974483, 1, 3)
	qc.tdg(3)
	qc.iswap(4, 2)
	qc.z(3)
	qc.crz(0.7853981633974483, 3, 2)
	qc.y(1)
	qc.cry(0.39269908169872414, 4, 3)
	qc.ccz(4, 3, 2)

qc.h(4)
qc.iswap(4, 3)
qc.cry(0.39269908169872414, 0, 2)
qc.ccx(3, 2, 0)
qc.cx(1, 0)
qc.ch(4, 3)
qc.cry(0.39269908169872414, 4, 1)
qc.h(1)
qc.p(0.39269908169872414, 2)
qc.crx(0.7853981633974483, 2, 0)
qc.measure(qreg, creg) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
