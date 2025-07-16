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

qc.append(TwoLocal(5, reps=1, parameter_prefix='theta_39349d'), [qreg[4], qreg[1], qreg[3], qreg[2], qreg[0]])
qc.append(Permutation(4, pattern=[3, 1, 2, 0]), [qreg[0], qreg[1], qreg[4], qreg[3]])
qc.append(HGate(), [qreg[3]])
qc.append(SwapGate(), [qreg[1], qreg[0]])
with qc.for_loop(range(3)) as i_3edeca:
	
	qr_9c7a30 = QuantumRegister(2)
	cr_9c7a30 = ClassicalRegister(2)
	qc.add_register(qr_9c7a30)
	qc.add_register(cr_9c7a30)
	qc.x(qr_9c7a30[0])
	qc.x(qr_9c7a30[1])
	qc.measure(qr_9c7a30[0], cr_9c7a30[0]) 
	qc.measure(qr_9c7a30[1], cr_9c7a30[1]) 
	with qc.while_loop((cr_9c7a30, 0b10)): 
		qc.append(MCXGate(4), [qreg[3], qreg[0], qreg[1], qreg[2], qreg[4]])
		qc.append(SwapGate(), [qreg[3], qreg[4]])
		qc.append(CUGate(4.332, 5.097, 0.39, 2.113), [qreg[4], qreg[0]])
		qc.append(C3XGate(), [qreg[3], qreg[1], qreg[2], qreg[0]])
		qc.measure(qr_9c7a30[0], cr_9c7a30[0]) 
		qc.measure(qr_9c7a30[1], cr_9c7a30[1]) 
	qc.reset(qr_9c7a30)
	
	qc.continue_loop()
	
	qr_3edeca = QuantumRegister(2)
	cr_3edeca = ClassicalRegister(2)
	qc.add_register(qr_3edeca)
	qc.add_register(cr_3edeca)
	qc.h(qr_3edeca[0])
	qc.cx(qr_3edeca[0], qr_3edeca[1])         
	qc.measure(qr_3edeca[0], cr_3edeca[0]) 
	qc.measure(qr_3edeca[1], cr_3edeca[1]) 
	with qc.switch(cr_3edeca) as case: 
		with case(0b00, 0b11): 
			qc.append(U3Gate(2.578, 6.151, 0.905), [qreg[3]])
			qc.append(HGate(), [qreg[1]])
			qc.append(C3XGate(), [qreg[4], qreg[3], qreg[0], qreg[2]])
			qc.append(MCPhaseGate(1.0, num_ctrl_qubits=2), [qreg[1], qreg[0], qreg[2]])
		with case(case.DEFAULT): 
			qc.append(HGate(), [qreg[0]])
			qc.append(AND(2), [qreg[1], qreg[4], qreg[2]])
			qc.append(ZFeatureMap(4, reps=1, parameter_prefix='x_30bc14'), [qreg[1], qreg[4], qreg[3], qreg[0]])
			qc.append(StatePreparation([(-0.1638231603591007+0.014804344454696076j), (-0.16970513626169134-0.21876506979702653j), (-0.19792504972117997-0.14041120139009336j), (-0.30473101683884335+0.011782850079203062j), (0.24731097054808046-0.03868826946967302j), (-0.2666757657938294+0.0006483603962589338j), (-0.11227540448368915-0.01845047600863671j), (-0.09162027888951776+0.28157128615884075j), (-0.061125272540709874+0.032415394552104584j), (0.2738665961963818-0.18620459012140525j), (0.07893069828998418-0.2155072271309697j), (-0.138967593444486-0.3369112122495715j), (-0.14590037667385825-0.11061555295366393j), (-0.3224360862753363-0.043496186913603775j), (-0.2506546589152679+0.06607311247138126j), (0.053801450720193204-0.02392168541999391j)]), [qreg[0], qreg[2], qreg[3], qreg[1]])
	qc.reset(qr_3edeca)
	
qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_2c51fa'), [qreg[3], qreg[4]])
qc.append(RZGate(5.378), [qreg[3]])
qc.append(ZZFeatureMap(4, reps=1, parameter_prefix='x_f8d2b7'), [qreg[4], qreg[3], qreg[0], qreg[1]])
qc.append(Diagonal(np.array([np.complex128(-0.948912436648045+0.3155395182456072j), np.complex128(-0.46661613346678277+0.8844599391654263j), np.complex128(0.9871504995741751-0.15979327642443666j), np.complex128(0.5135574848820985-0.858055190370394j), np.complex128(-0.8379073113278976-0.5458125480632097j), np.complex128(-0.7228275167307873-0.6910284951120348j), np.complex128(-0.13016579929282868+0.9914922413687659j), np.complex128(0.9205790897465541-0.3905561925272801j)])), [qreg[1], qreg[3], qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveIdentityEquivalent(),TemplateOptimization(),OptimizeAnnotated()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
