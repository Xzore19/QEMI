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

qc.append(RZGate(2.906), [qreg[0]])
qc.append(RZGate(0.907), [qreg[0]])
qc.append(RZGate(2.849), [qreg[4]])
qc.append(Isometry(np.array([[1.0, 0.0], [0.0, 1.0]]), 0, 0), [qreg[2]])
aux_add968 = QuantumRegister(5, 'aux_add968')
qc.add_register(aux_add968)
qc.append(DraperQFTAdder(5), [qreg[0], qreg[1], aux_add968[1], qreg[3], aux_add968[0], aux_add968[4], aux_add968[3], qreg[4], qreg[2], aux_add968[2]])
with qc.for_loop(range(3)) as i:
	
	qr_734e37 = AncillaRegister(2)
	cr_734e37 = ClassicalRegister(2)
	qc.add_register(qr_734e37)
	qc.add_register(cr_734e37)
	qc.x(qr_734e37[0])
	qc.x(qr_734e37[1])
	qc.measure(qr_734e37[0], cr_734e37[0]) 
	qc.measure(qr_734e37[1], cr_734e37[1]) 
	with qc.if_test((cr_734e37, 0b11)) as else_1: 
		pass
	with else_1: 
		qc.append(ZFeatureMap(2, reps=1, parameter_prefix='x_b119c7'), [qreg[3], qreg[4]])
		qc.append(C3XGate(), [qreg[2], qreg[0], qreg[3], qreg[4]])
		qc.append(SwapGate(), [qreg[4], qreg[0]])
		qc.append(CRXGate(3.212), [qreg[1], qreg[3]])
		qc.append(RZGate(4.671), [qreg[4]])
	
	qc.continue_loop()
	
	qr_d8b2d9 = AncillaRegister(2)
	cr_d8b2d9 = ClassicalRegister(2)
	qc.add_register(qr_d8b2d9)
	qc.add_register(cr_d8b2d9)
	qc.x(qr_d8b2d9[0])
	qc.x(qr_d8b2d9[1])
	qc.measure(qr_d8b2d9[0], cr_d8b2d9[0]) 
	qc.measure(qr_d8b2d9[1], cr_d8b2d9[1]) 
	with qc.if_test((cr_d8b2d9, 0b11)) as else_1: 
		pass
	with else_1: 
		qc.append(U3Gate(2.922, 0.267, 1.154), [qreg[1]])
		qc.append(CXGate(), [qreg[1], qreg[0]])
		aux_1e16df = AncillaRegister(5, 'aux_1e16df')
		qc.add_register(aux_1e16df)
		qc.append(DraperQFTAdder(5), [aux_1e16df[1], aux_1e16df[2], qreg[1], qreg[2], qreg[3], qreg[4], aux_1e16df[4], aux_1e16df[3], aux_1e16df[0], qreg[0]])
		aux_23a31a = AncillaRegister(3, 'aux_23a31a')
		qc.add_register(aux_23a31a)
		qc.append(DraperQFTAdder(4), [aux_23a31a[2], aux_23a31a[0], qreg[0], aux_23a31a[1], qreg[3], qreg[4], qreg[2], qreg[1]])
		qc.append(MCXGate(3), [qreg[3], qreg[4], qreg[1], qreg[2]])
	
	
qc.ry(0.7853981633974483, 4)
qc.append(CXGate(), [qreg[2], qreg[1]])
qc.append(SwapGate(), [qreg[1], qreg[4]])
qc.p(0.39269908169872414, 2)
qc.append(XGate(), [qreg[1]])
# qc.measure(qreg[0], creg[0]) 
# qc.measure(qreg[1], creg[1]) 
# qc.measure(qreg[2], creg[2]) 
# qc.measure(qreg[3], creg[3]) 
# qc.measure(qreg[4], creg[4]) 

qc.measure_all()

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(CollectMultiQBlocks()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=1) 
result = job.result().get_counts() 
print(result)
