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

qc.cp(1.5707963267948966, 1, 2)
qc.tdg(0)
qc.append(CXGate(), [qreg[3], qreg[0]])
qc.crz(1.5707963267948966, 1, 0)
def fun_52312a(): 
	qc =  QuantumCircuit(3) 
	qc.ccz(2, 1, 0)
	qc.ccx(2, 1, 0)
	qc.rz(0.7853981633974483, 0)
	return qc.to_gate() 
g_b6117a = fun_52312a().control(1) 
qc.append(g_b6117a, [2,3,0,1]) 
a = 0
with qc.for_loop(range(a)) as i_6a345d:
	a = 0
	with qc.for_loop(range(a)) as i_cb100c:
		qc.tdg(2)
		qc.append(CRXGate(4.32), [qreg[3], qreg[0]])
		qc.z(2)
		qc.cswap(3, 1, 0)
		qc.rx(0.7853981633974483, 2)
	
qc.append(CRXGate(3.955), [qreg[0], qreg[2]])
qc.append(XGate(), [qreg[0]])
qc.tdg(3)
def fun_7bfa88(): 
	qc =  QuantumCircuit(3) 
	qc.z(1)
	qc.y(1)
	qc.h(0)
	return qc.to_gate() 
g_962b8f = fun_7bfa88().control(1) 
qc.append(g_962b8f, [0,1,3,2]) 
qc.ch(3, 2)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CommutativeInverseCancellation(),CommutationAnalysis(),OptimizeCliffords()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
