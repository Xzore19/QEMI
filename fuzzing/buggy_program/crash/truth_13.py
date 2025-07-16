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

def fun_168886(): 
	qc =  QuantumCircuit(3) 
	qc.ccz(2, 1, 0)
	qc.ry(1.5707963267948966, 0)
	qc.cry(0.7853981633974483, 2, 0)
	return qc.to_gate() 
g_0b2121 = fun_168886().control(1) 
qc.append(g_0b2121, [2,0,3,1]) 
qc.crx(0.7853981633974483, 3, 1)
def fun_3bc80b(): 
	qc =  QuantumCircuit(3) 
	qc.rz(0.39269908169872414, 0)
	qc.swap(2, 1)
	qc.z(0)
	return qc.to_gate() 
g_5f1ce9 = fun_3bc80b().control(1) 
qc.append(g_5f1ce9, [0,1,4,2]) 
qc.append(ZFeatureMap(2, reps=1, parameter_prefix='x_efe934'), [qreg[3], qreg[2]])
qc.z(4)
def fun_a857e5(): 
	qc =  QuantumCircuit(3) 
	qc.rz(0.7853981633974483, 1)
	qc.cz(0, 2)
	qc.ry(0.39269908169872414, 2)
	return qc.to_gate() 
g_d8e89f = fun_a857e5().control(1) 
qc.append(g_d8e89f, [1,0,4,2]) 
qc.rx(1.5707963267948966, 4)
qc.swap(4, 1)
qc.ccx(4, 3, 1)
qc.t(2)
qc.ccx(3, 2, 1)
qc.crz(0.39269908169872414, 4, 3)
def fun_65c8b0(): 
	qc =  QuantumCircuit(3) 
	qc.x(1)
	qc.rx(0.7853981633974483, 2)
	qc.ry(1.5707963267948966, 0)
	return qc.to_gate() 
g_da030f = fun_65c8b0().control(1) 
qc.append(g_da030f, [1,4,2,0]) 
qc.cx(3, 2)
qc.x(0)
pass
qc.append(Initialize([(0.13291042658518132+0.11226135582657541j), (-0.5357426508787511-0.1404702675703086j), (0.76817692826332+0.023830158858463745j), (-0.036173757001493036+0.2664730983948776j)]), [qreg[3], qreg[2]])
def fun_8b2b83(): 
	qc =  QuantumCircuit(3) 
	qc.tdg(1)
	qc.z(2)
	qc.ry(1.5707963267948966, 2)
	return qc.to_gate() 
g_4e89d5 = fun_8b2b83().control(1) 
qc.append(g_4e89d5, [2,0,4,3]) 
qc.cx(3, 0)
qc.t(1)
qc.append(HGate(), [qreg[0]])
def fun_c2fa1d(): 
	qc =  QuantumCircuit(3) 
	qc.cx(2, 0)
	qc.y(2)
	qc.cp(0.39269908169872414, 2, 0)
	return qc.to_gate() 
g_0a2b27 = fun_c2fa1d().control(1) 
qc.append(g_0a2b27, [0,4,2,1]) 
def fun_0de787(): 
	qc =  QuantumCircuit(3) 
	qc.t(0)
	qc.y(2)
	qc.cswap(2, 1, 0)
	return qc.to_gate() 
g_6580bf = fun_0de787().control(1) 
qc.append(g_6580bf, [1,3,0,2]) 
qc.append(HGate(), [qreg[4]])
qc.cp(0.39269908169872414, 3, 4)
qc.append(StatePreparation([(-0.06468604903853252-0.3683990139582519j), (0.09287530354066321-0.0541196141930274j), (-0.3558238250803427-0.25206525147589004j), (-0.057200295948752665-0.056188798949270514j), (-0.024786776802973733+0.3272561350543239j), (-0.18809921835784765+0.06635218292721898j), (-0.017726675379574154-0.1463208508640412j), (0.231407641650445-0.09118424859084459j), (-0.024025342295948063-0.10337931233967448j), (0.3119341801959888+0.0971603351409195j), (0.02846073406575822+0.09294279149241962j), (-0.001444013274522232+0.03800433438317762j), (-0.2595352813288268+0.014590478272966795j), (-0.21515527158379313+0.2568766117941886j), (-0.07881457161852341+0.2985492377965682j), (0.12644463696093802+0.028298293196904332j)]), [qreg[4], qreg[2], qreg[0], qreg[3]])
qc.y(0)
qc.cx(2, 0)
def fun_0df4f8(): 
	qc =  QuantumCircuit(3) 
	qc.rx(1.5707963267948966, 0)
	qc.iswap(2, 1)
	qc.cp(1.5707963267948966, 1, 2)
	return qc.to_gate() 
g_e13f63 = fun_0df4f8().control(1) 
qc.append(g_e13f63, [4,3,2,0]) 
qc.ccz(4, 3, 2)
qc.cz(2, 4)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveIdentityEquivalent(),CommutativeInverseCancellation(),Optimize1qGatesSimpleCommutation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
