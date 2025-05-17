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

qc.append(RealAmplitudes(5, reps=1, parameter_prefix='theta_88d7e7'), [qreg[3], qreg[1], qreg[4], qreg[2], qreg[0]])
qc.append(CCXGate(), [qreg[0], qreg[4], qreg[1]])
qc.iswap(3, 1)
qc.append(RZGate(5.582), [qreg[0]])
qc.append(RZGate(3.548), [qreg[1]])
qc.append(CRXGate(3.375), [qreg[2], qreg[0]])
qc.append(RZGate(4.471), [qreg[2]])
qc.append(SwapGate(), [qreg[4], qreg[3]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[2], qreg[0], qreg[1], qreg[3], qreg[4]])
qc.append(CRXGate(4.395), [qreg[2], qreg[3]])
with qc.for_loop(range(5)) as i:
	qc.append(CUGate(2.755, 5.205, 2.469, 6.046), [qreg[1], qreg[4]])
	qc.append(CCXGate(), [qreg[0], qreg[3], qreg[4]])
	qc.crx(0.7853981633974483, 4, 0)
	qc.append(StatePreparation([(0.14933934878256194-0.051095998116752375j), (0.1673708693093814+0.1332765228114703j), (-0.06609295918416706+0.014948400345185995j), (-0.0403441352913949-0.008127335955817359j), (-0.24598014782498634-0.1146652399335868j), (-0.032194075676752414+0.3893693135717298j), (-0.1955114542691588+0.23382346867552872j), (-0.17148366382089775+0.2024940027129461j), (-0.009796759072699111-0.11382225420606715j), (0.1955290416540556+0.201116482410032j), (0.07191122400544822-0.332021742608608j), (0.13904056816081625-0.12145578175668428j), (0.16430673035518362-0.20081188790298815j), (0.08227261625861702-0.15212287938361285j), (-0.3686151467245643-0.20573026466315503j), (-0.04301981929523418-0.12210069776122107j)]), [qreg[0], qreg[3], qreg[2], qreg[4]])
	qc.x(0)
	qc.append(MCXGate(3), [qreg[0], qreg[3], qreg[4], qreg[1]])
	qc.append(PauliFeatureMap(3, reps=1, parameter_prefix='x_37c51a'), [qreg[4], qreg[3], qreg[0]])
	qc.append(XGate(), [qreg[1]])
	qc.append(ZZFeatureMap(3, reps=1, parameter_prefix='x_2713de'), [qreg[1], qreg[3], qreg[2]])
	qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[2], qreg[0], qreg[4], qreg[3], qreg[1]])
	qc.break_loop()
	qc.append(U3Gate(0.566, 3.797, 3.588), [qreg[0]])
	qc.iswap(4, 3)
	qc.append(OR(3), [qreg[0], qreg[4], qreg[2], qreg[1]])
	qc.append(NLocal(4, reps=1, parameter_prefix='theta_8da47c'), [qreg[2], qreg[3], qreg[4], qreg[1]])
	qc.append(NLocal(3, reps=1, parameter_prefix='theta_504663'), [qreg[1], qreg[4], qreg[0]])
	qc.append(CCXGate(), [qreg[4], qreg[0], qreg[3]])
	qc.append(HGate(), [qreg[4]])
	qc.append(Diagonal(np.array([np.complex128(0.34530021316609916-0.9384922816877327j), np.complex128(-0.5802792400258701+0.8144175855143347j), np.complex128(-0.9354250708555479+0.353525015826169j), np.complex128(-0.6751614978106169-0.7376699477911002j)])), [qreg[4], qreg[1]])
	qc.append(CRXGate(1.996), [qreg[3], qreg[4]])
	qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[1], qreg[2]])
qc.append(CUGate(4.133, 2.326, 4.659, 4.514), [qreg[3], qreg[2]])
qc.rx(1.5707963267948966, 0)
qc.append(CCXGate(), [qreg[3], qreg[4], qreg[1]])
qc.append(C3XGate(), [qreg[2], qreg[4], qreg[0], qreg[3]])
qc.append(CRXGate(1.768), [qreg[2], qreg[4]])
qc.append(U3Gate(2.364, 1.726, 2.26), [qreg[0]])
qc.append(Diagonal(np.array([np.complex128(0.864899661928122-0.5019447925784473j), np.complex128(-0.8865680654011219+0.4625981684041908j)])), [qreg[0]])
qc.append(MCXGate(4), [qreg[0], qreg[2], qreg[1], qreg[3], qreg[4]])
qc.x(2)
qc.append(MCXGate(1), [qreg[0], qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGatesSimpleCommutation()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
