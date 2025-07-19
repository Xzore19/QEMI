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

qreg = QuantumRegister(6) 
creg = ClassicalRegister(6) 
qc = QuantumCircuit(qreg, creg) 

qc.append(CXGate(), [qreg[3], qreg[4]])
qc.append(ZZFeatureMap(3, reps=1, parameter_prefix='x_1cb90c'), [qreg[3], qreg[0], qreg[1]])
qc.append(EfficientSU2(3, reps=1, parameter_prefix='theta_c74682'), [qreg[5], qreg[0], qreg[4]])
qc.append(RealAmplitudes(3, reps=1, parameter_prefix='theta_080ed5'), [qreg[3], qreg[2], qreg[0]])
qc.append(U3Gate(3.711, 0.377, 0.503), [qreg[5]])

qr_cfc18c = QuantumRegister(2)
cr_cfc18c = ClassicalRegister(2)
qc.add_register(qr_cfc18c)
qc.add_register(cr_cfc18c)
qc.x(qr_cfc18c[0])
qc.x(qr_cfc18c[1])
qc.measure(qr_cfc18c[0], cr_cfc18c[0]) 
qc.measure(qr_cfc18c[1], cr_cfc18c[1]) 
with qc.while_loop((cr_cfc18c, 0b10)): 
	
	qr_01e231 = QuantumRegister(2)
	cr_01e231 = ClassicalRegister(2)
	qc.add_register(qr_01e231)
	qc.add_register(cr_01e231)
	qc.x(qr_01e231[0])
	qc.x(qr_01e231[1])
	qc.measure(qr_01e231[0], cr_01e231[0]) 
	qc.measure(qr_01e231[1], cr_01e231[1]) 
	with qc.while_loop((cr_01e231, 0b11)): 
		qc.measure(qr_01e231[0], cr_01e231[0]) 
		qc.measure(qr_01e231[1], cr_01e231[1]) 
		qc.append(CCXGate(), [qreg[0], qreg[3], qreg[2]])
		qc.append(HGate(), [qreg[5]])
		qc.append(RXGate(0.77), [qreg[3]])
		qc.append(C3XGate(), [qreg[0], qreg[4], qreg[1], qreg[3]])
		qc.append(ZZFeatureMap(3, reps=1, parameter_prefix='x_712d2b'), [qreg[2], qreg[0], qreg[5]])
		qc.break_loop()
		qc.append(SwapGate(), [qreg[1], qreg[5]])
		qc.append(CXGate(), [qreg[1], qreg[3]])
		qc.append(CUGate(3.604, 4.12, 2.771, 4.752), [qreg[0], qreg[3]])
		qc.append(C3XGate(), [qreg[4], qreg[2], qreg[0], qreg[5]])
		aux_669092 = AncillaRegister(4, 'aux_669092')
		qc.add_register(aux_669092)
		qc.append(DraperQFTAdder(5), [qreg[3], qreg[5], aux_669092[0], aux_669092[2], qreg[4], qreg[0], aux_669092[1], qreg[2], qreg[1], aux_669092[3]])
	qc.reset(qr_01e231)
	
	qc.measure(qr_cfc18c[0], cr_cfc18c[0]) 
	qc.measure(qr_cfc18c[1], cr_cfc18c[1]) 
qc.reset(qr_cfc18c)
qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_75bb1b'), [qreg[3], qreg[5]])
qc.append(CRXGate(2.561), [qreg[2], qreg[4]])
qc.append(U3Gate(1.155, 2.764, 2.984), [qreg[2]])
qc.append(C3XGate(), [qreg[1], qreg[5], qreg[4], qreg[3]])
qc.append(XGate(), [qreg[1]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 
qc.measure(qreg[5], creg[5]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([Collect1qRuns(),Optimize1qGatesDecomposition(),RemoveResetInZeroState()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
