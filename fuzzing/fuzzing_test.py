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

qc.append(CCXGate(), [qreg[0], qreg[4], qreg[2]])
qc.append(CUGate(2.985, 0.192, 0.294, 0.481), [qreg[0], qreg[1]])
qc.append(C3XGate(), [qreg[4], qreg[2], qreg[3], qreg[0]])
qc.append(QFT(5), [qreg[0], qreg[1], qreg[3], qreg[2], qreg[4]])
qc.y(1)
qc.append(Diagonal(np.array([np.complex128(0.9932567862973362+0.11593513908340213j), np.complex128(0.9407730399338838-0.339036999947733j), np.complex128(-0.8287870690840246-0.559564110821193j), np.complex128(0.9081212582510608+0.41870727282017695j), np.complex128(0.5156889855670417+0.8567758575991947j), np.complex128(0.8729850371890446+0.48774698855456033j), np.complex128(0.013309327929753027+0.9999114269724385j), np.complex128(0.8297526728262185+0.5581312586997313j)])), [qreg[0], qreg[2], qreg[1]])
qc.cswap(3, 2, 0)
qc.append(Permutation(1, pattern=[0]), [qreg[4]])
qc.append(PauliFeatureMap(5, reps=1, parameter_prefix='x_ecc4e0'), [qreg[1], qreg[3], qreg[4], qreg[2], qreg[0]])
qc.append(U3Gate(4.69, 2.208, 1.627), [qreg[3]])
with qc.for_loop(range(5)) as i:
	qc.append(HGate(), [qreg[1]])
	qc.append(CRXGate(3.476), [qreg[0], qreg[4]])
	qc.x(4)
	qc.append(HGate(), [qreg[3]])
	qc.ch(1, 0)
	qc.append(RZGate(2.291), [qreg[1]])
	qc.append(RXGate(6.092), [qreg[1]])
	qc.append(Diagonal(np.array([np.complex128(-0.9840505566982352+0.177889015574019j), np.complex128(-0.8083724356095034-0.5886713899509294j), np.complex128(0.8121395680192308-0.5834632139711441j), np.complex128(-0.6505946385234778+0.7594251881024919j)])), [qreg[4], qreg[1]])
	qc.append(CXGate(), [qreg[0], qreg[1]])
	qc.append(HGate(), [qreg[3]])
	qc.break_loop()
	qc.append(StatePreparation([(-0.22301189033115804-0.10236055638013956j), (-0.03565161440843242+0.15145445096364088j), (0.3029834501896601+0.19637373267470862j), (0.09055986677009362-0.4298191228156338j), (-0.019522652536959235+0.05946466272371292j), (-0.41250908845696416-0.1663955851786964j), (-0.38506927158014415+0.16825079729681275j), (-0.18361401567941943-0.4245022294397543j)]), [qreg[1], qreg[0], qreg[4]])
	qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[0], qreg[1], qreg[4], qreg[3], qreg[2]])
	qc.append(AND(4), [qreg[3], qreg[0], qreg[2], qreg[1], qreg[4]])
	qc.append(CCXGate(), [qreg[1], qreg[2], qreg[3]])
	qc.append(Permutation(3, pattern=[2, 1, 0]), [qreg[4], qreg[2], qreg[1]])
	qc.append(SwapGate(), [qreg[0], qreg[1]])
	qc.append(XGate(), [qreg[4]])
	qc.append(RXGate(1.379), [qreg[4]])
	qc.append(CUGate(4.127, 2.085, 4.058, 5.004), [qreg[0], qreg[4]])
	qc.append(QFT(5), [qreg[4], qreg[0], qreg[3], qreg[2], qreg[1]])
qc.append(CRXGate(0.221), [qreg[4], qreg[0]])
qc.append(OR(4), [qreg[1], qreg[0], qreg[3], qreg[2], qreg[4]])
qc.append(RZGate(2.986), [qreg[3]])
qc.append(RealAmplitudes(2, reps=1, parameter_prefix='theta_ade6ed'), [qreg[2], qreg[1]])
qc.cp(1.5707963267948966, 2, 0)
qc.append(XGate(), [qreg[1]])
qc.append(HGate(), [qreg[0]])
qc.append(CCXGate(), [qreg[4], qreg[1], qreg[2]])
qc.append(XGate(), [qreg[4]])
qc.append(CRXGate(3.481), [qreg[2], qreg[1]])
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
