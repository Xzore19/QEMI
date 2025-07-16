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

qc.tdg(0)
qc.cswap(2, 1, 0)
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[2], qreg[0]])
qc.append(SwapGate(), [qreg[2], qreg[0]])
def fun_d22dd8(): 
	qc =  QuantumCircuit(3) 
	qc.tdg(0)
	qc.p(1.5707963267948966, 0)
	qc.swap(2, 1)
	return qc.to_gate() 
g_be365f = fun_d22dd8().control(1) 
qc.append(g_be365f, [1,2,0,3]) 
pass
qc.append(ZFeatureMap(2, reps=1, parameter_prefix='x_9519e2'), [qreg[2], qreg[3]])
qc.cswap(3, 2, 0)
qc.swap(3, 1)
qc.append(CUGate(2.962, 5.556, 1.287, 3.445), [qreg[2], qreg[1]])
qc.append(RXGate(5.037), [qreg[3]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([Collect1qRuns(),OptimizeAnnotated(),CommutativeInverseCancellation()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
result = job.result().get_counts() 
print(result)
