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

qc.append(U3Gate(2.554, 4.351, 0.736), [qreg[3]])
qc.append(CUGate(2.352, 4.412, 4.133, 2.008), [qreg[3], qreg[2]])
qc.append(HGate(), [qreg[3]])
qc.append(C3XGate(), [qreg[1], qreg[2], qreg[4], qreg[0]])
qc.rz(0.39269908169872414, 0)
def create_oracle(qreg):
    oracle = QuantumCircuit(qreg, name='Oracle')
    oracle.x(qreg[0])
    oracle.h(qreg[1])
    oracle.mcx([qreg[0]], qreg[1])
    oracle.h(qreg[1])
    oracle.x(qreg[0])
    return oracle.to_gate(label='Oracle')

def create_diffuser(qreg):
    diffuser = QuantumCircuit(qreg, name='Diffuser')
    diffuser.h(qreg)
    diffuser.x(qreg)
    diffuser.h(qreg[1])
    diffuser.mcx([qreg[0]], qreg[1])
    diffuser.h(qreg[1])
    diffuser.x(qreg)
    diffuser.h(qreg)
    return diffuser.to_gate(label='Diffuser')

backend = Aer.get_backend('aer_simulator')
oracle_gate = create_oracle(QuantumRegister(2))
diffuser_gate = create_diffuser(QuantumRegister(2))
results = []
grdc_qreg = QuantumRegister(2)
grdc_creg = ClassicalRegister(2)
grdc_qc = QuantumCircuit(grdc_qreg, grdc_creg)
grdc_qc.h(grdc_qreg)
for _ in range(1):
    grdc_qc.append(oracle_gate, qargs=grdc_qreg)
    grdc_qc.append(diffuser_gate, qargs=grdc_qreg)

qc.compose(grdc_qc, inplace = True, qubits = [5, 6]) 
qc.measure(qreg[5], cond_creg[0]) 
qc.measure(qreg[6], cond_creg[1]) 
with qc.if_test((cond_creg, 0b10)) as else_1: 
	def create_oracle(qreg):
	    oracle = QuantumCircuit(qreg, name='Oracle')
	    oracle.h(qreg[1])
	    oracle.mcx([qreg[0]], qreg[1])
	    oracle.h(qreg[1])
	    return oracle.to_gate(label='Oracle')
	
	def create_diffuser(qreg):
	    diffuser = QuantumCircuit(qreg, name='Diffuser')
	    diffuser.h(qreg)
	    diffuser.x(qreg)
	    diffuser.h(qreg[1])
	    diffuser.mcx([qreg[0]], qreg[1])
	    diffuser.h(qreg[1])
	    diffuser.x(qreg)
	    diffuser.h(qreg)
	    return diffuser.to_gate(label='Diffuser')
	
	backend = Aer.get_backend('aer_simulator')
	oracle_gate = create_oracle(QuantumRegister(2))
	diffuser_gate = create_diffuser(QuantumRegister(2))
	results = []
	grdc_qreg = QuantumRegister(2)
	grdc_creg = ClassicalRegister(2)
	grdc_qc = QuantumCircuit(grdc_qreg, grdc_creg)
	grdc_qc.h(grdc_qreg)
	for _ in range(1):
	    grdc_qc.append(oracle_gate, qargs=grdc_qreg)
	    grdc_qc.append(diffuser_gate, qargs=grdc_qreg)
	
	qc.compose(grdc_qc, inplace = True, qubits = [5, 6]) 
	qc.measure(qreg[5], cond_creg[0]) 
	qc.measure(qreg[6], cond_creg[1]) 
	with qc.while_loop((cond_creg, 0b10)): 
		qc.append(C3XGate(), [qreg[4], qreg[1], qreg[0], qreg[3]])
		qc.append(StatePreparation([(-0.15089067187235183+0.1289695951511149j), (0.2550918869044753-0.051005848384255356j), (0.16623034720167806+0.07230054570594342j), (-0.07703798767869245-0.09788096289004322j), (-0.028436403639503786+0.12714016505394762j), (0.07478183796445821+0.13936842691390083j), (-0.06437693945481603-0.19885321854998272j), (0.08230890891263634-0.1787372875832085j), (-0.13057978026372405+0.09740629643440635j), (-0.029122156732678046+0.11880616920035547j), (-0.06080670920972035+0.008336361260606202j), (0.21504493068465247+0.05040294514609499j), (-0.04123034688894584-0.20857935235005956j), (-0.22761332781890792-0.08248688943826671j), (0.15330686587507739+0.09923857405376264j), (0.032597721468844126-0.08665292784129765j), (-0.0885148783293555-0.1557006788914944j), (-0.06608265189108486-0.14055844157604777j), (0.16474986465303254-0.09901872565750869j), (-0.12187766388994876+0.09564467710840807j), (-0.09649950235710782+0.0428185845545461j), (-0.08156301882771276-0.05557320155995496j), (0.02722354316231862-0.08539233896473909j), (0.1627771758687312-0.006703346295594797j), (0.13704466127029902-0.07894063910008539j), (-0.12463398993568613+0.1157846781330754j), (0.04881027950224188+0.12577628014125936j), (-0.0034445932491116962-0.14906213786928377j), (0.19069006390804244-0.05053392397847821j), (-0.05102654611786124-0.26018107266782153j), (-0.25880477586360723-0.14105724666808794j), (0.027082472090048756+0.12859334983738496j)]), [qreg[3], qreg[0], qreg[1], qreg[4], qreg[2]])
		qc.append(ZFeatureMap(1, reps=1, parameter_prefix='x_09ce98'), [qreg[1]])
		qc.ccx(3, 2, 1)
		qc.append(C3XGate(), [qreg[4], qreg[3], qreg[2], qreg[1]])
		qc.measure(qreg[5], cond_creg[0]) 
		qc.measure(qreg[6], cond_creg[1]) 
	
	
with else_1: 
	pass 

qc.append(XOR(2), [qreg[3], qreg[0]])
qc.append(CCXGate(), [qreg[4], qreg[0], qreg[1]])
qc.cswap(3, 1, 0)
qc.append(QFT(1), [qreg[4]])
qc.append(Permutation(1, pattern=[0]), [qreg[0]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
