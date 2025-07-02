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

qc.append(MCPhaseGate(1.0, num_ctrl_qubits=2), [qreg[4], qreg[1], qreg[2]])
qc.append(TwoLocal(4, reps=1, parameter_prefix='theta_c97e18'), [qreg[1], qreg[2], qreg[4], qreg[3]])
qc.append(C3XGate(), [qreg[4], qreg[2], qreg[0], qreg[1]])
qc.append(RXGate(4.771), [qreg[1]])
aux_a50f29 = AncillaRegister(5, 'aux_a50f29')
qc.add_register(aux_a50f29)
qc.append(DraperQFTAdder(5), [qreg[1], aux_a50f29[0], qreg[2], qreg[0], qreg[3], aux_a50f29[1], aux_a50f29[3], aux_a50f29[4], qreg[4], aux_a50f29[2]])

qr_9f8e97 = QuantumRegister(2)
cr_9f8e97 = ClassicalRegister(2)
qc.add_register(qr_9f8e97)
qc.add_register(cr_9f8e97)
qc.x(qr_9f8e97[0])
qc.x(qr_9f8e97[1])
qc.measure(qr_9f8e97[0], cr_9f8e97[0]) 
qc.measure(qr_9f8e97[1], cr_9f8e97[1]) 
with qc.if_test((cr_9f8e97, 0b11)) as else_1: 
	
	qr_65d26d = QuantumRegister(2)
	cr_65d26d = ClassicalRegister(2)
	qc.add_register(qr_65d26d)
	qc.add_register(cr_65d26d)
	qc.x(qr_65d26d[0])
	qc.x(qr_65d26d[1])
	qc.measure(qr_65d26d[0], cr_65d26d[0]) 
	qc.measure(qr_65d26d[1], cr_65d26d[1]) 
	with qc.while_loop((cr_65d26d, 0b11)): 
		qc.measure(qr_65d26d[0], cr_65d26d[0]) 
		qc.measure(qr_65d26d[1], cr_65d26d[1]) 
		aux_bf960f = AncillaRegister(5, 'aux_bf960f')
		qc.add_register(aux_bf960f)
		qc.append(DraperQFTAdder(5), [aux_bf960f[0], qreg[1], aux_bf960f[3], qreg[0], aux_bf960f[4], qreg[3], qreg[2], aux_bf960f[2], qreg[4], aux_bf960f[1]])
		qc.append(RXGate(3.018), [qreg[0]])
		qc.p(1.5707963267948966, 3)
		aux_4c79a7 = AncillaRegister(3, 'aux_4c79a7')
		qc.add_register(aux_4c79a7)
		qc.append(DraperQFTAdder(4), [qreg[1], qreg[4], aux_4c79a7[0], aux_4c79a7[1], qreg[2], aux_4c79a7[2], qreg[0], qreg[3]])
		qc.append(XGate(), [qreg[0]])
		qc.break_loop()
		qc.ccz(2, 1, 0)
		qc.append(EfficientSU2(5, reps=1, parameter_prefix='theta_5cf175'), [qreg[3], qreg[4], qreg[2], qreg[1], qreg[0]])
		qc.cswap(4, 2, 1)
		qc.append(U3Gate(5.561, 3.438, 0.423), [qreg[2]])
		qc.append(HGate(), [qreg[4]])
	
with else_1: 
	
	qr_9f8e97 = QuantumRegister(2)
	cr_9f8e97 = ClassicalRegister(2)
	qc.add_register(qr_9f8e97)
	qc.add_register(cr_9f8e97)
	qc.x(qr_9f8e97[0])
	qc.x(qr_9f8e97[1])
	qc.measure(qr_9f8e97[0], cr_9f8e97[0]) 
	qc.measure(qr_9f8e97[1], cr_9f8e97[1]) 
	with qc.while_loop((cr_9f8e97, 0b11)): 
		qc.measure(qr_9f8e97[0], cr_9f8e97[0]) 
		qc.measure(qr_9f8e97[1], cr_9f8e97[1]) 
		qc.append(MCXGate(2), [qreg[3], qreg[1], qreg[2]])
		qc.append(RZGate(5.228), [qreg[2]])
		qc.tdg(1)
		qc.append(XGate(), [qreg[1]])
		qc.append(RXGate(6.194), [qreg[0]])
		qc.break_loop()
		qc.append(CUGate(1.441, 5.008, 5.559, 5.629), [qreg[3], qreg[1]])
		qc.t(4)
		qc.append(U3Gate(3.49, 3.674, 5.729), [qreg[0]])
		qc.append(U3Gate(1.884, 5.987, 5.576), [qreg[2]])
		qc.append(CXGate(), [qreg[2], qreg[1]])
	

qc.append(CCXGate(), [qreg[1], qreg[3], qreg[4]])
qc.append(CUGate(5.154, 5.065, 0.859, 0.481), [qreg[4], qreg[0]])
qc.append(CRXGate(0.05), [qreg[0], qreg[3]])
qc.append(RXGate(5.886), [qreg[0]])
qc.rz(1.5707963267948966, 3)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(RemoveDiagonalGatesBeforeMeasure()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
