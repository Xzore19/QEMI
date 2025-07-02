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

qc.append(StatePreparation([(-0.16177168189949537+0.030136089990827543j), (-0.17302434493609875+0.10981628131519731j), (-0.04339854618397232+0.045932421835163606j), (-0.04933236574055423+0.07437627253859393j), (0.10765552146323035-0.03738198353842716j), (-0.08930465900356242+0.23197231705606686j), (-0.07834408636401619+0.0009219840985914435j), (-0.13379272907043127-0.06296109887658576j), (0.09810666687651373+0.08133833928393092j), (0.1039536493823929+0.026781029509915465j), (0.06558227110211157+0.0053371029678262035j), (-0.005449597598125129-0.12718476691743144j), (0.12133748505911075+0.21671255820601482j), (0.0585144920839176-0.16031459840993728j), (0.18644426724915086+0.1911549992875039j), (0.08216761077653627+0.0606650461540468j), (-0.0945356989926482+0.15979661417359406j), (0.05655322897392653+0.032551714435830346j), (0.022119150041273204+0.1529875230360515j), (0.058578244310265204+0.008601673141675896j), (-0.10993079992492687-0.13319106859669982j), (0.02374519877435154-0.040852645901866706j), (0.04705137393360725-0.14378210720885662j), (-0.09026613999037103-0.3671130565240054j), (-0.2380680440205311-0.06726081846497123j), (0.06426383132751078-0.03291105019299087j), (-0.08079811534158701-0.07602523664841845j), (-0.01962365676490516-0.009424056133290518j), (-0.010554419193121962-0.08043592323297843j), (-0.2054779717775736+0.10039571012214966j), (0.1936334220964839+0.31221632866931043j), (0.07054010951917027-0.23091966424079072j)]), [qreg[3], qreg[4], qreg[2], qreg[0], qreg[1]])
qc.append(CRXGate(4.488), [qreg[3], qreg[1]])
qc.append(CXGate(), [qreg[0], qreg[3]])
qc.append(RealAmplitudes(2, reps=1, parameter_prefix='theta_e46504'), [qreg[1], qreg[4]])
qc.append(SwapGate(), [qreg[2], qreg[1]])

qr_a63310 = QuantumRegister(2)
cr_a63310 = ClassicalRegister(2)
qc.add_register(qr_a63310)
qc.add_register(cr_a63310)
qc.x(qr_a63310[0])
qc.x(qr_a63310[1])
qc.measure(qr_a63310[0], cr_a63310[0]) 
qc.measure(qr_a63310[1], cr_a63310[1]) 
with qc.while_loop((cr_a63310, 0b11)): 
	qc.measure(qr_a63310[0], cr_a63310[0]) 
	qc.measure(qr_a63310[1], cr_a63310[1]) 
	
	qr_9289c4 = QuantumRegister(2)
	cr_9289c4 = ClassicalRegister(2)
	qc.add_register(qr_9289c4)
	qc.add_register(cr_9289c4)
	qc.x(qr_9289c4[0])
	qc.x(qr_9289c4[1])
	qc.measure(qr_9289c4[0], cr_9289c4[0]) 
	qc.measure(qr_9289c4[1], cr_9289c4[1]) 
	with qc.if_test((cr_9289c4, 0b11)) as else_1: 
		qc.append(SwapGate(), [qreg[2], qreg[1]])
		qc.append(MCXGate(2), [qreg[0], qreg[2], qreg[3]])
		aux_77c03f = AncillaRegister(5, 'aux_77c03f')
		qc.add_register(aux_77c03f)
		qc.append(DraperQFTAdder(5), [qreg[2], aux_77c03f[0], qreg[3], qreg[4], aux_77c03f[3], aux_77c03f[4], qreg[1], aux_77c03f[1], qreg[0], aux_77c03f[2]])
		qc.append(OR(4), [qreg[0], qreg[3], qreg[2], qreg[1], qreg[4]])
		qc.append(HGate(), [qreg[0]])
	with else_1: 
		qc.crz(1.5707963267948966, 4, 0)
		qc.cp(0.7853981633974483, 2, 4)
		qc.append(HGate(), [qreg[1]])
		qc.append(SwapGate(), [qreg[0], qreg[3]])
		qc.append(CRXGate(1.554), [qreg[4], qreg[1]])
	
	
	qc.break_loop()
qc.append(CXGate(), [qreg[2], qreg[0]])
qc.append(C3XGate(), [qreg[0], qreg[3], qreg[4], qreg[1]])
qc.append(CCXGate(), [qreg[0], qreg[4], qreg[1]])
qc.append(RZGate(3.38), [qreg[4]])
qc.append(RZGate(5.749), [qreg[4]])
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
