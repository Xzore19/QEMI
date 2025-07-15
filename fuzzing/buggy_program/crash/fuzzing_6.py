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

qc.ch(2, 1)
qc.z(2)
qc.rx(0.39269908169872414, 0)
qc.ch(3, 0)
qc.crx(0.7853981633974483, 0, 3)

qr_5976e5 = QuantumRegister(2)
cr_5976e5 = ClassicalRegister(2)
qc.add_register(qr_5976e5)
qc.add_register(cr_5976e5)
qc.h(qr_5976e5[0])
qc.cx(qr_5976e5[0], qr_5976e5[1])         
qc.measure(qr_5976e5[0], cr_5976e5[0]) 
qc.measure(qr_5976e5[1], cr_5976e5[1]) 
with qc.switch(cr_5976e5) as case: 
	with case(0b00, 0b11): 
		a = 0
		with qc.for_loop(range(a)) as i_c5d0ca:
			qc.crx(1.5707963267948966, 2, 1)
			qc.z(3)
			qc.ch(3, 0)
			qc.rx(0.39269908169872414, 3)
			qc.tdg(3)
		
	with case(case.DEFAULT): 
		
		qr_5976e5 = QuantumRegister(2)
		cr_5976e5 = ClassicalRegister(2)
		qc.add_register(qr_5976e5)
		qc.add_register(cr_5976e5)
		qc.x(qr_5976e5[0])
		qc.x(qr_5976e5[1])
		qc.measure(qr_5976e5[0], cr_5976e5[0]) 
		qc.measure(qr_5976e5[1], cr_5976e5[1]) 
		with qc.while_loop((cr_5976e5, 0b11)): 
			qc.measure(qr_5976e5[0], cr_5976e5[0]) 
			qc.measure(qr_5976e5[1], cr_5976e5[1]) 
			qc.p(1.5707963267948966, 0)
			qc.cp(0.7853981633974483, 3, 2)
			qc.z(3)
			qc.y(3)
			qc.crz(0.39269908169872414, 0, 1)
			qc.break_loop()
			qc.ry(0.39269908169872414, 1)
			qc.ch(3, 2)
			qc.rx(0.39269908169872414, 1)
			qc.ccz(3, 1, 0)
			qc.cx(3, 0)
		qc.reset(qr_5976e5)
		
qc.reset(qr_5976e5)
qc.ccx(2, 1, 0)
qc.iswap(3, 2)
qc.z(1)
qc.crz(0.7853981633974483, 0, 3)
qc.x(2)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([Collect2qBlocks(),TemplateOptimization(),ConsolidateBlocks()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
