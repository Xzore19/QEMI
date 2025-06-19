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

qc.t(1)
qc.y(2)
qc.rx(0.39269908169872414, 1)
qc.cz(0, 3)
qc.cry(0.39269908169872414, 2, 1)

qr_03a12a = QuantumRegister(2)
cr_03a12a = ClassicalRegister(2)
qc.add_register(qr_03a12a)
qc.add_register(cr_03a12a)
qc.x(qr_03a12a[0])
qc.x(qr_03a12a[1])
qc.measure(qr_03a12a[0], cr_03a12a[0]) 
qc.measure(qr_03a12a[1], cr_03a12a[1]) 
with qc.if_test((cr_03a12a, 0b11)) as else_03a12a: 
	pass
with else_03a12a: 
	
	qr_1efb2a = QuantumRegister(2)
	cr_1efb2a = ClassicalRegister(2)
	qc.add_register(qr_1efb2a)
	qc.add_register(cr_1efb2a)
	qc.h(qr_1efb2a[0])
	qc.cx(qr_1efb2a[0], qr_1efb2a[1])         
	qc.measure(qr_1efb2a[0], cr_1efb2a[0]) 
	qc.measure(qr_1efb2a[1], cr_1efb2a[1]) 
	with qc.switch(cr_1efb2a) as case: 
		with case(0b00, 0b11): 
			qc.y(2)
			qc.cz(1, 2)
			qc.crz(1.5707963267948966, 2, 1)
			qc.cz(2, 3)
			qc.ch(1, 0)
		with case(case.DEFAULT): 
			qc.swap(1, 0)
			qc.cz(2, 3)
			qc.ch(2, 0)
			qc.y(3)
			qc.cry(1.5707963267948966, 0, 2)
	qc.reset(qr_1efb2a)
	
qc.reset(qr_03a12a)
qc.rx(0.7853981633974483, 3)
qc.x(0)
qc.p(0.39269908169872414, 1)
qc.ccx(3, 2, 0)
qc.ccz(3, 1, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CollectCliffords(),TemplateOptimization(),OptimizeSwapBeforeMeasure()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
