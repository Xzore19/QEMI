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

qc.append(MCXGate(4), [qreg[4], qreg[1], qreg[2], qreg[3], qreg[0]])
qc.rx(1.5707963267948966, 4)
aux_7b9aa9 = AncillaRegister(5, 'aux_7b9aa9')
qc.add_register(aux_7b9aa9)
qc.append(DraperQFTAdder(5), [qreg[1], aux_7b9aa9[0], qreg[3], qreg[4], qreg[0], qreg[2], aux_7b9aa9[4], aux_7b9aa9[1], aux_7b9aa9[3], aux_7b9aa9[2]])
qc.append(Isometry(np.array([[1.0, 0.0], [0.0, 1.0]]), 0, 0), [qreg[3]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[3], qreg[0]])
qc.append(CXGate(), [qreg[3], qreg[4]])
aux_513dbc = AncillaRegister(5, 'aux_513dbc')
qc.add_register(aux_513dbc)
qc.append(DraperQFTAdder(5), [qreg[1], qreg[0], aux_513dbc[1], aux_513dbc[0], aux_513dbc[3], qreg[3], aux_513dbc[4], qreg[2], aux_513dbc[2], qreg[4]])
qc.append(CUGate(4.035, 6.14, 2.969, 1.292), [qreg[1], qreg[3]])
qc.append(PauliFeatureMap(5, reps=1, parameter_prefix='x_77d39f'), [qreg[4], qreg[0], qreg[3], qreg[2], qreg[1]])
qc.ccx(4, 1, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Collect1qRuns()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
