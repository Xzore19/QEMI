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

<<<<<<< HEAD
qreg = QuantumRegister(4) 
creg = ClassicalRegister(4) 
qc = QuantumCircuit(qreg, creg) 

qc.crx(1.5707963267948966, 0, 1)
qc.ry(0.39269908169872414, 0)
qc.rz(1.5707963267948966, 3)
qc.t(2)
qc.cx(2, 1)

qr_07dd76 = QuantumRegister(2)
cr_07dd76 = ClassicalRegister(2)
qc.add_register(qr_07dd76)
qc.add_register(cr_07dd76)
qc.x(qr_07dd76[0])
qc.x(qr_07dd76[1])
qc.measure(qr_07dd76[0], cr_07dd76[0]) 
qc.measure(qr_07dd76[1], cr_07dd76[1]) 
with qc.while_loop((cr_07dd76, 0b10)): 
	
	qr_0107d6 = QuantumRegister(2)
	cr_0107d6 = ClassicalRegister(2)
	qc.add_register(qr_0107d6)
	qc.add_register(cr_0107d6)
	qc.x(qr_0107d6[0])
	qc.x(qr_0107d6[1])
	qc.measure(qr_0107d6[0], cr_0107d6[0]) 
	qc.measure(qr_0107d6[1], cr_0107d6[1]) 
	with qc.while_loop((cr_0107d6, 0b10)): 
		qc.ry(0.39269908169872414, 3)
		qc.crx(0.7853981633974483, 0, 3)
		qc.ccx(2, 1, 0)
		qc.iswap(2, 0)
		qc.cry(1.5707963267948966, 0, 3)
		qc.measure(qr_0107d6[0], cr_0107d6[0]) 
		qc.measure(qr_0107d6[1], cr_0107d6[1]) 
	qc.reset(qr_0107d6)
	
	qc.measure(qr_07dd76[0], cr_07dd76[0]) 
	qc.measure(qr_07dd76[1], cr_07dd76[1]) 
qc.reset(qr_07dd76)
qc.tdg(2)
qc.rz(0.39269908169872414, 1)
qc.z(0)
qc.rx(0.39269908169872414, 3)
qc.ch(3, 0)
=======
qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.t(3)
qc.cry(0.7853981633974483, 3, 0)
qc.y(3)
qc.append(HGate(), [qreg[0]])
qc.append(HGate(), [qreg[4]])

qr_cb4715 = QuantumRegister(2)
cr_cb4715 = ClassicalRegister(2)
qc.add_register(qr_cb4715)
qc.add_register(cr_cb4715)
qc.x(qr_cb4715[0])
qc.x(qr_cb4715[1])
qc.measure(qr_cb4715[0], cr_cb4715[0]) 
qc.measure(qr_cb4715[1], cr_cb4715[1]) 
with qc.while_loop((cr_cb4715, 0b10)): 
	
	qr_6479ad = QuantumRegister(2)
	cr_6479ad = ClassicalRegister(2)
	qc.add_register(qr_6479ad)
	qc.add_register(cr_6479ad)
	qc.x(qr_6479ad[0])
	qc.x(qr_6479ad[1])
	qc.measure(qr_6479ad[0], cr_6479ad[0]) 
	qc.measure(qr_6479ad[1], cr_6479ad[1]) 
	with qc.if_test((cr_6479ad, 0b11)) as else_1: 
		pass
	with else_1: 
		qc.append(QFT(2), [qreg[0], qreg[3]])
		qc.append(RZGate(2.311), [qreg[2]])
		qc.append(U3Gate(3.901, 3.276, 3.003), [qreg[2]])
		qc.cp(0.7853981633974483, 0, 2)
		qc.append(U3Gate(4.58, 1.758, 4.108), [qreg[3]])
	
	
	qc.measure(qr_cb4715[0], cr_cb4715[0]) 
	qc.measure(qr_cb4715[1], cr_cb4715[1]) 

qc.append(Initialize([(-0.7801186157474757-0.20229923273655934j), (0.5189847955399074+0.28485917186715687j)]), [qreg[3]])
qc.append(CXGate(), [qreg[3], qreg[1]])
qc.append(RXGate(4.351), [qreg[4]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[1], qreg[3], qreg[4], qreg[0]])
qc.crz(0.39269908169872414, 2, 4)
>>>>>>> I forget what I had modified
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
<<<<<<< HEAD
=======
qc.measure(qreg[4], creg[4]) 
>>>>>>> I forget what I had modified

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

<<<<<<< HEAD
p = PassManager([Collect1qRuns(),CommutativeInverseCancellation(),ConsolidateBlocks()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
=======
p = PassManager(CommutativeInverseCancellation()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
>>>>>>> I forget what I had modified
result = job.result().get_counts() 
print(result)
