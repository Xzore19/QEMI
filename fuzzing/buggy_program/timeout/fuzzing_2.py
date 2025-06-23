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

qc.append(HGate(), [qreg[2]])
qc.append(RXGate(4.468), [qreg[3]])
qc.append(XGate(), [qreg[1]])
qc.ccx(3, 2, 0)
qc.append(Permutation(2, pattern=[0, 1]), [qreg[1], qreg[2]])
with qc.for_loop(range(3)) as i:
	
	qr_e049ce = QuantumRegister(2)
	cr_e049ce = ClassicalRegister(2)
	qc.add_register(qr_e049ce)
	qc.add_register(cr_e049ce)
	qc.x(qr_e049ce[0])
	qc.x(qr_e049ce[1])
	qc.measure(qr_e049ce[0], cr_e049ce[0]) 
	qc.measure(qr_e049ce[1], cr_e049ce[1]) 
	with qc.if_test((cr_e049ce, 0b11)) as else_1: 
		qc.append(RXGate(6.092), [qreg[3]])
		qc.append(PauliFeatureMap(4, reps=1, parameter_prefix='x_d18cec'), [qreg[4], qreg[0], qreg[1], qreg[3]])
		qc.append(MCPhaseGate(1.0, num_ctrl_qubits=3), [qreg[1], qreg[4], qreg[3], qreg[0]])
		qc.append(HGate(), [qreg[2]])
		qc.cz(1, 3)
	with else_1: 
		qc.append(CRXGate(5.444), [qreg[1], qreg[3]])
		qc.append(ZZFeatureMap(5, reps=1, parameter_prefix='x_ed0ae3'), [qreg[2], qreg[4], qreg[1], qreg[3], qreg[0]])
		qc.append(NLocal(3, reps=1, parameter_prefix='theta_20fc8d'), [qreg[1], qreg[4], qreg[3]])
		qc.append(XGate(), [qreg[3]])
		qc.rz(1.5707963267948966, 4)
	
	
	qc.break_loop()
	
	qr_1dc687 = QuantumRegister(2)
	cr_1dc687 = ClassicalRegister(2)
	qc.add_register(qr_1dc687)
	qc.add_register(cr_1dc687)
	qc.x(qr_1dc687[0])
	qc.x(qr_1dc687[1])
	qc.measure(qr_1dc687[0], cr_1dc687[0]) 
	qc.measure(qr_1dc687[1], cr_1dc687[1]) 
	with qc.if_test((cr_1dc687, 0b11)) as else_1: 
		qc.append(HGate(), [qreg[1]])
		qc.append(U3Gate(2.245, 3.194, 1.046), [qreg[3]])
		aux_ecaa58 = AncillaRegister(5, 'aux_ecaa58')
		qc.add_register(aux_ecaa58)
		qc.append(DraperQFTAdder(5), [qreg[0], aux_ecaa58[2], aux_ecaa58[1], qreg[3], aux_ecaa58[4], qreg[1], qreg[2], aux_ecaa58[0], qreg[4], aux_ecaa58[3]])
		qc.append(SwapGate(), [qreg[1], qreg[3]])
		qc.append(CCXGate(), [qreg[1], qreg[2], qreg[4]])
	with else_1: 
		qc.append(RZGate(3.843), [qreg[2]])
		qc.cz(0, 2)
		qc.h(0)
		qc.cx(4, 1)
		aux_d490c3 = AncillaRegister(3, 'aux_d490c3')
		qc.add_register(aux_d490c3)
		qc.append(DraperQFTAdder(4), [aux_d490c3[0], qreg[4], qreg[3], aux_d490c3[2], qreg[0], aux_d490c3[1], qreg[2], qreg[1]])
	
	
aux_b39951 = AncillaRegister(3, 'aux_b39951')
qc.add_register(aux_b39951)
qc.append(DraperQFTAdder(4), [aux_b39951[2], aux_b39951[1], qreg[0], qreg[1], aux_b39951[0], qreg[2], qreg[4], qreg[3]])
aux_276c73 = AncillaRegister(1, 'aux_276c73')
qc.add_register(aux_276c73)
qc.append(DraperQFTAdder(3), [qreg[2], qreg[1], aux_276c73[0], qreg[0], qreg[3], qreg[4]])
qc.append(CRXGate(5.713), [qreg[3], qreg[2]])
qc.append(ZFeatureMap(5, reps=1, parameter_prefix='x_096b87'), [qreg[2], qreg[0], qreg[3], qreg[1], qreg[4]])
qc.append(XGate(), [qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Collect1qRuns()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
