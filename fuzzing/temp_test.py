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

qreg = QuantumRegister(7) 
creg = ClassicalRegister(5) 
cond_creg = ClassicalRegister(2) 
qc = QuantumCircuit(qreg, creg, cond_creg) 

qc.append(HGate(), [qreg[1]])
qc.append(XOR(1), [qreg[0]])
qc.append(AND(1), [qreg[3], qreg[1]])
qc.swap(2, 0)
qc.append(SwapGate(), [qreg[3], qreg[0]])
qc.append(PauliFeatureMap(2, reps=1, parameter_prefix='x_69eda3'), [qreg[3], qreg[1]])
qc.append(CCXGate(), [qreg[4], qreg[2], qreg[1]])
qc.append(CXGate(), [qreg[0], qreg[4]])
qc.append(DraperQFTAdder(2), [qreg[2], qreg[1], qreg[3], qreg[4]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[4], qreg[2], qreg[3], qreg[1], qreg[0]])
qc.cry(1.5707963267948966, 4, 3)
qc.append(XGate(), [qreg[0]])
qc.append(CXGate(), [qreg[0], qreg[2]])
qc.append(Initialize([(0.15018708747968454-0.1415430918840805j), (-0.09311032551810798+0.13375872410039563j), (-0.10531937818936252+0.14901768928429274j), (-0.44171181724012487+0.21784768871020213j), (0.026320408980146093-0.06992421937262003j), (-0.10884414547930464-0.10686652750390165j), (-0.04429928892159819-0.23562627337099154j), (0.1340817763056912-0.1438806140158594j), (-0.18320287138493524+0.01797490913240357j), (0.08881663099610884-0.34091469090774j), (-0.2639014924759435-0.042035390606738554j), (-0.24774842242963246-0.09413570414052252j), (-0.11073924600343997-0.14420567720926328j), (-0.07946234086417904-0.14578450358040654j), (0.05428769774581214+0.3929385101581568j), (-0.11087869998319062+0.007385178790339976j)]), [qreg[4], qreg[3], qreg[1], qreg[2]])
qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_df2dd7'), [qreg[4], qreg[3], qreg[1], qreg[0]])
qc.append(U3Gate(0.939, 3.406, 3.125), [qreg[3]])
qc.append(CRXGate(0.968), [qreg[4], qreg[2]])
qc.crx(0.39269908169872414, 3, 2)
qc.cry(0.7853981633974483, 1, 0)
qc.rz(0.39269908169872414, 1)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGatesDecomposition()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
