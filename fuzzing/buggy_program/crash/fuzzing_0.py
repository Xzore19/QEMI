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
=======
qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

# qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_74182d'), [qreg[0], qreg[3], qreg[1], qreg[4]])
qc.append(XGate(), [qreg[1]])
# qc.h(2)
# qc.cx(4, 2)
# qc.append(MCPhaseGate(1.0, num_ctrl_qubits=2), [qreg[4], qreg[2], qreg[3]])

qr_d3ecd5 = QuantumRegister(2)
cr_d3ecd5 = ClassicalRegister(2)
qc.add_register(qr_d3ecd5)
qc.add_register(cr_d3ecd5)
qc.x(qr_d3ecd5[0])
qc.x(qr_d3ecd5[1])
qc.measure(qr_d3ecd5[0], cr_d3ecd5[0]) 
qc.measure(qr_d3ecd5[1], cr_d3ecd5[1]) 
with qc.if_test((cr_d3ecd5, 0b11)) as else_1: 
	pass
with else_1: 
	
	qr_b1d4e4 = QuantumRegister(2)
	cr_b1d4e4 = ClassicalRegister(2)
	qc.add_register(qr_b1d4e4)
	qc.add_register(cr_b1d4e4)
	qc.x(qr_b1d4e4[0])
	qc.x(qr_b1d4e4[1])
	qc.measure(qr_b1d4e4[0], cr_b1d4e4[0]) 
	qc.measure(qr_b1d4e4[1], cr_b1d4e4[1]) 
	with qc.while_loop((cr_b1d4e4, 0b11)): 
		qc.measure(qr_b1d4e4[0], cr_b1d4e4[0]) 
		qc.measure(qr_b1d4e4[1], cr_b1d4e4[1]) 
		# qc.append(CRXGate(0.365), [qreg[3], qreg[2]])
		qc.append(RXGate(4.113), [qreg[1]])
		# qc.append(CUGate(0.161, 3.662, 4.401, 2.539), [qreg[1], qreg[3]])
		# qc.append(RXGate(2.505), [qreg[1]])
		# qc.append(PauliFeatureMap(4, reps=1, parameter_prefix='x_185e6b'), [qreg[3], qreg[4], qreg[2], qreg[1]])
		# qc.break_loop()
		# qc.cry(0.39269908169872414, 2, 1)
		# qc.cry(0.39269908169872414, 2, 1)
		# qc.append(Initialize([(0.22266139667895665+0.35156753972657057j), (0.24393015682759972+0.49543859100056015j), (0.2167041548567754-0.6086105667220096j), (0.2479240984804862+0.20742945140887764j)]), [qreg[2], qreg[1]])
		# qc.y(4)
		# qc.iswap(1, 0)
	

qc.append(Initialize([(0.6675295366963846+0.7159907893058729j), (0.024362866765987624-0.20289888612312826j)]), [qreg[1]])
# qc.append(MCXGate(3), [qreg[2], qreg[3], qreg[1], qreg[4]])
# qc.append(XGate(), [qreg[1]])
# qc.z(4)
# qc.append(SwapGate(), [qreg[3], qreg[1]])
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

p = PassManager(CommutativeInverseCancellation()) 
qc = p.run(qc) 

<<<<<<< HEAD
compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 
=======
compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 
>>>>>>> I forget what I had modified

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
