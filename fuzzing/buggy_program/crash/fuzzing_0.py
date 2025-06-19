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

qc.cz(1, 3)
qc.cz(2, 3)
qc.cry(0.39269908169872414, 1, 0)
qc.crx(0.7853981633974483, 2, 3)
qc.crx(1.5707963267948966, 2, 0)
with qc.for_loop(range(3)) as i_f99d40:
	with qc.for_loop(range(3)) as i_69b38c:
		qc.cx(2, 0)
		qc.t(0)
		qc.tdg(0)
		qc.y(0)
		qc.rx(1.5707963267948966, 2)
		qc.break_loop()
		qc.h(0)
		qc.cp(0.7853981633974483, 2, 1)
		qc.ccx(2, 1, 0)
		qc.t(0)
		qc.iswap(2, 1)
	
	qc.continue_loop()
	
	qr_f99d40 = QuantumRegister(2)
	cr_f99d40 = ClassicalRegister(2)
	qc.add_register(qr_f99d40)
	qc.add_register(cr_f99d40)
	qc.x(qr_f99d40[0])
	qc.x(qr_f99d40[1])
	qc.measure(qr_f99d40[0], cr_f99d40[0]) 
	qc.measure(qr_f99d40[1], cr_f99d40[1]) 
	with qc.while_loop((cr_f99d40, 0b10)): 
		qc.tdg(1)
		qc.iswap(3, 2)
		qc.iswap(3, 1)
		qc.cp(1.5707963267948966, 0, 2)
		qc.tdg(0)
		qc.measure(qr_f99d40[0], cr_f99d40[0]) 
		qc.measure(qr_f99d40[1], cr_f99d40[1]) 
	qc.reset(qr_f99d40)
	
qc.cx(1, 0)
qc.tdg(3)
qc.cswap(2, 1, 0)
qc.cry(0.7853981633974483, 3, 0)
qc.p(0.39269908169872414, 1)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(CommutativeInverseCancellation()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
