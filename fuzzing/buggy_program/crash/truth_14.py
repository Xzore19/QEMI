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
		pass
		
	with case(case.DEFAULT): 
		pass
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
