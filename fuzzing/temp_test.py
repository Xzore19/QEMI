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

qc.append(CUGate(2.935, 3.925, 5.207, 0.378), [qreg[0], qreg[3]])
qc.rx(1.5707963267948966, 1)
qc.append(RZGate(4.455), [qreg[2]])
qc.append(OR(4), [qreg[2], qreg[0], qreg[4], qreg[1], qreg[3]])
qc.append(RXGate(5.891), [qreg[3]])
qc.crx(0.39269908169872414, 4, 1)
qc.ch(1, 0)
qc.append(HGate(), [qreg[3]])
qc.z(3)
qc.append(Initialize([(0.18068488400361155+0.13277739094388033j), (0.029626073571596693-0.04703160143234595j), (-0.7052586176385955+0.1693779814530562j), (-0.04927421888864026+0.2908163178686879j), (0.2566504403714082+0.009514593578318275j), (-0.14242046511439446+0.17371694185970396j), (-0.2706806752859235+0.19994225510127653j), (-0.31825588525132353+0.05098902809583129j)]), [qreg[0], qreg[2], qreg[3]])
with qc.for_loop(range(5)) as i:
	qc.append(XGate(), [qreg[3]])
	qc.append(CXGate(), [qreg[3], qreg[4]])
	qc.append(PauliFeatureMap(3, reps=1, parameter_prefix='x_a00f18'), [qreg[4], qreg[2], qreg[1]])
	qc.t(0)
	qc.append(XGate(), [qreg[0]])
	qc.append(NLocal(3, reps=1, parameter_prefix='theta_4e8194'), [qreg[3], qreg[2], qreg[1]])
	qc.append(CUGate(3.515, 0.149, 2.305, 0.31), [qreg[4], qreg[1]])
	qc.ch(3, 2)
	qc.x(4)
	qc.append(SwapGate(), [qreg[2], qreg[1]])
	qc.break_loop()
qc.append(StatePreparation([(0.006223830313785116+0.08433220794545467j), (-0.038127311873431054+0.14338266821468057j), (-0.049849522796454146-0.023739975015232177j), (-0.05675798253564825+0.05841177362300007j), (-0.004652225870883047+0.10915587424506196j), (-0.10860238447578059+0.03741559987257307j), (0.29584438561395926-0.06220172396456733j), (0.043585609438382036-0.0398299519694928j), (-0.013360337518146201-0.07356995033992704j), (0.016867924328830077-0.17987432978460277j), (-0.0361336124144837+0.16378556773108888j), (0.14946585597797205-0.21607942134774075j), (0.08424438199850552+0.07370855815794275j), (-0.07394161837512697-0.12839177631593127j), (-0.2540883243875261+0.028445313767283657j), (-0.017230911356455113+0.21120123156239815j), (0.1264238188883435+0.06081124782889484j), (0.019614403408113653-0.026071151930567003j), (0.1716837331344475-0.14189839627391163j), (-0.19469880757817107-0.1953312384988525j), (-0.06761432639267795-0.20837660416678133j), (0.14850399533943456+0.03117091290406045j), (0.13278572854179702-0.13316931524109948j), (-0.23304663805991865+0.054931928270067105j), (-0.16433465741244305-0.049948638033794394j), (-0.017668947802849316+0.05707248693481861j), (0.1715316434035428+0.05716946330573339j), (-0.08067413527965084-0.0028570500827765216j), (0.2749676042806739-0.08151039381833616j), (0.21881471649318823+0.0566101087225232j), (0.08602775514671294+0.04873922031878563j), (0.0005632088298318079+0.18835596095631646j)]), [qreg[2], qreg[1], qreg[0], qreg[4], qreg[3]])
qc.swap(3, 0)
qc.append(CXGate(), [qreg[3], qreg[4]])
qc.append(U3Gate(5.627, 4.745, 1.278), [qreg[3]])
qc.cry(1.5707963267948966, 1, 3)
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[0], qreg[4]])
qc.append(MCXGate(3), [qreg[1], qreg[3], qreg[2], qreg[4]])
qc.x(4)
qc.crx(1.5707963267948966, 4, 1)
qc.append(SwapGate(), [qreg[2], qreg[3]])
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
