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

qc.append(Diagonal(np.array([np.complex128(-0.542935505404511-0.8397743964727362j), np.complex128(-0.9523937807233934+0.30487060606001504j)])), [qreg[1]])
qc.append(SwapGate(), [qreg[0], qreg[3]])
qc.append(QFT(3), [qreg[0], qreg[3], qreg[2]])
qc.append(CRXGate(4.22), [qreg[2], qreg[0]])

qr_b53d1a = QuantumRegister(2)
cr_b53d1a = ClassicalRegister(2)
qc.add_register(qr_b53d1a)
qc.add_register(cr_b53d1a)
qc.x(qr_b53d1a[0])
qc.x(qr_b53d1a[1])
qc.measure(qr_b53d1a[0], cr_b53d1a[0]) 
qc.measure(qr_b53d1a[1], cr_b53d1a[1]) 
with qc.while_loop((cr_b53d1a, 0b10)): 
	
	qr_d34c38 = QuantumRegister(2)
	cr_d34c38 = ClassicalRegister(2)
	qc.add_register(qr_d34c38)
	qc.add_register(cr_d34c38)
	qc.h(qr_d34c38[0])
	qc.cx(qr_d34c38[0], qr_d34c38[1])         
	qc.measure(qr_d34c38[0], cr_d34c38[0]) 
	qc.measure(qr_d34c38[1], cr_d34c38[1]) 
	with qc.switch(cr_d34c38) as case: 
		with case(0b00, 0b11): 
			qc.append(U3Gate(2.101, 5.43, 2.777), [qreg[0]])
			qc.append(CCXGate(), [qreg[2], qreg[1], qreg[4]])
			qc.append(C3XGate(), [qreg[4], qreg[2], qreg[0], qreg[3]])
			qc.append(XGate(), [qreg[4]])
		with case(case.DEFAULT): 
			qc.append(NLocal(2, reps=1, parameter_prefix='theta_c05b69'), [qreg[3], qreg[1]])
			qc.append(Diagonal(np.array([np.complex128(-0.9240871931591408+0.3821817099747984j), np.complex128(-0.7344125460818104-0.6787033314767452j), np.complex128(-0.5202623819364025-0.8540064718383935j), np.complex128(0.9897502534492438-0.14280908863639483j), np.complex128(0.8747241912479317-0.48462107800388937j), np.complex128(-0.9998996876020896-0.014163853050765526j), np.complex128(0.9068800744181308+0.42138881169694753j), np.complex128(-0.015567917132735226+0.9998788126348854j), np.complex128(-0.8886805433395184-0.4585268715024j), np.complex128(0.9331516919735376+0.3594828504489804j), np.complex128(0.8421047290993008+0.5393140321080041j), np.complex128(0.9776478772411686-0.21024896700301948j), np.complex128(-0.6060485096442139+0.7954276861902829j), np.complex128(-0.9550138673075542-0.29656114588777355j), np.complex128(-0.6769020435368207-0.7360731101294736j), np.complex128(0.9927056311106975-0.12056338565713733j), np.complex128(0.8303633828078225+0.5572222648925198j), np.complex128(0.2244962822543984+0.9744749454213554j), np.complex128(0.8271863246124214-0.5619277394596158j), np.complex128(0.26383172150196704-0.9645687236943299j), np.complex128(-0.18562247306412155-0.9826211362949402j), np.complex128(0.6920969666057567-0.7218045364328975j), np.complex128(0.03905185829238038-0.9992371852387759j), np.complex128(0.7574580945426506+0.6528837836949368j), np.complex128(-0.9974948018639497-0.07073980671729153j), np.complex128(0.527456014484544+0.849582340202573j), np.complex128(0.6616033440820225-0.7498539958548497j), np.complex128(0.2867326583602521+0.9580106380566257j), np.complex128(0.8321093295773815-0.554611633154481j), np.complex128(-0.8828646266128137-0.469627566349993j), np.complex128(0.25231115386707226+0.9676461551798088j), np.complex128(0.5671193946068903-0.8236355943381237j)])), [qreg[4], qreg[3], qreg[1], qreg[2], qreg[0]])
			qc.append(NLocal(4, reps=1, parameter_prefix='theta_1429da'), [qreg[3], qreg[2], qreg[4], qreg[1]])
			qc.append(SwapGate(), [qreg[1], qreg[0]])
	qc.reset(qr_d34c38)
	
	qc.measure(qr_b53d1a[0], cr_b53d1a[0]) 
	qc.measure(qr_b53d1a[1], cr_b53d1a[1]) 
qc.reset(qr_b53d1a)
qc.append(TwoLocal(4, reps=1, parameter_prefix='theta_06fe9c'), [qreg[0], qreg[1], qreg[2], qreg[3]])
qc.append(EfficientSU2(4, reps=1, parameter_prefix='theta_35aaa4'), [qreg[4], qreg[1], qreg[0], qreg[3]])
qc.append(CCXGate(), [qreg[2], qreg[3], qreg[1]])
qc.append(AND(1), [qreg[3], qreg[4]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([Collect2qBlocks(),CollectMultiQBlocks(),ElidePermutations()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
