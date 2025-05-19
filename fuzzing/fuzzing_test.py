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
	a = 0
	with qc.for_loop(range(a)) as i:
		qc.append(SwapGate(), [qreg[2], qreg[1]])
		qc.append(RZGate(5.924), [qreg[0]])
		qc.cswap(4, 3, 0)
		qc.append(Initialize([(0.2717504282255087+0.061939730280402616j), (-0.01973262009859736-0.0038770985232936153j), (-0.525111441083776+0.04173185471802687j), (0.3687196890857993-0.2085790564347137j), (-0.18095860737474215-0.008540362385234916j), (-0.13421706391552526-0.231162664998503j), (-0.22684858704849659+0.14346183570440088j), (0.06472698899802937-0.022079704950594036j), (-0.016783660039896422+0.04409740676592343j), (-0.05319643505736345+0.03461271027821566j), (0.20610446350030587+0.12855433704500707j), (-0.29823701083224885-0.22956371987421875j), (0.08146056117239447-0.21270518370672356j), (-0.0596011127757036-0.042308675815073j), (0.12029696489749131-0.06687806508309854j), (0.028573553124887872-0.00966214270453119j)]), [qreg[3], qreg[1], qreg[4], qreg[0]])
		qc.append(Diagonal(np.array([np.complex128(-0.86838353208779+0.4958931751887037j), np.complex128(-0.9752877367164957-0.22093852224185676j), np.complex128(0.8703470396049683-0.49243885980989327j), np.complex128(0.961671283766884-0.274204926976437j)])), [qreg[4], qreg[0]])
	
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
