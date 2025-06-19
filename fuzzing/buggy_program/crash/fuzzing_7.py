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

qc.cry(0.7853981633974483, 0, 3)
qc.cry(0.39269908169872414, 0, 2)
qc.ccx(3, 2, 0)
qc.z(2)
qc.swap(1, 0)

qr_45ff77 = QuantumRegister(2)
cr_45ff77 = ClassicalRegister(2)
qc.add_register(qr_45ff77)
qc.add_register(cr_45ff77)
qc.x(qr_45ff77[0])
qc.x(qr_45ff77[1])
qc.measure(qr_45ff77[0], cr_45ff77[0]) 
qc.measure(qr_45ff77[1], cr_45ff77[1]) 
with qc.if_test((cr_45ff77, 0b11)) as else_45ff77: 
	pass
with else_45ff77: 
	
	qr_16e9f2 = QuantumRegister(2)
	cr_16e9f2 = ClassicalRegister(2)
	qc.add_register(qr_16e9f2)
	qc.add_register(cr_16e9f2)
	qc.x(qr_16e9f2[0])
	qc.x(qr_16e9f2[1])
	qc.measure(qr_16e9f2[0], cr_16e9f2[0]) 
	qc.measure(qr_16e9f2[1], cr_16e9f2[1]) 
	with qc.if_test((cr_16e9f2, 0b11)) as else_16e9f2: 
		qc.cx(3, 0)
		qc.rx(0.7853981633974483, 3)
		qc.cry(1.5707963267948966, 0, 3)
		qc.iswap(3, 0)
		qc.cswap(3, 2, 1)
	with else_16e9f2: 
		qc.tdg(2)
		qc.cz(0, 2)
		qc.ccx(3, 2, 1)
		qc.crx(0.7853981633974483, 0, 2)
		qc.ch(2, 0)
	qc.reset(qr_16e9f2)
	
qc.reset(qr_45ff77)
qc.cx(3, 1)
qc.ccz(3, 1, 0)
qc.cswap(3, 2, 1)
qc.t(3)
qc.ry(1.5707963267948966, 3)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CollectCliffords(),Collect2qBlocks(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
