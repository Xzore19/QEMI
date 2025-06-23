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

qc.t(1)
qc.y(2)
qc.rx(0.39269908169872414, 1)
qc.cz(0, 3)
qc.cry(0.39269908169872414, 2, 1)
pass
qc.rx(0.7853981633974483, 3)
qc.x(0)
qc.p(0.39269908169872414, 1)
qc.ccx(3, 2, 0)
qc.ccz(3, 1, 0)
=======
qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.cswap(4, 3, 2)
qc.append(CRXGate(4.905), [qreg[1], qreg[2]])
qc.append(MCXGate(4), [qreg[0], qreg[1], qreg[2], qreg[4], qreg[3]])
qc.append(RZGate(2.077), [qreg[2]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[3], qreg[2], qreg[0], qreg[1], qreg[4]])
with qc.for_loop(range(3)) as i:
	with qc.for_loop(range(3)) as i:
		qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_2d238d'), [qreg[3], qreg[2], qreg[0], qreg[1]])
		qc.append(HGate(), [qreg[1]])
		qc.z(2)
		qc.append(CCXGate(), [qreg[4], qreg[3], qreg[2]])
		qc.append(CRXGate(4.995), [qreg[2], qreg[3]])
		qc.continue_loop()
		qc.append(HGate(), [qreg[3]])
		qc.append(U3Gate(5.216, 4.103, 3.021), [qreg[1]])
		qc.append(RZGate(3.974), [qreg[1]])
		qc.append(XGate(), [qreg[1]])
		qc.cry(0.7853981633974483, 3, 0)
	
	qc.continue_loop()
qc.iswap(4, 0)
qc.append(RealAmplitudes(5, reps=1, parameter_prefix='theta_eb1124'), [qreg[3], qreg[2], qreg[4], qreg[1], qreg[0]])
qc.p(0.39269908169872414, 0)
qc.append(RZGate(4.637), [qreg[4]])
aux_aa7a3b = AncillaRegister(3, 'aux_aa7a3b')
qc.add_register(aux_aa7a3b)
qc.append(DraperQFTAdder(4), [qreg[1], aux_aa7a3b[2], qreg[3], aux_aa7a3b[0], qreg[0], qreg[2], qreg[4], aux_aa7a3b[1]])
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

<<<<<<< HEAD
p = PassManager([CollectCliffords(),TemplateOptimization(),OptimizeSwapBeforeMeasure()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500) 
=======
p = PassManager(CommutativeInverseCancellation()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
>>>>>>> I forget what I had modified
result = job.result().get_counts() 
print(result)
