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

qc.cswap(3, 2, 0)
qc.cz(1, 2)
qc.rz(0.7853981633974483, 4)
qc.ry(0.39269908169872414, 0)
qc.cry(0.7853981633974483, 4, 2)
qc.cp(1.5707963267948966, 2, 0)
qc.rz(1.5707963267948966, 0)
qc.cx(4, 1)
qc.cz(1, 3)
qc.ccz(3, 1, 0)
with qc.for_loop(range(5)) as i:
	qc.z(4)
	qc.tdg(0)
	qc.crx(0.39269908169872414, 4, 2)
	qc.x(0)
	qc.cx(4, 2)
	qc.ccz(4, 3, 2)
	qc.tdg(2)
	qc.rz(0.7853981633974483, 2)
	qc.t(1)
	qc.iswap(4, 2)
	qc.break_loop()
	qc.crx(1.5707963267948966, 3, 4)
	qc.t(4)
	qc.swap(4, 1)
	qc.ccx(4, 1, 0)
	qc.ch(2, 1)
	qc.iswap(1, 0)
	qc.swap(4, 1)
	qc.y(1)
	qc.ccz(4, 3, 2)
	qc.x(2)
qc.h(4)
qc.ry(0.39269908169872414, 2)
qc.cry(0.7853981633974483, 0, 2)
qc.cx(1, 0)
qc.ccx(3, 2, 1)
qc.cz(1, 3)
qc.p(1.5707963267948966, 3)
qc.cry(1.5707963267948966, 1, 0)
qc.ccz(4, 1, 0)
qc.rz(0.7853981633974483, 2)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
