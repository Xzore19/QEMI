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

qc.cx(2, 1)
qc.append(SwapGate(), [qreg[3], qreg[0]])
qc.append(CXGate(), [qreg[4], qreg[2]])
qc.x(2)
qc.rx(1.5707963267948966, 4)

qr_a0d452 = QuantumRegister(2)
cr_a0d452 = ClassicalRegister(2)
qc.add_register(qr_a0d452)
qc.add_register(cr_a0d452)
qc.h(qr_a0d452[0])
qc.cx(qr_a0d452[0], qr_a0d452[1])         
qc.measure(qr_a0d452[0], cr_a0d452[0]) 
qc.measure(qr_a0d452[1], cr_a0d452[1]) 
with qc.switch(cr_a0d452) as case: 
	with case(0b00, 0b11): 
		qc.append(Permutation(2, pattern=[1, 0]), [qreg[4], qreg[3]])
		qc.append(Initialize([(0.3390950361578553+0.029097440110061813j), (-0.25900391820446067+0.44402385263101685j), (0.6802902349090859+0.12475921964035785j), (0.3375287891063456+0.16625983883086137j)]), [qreg[3], qreg[4]])
		qc.append(CUGate(0.706, 0.175, 2.26, 0.665), [qreg[3], qreg[1]])
		qc.cx(4, 3)
		qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[0], qreg[1], qreg[3]])
	with case(case.DEFAULT): 
		qc.append(CXGate(), [qreg[2], qreg[1]])
		qc.append(MCXGate(2), [qreg[0], qreg[3], qreg[1]])
		qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[4], qreg[1]])
		qc.append(CCXGate(), [qreg[4], qreg[3], qreg[0]])
		qc.append(RZGate(0.761), [qreg[3]])
qc.append(NLocal(4, reps=1, parameter_prefix='theta_6d704f'), [qreg[4], qreg[3], qreg[2], qreg[0]])
qc.t(2)
qc.cz(0, 4)
qc.append(C3XGate(), [qreg[1], qreg[3], qreg[2], qreg[0]])
qc.append(XGate(), [qreg[2]])
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
