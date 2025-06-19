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

qc.ch(3, 2)
qc.z(1)
qc.p(1.5707963267948966, 2)
qc.p(0.39269908169872414, 3)
qc.h(0)
with qc.for_loop(range(3)) as i_7de97f:
	
	qr_2d6395 = QuantumRegister(2)
	cr_2d6395 = ClassicalRegister(2)
	qc.add_register(qr_2d6395)
	qc.add_register(cr_2d6395)
	qc.x(qr_2d6395[0])
	qc.x(qr_2d6395[1])
	qc.measure(qr_2d6395[0], cr_2d6395[0]) 
	qc.measure(qr_2d6395[1], cr_2d6395[1]) 
	with qc.while_loop((cr_2d6395, 0b11)): 
		qc.measure(qr_2d6395[0], cr_2d6395[0]) 
		qc.measure(qr_2d6395[1], cr_2d6395[1]) 
		qc.x(3)
		qc.ry(0.39269908169872414, 0)
		qc.x(3)
		qc.ccz(3, 2, 0)
		qc.x(2)
		qc.break_loop()
		qc.tdg(0)
		qc.rx(0.7853981633974483, 1)
		qc.iswap(1, 0)
		qc.rz(0.7853981633974483, 3)
		qc.cx(3, 0)
	qc.reset(qr_2d6395)
	
	qc.break_loop()
	with qc.for_loop(range(3)) as i_7de97f:
		qc.ccx(3, 2, 1)
		qc.cp(0.39269908169872414, 2, 0)
		qc.x(1)
		qc.z(0)
		qc.cswap(2, 1, 0)
		qc.continue_loop()
		qc.tdg(1)
		qc.x(3)
		qc.p(0.39269908169872414, 3)
		qc.ccx(2, 1, 0)
		qc.iswap(2, 0)
	
qc.cz(1, 3)
qc.x(3)
qc.p(1.5707963267948966, 1)
qc.x(0)
qc.x(0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CollectCliffords(),CommutationAnalysis(),Optimize1qGatesSimpleCommutation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
