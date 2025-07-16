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

qc.x(2)
def fun_43e7ab(): 
	qc =  QuantumCircuit(3) 
	qc.ccx(2, 1, 0)
	qc.cx(2, 1)
	qc.t(0)
	return qc.to_gate() 
g_0a2703 = fun_43e7ab().control(1) 
qc.append(g_0a2703, [3,0,1,2]) 
qc.p(0.7853981633974483, 1)
qc.crz(0.7853981633974483, 2, 3)
qc.ccz(4, 3, 0)
def fun_5c4f0d(): 
	qc =  QuantumCircuit(3) 
	qc.cx(2, 1)
	qc.p(0.39269908169872414, 0)
	qc.cswap(2, 1, 0)
	return qc.to_gate() 
g_3602c7 = fun_5c4f0d().control(1) 
qc.append(g_3602c7, [4,2,0,3]) 
def fun_2f9c1d(): 
	qc =  QuantumCircuit(3) 
	qc.cry(0.39269908169872414, 0, 2)
	qc.crx(0.39269908169872414, 0, 2)
	qc.h(2)
	return qc.to_gate() 
g_083228 = fun_2f9c1d().control(1) 
qc.append(g_083228, [0,4,1,2]) 
qc.ch(4, 2)
qc.crz(0.7853981633974483, 4, 1)
qc.append(CXGate(), [qreg[2], qreg[1]])
qc.append(U3Gate(4.45, 4.21, 0.261), [qreg[4]])
qc.y(2)
qc.tdg(3)
def fun_154389(): 
	qc =  QuantumCircuit(3) 
	qc.z(1)
	qc.rz(0.39269908169872414, 2)
	qc.cry(0.39269908169872414, 2, 0)
	return qc.to_gate() 
g_99c911 = fun_154389().control(1) 
qc.append(g_99c911, [0,4,1,3]) 
qc.cx(3, 0)
with qc.for_loop(range(3)) as i_1f4340:
	pass
	
	qc.continue_loop()
qc.append(Initialize([(-0.7534410234367523+0.448413723879295j), (-0.45767201451838735+0.14760787094855002j)]), [qreg[2]])
qc.cry(1.5707963267948966, 2, 4)
def fun_b4503f(): 
	qc =  QuantumCircuit(3) 
	qc.x(2)
	qc.cz(0, 2)
	qc.swap(2, 1)
	return qc.to_gate() 
g_c75a51 = fun_b4503f().control(1) 
qc.append(g_c75a51, [3,4,1,0]) 
qc.append(XOR(3, seed=42), [qreg[4], qreg[2], qreg[1]])
def fun_70f31c(): 
	qc =  QuantumCircuit(3) 
	qc.cry(1.5707963267948966, 2, 0)
	qc.crz(0.7853981633974483, 0, 1)
	qc.cp(0.39269908169872414, 1, 2)
	return qc.to_gate() 
g_036836 = fun_70f31c().control(1) 
qc.append(g_036836, [2,3,4,0]) 
qc.crz(0.39269908169872414, 3, 0)
qc.cswap(4, 3, 1)
qc.append(XGate(), [qreg[0]])
qc.append(U3Gate(0.372, 0.484, 3.499), [qreg[3]])
qc.p(0.7853981633974483, 2)
qc.append(RXGate(0.836), [qreg[0]])
qc.append(XGate(), [qreg[2]])
qc.iswap(4, 1)
qc.rz(0.39269908169872414, 0)
def fun_7a46cb(): 
	qc =  QuantumCircuit(3) 
	qc.x(1)
	qc.cswap(2, 1, 0)
	qc.x(2)
	return qc.to_gate() 
g_9332ad = fun_7a46cb().control(1) 
qc.append(g_9332ad, [1,0,2,3]) 
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([OptimizeSwapBeforeMeasure(),CommutativeInverseCancellation(),ResetAfterMeasureSimplification()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
