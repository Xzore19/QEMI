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

qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[2], qreg[1]])
qc.append(XGate(), [qreg[3]])
qc.append(CXGate(), [qreg[4], qreg[2]])
qc.append(RZGate(1.488), [qreg[2]])
qc.ch(4, 0)
with qc.for_loop(range(3)) as i:
	a = 0
	with qc.for_loop(range(a)) as i:
		qc.append(RXGate(0.395), [qreg[2]])
		qc.append(CUGate(1.295, 4.028, 1.445, 5.481), [qreg[0], qreg[2]])
		qc.append(C3XGate(), [qreg[2], qreg[1], qreg[4], qreg[3]])
		qc.cz(0, 1)
		qc.cswap(2, 1, 0)
	
	qc.continue_loop()
	
	qr_b01aed = QuantumRegister(2)
	cr_b01aed = ClassicalRegister(2)
	qc.add_register(qr_b01aed)
	qc.add_register(cr_b01aed)
	qc.x(qr_b01aed[0])
	qc.x(qr_b01aed[1])
	qc.measure(qr_b01aed[0], cr_b01aed[0]) 
	qc.measure(qr_b01aed[1], cr_b01aed[1]) 
	with qc.while_loop((cr_b01aed, 0b10)): 
		qc.cry(0.39269908169872414, 2, 3)
		qc.append(CCXGate(), [qreg[2], qreg[0], qreg[1]])
		qc.append(RXGate(5.54), [qreg[1]])
		qc.tdg(3)
		qc.append(CCXGate(), [qreg[0], qreg[1], qreg[2]])
		qc.measure(qr_b01aed[0], cr_b01aed[0]) 
		qc.measure(qr_b01aed[1], cr_b01aed[1]) 
	
	
qc.x(0)
qc.append(U3Gate(3.441, 2.786, 1.95), [qreg[2]])
qc.ccz(4, 3, 2)
qc.append(XOR(1, seed=42), [qreg[1]])
qc.append(RXGate(3.37), [qreg[4]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
