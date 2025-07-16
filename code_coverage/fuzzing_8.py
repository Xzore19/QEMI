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

qc.append(CXGate(), [qreg[0], qreg[2]])
qc.append(C3XGate(), [qreg[3], qreg[0], qreg[1], qreg[2]])
qc.append(XOR(2, seed=42), [qreg[3], qreg[2]])
qc.append(RXGate(3.339), [qreg[0]])
with qc.for_loop(range(3)) as i_25e758:
	qc.append(CCXGate(), [qreg[1], qreg[0], qreg[3]])
	qc.append(RZGate(4.475), [qreg[1]])
	qc.append(CUGate(3.495, 5.843, 4.472, 0.952), [qreg[0], qreg[1]])
	qc.append(CXGate(), [qreg[0], qreg[3]])
	qc.continue_loop()
	qc.append(NLocal(4, reps=1, parameter_prefix='theta_6ecef1'), [qreg[1], qreg[0], qreg[4], qreg[3]])
	qc.append(SwapGate(), [qreg[4], qreg[3]])
	qc.append(HGate(), [qreg[0]])
	qc.append(QFT(4), [qreg[1], qreg[4], qreg[2], qreg[0]])
qc.append(PauliFeatureMap(5, reps=1, parameter_prefix='x_08a05c'), [qreg[2], qreg[1], qreg[4], qreg[3], qreg[0]])
qc.append(CRXGate(0.48), [qreg[4], qreg[2]])
qc.append(RZGate(1.552), [qreg[1]])
qc.append(XGate(), [qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([OptimizeSwapBeforeMeasure(),ElidePermutations(),Optimize1qGates()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
