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
pass
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
