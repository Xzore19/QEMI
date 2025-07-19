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

qreg = QuantumRegister(8) 
creg = ClassicalRegister(8) 
qc = QuantumCircuit(qreg, creg) 

qc.append(XGate(), [qreg[2]])
qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_643a17'), [qreg[3], qreg[6]])
qc.append(CCXGate(), [qreg[5], qreg[0], qreg[6]])
qc.append(SwapGate(), [qreg[5], qreg[7]])
qc.append(HGate(), [qreg[0]])

qr_c77f13 = QuantumRegister(2)
cr_c77f13 = ClassicalRegister(2)
qc.add_register(qr_c77f13)
qc.add_register(cr_c77f13)
qc.x(qr_c77f13[0])
qc.x(qr_c77f13[1])
qc.measure(qr_c77f13[0], cr_c77f13[0]) 
qc.measure(qr_c77f13[1], cr_c77f13[1]) 
with qc.if_test((cr_c77f13, 0b11)) as else_c77f13: 
	with qc.for_loop(range(3)) as i_9967a4:
		qc.append(RZGate(6.151), [qreg[0]])
		qc.append(CCXGate(), [qreg[4], qreg[1], qreg[3]])
		qc.append(XGate(), [qreg[4]])
		qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_67ba4a'), [qreg[4], qreg[3]])
		qc.append(CCXGate(), [qreg[5], qreg[7], qreg[6]])
		qc.continue_loop()
	
with else_c77f13: 
	pass 
qc.reset(qr_c77f13)
qc.append(OR(4), [qreg[4], qreg[0], qreg[1], qreg[7], qreg[3]])
qc.append(CCXGate(), [qreg[1], qreg[2], qreg[4]])
qc.append(RZGate(2.101), [qreg[1]])
qc.append(SwapGate(), [qreg[0], qreg[2]])
qc.append(PauliFeatureMap(2, reps=1, parameter_prefix='x_e393b8'), [qreg[5], qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 
qc.measure(qreg[5], creg[5]) 
qc.measure(qreg[6], creg[6]) 
qc.measure(qreg[7], creg[7]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveDiagonalGatesBeforeMeasure(),OptimizeCliffords(),CommutativeCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
