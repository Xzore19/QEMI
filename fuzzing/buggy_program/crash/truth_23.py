from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, AncillaRegister 
from qiskit_aer import Aer 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.circuit import Parameter, ParameterVector 
from qiskit.circuit.library import XGate 
from qiskit.transpiler.passes import * 
from qiskit.circuit.library import * 
from qiskit.transpiler import PassManager, generate_preset_pass_manager 
from math import pi 
import numpy as np 
np.random.seed(42) 

qreg = QuantumRegister(4) 
creg = ClassicalRegister(4) 
qc = QuantumCircuit(qreg, creg) 

qc.ccx(2, 1, 0)
qc.h(0)
qc.ry(0.7853981633974483, 1)
def fun_283304(): 
	qc =  QuantumCircuit(3) 
	qc.tdg(0)
	qc.cz(0, 1)
	qc.crz(0.7853981633974483, 2, 0)
	return qc.to_gate() 
g_6a4478 = fun_283304().control(1) 
qc.append(g_6a4478, [0,2,3,1]) 
def fun_183292(): 
	qc =  QuantumCircuit(3) 
	qc.z(1)
	qc.rz(0.39269908169872414, 2)
	qc.rz(0.7853981633974483, 1)
	return qc.to_gate() 
g_a5440e = fun_183292().control(1) 
qc.append(g_a5440e, [3,1,0,2]) 
with qc.for_loop(range(3)) as i_194e18:
	with qc.for_loop(range(3)) as i_a43755:
		qc.swap(3, 1)
		qc.cp(0.39269908169872414, 0, 3)
		qc.x(3)
		qc.append(C3XGate(), [qreg[0], qreg[3], qreg[2], qreg[1]])
		qc.ch(2, 1)
		qc.continue_loop()
	
	qc.continue_loop()
def fun_8d1590(): 
	qc =  QuantumCircuit(3) 
	qc.y(0)
	qc.cp(0.7853981633974483, 0, 1)
	qc.ccz(2, 1, 0)
	return qc.to_gate() 
g_84ee0d = fun_8d1590().control(1) 
qc.append(g_84ee0d, [1,2,3,0]) 
qc.rz(0.39269908169872414, 3)
qc.p(1.5707963267948966, 0)
qc.append(MCXGate(1), [qreg[3], qreg[2]])
def fun_233051(): 
	qc =  QuantumCircuit(3) 
	qc.p(0.7853981633974483, 2)
	qc.y(0)
	qc.cswap(2, 1, 0)
	return qc.to_gate() 
g_cc500d = fun_233051().control(1) 
qc.append(g_cc500d, [0,3,1,2]) 
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CommutativeInverseCancellation(),CollectMultiQBlocks(),HoareOptimizer()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
