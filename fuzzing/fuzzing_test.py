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
cond_qreg = QuantumRegister(2)
cond_creg = ClassicalRegister(2)
qc.add_register(cond_qreg)
qc.add_register(cond_creg)


qc.append(ZFeatureMap(1, reps=1, parameter_prefix='x_44f1b1'), [qreg[3]])
qc.append(XOR(1), [qreg[4]])
qc.cp(0.39269908169872414, 3, 2)
qc.append(C3XGate(), [qreg[2], qreg[1], qreg[3], qreg[0]])
qc.append(CCXGate(), [qreg[3], qreg[2], qreg[0]])
qc.append(Diagonal(np.array([np.complex128(0.49682388009645134-0.8678513882952006j), np.complex128(-0.6877063805639142+0.7259889352680802j), np.complex128(-0.8874360635128363-0.46093083339785496j), np.complex128(0.9009607195598608-0.43390065891881036j), np.complex128(0.3204977647340869+0.9472492717339264j), np.complex128(0.639722224944948+0.7686061897431514j), np.complex128(-0.06465881623542052+0.9979074293154822j), np.complex128(0.6345538231488664-0.7728786745195892j), np.complex128(0.18982609185723703+0.9818177299530743j), np.complex128(-0.9998573542370415-0.016889972708784114j), np.complex128(0.9803422895070485+0.19730432180790775j), np.complex128(-0.9598605560287058+0.28047765148094017j), np.complex128(0.9535472003646425-0.3012436500189711j), np.complex128(-0.9526923353285175-0.30393636538969077j), np.complex128(0.9857968594577107-0.16794210872593732j), np.complex128(-0.7187376795869028+0.6952813444513197j), np.complex128(-0.1538321622436636-0.9880969921315615j), np.complex128(-0.8663251216786224+0.4994805136824859j), np.complex128(0.9971215446463556+0.07581968874946644j), np.complex128(-0.5864032759527404+0.8100192577660695j), np.complex128(-0.2102177819274579+0.9776545832560187j), np.complex128(-0.48499490607960977+0.8745169758654376j), np.complex128(0.3821865244162652+0.9240852019995859j), np.complex128(0.7238871291432533+0.6899184185544976j), np.complex128(-0.9677575539071104+0.25188353827855897j), np.complex128(0.734687615687631+0.678405562591599j), np.complex128(-0.01976409295103679-0.9998046712382488j), np.complex128(0.12159867157080041+0.9925793485017793j), np.complex128(0.3312641056292075-0.9435380714744271j), np.complex128(-0.20307068105846074-0.9791640814973009j), np.complex128(0.9872192637202126-0.15936789306419705j), np.complex128(-0.9980797877216134+0.061941402483146724j)])), [qreg[2], qreg[0], qreg[3], qreg[1], qreg[4]])
qc.rz(1.5707963267948966, 3)
qc.append(Initialize([(-0.2013112308899025-0.16219141423137803j), (-0.019530832784978237-0.9658086146012279j)]), [qreg[0]])
qc.crx(0.7853981633974483, 2, 0)
qc.append(HGate(), [qreg[3]])
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

qc.compose(grdc_qc, inplace = True, qubits = cond_qreg)
qc.measure(cond_qreg[0], cond_creg[0])
qc.measure(cond_qreg[1], cond_creg[1])
with qc.if_test((cond_creg, 0b10)) as else_1: 
    pass
with else_1: 
	qc.measure(cond_qreg[0], cond_creg[0])
	qc.measure(cond_qreg[1], cond_creg[1])
	with qc.if_test((cond_creg, 0b10)) as else_1: 
	    pass
	with else_1: 
		qc.append(TwoLocal(3, reps=1, parameter_prefix='theta_eab7c2'), [qreg[2], qreg[4], qreg[3]])
		qc.append(RXGate(3.773), [qreg[0]])
		qc.tdg(4)
		qc.append(HGate(), [qreg[2]])
		qc.z(2)
		qc.append(ZZFeatureMap(5, reps=1, parameter_prefix='x_71a3fc'), [qreg[4], qreg[1], qreg[0], qreg[3], qreg[2]])
		qc.append(CUGate(3.662, 1.449, 2.941, 3.24), [qreg[2], qreg[0]])
		qc.append(Diagonal(np.array([np.complex128(-0.14531989485024938+0.9893847220170283j), np.complex128(0.7094835237344846+0.7047220228922174j), np.complex128(-0.5034339770922472-0.8640336976698783j), np.complex128(-0.24634787459423602-0.9691814714917442j), np.complex128(0.7696880919242095-0.6384201133658537j), np.complex128(0.9457737926780954+0.3248260043212229j), np.complex128(-0.38363790465027287-0.9234835992672248j), np.complex128(-0.9996910861897988-0.024854218810098635j), np.complex128(-0.3736012396716379+0.927589410092534j), np.complex128(-0.9591698969065008+0.2828305302975133j), np.complex128(-0.001286783988405868+0.9999991720931409j), np.complex128(0.8438819976942541-0.5365288193261895j), np.complex128(-0.9224193099044198+0.38618987132685656j), np.complex128(0.038454720117936825+0.9992603437046079j), np.complex128(0.8161327389012135-0.5778644758882516j), np.complex128(0.6011663488361858-0.7991239084315832j)])), [qreg[3], qreg[0], qreg[4], qreg[2]])
		qc.append(Diagonal(np.array([np.complex128(0.31717297152302554-0.9483677061853456j), np.complex128(0.562333884318674-0.8269102747862503j), np.complex128(0.2471568365479119-0.9689754889302561j), np.complex128(0.7526847040617283+0.6583811481744511j)])), [qreg[3], qreg[0]])
		qc.append(Initialize([(0.23125648347057118+0.2882329311219005j), (0.2718504656382868-0.09667284361867336j), (0.404072219490907-0.14693378545360408j), (-0.5434766318948656+0.5476889232226707j)]), [qreg[4], qreg[1]])
	
	

qc.append(RXGate(4.724), [qreg[0]])
qc.iswap(2, 0)
qc.append(U3Gate(0.836, 1.999, 3.64), [qreg[3]])
qc.append(QFT(2), [qreg[1], qreg[2]])
qc.cx(2, 0)
qc.append(CXGate(), [qreg[0], qreg[1]])
qc.ccx(2, 1, 0)
qc.append(CRXGate(3.858), [qreg[1], qreg[3]])
qc.append(SwapGate(), [qreg[4], qreg[0]])
qc.ccx(4, 3, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(TemplateOptimization()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
