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

qc.append(CCXGate(), [qreg[1], qreg[3], qreg[2]])
qc.h(2)
qc.swap(2, 0)
qc.append(U3Gate(3.371, 3.182, 4.717), [qreg[2]])
def fun_4869d2(): 
	qc =  QuantumCircuit(3) 
	qc.cswap(2, 1, 0)
	qc.ry(1.5707963267948966, 0)
	qc.cz(0, 1)
	return qc.to_gate() 
g_594795 = fun_4869d2().control(1) 
qc.append(g_594795, [3,1,2,0]) 

qr_568b6c = QuantumRegister(2)
cr_568b6c = ClassicalRegister(2)
qc.add_register(qr_568b6c)
qc.add_register(cr_568b6c)
qc.h(qr_568b6c[0])
qc.cx(qr_568b6c[0], qr_568b6c[1])         
qc.measure(qr_568b6c[0], cr_568b6c[0]) 
qc.measure(qr_568b6c[1], cr_568b6c[1]) 
with qc.switch(cr_568b6c) as case: 
	with case(0b00, 0b11): 
		
		qr_e0fe7d = QuantumRegister(2)
		cr_e0fe7d = ClassicalRegister(2)
		qc.add_register(qr_e0fe7d)
		qc.add_register(cr_e0fe7d)
		qc.x(qr_e0fe7d[0])
		qc.x(qr_e0fe7d[1])
		qc.measure(qr_e0fe7d[0], cr_e0fe7d[0]) 
		qc.measure(qr_e0fe7d[1], cr_e0fe7d[1]) 
		with qc.if_test((cr_e0fe7d, 0b11)) as else_e0fe7d: 
			qc.cry(0.7853981633974483, 0, 3)
			qc.p(0.7853981633974483, 1)
			qc.append(CUGate(0.322, 1.379, 1.987, 1.183), [qreg[3], qreg[1]])
			qc.append(StatePreparation([(-0.36427702281216034-0.11489569942592896j), (-0.34815688741926326-0.17064657907361674j), (-0.09491350886767948-0.018024464294138j), (-0.3792325187163538+0.2042249386149599j), (-0.09133473020564184+0.004412969090179079j), (0.10160663675936615-0.05381888485072329j), (-0.3076741707155298-0.0012456939538053504j), (-0.08283754253957905-0.27245445135401625j), (0.14741931901411387+0.17066932969312795j), (-0.01978830293918648+0.09867176589729817j), (0.09300674564986883+0.07496042040189016j), (0.36107600242252297+0.009445513256547716j), (-0.16635592517886008+0.14232585847497323j), (-0.1619167103970876-0.008649945547440944j), (0.12345674100468125-0.0623402797838662j), (0.03442675337889793+0.10635035359117023j)]), [qreg[3], qreg[2], qreg[1], qreg[0]])
			qc.ccx(2, 1, 0)
		with else_e0fe7d: 
			qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[0], qreg[1], qreg[2], qreg[3]])
			qc.z(1)
			qc.t(3)
			qc.crx(1.5707963267948966, 1, 3)
			qc.rx(0.39269908169872414, 1)
		qc.reset(qr_e0fe7d)
		
	with case(case.DEFAULT): 
		
		qr_568b6c = QuantumRegister(2)
		cr_568b6c = ClassicalRegister(2)
		qc.add_register(qr_568b6c)
		qc.add_register(cr_568b6c)
		qc.x(qr_568b6c[0])
		qc.x(qr_568b6c[1])
		qc.measure(qr_568b6c[0], cr_568b6c[0]) 
		qc.measure(qr_568b6c[1], cr_568b6c[1]) 
		with qc.if_test((cr_568b6c, 0b11)) as else_568b6c: 
			pass
		with else_568b6c: 
			qc.cp(0.7853981633974483, 2, 0)
			qc.ccz(3, 2, 1)
			qc.iswap(3, 2)
			qc.append(U3Gate(5.901, 2.656, 5.51), [qreg[2]])
			def fun_df20d3(): 
				qc =  QuantumCircuit(3) 
				qc.rz(1.5707963267948966, 0)
				qc.crx(0.7853981633974483, 0, 2)
				qc.z(2)
				return qc.to_gate() 
			g_a77115 = fun_df20d3().control(1) 
			qc.append(g_a77115, [1,3,0,2]) 
		qc.reset(qr_568b6c)
		
qc.reset(qr_568b6c)
qc.append(Permutation(2, pattern=[0, 1]), [qreg[0], qreg[2]])
qc.append(CUGate(2.237, 3.514, 0.868, 0.447), [qreg[1], qreg[3]])
qc.append(NLocal(4, reps=1, parameter_prefix='theta_446ebc'), [qreg[2], qreg[3], qreg[1], qreg[0]])
def fun_edb8b5(): 
	qc =  QuantumCircuit(3) 
	qc.tdg(0)
	qc.ch(2, 1)
	qc.ccz(2, 1, 0)
	return qc.to_gate() 
g_e3a7cc = fun_edb8b5().control(1) 
qc.append(g_e3a7cc, [2,3,0,1]) 
qc.t(2)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveResetInZeroState(),Optimize1qGates(),HoareOptimizer()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
