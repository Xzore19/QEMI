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

qc.rx(0.39269908169872414, 0)
qc.p(0.7853981633974483, 2)
qc.cswap(3, 2, 0)
qc.cry(0.39269908169872414, 1, 2)
def fun_727689(): 
	qc =  QuantumCircuit(3) 
	qc.iswap(2, 0)
	qc.rx(1.5707963267948966, 1)
	qc.rx(1.5707963267948966, 0)
	return qc.to_gate() 
g_ab496c = fun_727689().control(1) 
qc.append(g_ab496c, [3,1,0,2]) 
with qc.for_loop(range(3)) as i_71ece3:
	with qc.for_loop(range(3)) as i_1dffc1:
		qc.ccz(3, 1, 0)
		qc.append(C3XGate(), [qreg[1], qreg[0], qreg[3], qreg[2]])
		qc.x(1)
		def fun_03e927(): 
			qc =  QuantumCircuit(3) 
			qc.t(1)
			qc.cry(0.7853981633974483, 0, 2)
			qc.tdg(0)
			return qc.to_gate() 
		g_bf382a = fun_03e927().control(1) 
		qc.append(g_bf382a, [1,2,3,0]) 
		qc.append(DraperQFTAdder(2), [qreg[1], qreg[3], qreg[2], qreg[0]])
		qc.break_loop()
		qc.ccx(3, 2, 0)
		qc.iswap(3, 1)
		qc.append(C3XGate(), [qreg[3], qreg[2], qreg[0], qreg[1]])
		def fun_bbde5f(): 
			qc =  QuantumCircuit(3) 
			qc.rz(0.7853981633974483, 1)
			qc.p(1.5707963267948966, 0)
			qc.crx(1.5707963267948966, 1, 0)
			return qc.to_gate() 
		g_c06253 = fun_bbde5f().control(1) 
		qc.append(g_c06253, [0,1,3,2]) 
		qc.z(3)
	
	qc.continue_loop()
	
	qr_71ece3 = QuantumRegister(2)
	cr_71ece3 = ClassicalRegister(2)
	qc.add_register(qr_71ece3)
	qc.add_register(cr_71ece3)
	qc.h(qr_71ece3[0])
	qc.cx(qr_71ece3[0], qr_71ece3[1])         
	qc.measure(qr_71ece3[0], cr_71ece3[0]) 
	qc.measure(qr_71ece3[1], cr_71ece3[1]) 
	with qc.switch(cr_71ece3) as case: 
		with case(0b00, 0b11): 
			qc.append(RXGate(5.079), [qreg[3]])
			qc.append(Isometry(np.array([[1.0, 0.0], [0.0, 1.0]]), 0, 0), [qreg[1]])
			qc.x(0)
			qc.append(NLocal(4, reps=1, parameter_prefix='theta_43646d'), [qreg[1], qreg[3], qreg[0], qreg[2]])
			qc.append(Diagonal(np.array([np.complex128(-0.07411927188734996+0.9972493838227673j), np.complex128(-0.7096598557932697-0.7045444550030009j)])), [qreg[1]])
		with case(case.DEFAULT): 
			qc.ccz(2, 1, 0)
			qc.append(HGate(), [qreg[1]])
			qc.swap(2, 1)
			qc.append(RXGate(3.075), [qreg[1]])
			qc.append(U3Gate(2.648, 6.051, 0.22), [qreg[3]])
	qc.reset(qr_71ece3)
	
qc.cswap(2, 1, 0)
qc.cz(0, 3)
qc.append(CRXGate(0.946), [qreg[1], qreg[2]])
qc.ccx(3, 2, 1)
def fun_5318c3(): 
	qc =  QuantumCircuit(3) 
	qc.cx(2, 1)
	qc.iswap(1, 0)
	qc.x(0)
	return qc.to_gate() 
g_9ced98 = fun_5318c3().control(1) 
qc.append(g_9ced98, [2,0,1,3]) 
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CommutativeInverseCancellation(),Optimize1qGatesSimpleCommutation(),Optimize1qGates()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
