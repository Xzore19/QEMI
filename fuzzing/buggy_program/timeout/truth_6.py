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

qc.z(1)
qc.cz(1, 2)
aux_b5f9ad = AncillaRegister(3, 'aux_b5f9ad')
qc.add_register(aux_b5f9ad)
qc.append(DraperQFTAdder(4), [qreg[4], qreg[1], aux_b5f9ad[1], aux_b5f9ad[0], aux_b5f9ad[2], qreg[3], qreg[0], qreg[2]])
qc.append(SwapGate(), [qreg[2], qreg[0]])
qc.append(RealAmplitudes(3, reps=1, parameter_prefix='theta_45d513'), [qreg[0], qreg[4], qreg[1]])

qr_e335c0 = QuantumRegister(2)
cr_e335c0 = ClassicalRegister(2)
qc.add_register(qr_e335c0)
qc.add_register(cr_e335c0)
qc.x(qr_e335c0[0])
qc.x(qr_e335c0[1])
qc.measure(qr_e335c0[0], cr_e335c0[0]) 
qc.measure(qr_e335c0[1], cr_e335c0[1]) 
with qc.while_loop((cr_e335c0, 0b11)): 
	qc.measure(qr_e335c0[0], cr_e335c0[0]) 
	qc.measure(qr_e335c0[1], cr_e335c0[1]) 
	
	qr_3ba987 = QuantumRegister(2)
	cr_3ba987 = ClassicalRegister(2)
	qc.add_register(qr_3ba987)
	qc.add_register(cr_3ba987)
	qc.x(qr_3ba987[0])
	qc.x(qr_3ba987[1])
	qc.measure(qr_3ba987[0], cr_3ba987[0]) 
	qc.measure(qr_3ba987[1], cr_3ba987[1]) 
	with qc.while_loop((cr_3ba987, 0b11)): 
		qc.measure(qr_3ba987[0], cr_3ba987[0]) 
		qc.measure(qr_3ba987[1], cr_3ba987[1]) 
		qc.append(CUGate(3.564, 4.646, 4.434, 4.618), [qreg[2], qreg[4]])
		qc.cz(2, 4)
		qc.tdg(1)
		qc.append(XGate(), [qreg[0]])
		qc.append(RZGate(5.785), [qreg[4]])
		qc.break_loop()
		aux_655c66 = AncillaRegister(3, 'aux_655c66')
		qc.add_register(aux_655c66)
		qc.append(DraperQFTAdder(4), [qreg[4], qreg[0], aux_655c66[2], qreg[3], aux_655c66[0], qreg[1], qreg[2], aux_655c66[1]])
		qc.swap(1, 0)
		qc.append(CXGate(), [qreg[0], qreg[3]])
		qc.cp(0.39269908169872414, 1, 0)
		qc.append(C3XGate(), [qreg[2], qreg[4], qreg[0], qreg[1]])
	
	qc.break_loop()
qc.append(RZGate(3.783), [qreg[1]])
qc.append(StatePreparation([(-0.2056771808916171+0.14981231558213803j), (-0.13074736983889315+0.14944929817190475j), (-0.08499202214393878-0.1662000391354798j), (-0.04423955952715373-0.06470908416992689j), (-0.1942554091255108-0.4339919648679424j), (0.14420677796986275-0.16453090541937118j), (0.10705400290131281-0.2433401257855178j), (0.11149714659299101+0.30399468007363556j), (-0.045562120971324206+0.1429676920291779j), (0.0418340797855927+0.04935617605922321j), (0.05862745671297311+0.15066129281101137j), (0.18612431468779425+0.26134847154942115j), (-0.009361742038327348+0.1896503297827783j), (-0.21427509729708372+0.3191517115278015j), (-0.17576024670640142+0.15903570137601233j), (-0.09633681652778442-0.016992323598399j)]), [qreg[0], qreg[3], qreg[2], qreg[1]])
qc.append(CXGate(), [qreg[1], qreg[3]])
qc.append(CXGate(), [qreg[3], qreg[1]])
qc.t(0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(CollectCliffords()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
