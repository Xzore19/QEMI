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

qc.append(CCXGate(), [qreg[3], qreg[1], qreg[4]])
aux_c415d5 = AncillaRegister(5, 'aux_c415d5')
qc.add_register(aux_c415d5)
qc.append(DraperQFTAdder(5), [aux_c415d5[3], aux_c415d5[1], qreg[2], qreg[3], aux_c415d5[4], qreg[4], qreg[1], aux_c415d5[2], qreg[0], aux_c415d5[0]])
qc.append(CUGate(1.96, 3.066, 4.638, 0.593), [qreg[0], qreg[3]])
qc.cry(0.7853981633974483, 4, 0)
aux_cfb499 = AncillaRegister(5, 'aux_cfb499')
qc.add_register(aux_cfb499)
qc.append(DraperQFTAdder(5), [qreg[3], aux_cfb499[3], qreg[4], aux_cfb499[1], aux_cfb499[0], qreg[2], aux_cfb499[4], qreg[0], qreg[1], aux_cfb499[2]])
with qc.for_loop(range(3)) as i:
	
	qr_e4fa33 = QuantumRegister(2)
	cr_e4fa33 = ClassicalRegister(2)
	qc.add_register(qr_e4fa33)
	qc.add_register(cr_e4fa33)
	qc.x(qr_e4fa33[0])
	qc.x(qr_e4fa33[1])
	qc.measure(qr_e4fa33[0], cr_e4fa33[0]) 
	qc.measure(qr_e4fa33[1], cr_e4fa33[1]) 
	with qc.if_test((cr_e4fa33, 0b11)) as else_1: 
		qc.append(Permutation(4, pattern=[1, 2, 0, 3]), [qreg[2], qreg[1], qreg[3], qreg[4]])
		qc.append(Diagonal(np.array([np.complex128(0.22788585467211767+0.9736878541094977j), np.complex128(-0.10621198007289596-0.9943435097032588j), np.complex128(0.3657186717879957+0.9307254445354034j), np.complex128(-0.9837445352255548-0.17957363229009154j), np.complex128(0.14586458415279543+0.9893045653841551j), np.complex128(-0.9250150517408299-0.3799304594960896j), np.complex128(-0.7359037380281842-0.6770861749852419j), np.complex128(-0.9482498192742984-0.3175252434787828j), np.complex128(0.702516836222384+0.7116671236077243j), np.complex128(0.9484641251476261+0.31688452677268464j), np.complex128(-0.8263633843058942+0.5631372453305757j), np.complex128(-0.44455320748884997-0.8957524466678143j), np.complex128(0.3603798634588544+0.9328056357105575j), np.complex128(-0.9966247261506742-0.08209235789702785j), np.complex128(-0.12235484335133813+0.9924864192060612j), np.complex128(-0.7260150619932128-0.687678798392819j)])), [qreg[0], qreg[2], qreg[4], qreg[3]])
		qc.x(3)
		qc.h(2)
		qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_39b054'), [qreg[3], qreg[0]])
	with else_1: 
		aux_f7f6f2 = AncillaRegister(5, 'aux_f7f6f2')
		qc.add_register(aux_f7f6f2)
		qc.append(DraperQFTAdder(5), [qreg[4], aux_f7f6f2[3], qreg[1], aux_f7f6f2[1], qreg[0], aux_f7f6f2[0], qreg[2], qreg[3], aux_f7f6f2[4], aux_f7f6f2[2]])
		qc.append(C3XGate(), [qreg[0], qreg[1], qreg[4], qreg[3]])
		qc.rz(1.5707963267948966, 1)
		qc.append(Initialize([(0.7596172455186108-0.45003876788373054j), (0.21278394427738673+0.41853284312007155j)]), [qreg[1]])
		qc.append(U3Gate(6.093, 5.62, 1.644), [qreg[3]])
	
	
	qc.continue_loop()
qc.append(CCXGate(), [qreg[3], qreg[2], qreg[1]])
qc.append(Initialize([(0.4363427340506955+0.1682737950456943j), (-0.10772830530908506+0.4835264310339265j), (0.6301644832609657+0.11945481870056689j), (-0.3415717615961419-0.08853108535804206j)]), [qreg[2], qreg[0]])
qc.p(1.5707963267948966, 3)
qc.append(AND(3), [qreg[1], qreg[4], qreg[3], qreg[2]])
qc.cx(4, 1)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(ResetAfterMeasureSimplification()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
