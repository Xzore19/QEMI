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

qc.y(3)
qc.z(0)
qc.cry(0.7853981633974483, 0, 1)
qc.cx(1, 0)
qc.ry(0.39269908169872414, 1)
with qc.for_loop(range(3)) as i_099576:
	
	qr_ebc45d = QuantumRegister(2)
	cr_ebc45d = ClassicalRegister(2)
	qc.add_register(qr_ebc45d)
	qc.add_register(cr_ebc45d)
	qc.h(qr_ebc45d[0])
	qc.cx(qr_ebc45d[0], qr_ebc45d[1])         
	qc.measure(qr_ebc45d[0], cr_ebc45d[0]) 
	qc.measure(qr_ebc45d[1], cr_ebc45d[1]) 
	with qc.switch(cr_ebc45d) as case: 
		with case(0b00, 0b11): 
			qc.rz(1.5707963267948966, 1)
			qc.z(1)
			qc.t(1)
			qc.h(2)
			qc.rx(0.39269908169872414, 1)
		with case(case.DEFAULT): 
			qc.cx(2, 0)
			qc.cp(1.5707963267948966, 3, 0)
			qc.y(2)
			qc.crz(0.7853981633974483, 0, 1)
			qc.swap(3, 0)
	qc.reset(qr_ebc45d)
	
	qc.break_loop()
	with qc.for_loop(range(3)) as i_099576:
		qc.cswap(3, 2, 1)
		qc.rz(1.5707963267948966, 3)
		qc.t(2)
		qc.cswap(3, 1, 0)
		qc.x(1)
		qc.break_loop()
		qc.z(1)
		qc.cx(3, 1)
		qc.crz(0.7853981633974483, 3, 2)
		qc.cry(0.39269908169872414, 0, 3)
		qc.z(0)
	
qc.x(2)
qc.t(1)
qc.x(0)
qc.cswap(3, 2, 0)
qc.cswap(3, 2, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([ConsolidateBlocks(),CollectCliffords(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
