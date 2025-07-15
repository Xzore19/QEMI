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

qc.rz(1.5707963267948966, 3)
qc.append(XGate(), [qreg[2]])
qc.crz(0.7853981633974483, 4, 2)
qc.append(C3XGate(), [qreg[4], qreg[2], qreg[0], qreg[1]])
qc.swap(4, 3)

qr_25eec7 = QuantumRegister(2)
cr_25eec7 = ClassicalRegister(2)
qc.add_register(qr_25eec7)
qc.add_register(cr_25eec7)
qc.x(qr_25eec7[0])
qc.x(qr_25eec7[1])
qc.measure(qr_25eec7[0], cr_25eec7[0]) 
qc.measure(qr_25eec7[1], cr_25eec7[1]) 
with qc.while_loop((cr_25eec7, 0b11)): 
	qc.measure(qr_25eec7[0], cr_25eec7[0]) 
	qc.measure(qr_25eec7[1], cr_25eec7[1]) 
	
	qr_8017ba = QuantumRegister(2)
	cr_8017ba = ClassicalRegister(2)
	qc.add_register(qr_8017ba)
	qc.add_register(cr_8017ba)
	qc.x(qr_8017ba[0])
	qc.x(qr_8017ba[1])
	qc.measure(qr_8017ba[0], cr_8017ba[0]) 
	qc.measure(qr_8017ba[1], cr_8017ba[1]) 
	with qc.while_loop((cr_8017ba, 0b11)): 
		qc.measure(qr_8017ba[0], cr_8017ba[0]) 
		qc.measure(qr_8017ba[1], cr_8017ba[1]) 
		qc.append(HGate(), [qreg[0]])
		qc.cx(4, 2)
		qc.append(HGate(), [qreg[1]])
		qc.cz(0, 4)
		qc.append(C3XGate(), [qreg[0], qreg[2], qreg[1], qreg[4]])
		qc.break_loop()
		aux_758eaa = AncillaRegister(5, 'aux_758eaa')
		qc.add_register(aux_758eaa)
		qc.append(DraperQFTAdder(5), [aux_758eaa[1], qreg[3], aux_758eaa[4], qreg[0], aux_758eaa[0], qreg[2], aux_758eaa[3], qreg[4], aux_758eaa[2], qreg[1]])
		qc.append(CCXGate(), [qreg[1], qreg[2], qreg[3]])
		qc.append(HGate(), [qreg[4]])
		qc.append(Permutation(5, pattern=[1, 0, 3, 4, 2]), [qreg[2], qreg[4], qreg[0], qreg[3], qreg[1]])
		qc.append(XOR(2, seed=42), [qreg[0], qreg[3]])
	
	qc.break_loop()
qc.cx(3, 0)
qc.append(U3Gate(6.183, 1.33, 5.409), [qreg[1]])
qc.append(SwapGate(), [qreg[0], qreg[3]])
qc.append(CUGate(1.097, 2.324, 3.815, 5.52), [qreg[0], qreg[1]])
aux_d00747 = AncillaRegister(5, 'aux_d00747')
qc.add_register(aux_d00747)
qc.append(DraperQFTAdder(5), [qreg[2], qreg[4], aux_d00747[4], qreg[0], aux_d00747[3], aux_d00747[1], aux_d00747[0], qreg[3], qreg[1], aux_d00747[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(RemoveIdentityEquivalent()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
