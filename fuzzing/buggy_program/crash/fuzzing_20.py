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
qc.append(CXGate(), [qreg[3], qreg[2]])
qc.x(1)
qc.cry(0.39269908169872414, 1, 3)
def fun_2523cd(): 
	qc =  QuantumCircuit(3) 
	qc.ry(0.39269908169872414, 1)
	qc.y(2)
	qc.cry(0.7853981633974483, 2, 0)
	return qc.to_gate() 
g_09c710 = fun_2523cd().control(1) 
qc.append(g_09c710, [0,1,3,2]) 
with qc.for_loop(range(3)) as i_3cf384:
	with qc.for_loop(range(3)) as i_cbe5cb:
		qc.append(Permutation(4, pattern=[0, 1, 3, 2]), [qreg[0], qreg[1], qreg[3], qreg[2]])
		qc.append(SwapGate(), [qreg[2], qreg[0]])
		def fun_b5cf1a(): 
			qc =  QuantumCircuit(3) 
			qc.cx(2, 0)
			qc.crz(1.5707963267948966, 2, 1)
			qc.ch(2, 0)
			return qc.to_gate() 
		g_25d5fc = fun_b5cf1a().control(1) 
		qc.append(g_25d5fc, [2,1,0,3]) 
		qc.swap(1, 0)
		qc.append(RZGate(4.836), [qreg[1]])
		qc.continue_loop()
		qc.ccz(3, 2, 1)
		qc.h(1)
		qc.h(0)
		qc.append(U3Gate(2.097, 1.43, 5.895), [qreg[1]])
		qc.y(3)
	
	qc.continue_loop()
	
	qr_3cf384 = QuantumRegister(2)
	cr_3cf384 = ClassicalRegister(2)
	qc.add_register(qr_3cf384)
	qc.add_register(cr_3cf384)
	qc.x(qr_3cf384[0])
	qc.x(qr_3cf384[1])
	qc.measure(qr_3cf384[0], cr_3cf384[0]) 
	qc.measure(qr_3cf384[1], cr_3cf384[1]) 
	with qc.if_test((cr_3cf384, 0b11)) as else_3cf384: 
		pass
	with else_3cf384: 
		qc.rx(0.7853981633974483, 0)
		qc.y(2)
		qc.y(3)
		qc.append(CRXGate(4.287), [qreg[0], qreg[1]])
		qc.cx(3, 1)
	qc.reset(qr_3cf384)
	
qc.t(2)
qc.y(2)
def fun_ff0641(): 
	qc =  QuantumCircuit(3) 
	qc.x(1)
	qc.p(1.5707963267948966, 1)
	qc.cz(0, 1)
	return qc.to_gate() 
g_6fe8ec = fun_ff0641().control(1) 
qc.append(g_6fe8ec, [2,1,0,3]) 
qc.append(HGate(), [qreg[3]])
qc.t(1)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([OptimizeAnnotated(),ElidePermutations(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
