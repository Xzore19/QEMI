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

qc.append(U3Gate(4.29, 1.58, 3.66), [qreg[0]])
qc.append(CCXGate(), [qreg[3], qreg[1], qreg[4]])
qc.p(1.5707963267948966, 1)
qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_8f4cf8'), [qreg[3], qreg[4], qreg[0], qreg[2]])
qc.cswap(4, 1, 0)
with qc.for_loop(range(3)) as i:
	a = 0
	with qc.for_loop(range(a)) as i:
		qc.append(Permutation(1, pattern=[0]), [qreg[3]])
		qc.append(AND(4), [qreg[4], qreg[3], qreg[1], qreg[0], qreg[2]])
		qc.append(StatePreparation([(0.06988683018377573-0.20503903291093672j), (0.19474621245745333+0.18055373428859645j), (-0.05456002421860923-0.09348074852815012j), (-0.07676935308699719-0.15288629872918508j), (0.019808432780545213-0.1733283803236083j), (0.4035177011740865-0.09379660092498705j), (-0.15080250668929143+0.10372450928364378j), (-0.05073286223700362+0.44767958669831415j), (0.03474972084840947-0.23601094819266896j), (0.037033888776376755+0.13328656537581168j), (-0.2533061939546118-0.04788564401506931j), (-0.1186983759383854-0.040728622322801264j), (-0.14470686848973968+0.07514997309323072j), (0.11515395157068559+0.26369898348915405j), (-0.07217232375224752-0.015226837818358136j), (-0.1135685469553104+0.3421125957748678j)]), [qreg[2], qreg[4], qreg[0], qreg[1]])
		qc.z(2)
		qc.ccx(4, 3, 0)
	
	qc.break_loop()
qc.append(ZFeatureMap(5, reps=1, parameter_prefix='x_47cb2d'), [qreg[4], qreg[3], qreg[2], qreg[1], qreg[0]])
qc.append(U3Gate(6.08, 3.02, 4.297), [qreg[1]])
qc.ry(0.39269908169872414, 3)
aux_725fed = AncillaRegister(3, 'aux_725fed')
qc.add_register(aux_725fed)
qc.append(DraperQFTAdder(4), [aux_725fed[1], aux_725fed[0], qreg[0], qreg[1], aux_725fed[2], qreg[4], qreg[3], qreg[2]])
qc.crx(1.5707963267948966, 2, 1)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
