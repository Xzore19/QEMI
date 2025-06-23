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

qc.cz(1, 3)
qc.append(C3XGate(), [qreg[4], qreg[1], qreg[3], qreg[0]])
qc.append(CCXGate(), [qreg[2], qreg[3], qreg[0]])
qc.x(0)
qc.append(U3Gate(5.767, 4.201, 5.828), [qreg[0]])

qr_fadccd = QuantumRegister(2)
cr_fadccd = ClassicalRegister(2)
qc.add_register(qr_fadccd)
qc.add_register(cr_fadccd)
qc.x(qr_fadccd[0])
qc.x(qr_fadccd[1])
qc.measure(qr_fadccd[0], cr_fadccd[0]) 
qc.measure(qr_fadccd[1], cr_fadccd[1]) 
with qc.if_test((cr_fadccd, 0b11)) as else_1: 
	
	qr_9a385d = QuantumRegister(2)
	cr_9a385d = ClassicalRegister(2)
	qc.add_register(qr_9a385d)
	qc.add_register(cr_9a385d)
	qc.x(qr_9a385d[0])
	qc.x(qr_9a385d[1])
	qc.measure(qr_9a385d[0], cr_9a385d[0]) 
	qc.measure(qr_9a385d[1], cr_9a385d[1]) 
	with qc.while_loop((cr_9a385d, 0b10)): 
		aux_339be4 = AncillaRegister(5, 'aux_339be4')
		qc.add_register(aux_339be4)
		qc.append(DraperQFTAdder(5), [qreg[4], aux_339be4[1], qreg[2], aux_339be4[0], aux_339be4[4], qreg[1], qreg[0], aux_339be4[3], qreg[3], aux_339be4[2]])
		qc.rz(1.5707963267948966, 2)
		qc.append(TwoLocal(5, reps=1, parameter_prefix='theta_52bd5c'), [qreg[2], qreg[1], qreg[3], qreg[4], qreg[0]])
		qc.append(CUGate(6.166, 0.288, 2.109, 4.14), [qreg[2], qreg[1]])
		qc.append(QFT(2), [qreg[2], qreg[0]])
		qc.measure(qr_9a385d[0], cr_9a385d[0]) 
		qc.measure(qr_9a385d[1], cr_9a385d[1]) 
	
	
with else_1: 
	pass 

qc.append(Permutation(5, pattern=[3, 4, 1, 0, 2]), [qreg[1], qreg[0], qreg[4], qreg[3], qreg[2]])
qc.p(1.5707963267948966, 2)
aux_54f420 = AncillaRegister(5, 'aux_54f420')
qc.add_register(aux_54f420)
qc.append(DraperQFTAdder(5), [aux_54f420[1], aux_54f420[4], aux_54f420[3], aux_54f420[2], qreg[1], qreg[4], aux_54f420[0], qreg[3], qreg[2], qreg[0]])
qc.append(U3Gate(0.327, 0.065, 3.929), [qreg[0]])
qc.append(XGate(), [qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(TemplateOptimization()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
