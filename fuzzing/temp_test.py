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

qc.append(TwoLocal(3, reps=1, parameter_prefix='theta_4bc563'), [qreg[2], qreg[4], qreg[0]])
qc.ccz(4, 3, 2)
qc.append(CUGate(3.769, 3.26, 6.08, 0.066), [qreg[3], qreg[2]])
qc.cp(1.5707963267948966, 0, 1)
aux_f7a897 = AncillaRegister(1, 'aux_f7a897')
qc.add_register(aux_f7a897)
qc.append(DraperQFTAdder(3), [qreg[3], qreg[0], aux_f7a897[0], qreg[2], qreg[4], qreg[1]])

qr_7ab4bc = QuantumRegister(2)
cr_7ab4bc = ClassicalRegister(2)
qc.add_register(qr_7ab4bc)
qc.add_register(cr_7ab4bc)
qc.x(qr_7ab4bc[0])
qc.x(qr_7ab4bc[1])
qc.measure(qr_7ab4bc[0], cr_7ab4bc[0]) 
qc.measure(qr_7ab4bc[1], cr_7ab4bc[1]) 
with qc.if_test((cr_7ab4bc, 0b11)) as else_1: 
	
	qr_52cca2 = QuantumRegister(2)
	cr_52cca2 = ClassicalRegister(2)
	qc.add_register(qr_52cca2)
	qc.add_register(cr_52cca2)
	qc.x(qr_52cca2[0])
	qc.x(qr_52cca2[1])
	qc.measure(qr_52cca2[0], cr_52cca2[0]) 
	qc.measure(qr_52cca2[1], cr_52cca2[1]) 
	with qc.while_loop((cr_52cca2, 0b10)): 
		qc.append(C3XGate(), [qreg[3], qreg[1], qreg[0], qreg[2]])
		qc.append(CXGate(), [qreg[4], qreg[3]])
		qc.iswap(2, 1)
		qc.append(Permutation(5, pattern=[2, 3, 1, 4, 0]), [qreg[2], qreg[1], qreg[4], qreg[3], qreg[0]])
		qc.append(RZGate(2.186), [qreg[4]])
		qc.measure(qr_52cca2[0], cr_52cca2[0]) 
		qc.measure(qr_52cca2[1], cr_52cca2[1]) 
	
	
with else_1: 
	pass 

qc.append(XGate(), [qreg[4]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[3], qreg[0], qreg[1]])
qc.append(HGate(), [qreg[3]])
qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_d8069f'), [qreg[4], qreg[3]])
qc.append(CRXGate(0.125), [qreg[4], qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(ConsolidateBlocks()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
