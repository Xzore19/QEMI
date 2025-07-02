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

<<<<<<< HEAD
qreg = QuantumRegister(4) 
creg = ClassicalRegister(4) 
qc = QuantumCircuit(qreg, creg) 

qc.cz(1, 3)
qc.cz(2, 3)
qc.cry(0.39269908169872414, 1, 0)
qc.crx(0.7853981633974483, 2, 3)
qc.crx(1.5707963267948966, 2, 0)
with qc.for_loop(range(3)) as i_f99d40:
	with qc.for_loop(range(3)) as i_69b38c:
		qc.cx(2, 0)
		qc.t(0)
		qc.tdg(0)
		qc.y(0)
		qc.rx(1.5707963267948966, 2)
		qc.break_loop()
	
	qc.continue_loop()
qc.cx(1, 0)
qc.tdg(3)
qc.cswap(2, 1, 0)
qc.cry(0.7853981633974483, 3, 0)
qc.p(0.39269908169872414, 1)
=======
qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

# qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_74182d'), [qreg[0], qreg[3], qreg[1], qreg[4]])
qc.append(XGate(), [qreg[1]])
# qc.h(2)
# qc.cx(4, 2)
# qc.append(MCPhaseGate(1.0, num_ctrl_qubits=2), [qreg[4], qreg[2], qreg[3]])
qc.append(Initialize([(0.6675295366963846+0.7159907893058729j), (0.024362866765987624-0.20289888612312826j)]), [qreg[1]])
# qc.append(MCXGate(3), [qreg[2], qreg[3], qreg[1], qreg[4]])
# qc.append(XGate(), [qreg[1]])
# qc.z(4)
# qc.append(SwapGate(), [qreg[3], qreg[1]])
>>>>>>> I forget what I had modified
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
<<<<<<< HEAD
=======
qc.measure(qreg[4], creg[4]) 
>>>>>>> I forget what I had modified

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(CommutativeInverseCancellation()) 
qc = p.run(qc) 

<<<<<<< HEAD
compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 
=======
compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 
>>>>>>> I forget what I had modified

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
