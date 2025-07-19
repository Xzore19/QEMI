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

qreg = QuantumRegister(6) 
creg = ClassicalRegister(6) 
qc = QuantumCircuit(qreg, creg) 

qc.append(CXGate(), [qreg[3], qreg[4]])
qc.append(ZZFeatureMap(3, reps=1, parameter_prefix='x_1cb90c'), [qreg[3], qreg[0], qreg[1]])
qc.append(EfficientSU2(3, reps=1, parameter_prefix='theta_c74682'), [qreg[5], qreg[0], qreg[4]])
qc.append(RealAmplitudes(3, reps=1, parameter_prefix='theta_080ed5'), [qreg[3], qreg[2], qreg[0]])
qc.append(U3Gate(3.711, 0.377, 0.503), [qreg[5]])
pass
qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_75bb1b'), [qreg[3], qreg[5]])
qc.append(CRXGate(2.561), [qreg[2], qreg[4]])
qc.append(U3Gate(1.155, 2.764, 2.984), [qreg[2]])
qc.append(C3XGate(), [qreg[1], qreg[5], qreg[4], qreg[3]])
qc.append(XGate(), [qreg[1]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 
qc.measure(qreg[5], creg[5]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([Collect1qRuns(),Optimize1qGatesDecomposition(),RemoveResetInZeroState()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
