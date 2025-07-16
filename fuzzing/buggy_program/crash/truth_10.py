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

qc.append(CXGate(), [qreg[3], qreg[1]])
qc.t(3)
qc.append(XOR(1, seed=42), [qreg[1]])
qc.t(2)
qc.swap(2, 0)
pass
qc.append(Initialize([(0.403137529045925-0.7768001840593867j), (0.19317436260445772+0.4435597731449621j)]), [qreg[3]])
qc.append(U3Gate(6.189, 1.846, 5.534), [qreg[3]])
qc.cp(1.5707963267948966, 1, 0)
def fun_a6cd43(): 
	qc =  QuantumCircuit(3) 
	qc.h(1)
	qc.cswap(2, 1, 0)
	qc.tdg(2)
	return qc.to_gate() 
g_a058c2 = fun_a6cd43().control(1) 
qc.append(g_a058c2, [0,1,2,3]) 
qc.append(RXGate(1.22), [qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([Optimize1qGates(),CommutativeInverseCancellation(),OptimizeCliffords()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
