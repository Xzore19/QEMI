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

qc.append(XGate(), [qreg[1]])
qc.append(SwapGate(), [qreg[2], qreg[0]])
qc.append(CRXGate(4.105), [qreg[4], qreg[1]])
qc.append(CUGate(0.932, 3.574, 1.685, 1.315), [qreg[1], qreg[4]])
qc.append(RXGate(1.679), [qreg[2]])

qr_e0320b = QuantumRegister(2)
cr_e0320b = ClassicalRegister(2)
qc.add_register(qr_e0320b)
qc.add_register(cr_e0320b)
qc.h(qr_e0320b[0])
qc.cx(qr_e0320b[0], qr_e0320b[1])         
qc.measure(qr_e0320b[0], cr_e0320b[0]) 
qc.measure(qr_e0320b[1], cr_e0320b[1]) 
with qc.switch(cr_e0320b) as case: 
	with case(0b00, 0b11): 
		qc.p(1.5707963267948966, 4)
		qc.append(HGate(), [qreg[0]])
		qc.append(SwapGate(), [qreg[2], qreg[0]])
		qc.append(XOR(4, seed=42), [qreg[3], qreg[4], qreg[2], qreg[1]])
		qc.append(CRXGate(5.799), [qreg[1], qreg[0]])
	with case(case.DEFAULT): 
		pass
qc.t(1)
qc.append(MCXGate(4), [qreg[1], qreg[3], qreg[2], qreg[4], qreg[0]])
qc.cx(4, 0)
qc.append(U3Gate(2.316, 4.702, 4.216), [qreg[0]])
qc.append(SwapGate(), [qreg[3], qreg[4]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1,basis_gates=["cx", "h", "id", "t"] ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
