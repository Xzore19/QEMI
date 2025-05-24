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

qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[3], qreg[4]])
qc.append(XGate(), [qreg[3]])
qc.append(RZGate(3.715), [qreg[3]])
qc.append(NLocal(4, reps=1, parameter_prefix='theta_b2a3da'), [qreg[1], qreg[0], qreg[3], qreg[2]])
qc.rx(0.39269908169872414, 3)

qr_1131f9 = QuantumRegister(2)
cr_1131f9 = ClassicalRegister(2)
qc.add_register(qr_1131f9)
qc.add_register(cr_1131f9)
qc.h(qr_1131f9[0])
qc.cx(qr_1131f9[0], qr_1131f9[1])         
qc.measure(qr_1131f9[0], cr_1131f9[0]) 
qc.measure(qr_1131f9[1], cr_1131f9[1]) 
with qc.switch(cr_1131f9) as case: 
	with case(0b00, 0b11): 
		qc.append(SwapGate(), [qreg[1], qreg[0]])
		qc.append(CXGate(), [qreg[2], qreg[3]])
		qc.cswap(4, 3, 2)
		qc.append(CUGate(4.31, 2.328, 2.28, 3.364), [qreg[4], qreg[3]])
		qc.cx(4, 3)
	with case(case.DEFAULT): 
		pass
qc.append(XGate(), [qreg[2]])
qc.append(AND(4), [qreg[3], qreg[4], qreg[2], qreg[1], qreg[0]])
qc.append(AND(4), [qreg[1], qreg[2], qreg[3], qreg[0], qreg[4]])
qc.append(CCXGate(), [qreg[4], qreg[0], qreg[1]])
qc.append(U3Gate(4.509, 1.392, 4.258), [qreg[3]])
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
