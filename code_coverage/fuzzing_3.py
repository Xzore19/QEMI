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

qc.append(CRXGate(4.432), [qreg[2], qreg[3]])
qc.append(CUGate(5.943, 3.678, 5.302, 1.384), [qreg[0], qreg[3]])
qc.append(PauliFeatureMap(5, reps=1, parameter_prefix='x_cfab09'), [qreg[0], qreg[2], qreg[3], qreg[1], qreg[4]])
qc.append(Permutation(3, pattern=[1, 2, 0]), [qreg[2], qreg[3], qreg[4]])
a = 0
with qc.for_loop(range(a)) as i_afe774:
	qc.append(XOR(3, seed=42), [qreg[3], qreg[4], qreg[2]])
	qc.append(RZGate(1.047), [qreg[3]])
	qc.append(CCXGate(), [qreg[0], qreg[1], qreg[2]])
	qc.append(CUGate(0.353, 4.364, 3.461, 3.04), [qreg[0], qreg[3]])
qc.append(Initialize([(-0.3521644846284253+0.03351565498587801j), (0.07372783982919878-0.03289924240985052j), (-0.6554925384115662+0.18486344534704957j), (-0.6358212131403486-0.015004855952537637j)]), [qreg[3], qreg[2]])
qc.append(PauliFeatureMap(5, reps=1, parameter_prefix='x_da4fd3'), [qreg[4], qreg[3], qreg[1], qreg[2], qreg[0]])
qc.append(RXGate(0.043), [qreg[2]])
qc.append(C3XGate(), [qreg[2], qreg[0], qreg[3], qreg[1]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CommutativeCancellation(),RemoveDiagonalGatesBeforeMeasure(),Collect1qRuns()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
