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

qc.append(CXGate(), [qreg[0], qreg[4]])
qc.append(CRXGate(4.02), [qreg[2], qreg[4]])
aux_f27db3 = AncillaRegister(5, 'aux_f27db3')
qc.add_register(aux_f27db3)
qc.append(DraperQFTAdder(5), [aux_f27db3[3], qreg[2], aux_f27db3[4], aux_f27db3[0], qreg[4], qreg[1], qreg[0], aux_f27db3[1], aux_f27db3[2], qreg[3]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[0], qreg[3]])
qc.ccz(3, 2, 1)

qr_d02f03 = QuantumRegister(2)
cr_d02f03 = ClassicalRegister(2)
qc.add_register(qr_d02f03)
qc.add_register(cr_d02f03)
qc.x(qr_d02f03[0])
qc.x(qr_d02f03[1])
qc.measure(qr_d02f03[0], cr_d02f03[0]) 
qc.measure(qr_d02f03[1], cr_d02f03[1]) 
with qc.if_test((cr_d02f03, 0b11)) as else_1: 
	
	qr_73e5dd = QuantumRegister(2)
	cr_73e5dd = ClassicalRegister(2)
	qc.add_register(qr_73e5dd)
	qc.add_register(cr_73e5dd)
	qc.x(qr_73e5dd[0])
	qc.x(qr_73e5dd[1])
	qc.measure(qr_73e5dd[0], cr_73e5dd[0]) 
	qc.measure(qr_73e5dd[1], cr_73e5dd[1]) 
	with qc.while_loop((cr_73e5dd, 0b10)): 
		qc.append(U3Gate(2.993, 5.923, 3.553), [qreg[3]])
		qc.crz(1.5707963267948966, 0, 1)
		qc.append(XGate(), [qreg[0]])
		qc.append(RZGate(0.724), [qreg[4]])
		aux_f7568b = AncillaRegister(5, 'aux_f7568b')
		qc.add_register(aux_f7568b)
		qc.append(DraperQFTAdder(5), [qreg[2], aux_f7568b[1], aux_f7568b[4], qreg[3], qreg[4], qreg[1], aux_f7568b[2], qreg[0], aux_f7568b[3], aux_f7568b[0]])
		qc.measure(qr_73e5dd[0], cr_73e5dd[0]) 
		qc.measure(qr_73e5dd[1], cr_73e5dd[1]) 
	
	
with else_1: 
	pass 

qc.p(0.39269908169872414, 2)
qc.append(U3Gate(1.03, 2.296, 1.401), [qreg[1]])
qc.append(Diagonal(np.array([np.complex128(0.7912917092076378-0.6114388202749765j), np.complex128(0.10119276761749965-0.9948668372108453j), np.complex128(0.21193004828878348+0.9772848380243674j), np.complex128(0.9863561729631329-0.16462533236875257j)])), [qreg[0], qreg[3]])
qc.append(C3XGate(), [qreg[0], qreg[2], qreg[3], qreg[1]])
qc.append(HGate(), [qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGatesDecomposition()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
