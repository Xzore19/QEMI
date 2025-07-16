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

qreg = QuantumRegister(6) 
creg = ClassicalRegister(6) 
qc = QuantumCircuit(qreg, creg) 

qc.x(4)
def fun_f332e9(): 
	qc =  QuantumCircuit(3) 
	qc.crz(0.39269908169872414, 0, 1)
	qc.rx(1.5707963267948966, 2)
	qc.ry(0.7853981633974483, 1)
	return qc.to_gate() 
g_b1a7a8 = fun_f332e9().control(1) 
qc.append(g_b1a7a8, [5,2,1,4]) 
qc.cx(2, 0)
qc.y(4)
qc.ry(0.39269908169872414, 2)
qc.iswap(2, 0)
qc.append(CUGate(1.956, 4.426, 2.293, 0.479), [qreg[3], qreg[1]])
qc.rz(1.5707963267948966, 0)
pass
qc.tdg(5)
qc.append(Initialize([(0.16243484948575682+0.7594570719715835j), (-0.4909082274329134+0.3947771368045058j)]), [qreg[0]])
qc.cz(3, 5)
qc.ry(0.39269908169872414, 1)
def fun_f5d39d(): 
	qc =  QuantumCircuit(3) 
	qc.cp(0.7853981633974483, 2, 0)
	qc.p(0.7853981633974483, 2)
	qc.cx(2, 0)
	return qc.to_gate() 
g_a5b2be = fun_f5d39d().control(1) 
qc.append(g_a5b2be, [0,1,5,4]) 
qc.cswap(3, 1, 0)
def fun_b2339b(): 
	qc =  QuantumCircuit(3) 
	qc.h(0)
	qc.cx(2, 0)
	qc.t(2)
	return qc.to_gate() 
g_efc28e = fun_b2339b().control(1) 
qc.append(g_efc28e, [1,5,4,0]) 
qc.ccx(3, 2, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 
qc.measure(qreg[5], creg[5]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([OptimizeSwapBeforeMeasure(),Optimize1qGatesSimpleCommutation(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
