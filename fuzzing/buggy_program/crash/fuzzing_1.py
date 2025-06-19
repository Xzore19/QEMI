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

qreg = QuantumRegister(4) 
creg = ClassicalRegister(4) 
qc = QuantumCircuit(qreg, creg) 

qc.ch(3, 1)
qc.iswap(3, 1)
qc.t(0)
qc.crz(1.5707963267948966, 0, 3)
qc.p(0.39269908169872414, 3)
with qc.for_loop(range(3)) as i_8c6ece:
	
	qr_830316 = QuantumRegister(2)
	cr_830316 = ClassicalRegister(2)
	qc.add_register(qr_830316)
	qc.add_register(cr_830316)
	qc.x(qr_830316[0])
	qc.x(qr_830316[1])
	qc.measure(qr_830316[0], cr_830316[0]) 
	qc.measure(qr_830316[1], cr_830316[1]) 
	with qc.if_test((cr_830316, 0b11)) as else_830316: 
		pass
	with else_830316: 
		qc.tdg(3)
		qc.z(0)
		qc.cx(3, 1)
		qc.ch(1, 0)
		qc.p(0.39269908169872414, 0)
	qc.reset(qr_830316)
	
	qc.continue_loop()
	
	qr_8c6ece = QuantumRegister(2)
	cr_8c6ece = ClassicalRegister(2)
	qc.add_register(qr_8c6ece)
	qc.add_register(cr_8c6ece)
	qc.x(qr_8c6ece[0])
	qc.x(qr_8c6ece[1])
	qc.measure(qr_8c6ece[0], cr_8c6ece[0]) 
	qc.measure(qr_8c6ece[1], cr_8c6ece[1]) 
	with qc.while_loop((cr_8c6ece, 0b10)): 
		qc.ry(0.7853981633974483, 2)
		qc.rz(0.39269908169872414, 1)
		qc.rz(1.5707963267948966, 1)
		qc.cry(0.7853981633974483, 2, 1)
		qc.t(0)
		qc.measure(qr_8c6ece[0], cr_8c6ece[0]) 
		qc.measure(qr_8c6ece[1], cr_8c6ece[1]) 
	qc.reset(qr_8c6ece)
	
qc.h(1)
qc.ccx(3, 1, 0)
qc.p(0.7853981633974483, 3)
qc.ccz(3, 2, 0)
qc.cswap(2, 1, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([TemplateOptimization(),CollectCliffords(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
