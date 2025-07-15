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

qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_604211'), [qreg[3], qreg[2], qreg[0], qreg[4]])
qc.rz(0.39269908169872414, 3)
qc.append(CUGate(0.265, 1.499, 3.264, 2.942), [qreg[2], qreg[1]])
aux_2b7b35 = AncillaRegister(5, 'aux_2b7b35')
qc.add_register(aux_2b7b35)
qc.append(DraperQFTAdder(5), [aux_2b7b35[4], qreg[1], aux_2b7b35[1], aux_2b7b35[2], aux_2b7b35[0], aux_2b7b35[3], qreg[3], qreg[4], qreg[2], qreg[0]])
qc.append(XGate(), [qreg[4]])

qr_f55541 = QuantumRegister(2)
cr_f55541 = ClassicalRegister(2)
qc.add_register(qr_f55541)
qc.add_register(cr_f55541)
qc.h(qr_f55541[0])
qc.cx(qr_f55541[0], qr_f55541[1])         
qc.measure(qr_f55541[0], cr_f55541[0]) 
qc.measure(qr_f55541[1], cr_f55541[1]) 
with qc.switch(cr_f55541) as case: 
	with case(0b00, 0b11): 
		
		qr_3c79ae = QuantumRegister(2)
		cr_3c79ae = ClassicalRegister(2)
		qc.add_register(qr_3c79ae)
		qc.add_register(cr_3c79ae)
		qc.x(qr_3c79ae[0])
		qc.x(qr_3c79ae[1])
		qc.measure(qr_3c79ae[0], cr_3c79ae[0]) 
		qc.measure(qr_3c79ae[1], cr_3c79ae[1]) 
		with qc.if_test((cr_3c79ae, 0b11)) as else_3c79ae: 
			qc.tdg(1)
			qc.append(C3XGate(), [qreg[4], qreg[1], qreg[0], qreg[3]])
			qc.ccz(3, 2, 1)
			qc.append(SwapGate(), [qreg[0], qreg[2]])
			qc.append(C3XGate(), [qreg[4], qreg[3], qreg[2], qreg[1]])
		with else_3c79ae: 
			pass 
		qc.reset(qr_3c79ae)
		
	with case(case.DEFAULT): 
		pass
qc.reset(qr_f55541)
qc.append(SwapGate(), [qreg[2], qreg[4]])
qc.cz(2, 4)
qc.append(RXGate(5.268), [qreg[0]])
qc.cx(2, 0)
qc.append(U3Gate(4.605, 0.437, 0.991), [qreg[4]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=1) 
result = job.result().get_counts() 
print(result)
