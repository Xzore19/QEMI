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

qc.append(HGate(), [qreg[3]])
qc.append(AND(1), [qreg[4], qreg[3]])
qc.append(CRXGate(1.636), [qreg[2], qreg[0]])
qc.append(RXGate(6.054), [qreg[0]])
qc.append(ZFeatureMap(5, reps=1, parameter_prefix='x_21ce9a'), [qreg[0], qreg[1], qreg[4], qreg[3], qreg[2]])

qr_3425c8 = QuantumRegister(2)
cr_3425c8 = ClassicalRegister(2)
qc.add_register(qr_3425c8)
qc.add_register(cr_3425c8)
qc.h(qr_3425c8[0])
qc.cx(qr_3425c8[0], qr_3425c8[1])         
qc.measure(qr_3425c8[0], cr_3425c8[0]) 
qc.measure(qr_3425c8[1], cr_3425c8[1]) 
with qc.switch(cr_3425c8) as case: 
	with case(0b00, 0b11): 
		qc.append(XGate(), [qreg[2]])
		qc.ry(0.39269908169872414, 2)
		qc.append(TwoLocal(2, reps=1, parameter_prefix='theta_8af313'), [qreg[0], qreg[2]])
		qc.append(C3XGate(), [qreg[0], qreg[3], qreg[4], qreg[2]])
		qc.append(CXGate(), [qreg[4], qreg[2]])
	with case(case.DEFAULT): 
		pass
qc.append(RZGate(3.584), [qreg[0]])
qc.append(SwapGate(), [qreg[2], qreg[3]])
qc.append(CRXGate(4.055), [qreg[3], qreg[0]])
qc.append(C3XGate(), [qreg[4], qreg[3], qreg[1], qreg[2]])
qc.append(ZZFeatureMap(3, reps=1, parameter_prefix='x_bc1e08'), [qreg[3], qreg[1], qreg[0]])
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

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
