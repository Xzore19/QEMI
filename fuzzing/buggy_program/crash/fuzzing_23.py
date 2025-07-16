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
		def fun_925e37(): 
			qc =  QuantumCircuit(3) 
			qc.ry(1.5707963267948966, 1)
			qc.swap(2, 1)
			qc.cz(0, 2)
			return qc.to_gate() 
		g_3c79ec = fun_925e37().control(1) 
		qc.append(g_3c79ec, [2,1,3,0]) 
		def fun_99e3aa(): 
			qc =  QuantumCircuit(3) 
			qc.crz(0.39269908169872414, 2, 0)
			qc.y(2)
			qc.cp(0.7853981633974483, 0, 1)
			return qc.to_gate() 
		g_88a410 = fun_99e3aa().control(1) 
		qc.append(g_88a410, [0,1,2,3]) 
		qc.tdg(0)
		def fun_a0f0e8(): 
			qc =  QuantumCircuit(3) 
			qc.ccx(2, 1, 0)
			qc.y(2)
			qc.rz(0.39269908169872414, 1)
			return qc.to_gate() 
		g_0d7a33 = fun_a0f0e8().control(1) 
		qc.append(g_0d7a33, [1,0,3,2]) 
		qc.cry(0.7853981633974483, 1, 3)
	
	qc.continue_loop()
	
	qr_194e18 = QuantumRegister(2)
	cr_194e18 = ClassicalRegister(2)
	qc.add_register(qr_194e18)
	qc.add_register(cr_194e18)
	qc.h(qr_194e18[0])
	qc.cx(qr_194e18[0], qr_194e18[1])         
	qc.measure(qr_194e18[0], cr_194e18[0]) 
	qc.measure(qr_194e18[1], cr_194e18[1]) 
	with qc.switch(cr_194e18) as case: 
		with case(0b00, 0b11): 
			qc.append(C3XGate(), [qreg[0], qreg[3], qreg[2], qreg[1]])
			qc.p(0.39269908169872414, 3)
			qc.crz(1.5707963267948966, 3, 2)
			qc.y(1)
			qc.y(2)
		with case(case.DEFAULT): 
			qc.ch(3, 1)
			qc.rx(1.5707963267948966, 3)
			qc.z(3)
			qc.swap(3, 0)
			aux_82f8a8 = AncillaRegister(2, 'aux_82f8a8')
			qc.add_register(aux_82f8a8)
			qc.append(DraperQFTAdder(3), [qreg[0], aux_82f8a8[0], qreg[1], qreg[3], aux_82f8a8[1], qreg[2]])
	qc.reset(qr_194e18)
	
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
