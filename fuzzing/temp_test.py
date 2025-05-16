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

qc.append(CUGate(5.311, 4.563, 3.457, 1.5), [qreg[2], qreg[4]])
qc.append(Initialize([(-0.1461128829115177+0.2583908884121786j), (0.061292745465562404-0.10935970618117259j), (0.18704706966700477+0.15550750658627968j), (0.1463129023297423+0.05577145995745344j), (0.055273051879153955-0.2231538132456037j), (0.33470002400089227+0.025250146705064726j), (0.1505118894351209-0.14786464096060875j), (0.002415268940122103+0.07494968986412376j), (0.07959127422253202-0.10924323339734868j), (-0.03138590312584835+0.11987209094557623j), (0.44787141944307785+0.07201575972071898j), (0.06441351738534806+0.013637054739571516j), (-0.18869104834394443-0.21949592775541177j), (0.01167165556535853-0.24108440892944016j), (0.38551630606530696+0.2082985804177428j), (-0.12675778411074615+0.05452969971542001j)]), [qreg[3], qreg[2], qreg[0], qreg[1]])
qc.append(XGate(), [qreg[4]])
qc.append(Permutation(2, pattern=[0, 1]), [qreg[2], qreg[0]])
qc.append(CUGate(6.147, 4.432, 0.137, 2.875), [qreg[2], qreg[1]])
aux_680326 = AncillaRegister(3, 'aux_680326')
qc.add_register(aux_680326)
qc.append(WeightedAdder(2, weights=[np.int64(3), np.int64(3)]), [qreg[2], qreg[0], aux_680326[1], aux_680326[2], aux_680326[0], qreg[1], qreg[4], qreg[3]])
qc.append(XGate(), [qreg[0]])
qc.append(CXGate(), [qreg[1], qreg[4]])
aux_d56b93 = AncillaRegister(8, 'aux_d56b93')
qc.add_register(aux_d56b93)
qc.append(WeightedAdder(5, weights=[np.int64(3), np.int64(2), np.int64(3), np.int64(2), np.int64(3)]), [qreg[4], aux_d56b93[0], aux_d56b93[3], qreg[1], aux_d56b93[2], qreg[2], aux_d56b93[7], qreg[0], aux_d56b93[5], qreg[3], aux_d56b93[4], aux_d56b93[6], aux_d56b93[1]])
qc.append(C3XGate(), [qreg[4], qreg[2], qreg[0], qreg[3]])
with qc.for_loop(range(5)) as i:
	qc.append(CRXGate(4.356), [qreg[4], qreg[0]])
	qc.append(RZGate(0.638), [qreg[3]])
	qc.append(C3XGate(), [qreg[0], qreg[1], qreg[3], qreg[2]])
	qc.append(SwapGate(), [qreg[4], qreg[1]])
	qc.append(HGate(), [qreg[4]])
	qc.append(HGate(), [qreg[2]])
	qc.append(HGate(), [qreg[3]])
	qc.append(MCXGate(1), [qreg[4], qreg[2]])
	qc.append(CRXGate(5.104), [qreg[3], qreg[4]])
	qc.append(HGate(), [qreg[3]])
	qc.break_loop()
aux_e75871 = AncillaRegister(7, 'aux_e75871')
qc.add_register(aux_e75871)
qc.append(WeightedAdder(4, weights=[np.int64(3), np.int64(3), np.int64(1), np.int64(2)]), [aux_e75871[0], aux_e75871[5], aux_e75871[1], aux_e75871[6], qreg[4], aux_e75871[3], qreg[1], aux_e75871[4], qreg[3], aux_e75871[2], qreg[0], qreg[2]])
qc.append(RXGate(2.306), [qreg[4]])
qc.append(U3Gate(1.677, 0.317, 3.522), [qreg[3]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=2), [qreg[3], qreg[1], qreg[4]])
qc.append(CCXGate(), [qreg[3], qreg[4], qreg[0]])
qc.append(CXGate(), [qreg[0], qreg[3]])
qc.append(SwapGate(), [qreg[0], qreg[4]])
qc.append(U3Gate(1.384, 0.154, 1.863), [qreg[2]])
qc.append(CCXGate(), [qreg[4], qreg[2], qreg[3]])
qc.append(CRXGate(5.389), [qreg[2], qreg[1]])
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
