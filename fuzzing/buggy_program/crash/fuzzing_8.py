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

qc.cp(1.5707963267948966, 1, 3)
qc.cz(1, 2)
qc.h(2)
qc.rx(1.5707963267948966, 3)
qc.y(2)

qr_af2a34 = QuantumRegister(2)
cr_af2a34 = ClassicalRegister(2)
qc.add_register(qr_af2a34)
qc.add_register(cr_af2a34)
qc.x(qr_af2a34[0])
qc.x(qr_af2a34[1])
qc.measure(qr_af2a34[0], cr_af2a34[0]) 
qc.measure(qr_af2a34[1], cr_af2a34[1]) 
with qc.if_test((cr_af2a34, 0b11)) as else_af2a34: 
	
	qr_0872bd = QuantumRegister(2)
	cr_0872bd = ClassicalRegister(2)
	qc.add_register(qr_0872bd)
	qc.add_register(cr_0872bd)
	qc.x(qr_0872bd[0])
	qc.x(qr_0872bd[1])
	qc.measure(qr_0872bd[0], cr_0872bd[0]) 
	qc.measure(qr_0872bd[1], cr_0872bd[1]) 
	with qc.while_loop((cr_0872bd, 0b10)): 
		qc.crz(0.7853981633974483, 3, 2)
		qc.cp(1.5707963267948966, 3, 1)
		qc.cp(1.5707963267948966, 0, 3)
		qc.cz(0, 1)
		qc.cx(1, 0)
		qc.measure(qr_0872bd[0], cr_0872bd[0]) 
		qc.measure(qr_0872bd[1], cr_0872bd[1]) 
	qc.reset(qr_0872bd)
	
with else_af2a34: 
	a = 0
	with qc.for_loop(range(a)) as i_af2a34:
		qc.ch(2, 0)
		qc.rx(1.5707963267948966, 1)
		qc.ry(0.39269908169872414, 0)
		qc.swap(1, 0)
		qc.cswap(3, 1, 0)
	
qc.reset(qr_af2a34)
qc.iswap(3, 1)
qc.y(2)
qc.cswap(2, 1, 0)
qc.t(3)
qc.rz(0.39269908169872414, 3)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([OptimizeSwapBeforeMeasure(),CollectCliffords(),Optimize1qGatesSimpleCommutation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
