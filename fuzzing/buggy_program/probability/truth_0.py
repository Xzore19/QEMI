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

qreg = QuantumRegister(8) 
creg = ClassicalRegister(8) 
qc = QuantumCircuit(qreg, creg) 

qc.ch(2, 0)
qc.append(RXGate(4.549), [qreg[0]])
qc.ry(0.39269908169872414, 3)
def fun_6e0f0f(): 
	qc =  QuantumCircuit(3) 
	qc.ccz(2, 1, 0)
	qc.z(1)
	qc.t(0)
	return qc.to_gate() 
g_0026b5 = fun_6e0f0f().control(1) 
qc.append(g_0026b5, [1,3,4,7]) 
qc.append(CRXGate(3.303), [qreg[1], qreg[6]])
def fun_2760dd(): 
	qc =  QuantumCircuit(3) 
	qc.ch(1, 0)
	qc.cz(1, 2)
	qc.rx(0.39269908169872414, 1)
	return qc.to_gate() 
g_90eb10 = fun_2760dd().control(1) 
qc.append(g_90eb10, [2,6,7,1]) 
qc.ry(0.7853981633974483, 0)

qr_f1d21c = QuantumRegister(2)
cr_f1d21c = ClassicalRegister(2)
qc.add_register(qr_f1d21c)
qc.add_register(cr_f1d21c)
qc.x(qr_f1d21c[0])
qc.x(qr_f1d21c[1])
qc.measure(qr_f1d21c[0], cr_f1d21c[0]) 
qc.measure(qr_f1d21c[1], cr_f1d21c[1]) 
with qc.while_loop((cr_f1d21c, 0b11)): 
	qc.measure(qr_f1d21c[0], cr_f1d21c[0]) 
	qc.measure(qr_f1d21c[1], cr_f1d21c[1]) 
	qc.t(0)
	qc.crx(0.7853981633974483, 6, 0)
	qc.append(Initialize([(0.2605426651219442-0.6856310238772978j), (0.4733396543358393-0.4878290585659602j)]), [qreg[4]])
	qc.append(CCXGate(), [qreg[6], qreg[2], qreg[0]])
	def fun_855845(): 
		qc =  QuantumCircuit(3) 
		qc.z(1)
		qc.cz(0, 2)
		qc.swap(2, 0)
		return qc.to_gate() 
	g_fcf04f = fun_855845().control(1) 
	qc.append(g_fcf04f, [6,2,0,7]) 
	def fun_8bcada(): 
		qc =  QuantumCircuit(3) 
		qc.z(1)
		qc.ch(2, 0)
		qc.crz(0.39269908169872414, 0, 1)
		return qc.to_gate() 
	g_49d70e = fun_8bcada().control(1) 
	qc.append(g_49d70e, [5,6,1,3]) 
	qc.ccx(4, 3, 2)
	qc.break_loop()
qc.reset(qr_f1d21c)
qc.t(7)
def fun_f75e18(): 
	qc =  QuantumCircuit(3) 
	qc.tdg(0)
	qc.ccz(2, 1, 0)
	qc.x(1)
	return qc.to_gate() 
g_e83df8 = fun_f75e18().control(1) 
qc.append(g_e83df8, [4,5,0,3]) 
def fun_de81a4(): 
	qc =  QuantumCircuit(3) 
	qc.crz(1.5707963267948966, 0, 2)
	qc.rz(0.39269908169872414, 0)
	qc.rx(1.5707963267948966, 2)
	return qc.to_gate() 
g_8f7793 = fun_de81a4().control(1) 
qc.append(g_8f7793, [5,7,2,1]) 
qc.crz(0.7853981633974483, 0, 4)
def fun_d2bab6(): 
	qc =  QuantumCircuit(3) 
	qc.iswap(2, 1)
	qc.ccx(2, 1, 0)
	qc.crz(1.5707963267948966, 1, 0)
	return qc.to_gate() 
g_838c48 = fun_d2bab6().control(1) 
qc.append(g_838c48, [0,1,6,5]) 
qc.append(RZGate(3.149), [qreg[6]])
qc.append(Initialize([(-0.06447154741786743+0.4269647912624222j), (0.23340374562632413-0.017186939202036948j), (-0.22725871425701022+0.1768719433028057j), (0.24059568473961934-0.09279042939093424j), (0.018370642826957863-0.1929033518937111j), (0.10860004925214772+0.4242685119334963j), (0.47867702726731437-0.1111992935153398j), (-0.24849365815426105+0.2770419288640283j)]), [qreg[6], qreg[7], qreg[5]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 
qc.measure(qreg[5], creg[5]) 
qc.measure(qreg[6], creg[6]) 
qc.measure(qreg[7], creg[7]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([ResetAfterMeasureSimplification(),CommutativeCancellation(),RemoveDiagonalGatesBeforeMeasure()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=800) 
result = job.result().get_counts() 
print(result)
