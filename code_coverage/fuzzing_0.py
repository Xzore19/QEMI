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

qc.append(NLocal(3, reps=1, parameter_prefix='theta_4dc143'), [qreg[2], qreg[4], qreg[3]])
qc.append(EfficientSU2(3, reps=1, parameter_prefix='theta_08c1ed'), [qreg[4], qreg[1], qreg[0]])
qc.append(CCXGate(), [qreg[1], qreg[3], qreg[4]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[1], qreg[3]])

qr_d08761 = QuantumRegister(2)
cr_d08761 = ClassicalRegister(2)
qc.add_register(qr_d08761)
qc.add_register(cr_d08761)
qc.x(qr_d08761[0])
qc.x(qr_d08761[1])
qc.measure(qr_d08761[0], cr_d08761[0]) 
qc.measure(qr_d08761[1], cr_d08761[1]) 
with qc.if_test((cr_d08761, 0b11)) as else_d08761: 
	pass
with else_d08761: 
	with qc.for_loop(range(3)) as i_531b84:
		qc.append(CCXGate(), [qreg[4], qreg[3], qreg[2]])
		qc.append(CUGate(6.184, 4.224, 0.373, 0.093), [qreg[3], qreg[0]])
		qc.append(DraperQFTAdder(2), [qreg[3], qreg[4], qreg[0], qreg[2]])
		qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_15cdce'), [qreg[1], qreg[3], qreg[4], qreg[0]])
		qc.break_loop()
		qc.append(ZZFeatureMap(5, reps=1, parameter_prefix='x_859f7d'), [qreg[2], qreg[3], qreg[1], qreg[4], qreg[0]])
		qc.append(U3Gate(1.711, 1.785, 3.637), [qreg[0]])
		qc.append(QFT(1), [qreg[1]])
		qc.append(RZGate(5.091), [qreg[1]])
	
qc.reset(qr_d08761)
qc.append(StatePreparation([(0.7918334666492596+0.1458264819328434j), (0.39501428215518997-0.4423777968600206j)]), [qreg[1]])
qc.append(C3XGate(), [qreg[4], qreg[1], qreg[2], qreg[0]])
qc.append(CUGate(2.067, 5.84, 1.659, 1.083), [qreg[3], qreg[1]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[4], qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([ElidePermutations(),RemoveResetInZeroState(),RemoveIdentityEquivalent()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
