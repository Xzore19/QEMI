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

qc.append(OR(3), [qreg[1], qreg[2], qreg[0], qreg[3]])
qc.append(SwapGate(), [qreg[3], qreg[0]])
qc.x(3)
qc.cp(1.5707963267948966, 0, 3)
qc.rx(0.7853981633974483, 0)

qr_4c231b = QuantumRegister(2)
cr_4c231b = ClassicalRegister(2)
qc.add_register(qr_4c231b)
qc.add_register(cr_4c231b)
qc.x(qr_4c231b[0])
qc.x(qr_4c231b[1])
qc.measure(qr_4c231b[0], cr_4c231b[0]) 
qc.measure(qr_4c231b[1], cr_4c231b[1]) 
with qc.while_loop((cr_4c231b, 0b10)): 
	
	qr_8e1dad = QuantumRegister(2)
	cr_8e1dad = ClassicalRegister(2)
	qc.add_register(qr_8e1dad)
	qc.add_register(cr_8e1dad)
	qc.x(qr_8e1dad[0])
	qc.x(qr_8e1dad[1])
	qc.measure(qr_8e1dad[0], cr_8e1dad[0]) 
	qc.measure(qr_8e1dad[1], cr_8e1dad[1]) 
	with qc.if_test((cr_8e1dad, 0b11)) as else_8e1dad: 
		qc.append(RZGate(4.265), [qreg[1]])
		qc.iswap(1, 0)
		qc.z(0)
		qc.append(XGate(), [qreg[3]])
		qc.append(RXGate(2.513), [qreg[1]])
	with else_8e1dad: 
		qc.append(CXGate(), [qreg[0], qreg[2]])
		def fun_07824e(): 
			qc =  QuantumCircuit(3) 
			qc.ry(1.5707963267948966, 0)
			qc.p(0.7853981633974483, 2)
			qc.crx(0.39269908169872414, 0, 2)
			return qc.to_gate() 
		g_14e4cf = fun_07824e().control(1) 
		qc.append(g_14e4cf, [3,0,2,1]) 
		def fun_1ddf3d(): 
			qc =  QuantumCircuit(3) 
			qc.cry(0.7853981633974483, 1, 0)
			qc.h(2)
			qc.iswap(2, 1)
			return qc.to_gate() 
		g_07493c = fun_1ddf3d().control(1) 
		qc.append(g_07493c, [1,2,0,3]) 
		qc.h(3)
		def fun_66c61a(): 
			qc =  QuantumCircuit(3) 
			qc.tdg(0)
			qc.crx(1.5707963267948966, 0, 2)
			qc.cswap(2, 1, 0)
			return qc.to_gate() 
		g_fc4e24 = fun_66c61a().control(1) 
		qc.append(g_fc4e24, [3,0,1,2]) 
	qc.reset(qr_8e1dad)
	
	qc.measure(qr_4c231b[0], cr_4c231b[0]) 
	qc.measure(qr_4c231b[1], cr_4c231b[1]) 
qc.reset(qr_4c231b)
qc.append(Initialize([(0.5286580026953233-0.5838877827938295j), (-0.16127168119912175+0.594632002278305j)]), [qreg[0]])
qc.ry(0.39269908169872414, 3)
qc.cx(3, 0)
qc.cry(1.5707963267948966, 1, 3)
def fun_c879f9(): 
	qc =  QuantumCircuit(3) 
	qc.ch(2, 1)
	qc.iswap(2, 1)
	qc.ccx(2, 1, 0)
	return qc.to_gate() 
g_ec369b = fun_c879f9().control(1) 
qc.append(g_ec369b, [3,1,2,0]) 
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CommutativeInverseCancellation(),OptimizeAnnotated(),Optimize1qGatesDecomposition()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
