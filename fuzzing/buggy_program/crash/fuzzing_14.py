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

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

def fun_f07a32(): 
	qc =  QuantumCircuit(3) 
	qc.cswap(2, 1, 0)
	qc.ccx(2, 1, 0)
	qc.x(0)
	return qc.to_gate() 
g_4c73f5 = fun_f07a32().control(1) 
qc.append(g_4c73f5, [0,3,4,2]) 
qc.cp(0.7853981633974483, 0, 2)
qc.ry(0.39269908169872414, 2)
qc.h(0)
qc.ccz(3, 2, 0)
qc.cswap(4, 2, 0)
qc.ry(1.5707963267948966, 4)
qc.rz(0.39269908169872414, 3)
qc.append(Permutation(1, pattern=[0]), [qreg[2]])
qc.append(RXGate(3.155), [qreg[0]])
qc.crz(0.7853981633974483, 3, 2)
qc.y(3)
qc.append(CXGate(), [qreg[1], qreg[4]])
qc.append(HGate(), [qreg[4]])
qc.p(1.5707963267948966, 4)

qr_f78879 = QuantumRegister(2)
cr_f78879 = ClassicalRegister(2)
qc.add_register(qr_f78879)
qc.add_register(cr_f78879)
qc.h(qr_f78879[0])
qc.cx(qr_f78879[0], qr_f78879[1])         
qc.measure(qr_f78879[0], cr_f78879[0]) 
qc.measure(qr_f78879[1], cr_f78879[1]) 
with qc.switch(cr_f78879) as case: 
	with case(0b00, 0b11): 
		
		qr_085952 = QuantumRegister(2)
		cr_085952 = ClassicalRegister(2)
		qc.add_register(qr_085952)
		qc.add_register(cr_085952)
		qc.x(qr_085952[0])
		qc.x(qr_085952[1])
		qc.measure(qr_085952[0], cr_085952[0]) 
		qc.measure(qr_085952[1], cr_085952[1]) 
		with qc.if_test((cr_085952, 0b11)) as else_085952: 
			pass
		with else_085952: 
			qc.append(XOR(1, seed=42), [qreg[2]])
			qc.append(TwoLocal(2, reps=1, parameter_prefix='theta_34ee81'), [qreg[1], qreg[4]])
			qc.cry(1.5707963267948966, 3, 4)
			qc.cry(1.5707963267948966, 0, 3)
			def fun_ba5604(): 
				qc =  QuantumCircuit(3) 
				qc.cp(0.7853981633974483, 2, 0)
				qc.ccx(2, 1, 0)
				qc.h(0)
				return qc.to_gate() 
			g_04b556 = fun_ba5604().control(1) 
			qc.append(g_04b556, [3,0,1,2]) 
			qc.append(RXGate(1.76), [qreg[0]])
			def fun_b17b7f(): 
				qc =  QuantumCircuit(3) 
				qc.cry(0.7853981633974483, 2, 1)
				qc.tdg(0)
				qc.h(2)
				return qc.to_gate() 
			g_018d22 = fun_b17b7f().control(1) 
			qc.append(g_018d22, [3,1,2,4]) 
			qc.rx(1.5707963267948966, 1)
			qc.swap(4, 1)
			def fun_f0ae92(): 
				qc =  QuantumCircuit(3) 
				qc.rx(0.39269908169872414, 0)
				qc.tdg(2)
				qc.crz(0.7853981633974483, 2, 0)
				return qc.to_gate() 
			g_e25768 = fun_f0ae92().control(1) 
			qc.append(g_e25768, [2,0,4,1]) 
			qc.append(C3XGate(), [qreg[2], qreg[4], qreg[1], qreg[3]])
			qc.append(CXGate(), [qreg[4], qreg[0]])
			qc.append(QFT(4), [qreg[1], qreg[0], qreg[3], qreg[4]])
			qc.z(4)
			qc.append(CXGate(), [qreg[3], qreg[2]])
		qc.reset(qr_085952)
		
	with case(case.DEFAULT): 
		
		qr_f78879 = QuantumRegister(2)
		cr_f78879 = ClassicalRegister(2)
		qc.add_register(qr_f78879)
		qc.add_register(cr_f78879)
		qc.h(qr_f78879[0])
		qc.cx(qr_f78879[0], qr_f78879[1])         
		qc.measure(qr_f78879[0], cr_f78879[0]) 
		qc.measure(qr_f78879[1], cr_f78879[1]) 
		with qc.switch(cr_f78879) as case: 
			with case(0b00, 0b11): 
				def fun_c70355(): 
					qc =  QuantumCircuit(3) 
					qc.ccz(2, 1, 0)
					qc.cswap(2, 1, 0)
					qc.ccx(2, 1, 0)
					return qc.to_gate() 
				g_7aec88 = fun_c70355().control(1) 
				qc.append(g_7aec88, [2,4,1,0]) 
				qc.cry(0.39269908169872414, 1, 2)
				qc.rx(1.5707963267948966, 4)
				qc.h(3)
				qc.ccx(4, 3, 2)
				qc.append(XOR(4, seed=42), [qreg[2], qreg[1], qreg[0], qreg[3]])
				qc.iswap(3, 0)
				qc.append(U3Gate(0.275, 2.822, 0.682), [qreg[0]])
				qc.h(2)
				qc.h(0)
				qc.append(RZGate(0.484), [qreg[1]])
				def fun_e787b0(): 
					qc =  QuantumCircuit(3) 
					qc.ry(1.5707963267948966, 0)
					qc.cz(0, 2)
					qc.swap(1, 0)
					return qc.to_gate() 
				g_a6e419 = fun_e787b0().control(1) 
				qc.append(g_a6e419, [3,2,1,4]) 
				qc.crz(1.5707963267948966, 3, 2)
				qc.append(CRXGate(2.474), [qreg[2], qreg[1]])
				qc.ccz(4, 2, 1)
			with case(case.DEFAULT): 
				qc.append(RZGate(2.288), [qreg[2]])
				qc.cx(4, 2)
				qc.append(Permutation(2, pattern=[1, 0]), [qreg[1], qreg[4]])
				qc.append(StatePreparation([(-0.34425792104389585-0.46634449646651954j), (0.44244962127531307+0.05100026436727047j), (0.3613326118317902+0.4698460782307226j), (0.31745803128012356-0.11640620625850844j)]), [qreg[1], qreg[4]])
				qc.cz(2, 3)
				qc.append(RXGate(1.488), [qreg[0]])
				def fun_f3012b(): 
					qc =  QuantumCircuit(3) 
					qc.swap(2, 1)
					qc.crz(0.39269908169872414, 2, 1)
					qc.x(0)
					return qc.to_gate() 
				g_efca8b = fun_f3012b().control(1) 
				qc.append(g_efca8b, [0,1,2,3]) 
				qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[4], qreg[0]])
				qc.append(XGate(), [qreg[2]])
				qc.iswap(4, 3)
				qc.append(RXGate(4.694), [qreg[3]])
				qc.ch(4, 2)
				qc.x(1)
				qc.iswap(4, 3)
				qc.ccz(4, 3, 2)
		qc.reset(qr_f78879)
		
