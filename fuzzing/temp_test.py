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

qreg = QuantumRegister(7) 
creg = ClassicalRegister(5) 
cond_creg = ClassicalRegister(2) 
qc = QuantumCircuit(qreg, creg, cond_creg) 

qc.append(EfficientSU2(4, reps=1, parameter_prefix='theta_3922f7'), [qreg[1], qreg[3], qreg[2], qreg[4]])
qc.append(RZGate(4.884), [qreg[0]])
qc.append(SwapGate(), [qreg[0], qreg[4]])
qc.append(AND(4), [qreg[0], qreg[4], qreg[3], qreg[2], qreg[1]])
qc.append(CUGate(1.886, 1.191, 0.698, 1.28), [qreg[2], qreg[0]])
qc.x(1)
qc.crx(0.7853981633974483, 4, 1)
qc.append(RXGate(3.603), [qreg[1]])
qc.append(CRXGate(1.593), [qreg[1], qreg[4]])
qc.append(C3XGate(), [qreg[4], qreg[3], qreg[2], qreg[0]])
qc.measure(qreg[0], creg[0])
qc.measure(qreg[1], creg[1])
qc.measure(qreg[2], creg[2])
qc.measure(qreg[3], creg[3])
qc.measure(qreg[4], creg[4])

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator")

p = PassManager(Collect1qRuns())
qc = p.run(qc)

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 2, routing_method = "none", layout_method = "noise_adaptive", approximation_degree = 1 )

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=100000)
result = job.result().get_counts()
print(result)