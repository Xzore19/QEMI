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

qc.p(0.7853981633974483, 0)
qc.tdg(0)
def fun_8f1560(): 
	qc =  QuantumCircuit(3) 
	qc.t(0)
	qc.cp(0.39269908169872414, 0, 1)
	qc.cp(0.7853981633974483, 2, 0)
	return qc.to_gate() 
g_6db1f5 = fun_8f1560().control(1) 
qc.append(g_6db1f5, [2,3,1,0]) 
qc.tdg(2)
qc.cswap(2, 1, 0)
a = 0
with qc.for_loop(range(a)) as i_51acd0:
	with qc.for_loop(range(3)) as i_f0e856:
		qc.cx(2, 0)
		def fun_04dffc(): 
			qc =  QuantumCircuit(3) 
			qc.tdg(1)
			qc.cry(0.7853981633974483, 0, 2)
			qc.cx(2, 0)
			return qc.to_gate() 
		g_4b20cd = fun_04dffc().control(1) 
		qc.append(g_4b20cd, [1,0,3,2]) 
		qc.ccx(3, 2, 0)
		qc.cswap(2, 1, 0)
		qc.append(CUGate(2.594, 1.501, 4.837, 3.325), [qreg[0], qreg[3]])
		qc.break_loop()
		qc.ch(3, 0)
		def fun_8ad386(): 
			qc =  QuantumCircuit(3) 
			qc.tdg(0)
			qc.cp(0.7853981633974483, 0, 2)
			qc.t(2)
			return qc.to_gate() 
		g_705d88 = fun_8ad386().control(1) 
		qc.append(g_705d88, [2,3,0,1]) 
		qc.rz(0.39269908169872414, 2)
		qc.append(U3Gate(1.806, 2.107, 3.384), [qreg[1]])
		qc.p(0.7853981633974483, 3)
	
qc.append(U3Gate(2.374, 0.371, 2.412), [qreg[0]])
qc.rz(0.39269908169872414, 3)
qc.iswap(1, 0)
qc.append(QFT(4), [qreg[3], qreg[0], qreg[1], qreg[2]])
def fun_29f391(): 
	qc =  QuantumCircuit(3) 
	qc.cry(1.5707963267948966, 1, 0)
	qc.t(0)
	qc.rx(0.39269908169872414, 1)
	return qc.to_gate() 
g_0dc9e3 = fun_29f391().control(1) 
qc.append(g_0dc9e3, [1,3,0,2]) 
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([ElidePermutations(),Optimize1qGatesSimpleCommutation(),RemoveResetInZeroState()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
