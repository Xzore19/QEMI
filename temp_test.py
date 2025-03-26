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

qc.cswap(4, 2, 0)
qc.cx(4, 0)
qc.rx(1.5707963267948966, 2)
qc.rx(1.5707963267948966, 4)
qc.rz(0.39269908169872414, 2)
qc.measure(qreg[4], creg[4])
with qc.if_test((creg[4], 1)) as else_1: 
	qc.iswap(2, 0)
	qc.cswap(4, 3, 1)
	qc.y(3)
	qc.cx(2, 1)
	qc.cswap(2, 1, 0)
with else_1: 
	qc.crz(0.7853981633974483, 3, 2)
	qc.cz(3, 4)
	qc.cx(4, 2)
	qc.cp(0.39269908169872414, 2, 4)
	qc.t(1)

qc.p(1.5707963267948966, 0)
qc.ccx(3, 2, 1)
qc.swap(4, 1)
qc.rz(1.5707963267948966, 2)
qc.ry(1.5707963267948966, 0)

qc.measure(qreg, creg) 

simulator = Aer.get_backend("aer_simulator") 

p = PassManager(HoareOptimizer()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "none", layout_method = "noise_adaptive", approximation_degree = 0.3259032590325903 ) 
job = simulator.run(compiled_circuit, shots=2000) 
result = job.result().get_counts() 
print("results:", result)
