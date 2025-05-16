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

qreg = QuantumRegister(7) 
creg = ClassicalRegister(5) 
cond_creg = ClassicalRegister(2) 
qc = QuantumCircuit(qreg, creg, cond_creg) 

qc.crx(0.7853981633974483, 1, 4)
qc.append(AND(1), [qreg[3], qreg[4]])
qc.ccx(4, 2, 0)
qc.append(CXGate(), [qreg[1], qreg[2]])
qc.append(HGate(), [qreg[4]])
qc.append(MCXGate(4), [qreg[2], qreg[3], qreg[4], qreg[0], qreg[1]])
qc.append(PauliFeatureMap(5, reps=1, parameter_prefix='x_370c56'), [qreg[1], qreg[3], qreg[4], qreg[2], qreg[0]])
qc.ccx(4, 3, 1)
qc.cp(1.5707963267948966, 0, 3)
qc.cswap(3, 1, 0)
with qc.for_loop(range(5)) as i:
	qc.append(CRXGate(4.119), [qreg[1], qreg[3]])
	qc.append(CUGate(2.612, 0.097, 0.995, 4.183), [qreg[2], qreg[0]])
	qc.t(0)
	qc.append(NLocal(5, reps=1, parameter_prefix='theta_8f937d'), [qreg[1], qreg[4], qreg[3], qreg[2], qreg[0]])
	qc.append(CRXGate(0.786), [qreg[3], qreg[1]])
	qc.append(ZFeatureMap(2, reps=1, parameter_prefix='x_ea808f'), [qreg[0], qreg[1]])
	qc.p(1.5707963267948966, 0)
	qc.append(RXGate(4.872), [qreg[1]])
	qc.cz(2, 4)
	qc.x(4)
	qc.break_loop()
	qc.tdg(0)
	qc.append(OR(1), [qreg[4], qreg[2]])
	qc.append(HGate(), [qreg[4]])
	qc.ccx(4, 1, 0)
	qc.append(CXGate(), [qreg[1], qreg[2]])
	qc.append(NLocal(5, reps=1, parameter_prefix='theta_f13468'), [qreg[2], qreg[0], qreg[4], qreg[3], qreg[1]])
	qc.append(CUGate(5.418, 5.163, 0.675, 5.541), [qreg[3], qreg[1]])
	qc.append(U3Gate(4.335, 4.438, 3.223), [qreg[2]])
	qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[3], qreg[1]])
	qc.h(1)
qc.append(C3XGate(), [qreg[3], qreg[4], qreg[2], qreg[1]])
qc.append(C3XGate(), [qreg[4], qreg[2], qreg[3], qreg[1]])
qc.append(TwoLocal(2, reps=1, parameter_prefix='theta_23fab5'), [qreg[3], qreg[1]])
qc.z(0)
qc.append(XGate(), [qreg[0]])
aux_4e868e = AncillaRegister(5, 'aux_4e868e')
qc.add_register(aux_4e868e)
qc.append(DraperQFTAdder(5), [aux_4e868e[4], aux_4e868e[1], qreg[0], aux_4e868e[3], aux_4e868e[2], aux_4e868e[0], qreg[3], qreg[1], qreg[2], qreg[4]])
qc.ccz(3, 1, 0)
aux_4f88d8 = AncillaRegister(8, 'aux_4f88d8')
qc.add_register(aux_4f88d8)
qc.append(WeightedAdder(5, weights=[np.int64(1), np.int64(1), np.int64(3), np.int64(2), np.int64(3)]), [qreg[3], aux_4f88d8[5], qreg[2], aux_4f88d8[0], qreg[1], aux_4f88d8[6], aux_4f88d8[4], aux_4f88d8[7], aux_4f88d8[3], qreg[0], aux_4f88d8[2], aux_4f88d8[1], qreg[4]])
qc.append(StatePreparation([(-0.230134753605035+0.002538793267130787j), (-0.049887873691098136+0.035107873983589354j), (-0.19984944124546386+0.191266743627692j), (-0.1255794351566432-0.07653563927028073j), (-0.025415976993650197-0.13744476976991088j), (0.19068106693180295-0.07316584575890855j), (-0.16762863480559784+0.03386662349951625j), (0.16173338613255056+0.20384088022311606j), (-0.015474890345185677+0.009372606947051733j), (0.07087172796788606-0.10210395120497644j), (0.04646025262980881+0.007267962852995362j), (0.01438271264693858-0.1423555648820935j), (-0.3068437098324478-0.045318153315099405j), (0.013462652663691581+0.06069325869200436j), (0.08043644407354876+0.19570379236204077j), (0.16021788334356915+0.04895444916949576j), (0.0478997033925427-0.13237129657391802j), (0.02817137189772855+0.08846479506085307j), (-0.19153098788241826+0.035144031665293014j), (-0.05892541577334022+0.10752833227221875j), (0.11257274858627592+0.08941640525632216j), (-0.12441278739381978-0.10667508798284624j), (0.03298685091348546-0.15403114731325773j), (-0.11335993270386822+0.08469174379453609j), (0.12952697494417667+0.10699559650246519j), (-0.001548884935507122+0.02373430588541109j), (0.13398416220941334+0.0887969358534191j), (-0.24392254183079476-0.26292656937630765j), (-0.23012998396122933+0.016566979838801243j), (-0.061108524535441626-0.10159812986406198j), (0.13463110254523558-0.05574798126809526j), (-0.07904171084032602+0.1542963784367604j)]), [qreg[0], qreg[4], qreg[2], qreg[1], qreg[3]])
qc.ccx(4, 3, 0)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
