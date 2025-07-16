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

qc.append(RXGate(4.103), [qreg[0]])
qc.append(RXGate(0.679), [qreg[2]])
qc.append(C3XGate(), [qreg[4], qreg[2], qreg[0], qreg[1]])
qc.append(U3Gate(1.916, 2.873, 2.351), [qreg[0]])

qr_968c91 = QuantumRegister(2)
cr_968c91 = ClassicalRegister(2)
qc.add_register(qr_968c91)
qc.add_register(cr_968c91)
qc.x(qr_968c91[0])
qc.x(qr_968c91[1])
qc.measure(qr_968c91[0], cr_968c91[0]) 
qc.measure(qr_968c91[1], cr_968c91[1]) 
with qc.while_loop((cr_968c91, 0b10)): 
	
	qr_aa961e = QuantumRegister(2)
	cr_aa961e = ClassicalRegister(2)
	qc.add_register(qr_aa961e)
	qc.add_register(cr_aa961e)
	qc.x(qr_aa961e[0])
	qc.x(qr_aa961e[1])
	qc.measure(qr_aa961e[0], cr_aa961e[0]) 
	qc.measure(qr_aa961e[1], cr_aa961e[1]) 
	with qc.while_loop((cr_aa961e, 0b10)): 
		qc.append(XGate(), [qreg[1]])
		qc.append(CUGate(0.646, 3.329, 2.395, 1.087), [qreg[3], qreg[4]])
		qc.append(C3XGate(), [qreg[0], qreg[4], qreg[1], qreg[3]])
		qc.append(CCXGate(), [qreg[4], qreg[1], qreg[3]])
		qc.measure(qr_aa961e[0], cr_aa961e[0]) 
		qc.measure(qr_aa961e[1], cr_aa961e[1]) 
	qc.reset(qr_aa961e)
	
	qc.measure(qr_968c91[0], cr_968c91[0]) 
	qc.measure(qr_968c91[1], cr_968c91[1]) 
qc.reset(qr_968c91)
qc.append(CRXGate(4.667), [qreg[0], qreg[4]])
qc.append(CXGate(), [qreg[2], qreg[0]])
qc.append(CCXGate(), [qreg[1], qreg[4], qreg[3]])
qc.append(SwapGate(), [qreg[2], qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveFinalReset(),CommutativeInverseCancellation(),RemoveDiagonalGatesBeforeMeasure()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