qc.reset(qr_f78879)
qc.crx(0.39269908169872414, 2, 4)
qc.rz(0.39269908169872414, 4)
qc.swap(4, 2)
qc.append(XGate(), [qreg[2]])
qc.append(Initialize([(0.44098813351837124+0.7127511799086933j), (-0.11300075180417098+0.533616015245458j)]), [qreg[3]])
qc.ccx(3, 2, 0)
qc.ccx(2, 1, 0)
qc.append(CRXGate(4.112), [qreg[0], qreg[1]])
qc.h(2)
def fun_e62c7a(): 
	qc =  QuantumCircuit(3) 
	qc.cx(2, 0)
	qc.tdg(2)
	qc.swap(2, 0)
	return qc.to_gate() 
g_715df5 = fun_e62c7a().control(1) 
qc.append(g_715df5, [0,4,1,3]) 
def fun_d5a23f(): 
	qc =  QuantumCircuit(3) 
	qc.rz(0.7853981633974483, 0)
	qc.h(0)
	qc.rx(1.5707963267948966, 1)
	return qc.to_gate() 
g_b3dcd9 = fun_d5a23f().control(1) 
qc.append(g_b3dcd9, [0,4,3,1]) 
qc.append(CUGate(3.01, 5.135, 0.668, 1.561), [qreg[1], qreg[4]])
qc.x(2)
qc.append(HGate(), [qreg[1]])
qc.z(2)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveDiagonalGatesBeforeMeasure(),CommutativeInverseCancellation(),ElidePermutations()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
