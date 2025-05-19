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

qc.t(0)
qc.append(Permutation(2, pattern=[1, 0]), [qreg[3], qreg[4]])
qc.append(NLocal(4, reps=1, parameter_prefix='theta_785bbe'), [qreg[1], qreg[3], qreg[0], qreg[4]])
qc.append(RXGate(0.664), [qreg[2]])
qc.append(U3Gate(5.949, 5.825, 0.789), [qreg[4]])

qr_d54907 = QuantumRegister(2)
cr_d54907 = ClassicalRegister(2)
qc.add_register(qr_d54907)
qc.add_register(cr_d54907)
qc.x(qr_d54907[0])
qc.x(qr_d54907[1])
qc.measure(qr_d54907[0], cr_d54907[0]) 
qc.measure(qr_d54907[1], cr_d54907[1]) 
with qc.while_loop((cr_d54907, 0b10)): 
	
	qr_58a51b = QuantumRegister(2)
	cr_58a51b = ClassicalRegister(2)
	qc.add_register(qr_58a51b)
	qc.add_register(cr_58a51b)
	qc.x(qr_58a51b[0])
	qc.x(qr_58a51b[1])
	qc.measure(qr_58a51b[0], cr_58a51b[0]) 
	qc.measure(qr_58a51b[1], cr_58a51b[1]) 
	with qc.while_loop((cr_58a51b, 0b10)): 
		qc.append(U3Gate(2.373, 2.354, 3.428), [qreg[4]])
		qc.append(NLocal(4, reps=1, parameter_prefix='theta_d5aa9f'), [qreg[2], qreg[0], qreg[4], qreg[3]])
		qc.append(CRXGate(4.539), [qreg[3], qreg[2]])
		qc.ccz(4, 3, 2)
		qc.append(EfficientSU2(3, reps=1, parameter_prefix='theta_14a197'), [qreg[4], qreg[3], qreg[0]])
		qc.measure(qr_58a51b[0], cr_58a51b[0]) 
		qc.measure(qr_58a51b[1], cr_58a51b[1]) 
	
	
	qc.measure(qr_d54907[0], cr_d54907[0]) 
	qc.measure(qr_d54907[1], cr_d54907[1]) 

qc.append(MCXGate(3), [qreg[2], qreg[1], qreg[0], qreg[4]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[2], qreg[1]])
qc.t(3)
qc.append(CUGate(5.973, 3.024, 1.637, 3.79), [qreg[1], qreg[4]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=2), [qreg[4], qreg[1], qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(CommutativeCancellation()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
