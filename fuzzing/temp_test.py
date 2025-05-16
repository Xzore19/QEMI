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

qc.append(RXGate(3.713), [qreg[0]])
qc.append(RXGate(0.742), [qreg[1]])
qc.append(AND(4), [qreg[4], qreg[3], qreg[1], qreg[2], qreg[0]])
qc.append(RXGate(5.622), [qreg[3]])
qc.append(RXGate(2.765), [qreg[1]])
qc.z(3)
qc.crx(1.5707963267948966, 2, 3)
qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_210221'), [qreg[1], qreg[2]])
qc.append(CCXGate(), [qreg[0], qreg[2], qreg[3]])
qc.crx(0.7853981633974483, 2, 3)
with qc.for_loop(range(5)) as i:
	qc.append(RXGate(1.006), [qreg[0]])
	qc.append(CUGate(4.83, 0.92, 3.972, 0.37), [qreg[2], qreg[0]])
	qc.append(XGate(), [qreg[2]])
	qc.cz(0, 2)
	qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[3], qreg[0]])
	qc.append(CUGate(2.913, 4.028, 4.716, 0.244), [qreg[1], qreg[3]])
	qc.append(AND(2), [qreg[1], qreg[2], qreg[0]])
	qc.z(0)
	qc.append(RealAmplitudes(3, reps=1, parameter_prefix='theta_1da057'), [qreg[4], qreg[0], qreg[3]])
	aux_52f2b8 = AncillaRegister(8, 'aux_52f2b8')
	qc.add_register(aux_52f2b8)
	qc.append(WeightedAdder(5, weights=[np.int64(3), np.int64(3), np.int64(3), np.int64(2), np.int64(1)]), [qreg[3], aux_52f2b8[4], qreg[4], aux_52f2b8[0], qreg[0], qreg[1], aux_52f2b8[1], aux_52f2b8[3], qreg[2], aux_52f2b8[2], aux_52f2b8[5], aux_52f2b8[6], aux_52f2b8[7]])
	qc.break_loop()
qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_d6d54b'), [qreg[0], qreg[1]])
qc.append(C3XGate(), [qreg[2], qreg[4], qreg[1], qreg[0]])
qc.append(XGate(), [qreg[0]])
aux_4e7930 = AncillaRegister(5, 'aux_4e7930')
qc.add_register(aux_4e7930)
qc.append(DraperQFTAdder(5), [aux_4e7930[1], qreg[3], aux_4e7930[4], aux_4e7930[3], aux_4e7930[0], qreg[2], qreg[0], aux_4e7930[2], qreg[4], qreg[1]])
qc.append(MCXGate(4), [qreg[4], qreg[0], qreg[1], qreg[2], qreg[3]])
qc.swap(4, 2)
qc.append(RXGate(5.464), [qreg[0]])
aux_a858a6 = AncillaRegister(4, 'aux_a858a6')
qc.add_register(aux_a858a6)
qc.append(WeightedAdder(3, weights=[np.int64(1), np.int64(3), np.int64(1)]), [aux_a858a6[1], aux_a858a6[0], aux_a858a6[3], qreg[0], qreg[1], qreg[2], aux_a858a6[2], qreg[4], qreg[3]])
qc.append(U3Gate(2.877, 1.629, 0.733), [qreg[2]])
qc.cp(0.7853981633974483, 3, 4)
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
