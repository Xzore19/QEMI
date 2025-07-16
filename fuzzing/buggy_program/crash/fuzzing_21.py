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

qc.tdg(0)
qc.cswap(2, 1, 0)
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[2], qreg[0]])
qc.append(SwapGate(), [qreg[2], qreg[0]])
def fun_d22dd8(): 
	qc =  QuantumCircuit(3) 
	qc.tdg(0)
	qc.p(1.5707963267948966, 0)
	qc.swap(2, 1)
	return qc.to_gate() 
g_be365f = fun_d22dd8().control(1) 
qc.append(g_be365f, [1,2,0,3]) 
a = 0
with qc.for_loop(range(a)) as i_0abbcc:
	with qc.for_loop(range(3)) as i_661b06:
		qc.rz(0.39269908169872414, 1)
		qc.swap(2, 0)
		def fun_15cca4(): 
			qc =  QuantumCircuit(3) 
			qc.crz(1.5707963267948966, 0, 1)
			qc.rx(0.39269908169872414, 2)
			qc.crx(1.5707963267948966, 0, 1)
			return qc.to_gate() 
		g_b2d88e = fun_15cca4().control(1) 
		qc.append(g_b2d88e, [1,2,0,3]) 
		qc.append(Diagonal(np.array([np.complex128(-0.704607364168713+0.7095973945549819j), np.complex128(-0.5914055082255699+0.8063743081475595j)])), [qreg[2]])
		qc.crx(0.39269908169872414, 2, 3)
		qc.break_loop()
		qc.append(CRXGate(5.165), [qreg[2], qreg[1]])
		qc.rx(1.5707963267948966, 1)
		def fun_21a6de(): 
			qc =  QuantumCircuit(3) 
			qc.y(2)
			qc.cswap(2, 1, 0)
			qc.swap(1, 0)
			return qc.to_gate() 
		g_fe9adb = fun_21a6de().control(1) 
		qc.append(g_fe9adb, [2,0,1,3]) 
		qc.crx(0.7853981633974483, 2, 3)
		qc.append(ZZFeatureMap(2, reps=1, parameter_prefix='x_6abd97'), [qreg[3], qreg[1]])
	
qc.append(ZFeatureMap(2, reps=1, parameter_prefix='x_9519e2'), [qreg[2], qreg[3]])
qc.cswap(3, 2, 0)
qc.swap(3, 1)
qc.append(CUGate(2.962, 5.556, 1.287, 3.445), [qreg[2], qreg[1]])
qc.append(RXGate(5.037), [qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([Collect1qRuns(),OptimizeAnnotated(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
