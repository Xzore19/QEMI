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

qc.p(0.39269908169872414, 0)
qc.ry(1.5707963267948966, 3)
qc.ry(0.7853981633974483, 0)
qc.crx(0.7853981633974483, 1, 2)
qc.cx(2, 0)

qr_925e70 = QuantumRegister(2)
cr_925e70 = ClassicalRegister(2)
qc.add_register(qr_925e70)
qc.add_register(cr_925e70)
qc.x(qr_925e70[0])
qc.x(qr_925e70[1])
qc.measure(qr_925e70[0], cr_925e70[0]) 
qc.measure(qr_925e70[1], cr_925e70[1]) 
with qc.while_loop((cr_925e70, 0b11)): 
	qc.measure(qr_925e70[0], cr_925e70[0]) 
	qc.measure(qr_925e70[1], cr_925e70[1]) 
	
	qr_b69761 = QuantumRegister(2)
	cr_b69761 = ClassicalRegister(2)
	qc.add_register(qr_b69761)
	qc.add_register(cr_b69761)
	qc.h(qr_b69761[0])
	qc.cx(qr_b69761[0], qr_b69761[1])         
	qc.measure(qr_b69761[0], cr_b69761[0]) 
	qc.measure(qr_b69761[1], cr_b69761[1]) 
	with qc.switch(cr_b69761) as case: 
		with case(0b00, 0b11): 
			qc.z(1)
			qc.tdg(2)
			qc.cry(0.7853981633974483, 1, 2)
			qc.tdg(1)
			qc.cz(1, 2)
		with case(case.DEFAULT): 
			qc.tdg(1)
			qc.iswap(2, 1)
			qc.rx(0.7853981633974483, 3)
			qc.cz(0, 1)
			qc.cz(1, 3)
	qc.reset(qr_b69761)
	
	qc.break_loop()
	
	qr_925e70 = QuantumRegister(2)
	cr_925e70 = ClassicalRegister(2)
	qc.add_register(qr_925e70)
	qc.add_register(cr_925e70)
	qc.x(qr_925e70[0])
	qc.x(qr_925e70[1])
	qc.measure(qr_925e70[0], cr_925e70[0]) 
	qc.measure(qr_925e70[1], cr_925e70[1]) 
	with qc.while_loop((cr_925e70, 0b11)): 
		qc.measure(qr_925e70[0], cr_925e70[0]) 
		qc.measure(qr_925e70[1], cr_925e70[1]) 
		qc.cz(0, 2)
		qc.cry(0.7853981633974483, 1, 3)
		qc.tdg(2)
		qc.crz(0.7853981633974483, 2, 0)
		qc.ch(3, 2)
		qc.break_loop()
		qc.y(2)
		qc.p(0.39269908169872414, 3)
		qc.swap(3, 0)
		qc.crx(0.7853981633974483, 3, 1)
		qc.cswap(3, 2, 0)
	qc.reset(qr_925e70)
	
qc.reset(qr_925e70)
qc.h(0)
qc.cp(1.5707963267948966, 3, 1)
qc.ccz(2, 1, 0)
qc.iswap(3, 2)
qc.ccx(3, 1, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([OptimizeAnnotated(),CollectCliffords(),CollectMultiQBlocks()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
