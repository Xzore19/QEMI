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

def fun_165819(): 
	qc =  QuantumCircuit(3) 
	qc.crx(0.7853981633974483, 1, 2)
	qc.cz(0, 2)
	qc.cp(0.39269908169872414, 2, 1)
	return qc.to_gate() 
g_ddff4e = fun_165819().control(1) 
qc.append(g_ddff4e, [0,2,3,4]) 
qc.rz(0.7853981633974483, 3)
qc.swap(1, 0)
def fun_2bf06e(): 
	qc =  QuantumCircuit(3) 
	qc.y(2)
	qc.z(1)
	qc.cry(1.5707963267948966, 2, 0)
	return qc.to_gate() 
g_060b5c = fun_2bf06e().control(1) 
qc.append(g_060b5c, [0,2,3,4]) 
qc.ch(2, 0)
qc.crz(1.5707963267948966, 0, 2)
qc.cswap(4, 1, 0)
def fun_581ba4(): 
	qc =  QuantumCircuit(3) 
	qc.ry(0.39269908169872414, 1)
	qc.h(0)
	qc.cx(2, 1)
	return qc.to_gate() 
g_3f56f6 = fun_581ba4().control(1) 
qc.append(g_3f56f6, [4,2,3,0]) 
qc.append(CRXGate(0.855), [qreg[0], qreg[1]])
def fun_7fc247(): 
	qc =  QuantumCircuit(3) 
	qc.ry(1.5707963267948966, 0)
	qc.t(1)
	qc.p(1.5707963267948966, 0)
	return qc.to_gate() 
g_f4c727 = fun_7fc247().control(1) 
qc.append(g_f4c727, [0,4,1,2]) 
qc.ch(3, 0)
qc.cx(4, 3)
qc.z(4)
qc.append(U3Gate(5.805, 3.139, 1.149), [qreg[4]])
qc.cry(1.5707963267948966, 1, 0)
pass
def fun_ae942c(): 
	qc =  QuantumCircuit(3) 
	qc.y(1)
	qc.cz(0, 1)
	qc.cp(0.39269908169872414, 2, 1)
	return qc.to_gate() 
g_6cbeaa = fun_ae942c().control(1) 
qc.append(g_6cbeaa, [3,1,2,0]) 
def fun_b46d23(): 
	qc =  QuantumCircuit(3) 
	qc.rz(0.7853981633974483, 1)
	qc.crz(1.5707963267948966, 0, 1)
	qc.rz(0.7853981633974483, 2)
	return qc.to_gate() 
g_6ce2f6 = fun_b46d23().control(1) 
qc.append(g_6ce2f6, [3,1,2,0]) 
qc.t(3)
qc.append(Initialize([(-0.10929250297514027+0.07634295421244752j), (-0.1663830001507047+0.9770074715151342j)]), [qreg[4]])
def fun_ca9cb0(): 
	qc =  QuantumCircuit(3) 
	qc.ccz(2, 1, 0)
	qc.crx(1.5707963267948966, 0, 1)
	qc.ry(0.7853981633974483, 1)
	return qc.to_gate() 
g_bedb52 = fun_ca9cb0().control(1) 
qc.append(g_bedb52, [0,4,3,1]) 
qc.crx(1.5707963267948966, 0, 2)
def fun_717bd8(): 
	qc =  QuantumCircuit(3) 
	qc.p(0.39269908169872414, 1)
	qc.ccz(2, 1, 0)
	qc.rz(0.7853981633974483, 0)
	return qc.to_gate() 
g_ac03c2 = fun_717bd8().control(1) 
qc.append(g_ac03c2, [4,3,2,0]) 
qc.crx(0.7853981633974483, 2, 1)
qc.crz(0.39269908169872414, 3, 4)
qc.t(4)
qc.cry(0.39269908169872414, 4, 2)
qc.ccz(4, 2, 0)
qc.swap(4, 2)
qc.rz(1.5707963267948966, 1)
def fun_c1778e(): 
	qc =  QuantumCircuit(3) 
	qc.ry(0.7853981633974483, 1)
	qc.x(1)
	qc.ry(0.7853981633974483, 2)
	return qc.to_gate() 
g_838dfb = fun_c1778e().control(1) 
qc.append(g_838dfb, [2,0,1,4]) 
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CommutativeInverseCancellation(),RemoveFinalReset(),RemoveIdentityEquivalent()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
