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

qc.cswap(4, 2, 1)
qc.append(C3XGate(), [qreg[4], qreg[1], qreg[3], qreg[2]])
qc.append(ZZFeatureMap(3, reps=1, parameter_prefix='x_4dbe03'), [qreg[3], qreg[0], qreg[1]])
qc.append(RZGate(2.906), [qreg[0]])
qc.append(XGate(), [qreg[2]])
qc.append(SwapGate(), [qreg[1], qreg[2]])
qc.ch(4, 3)
qc.append(SwapGate(), [qreg[2], qreg[4]])
qc.t(2)
qc.append(CRXGate(2.222), [qreg[4], qreg[2]])
qc.measure(qreg[5], cond_creg[0]) 
qc.measure(qreg[6], cond_creg[1]) 
with qc.while_loop((cond_creg, 0b11)): 
	qc.append(CUGate(1.947, 3.831, 5.057, 3.421), [qreg[3], qreg[1]])
	qc.append(MCXGate(1), [qreg[1], qreg[2]])
	qc.append(SwapGate(), [qreg[0], qreg[3]])
	qc.append(CCXGate(), [qreg[1], qreg[4], qreg[3]])
	qc.p(0.39269908169872414, 1)
	qc.rz(0.7853981633974483, 4)
	qc.append(CUGate(1.874, 5.808, 5.983, 5.413), [qreg[0], qreg[4]])
	qc.append(RZGate(3.071), [qreg[2]])
	qc.append(HGate(), [qreg[0]])
	qc.append(RXGate(3.912), [qreg[1]])
	qc.measure(qreg[5], cond_creg[0]) 
	qc.measure(qreg[6], cond_creg[1]) 
	qc.break_loop()
qc.append(ZFeatureMap(5, reps=1, parameter_prefix='x_a77ec0'), [qreg[3], qreg[1], qreg[2], qreg[4], qreg[0]])
qc.append(TwoLocal(5, reps=1, parameter_prefix='theta_a9db03'), [qreg[4], qreg[1], qreg[2], qreg[0], qreg[3]])
qc.append(Initialize([(-0.1880149244320798+0.28751676829452244j), (0.3389977568318379+0.12032387439512171j), (-0.054418500402360924-0.21996087912255377j), (0.1055907885471699-0.4230030563931634j), (0.07381538185488677+0.3639631791798963j), (0.4969803038709219-0.2121729581521602j), (-0.17127298705256752+0.16852833095121855j), (-0.06458228270771983+0.13903316765714072j)]), [qreg[1], qreg[2], qreg[3]])
qc.crz(0.7853981633974483, 2, 0)
qc.append(ZFeatureMap(1, reps=1, parameter_prefix='x_029315'), [qreg[1]])
qc.append(ZZFeatureMap(2, reps=1, parameter_prefix='x_5d3c54'), [qreg[0], qreg[3]])
qc.append(SwapGate(), [qreg[2], qreg[0]])
qc.append(C3XGate(), [qreg[2], qreg[0], qreg[1], qreg[3]])
qc.append(CRXGate(5.913), [qreg[2], qreg[3]])
qc.append(ZZFeatureMap(4, reps=1, parameter_prefix='x_ab560c'), [qreg[3], qreg[1], qreg[0], qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
