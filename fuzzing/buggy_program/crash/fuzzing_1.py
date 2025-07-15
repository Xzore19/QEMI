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

<<<<<<< HEAD
qreg = QuantumRegister(4) 
creg = ClassicalRegister(4) 
qc = QuantumCircuit(qreg, creg) 

qc.ch(3, 1)
qc.iswap(3, 1)
qc.t(0)
qc.crz(1.5707963267948966, 0, 3)
qc.p(0.39269908169872414, 3)
with qc.for_loop(range(3)) as i_8c6ece:
	
	qr_830316 = QuantumRegister(2)
	cr_830316 = ClassicalRegister(2)
	qc.add_register(qr_830316)
	qc.add_register(cr_830316)
	qc.x(qr_830316[0])
	qc.x(qr_830316[1])
	qc.measure(qr_830316[0], cr_830316[0]) 
	qc.measure(qr_830316[1], cr_830316[1]) 
	with qc.if_test((cr_830316, 0b11)) as else_830316: 
		pass
	with else_830316: 
		qc.tdg(3)
		qc.z(0)
		qc.cx(3, 1)
		qc.ch(1, 0)
		qc.p(0.39269908169872414, 0)
	qc.reset(qr_830316)
	
	qc.continue_loop()
	
	qr_8c6ece = QuantumRegister(2)
	cr_8c6ece = ClassicalRegister(2)
	qc.add_register(qr_8c6ece)
	qc.add_register(cr_8c6ece)
	qc.x(qr_8c6ece[0])
	qc.x(qr_8c6ece[1])
	qc.measure(qr_8c6ece[0], cr_8c6ece[0]) 
	qc.measure(qr_8c6ece[1], cr_8c6ece[1]) 
	with qc.while_loop((cr_8c6ece, 0b10)): 
		qc.ry(0.7853981633974483, 2)
		qc.rz(0.39269908169872414, 1)
		qc.rz(1.5707963267948966, 1)
		qc.cry(0.7853981633974483, 2, 1)
		qc.t(0)
		qc.measure(qr_8c6ece[0], cr_8c6ece[0]) 
		qc.measure(qr_8c6ece[1], cr_8c6ece[1]) 
	qc.reset(qr_8c6ece)
	
qc.h(1)
qc.ccx(3, 1, 0)
qc.p(0.7853981633974483, 3)
qc.ccz(3, 2, 0)
qc.cswap(2, 1, 0)
=======
qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.cx(3, 0)
qc.append(CUGate(1.908, 0.56, 3.374, 0.878), [qreg[4], qreg[3]])
qc.append(QFT(1), [qreg[3]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[2], qreg[1], qreg[0], qreg[3], qreg[4]])
qc.ry(1.5707963267948966, 1)

qr_dfaece = QuantumRegister(2)
cr_dfaece = ClassicalRegister(2)
qc.add_register(qr_dfaece)
qc.add_register(cr_dfaece)
qc.x(qr_dfaece[0])
qc.x(qr_dfaece[1])
qc.measure(qr_dfaece[0], cr_dfaece[0]) 
qc.measure(qr_dfaece[1], cr_dfaece[1]) 
with qc.if_test((cr_dfaece, 0b11)) as else_1: 
	pass
with else_1: 
	
	qr_33d48b = QuantumRegister(2)
	cr_33d48b = ClassicalRegister(2)
	qc.add_register(qr_33d48b)
	qc.add_register(cr_33d48b)
	qc.x(qr_33d48b[0])
	qc.x(qr_33d48b[1])
	qc.measure(qr_33d48b[0], cr_33d48b[0]) 
	qc.measure(qr_33d48b[1], cr_33d48b[1]) 
	with qc.if_test((cr_33d48b, 0b11)) as else_1: 
		qc.append(HGate(), [qreg[3]])
		qc.append(RZGate(2.1), [qreg[3]])
		qc.append(CRXGate(1.925), [qreg[1], qreg[4]])
		qc.append(PauliFeatureMap(2, reps=1, parameter_prefix='x_2b605d'), [qreg[0], qreg[1]])
		qc.append(XOR(4, seed=42), [qreg[4], qreg[0], qreg[1], qreg[2]])
	with else_1: 
		qc.append(CCXGate(), [qreg[2], qreg[3], qreg[1]])
		qc.y(4)
		qc.append(RZGate(0.407), [qreg[4]])
		qc.p(0.7853981633974483, 4)
		qc.append(U3Gate(3.322, 1.386, 4.957), [qreg[2]])
	
	

qc.append(Initialize([(-0.8040761904070083+0.3981863787993072j), (-0.4271771916122071-0.1114842353230044j)]), [qreg[1]])
qc.append(CUGate(3.308, 5.586, 2.761, 3.263), [qreg[2], qreg[4]])
qc.append(RZGate(0.756), [qreg[1]])
qc.ch(4, 2)
qc.append(XGate(), [qreg[4]])
>>>>>>> I forget what I had modified
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
<<<<<<< HEAD
=======
qc.measure(qreg[4], creg[4]) 
>>>>>>> I forget what I had modified

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

<<<<<<< HEAD
p = PassManager([TemplateOptimization(),CollectCliffords(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
=======
p = PassManager(CommutativeInverseCancellation()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
>>>>>>> I forget what I had modified
result = job.result().get_counts() 
print(result)
