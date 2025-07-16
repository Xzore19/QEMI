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

qc.append(EfficientSU2(3, reps=1, parameter_prefix='theta_8c0b08'), [qreg[4], qreg[3], qreg[0]])
qc.append(CCXGate(), [qreg[3], qreg[0], qreg[4]])
qc.append(XGate(), [qreg[0]])
qc.append(U3Gate(1.295, 3.604, 1.761), [qreg[4]])
with qc.for_loop(range(3)) as i_8a6ba0:
	qc.append(OR(4), [qreg[3], qreg[0], qreg[2], qreg[4], qreg[1]])
	qc.append(Permutation(4, pattern=[2, 0, 3, 1]), [qreg[1], qreg[0], qreg[2], qreg[3]])
	qc.append(ZFeatureMap(4, reps=1, parameter_prefix='x_ada073'), [qreg[0], qreg[3], qreg[1], qreg[2]])
	qc.append(DraperQFTAdder(2), [qreg[0], qreg[2], qreg[1], qreg[4]])
	qc.break_loop()
	qc.append(OR(2), [qreg[4], qreg[0], qreg[3]])
	qc.append(U3Gate(0.469, 5.687, 1.914), [qreg[4]])
	aux_683bde = AncillaRegister(3, 'aux_683bde')
	qc.add_register(aux_683bde)
	qc.append(DraperQFTAdder(4), [qreg[0], qreg[1], qreg[3], aux_683bde[0], qreg[4], aux_683bde[2], qreg[2], aux_683bde[1]])
	qc.append(AND(4), [qreg[2], qreg[1], qreg[0], qreg[4], qreg[3]])
qc.append(SwapGate(), [qreg[0], qreg[1]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[2], qreg[0]])
qc.append(U3Gate(5.44, 1.754, 2.196), [qreg[4]])
qc.append(CUGate(2.6, 1.387, 1.32, 1.929), [qreg[2], qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveFinalReset(),Collect2qBlocks(),Collect1qRuns()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
