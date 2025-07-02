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

qc.cry(1.5707963267948966, 3, 0)
qc.append(RXGate(1.399), [qreg[0]])
qc.append(XGate(), [qreg[2]])
qc.append(XGate(), [qreg[3]])
qc.append(U3Gate(2.613, 3.943, 0.454), [qreg[1]])

qr_3565cd = QuantumRegister(2)
cr_3565cd = ClassicalRegister(2)
qc.add_register(qr_3565cd)
qc.add_register(cr_3565cd)
qc.x(qr_3565cd[0])
qc.x(qr_3565cd[1])
qc.measure(qr_3565cd[0], cr_3565cd[0]) 
qc.measure(qr_3565cd[1], cr_3565cd[1]) 
with qc.while_loop((cr_3565cd, 0b11)): 
	qc.measure(qr_3565cd[0], cr_3565cd[0]) 
	qc.measure(qr_3565cd[1], cr_3565cd[1]) 
	
	qr_fedaa7 = QuantumRegister(2)
	cr_fedaa7 = ClassicalRegister(2)
	qc.add_register(qr_fedaa7)
	qc.add_register(cr_fedaa7)
	qc.x(qr_fedaa7[0])
	qc.x(qr_fedaa7[1])
	qc.measure(qr_fedaa7[0], cr_fedaa7[0]) 
	qc.measure(qr_fedaa7[1], cr_fedaa7[1]) 
	with qc.if_test((cr_fedaa7, 0b11)) as else_1: 
		qc.append(RZGate(5.643), [qreg[1]])
		aux_14e3fd = AncillaRegister(3, 'aux_14e3fd')
		qc.add_register(aux_14e3fd)
		qc.append(DraperQFTAdder(4), [qreg[3], qreg[1], aux_14e3fd[2], aux_14e3fd[1], qreg[2], aux_14e3fd[0], qreg[4], qreg[0]])
		aux_b7a77d = AncillaRegister(3, 'aux_b7a77d')
		qc.add_register(aux_b7a77d)
		qc.append(DraperQFTAdder(4), [aux_b7a77d[2], aux_b7a77d[1], qreg[3], aux_b7a77d[0], qreg[0], qreg[4], qreg[2], qreg[1]])
		qc.append(CXGate(), [qreg[3], qreg[2]])
		qc.cry(1.5707963267948966, 4, 1)
	with else_1: 
		qc.append(RZGate(2.849), [qreg[0]])
		qc.append(PauliFeatureMap(2, reps=1, parameter_prefix='x_a71b61'), [qreg[0], qreg[1]])
		aux_71a1e4 = AncillaRegister(1, 'aux_71a1e4')
		qc.add_register(aux_71a1e4)
		qc.append(DraperQFTAdder(3), [qreg[2], qreg[1], qreg[4], aux_71a1e4[0], qreg[3], qreg[0]])
		qc.ry(1.5707963267948966, 0)
		qc.append(CXGate(), [qreg[1], qreg[0]])
	
	
	qc.break_loop()
qc.append(CUGate(0.22, 4.834, 0.939, 5.56), [qreg[0], qreg[1]])
qc.append(U3Gate(0.446, 2.797, 3.717), [qreg[4]])
qc.append(HGate(), [qreg[4]])
aux_50732d = AncillaRegister(3, 'aux_50732d')
qc.add_register(aux_50732d)
qc.append(DraperQFTAdder(4), [aux_50732d[0], qreg[3], qreg[4], qreg[2], aux_50732d[1], qreg[1], qreg[0], aux_50732d[2]])
qc.append(DraperQFTAdder(2), [qreg[1], qreg[4], qreg[0], qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Collect2qBlocks()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
