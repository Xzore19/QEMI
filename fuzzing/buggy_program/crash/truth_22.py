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

qc.x(3)
qc.append(NLocal(4, reps=1, parameter_prefix='theta_77340d'), [qreg[0], qreg[2], qreg[1], qreg[3]])
qc.ry(1.5707963267948966, 2)
qc.ry(0.39269908169872414, 1)
def fun_d590ed(): 
	qc =  QuantumCircuit(3) 
	qc.t(2)
	qc.cswap(2, 1, 0)
	qc.x(1)
	return qc.to_gate() 
g_abd66f = fun_d590ed().control(1) 
qc.append(g_abd66f, [3,1,0,2]) 
with qc.for_loop(range(3)) as i_305094:
	with qc.for_loop(range(3)) as i_df9fc4:
		qc.ccz(3, 1, 0)
		def fun_a81473(): 
			qc =  QuantumCircuit(3) 
			qc.z(1)
			qc.y(0)
			qc.y(0)
			return qc.to_gate() 
		g_0b84f1 = fun_a81473().control(1) 
		qc.append(g_0b84f1, [1,2,3,0]) 
		qc.cry(0.39269908169872414, 1, 0)
		qc.append(SwapGate(), [qreg[3], qreg[2]])
		qc.append(XGate(), [qreg[1]])
		qc.continue_loop()
		qc.h(1)
		qc.cry(0.39269908169872414, 2, 0)
		qc.z(3)
		qc.y(0)
		qc.append(ZZFeatureMap(2, reps=1, parameter_prefix='x_6a0664'), [qreg[3], qreg[0]])
	
	qc.continue_loop()
qc.append(XGate(), [qreg[3]])
qc.iswap(2, 1)
qc.cz(1, 3)
qc.cz(0, 3)
qc.ccx(3, 2, 1)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([CommutativeInverseCancellation(),RemoveDiagonalGatesBeforeMeasure(),ElidePermutations()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
