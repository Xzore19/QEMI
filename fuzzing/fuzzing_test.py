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

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.append(U3Gate(0.438, 4.91, 5.309), [qreg[2]])
qc.ry(0.39269908169872414, 3)
qc.append(SwapGate(), [qreg[2], qreg[3]])
def fun_c41a08(): 
	qc =  QuantumCircuit(3) 
	qc.z(2)
	qc.x(2)
	qc.t(2)
	return qc.to_gate() 
g_68df79 = fun_c41a08().control(1) 
qc.append(g_68df79, [2,0,4,1]) 
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[1], qreg[2], qreg[3]])
qc.tdg(1)
qc.crx(0.7853981633974483, 2, 3)
with qc.for_loop(range(3)) as i_89f620:
	qc.append(CCXGate(), [qreg[0], qreg[2], qreg[4]])
	qc.ccx(4, 3, 2)
	qc.rx(0.39269908169872414, 4)
	def fun_47410b(): 
		qc =  QuantumCircuit(3) 
		qc.iswap(2, 0)
		qc.swap(2, 0)
		qc.p(1.5707963267948966, 0)
		return qc.to_gate() 
	g_ba29c2 = fun_47410b().control(1) 
	qc.append(g_ba29c2, [0,3,4,2]) 
	def fun_ddf71c(): 
		qc =  QuantumCircuit(3) 
		qc.rz(1.5707963267948966, 0)
		qc.p(0.7853981633974483, 2)
		qc.ccx(2, 1, 0)
		return qc.to_gate() 
	g_e7409e = fun_ddf71c().control(1) 
	qc.append(g_e7409e, [3,0,2,1]) 
	qc.z(2)
	def fun_c7cd0c(): 
		qc =  QuantumCircuit(3) 
		qc.iswap(1, 0)
		qc.t(1)
		qc.p(0.7853981633974483, 2)
		return qc.to_gate() 
	g_7b3d0e = fun_c7cd0c().control(1) 
	qc.append(g_7b3d0e, [0,3,2,4]) 
	qc.break_loop()
	qc.h(3)
	qc.append(RXGate(5.925), [qreg[2]])
	qc.swap(4, 1)
	qc.crx(1.5707963267948966, 2, 0)
	qc.append(HGate(), [qreg[1]])
	qc.cp(0.39269908169872414, 1, 0)
	def fun_4caaae(): 
		qc =  QuantumCircuit(3) 
		qc.iswap(2, 1)
		qc.swap(2, 0)
		qc.ccz(2, 1, 0)
		return qc.to_gate() 
	g_8b780b = fun_4caaae().control(1) 
	qc.append(g_8b780b, [2,3,4,1]) 
qc.append(TwoLocal(2, reps=1, parameter_prefix='theta_9fce73'), [qreg[1], qreg[4]])
def fun_954f93(): 
	qc =  QuantumCircuit(3) 
	qc.tdg(1)
	qc.crx(1.5707963267948966, 2, 1)
	qc.tdg(0)
	return qc.to_gate() 
g_daf7a0 = fun_954f93().control(1) 
qc.append(g_daf7a0, [4,3,0,2]) 
qc.append(CXGate(), [qreg[4], qreg[1]])
qc.cz(0, 1)
qc.swap(2, 1)
qc.cx(3, 1)
qc.p(0.39269908169872414, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveFinalReset(),RemoveIdentityEquivalent(),OptimizeCliffords()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=3200) 
result = job.result().get_counts() 
print(result)
