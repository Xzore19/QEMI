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

aux_0ccea9 = AncillaRegister(5, 'aux_0ccea9')
qc.add_register(aux_0ccea9)
qc.append(DraperQFTAdder(5), [aux_0ccea9[1], aux_0ccea9[2], aux_0ccea9[4], qreg[3], qreg[1], qreg[0], aux_0ccea9[3], qreg[2], aux_0ccea9[0], qreg[4]])
qc.append(SwapGate(), [qreg[2], qreg[3]])
qc.append(RXGate(5.949), [qreg[2]])
aux_84fdbf = AncillaRegister(1, 'aux_84fdbf')
qc.add_register(aux_84fdbf)
qc.append(DraperQFTAdder(3), [qreg[3], aux_84fdbf[0], qreg[0], qreg[4], qreg[1], qreg[2]])
qc.y(1)

qr_9b6561 = QuantumRegister(2)
cr_9b6561 = ClassicalRegister(2)
qc.add_register(qr_9b6561)
qc.add_register(cr_9b6561)
qc.x(qr_9b6561[0])
qc.x(qr_9b6561[1])
qc.measure(qr_9b6561[0], cr_9b6561[0]) 
qc.measure(qr_9b6561[1], cr_9b6561[1]) 
with qc.while_loop((cr_9b6561, 0b11)): 
	qc.measure(qr_9b6561[0], cr_9b6561[0]) 
	qc.measure(qr_9b6561[1], cr_9b6561[1]) 
	with qc.for_loop(range(3)) as i:
		qc.append(AND(1), [qreg[2], qreg[1]])
		qc.cz(2, 3)
		qc.append(XGate(), [qreg[2]])
		qc.iswap(2, 0)
		qc.append(C3XGate(), [qreg[0], qreg[4], qreg[3], qreg[2]])
		qc.continue_loop()
		qc.append(RZGate(4.416), [qreg[3]])
		qc.append(RZGate(0.533), [qreg[4]])
		qc.append(CUGate(0.141, 6.058, 5.567, 1.746), [qreg[4], qreg[2]])
		qc.append(OR(3), [qreg[3], qreg[1], qreg[2], qreg[4]])
		qc.append(CXGate(), [qreg[0], qreg[1]])
	
	qc.break_loop()
aux_1cc5de = AncillaRegister(5, 'aux_1cc5de')
qc.add_register(aux_1cc5de)
qc.append(DraperQFTAdder(5), [qreg[2], qreg[1], qreg[4], qreg[3], aux_1cc5de[0], aux_1cc5de[2], qreg[0], aux_1cc5de[4], aux_1cc5de[3], aux_1cc5de[1]])
qc.append(CCXGate(), [qreg[3], qreg[2], qreg[1]])
qc.append(MCXGate(3), [qreg[1], qreg[4], qreg[3], qreg[2]])
qc.append(CRXGate(0.714), [qreg[2], qreg[0]])
qc.append(QFT(3), [qreg[0], qreg[4], qreg[1]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(OptimizeAnnotated()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
