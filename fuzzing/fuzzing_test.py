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

qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_604211'), [qreg[3], qreg[2], qreg[0], qreg[4]])
qc.rz(0.39269908169872414, 3)
qc.append(CUGate(0.265, 1.499, 3.264, 2.942), [qreg[2], qreg[1]])
aux_2b7b35 = AncillaRegister(5, 'aux_2b7b35')
qc.add_register(aux_2b7b35)
qc.append(DraperQFTAdder(5), [aux_2b7b35[4], qreg[1], aux_2b7b35[1], aux_2b7b35[2], aux_2b7b35[0], aux_2b7b35[3], qreg[3], qreg[4], qreg[2], qreg[0]])
qc.append(XGate(), [qreg[4]])

qr_f55541 = QuantumRegister(2)
cr_f55541 = ClassicalRegister(2)
qc.add_register(qr_f55541)
qc.add_register(cr_f55541)
qc.h(qr_f55541[0])
qc.cx(qr_f55541[0], qr_f55541[1])         
qc.measure(qr_f55541[0], cr_f55541[0]) 
qc.measure(qr_f55541[1], cr_f55541[1]) 
with qc.switch(cr_f55541) as case: 
	with case(0b00, 0b11): 
		
		qr_3c79ae = QuantumRegister(2)
		cr_3c79ae = ClassicalRegister(2)
		qc.add_register(qr_3c79ae)
		qc.add_register(cr_3c79ae)
		qc.x(qr_3c79ae[0])
		qc.x(qr_3c79ae[1])
		qc.measure(qr_3c79ae[0], cr_3c79ae[0]) 
		qc.measure(qr_3c79ae[1], cr_3c79ae[1]) 
		with qc.if_test((cr_3c79ae, 0b11)) as else_3c79ae: 
			qc.tdg(1)
			qc.append(C3XGate(), [qreg[4], qreg[1], qreg[0], qreg[3]])
			qc.ccz(3, 2, 1)
			qc.append(SwapGate(), [qreg[0], qreg[2]])
			qc.append(C3XGate(), [qreg[4], qreg[3], qreg[2], qreg[1]])
		with else_3c79ae: 
			qc.swap(3, 2)
			qc.append(CRXGate(0.217), [qreg[4], qreg[0]])
			qc.cp(1.5707963267948966, 2, 0)
			qc.crx(0.39269908169872414, 1, 0)
			qc.append(NLocal(4, reps=1, parameter_prefix='theta_4a2a3d'), [qreg[4], qreg[2], qreg[0], qreg[1]])
		qc.reset(qr_3c79ae)
		
	with case(case.DEFAULT): 
		with qc.for_loop(range(3)) as i_f55541:
			aux_a6e591 = AncillaRegister(3, 'aux_a6e591')
			qc.add_register(aux_a6e591)
			qc.append(DraperQFTAdder(4), [aux_a6e591[1], qreg[4], qreg[0], qreg[2], qreg[1], qreg[3], aux_a6e591[0], aux_a6e591[2]])
			qc.ry(0.7853981633974483, 1)
			qc.append(Permutation(3, pattern=[0, 2, 1]), [qreg[4], qreg[3], qreg[2]])
			qc.append(CRXGate(4.793), [qreg[1], qreg[2]])
			qc.iswap(2, 0)
			qc.break_loop()
			qc.cry(0.39269908169872414, 4, 3)
			qc.append(RZGate(4.594), [qreg[2]])
			qc.append(RZGate(3.121), [qreg[0]])
			qc.append(MCXGate(2), [qreg[4], qreg[0], qreg[3]])
			qc.append(StatePreparation([(0.09656440447325984+0.03320920153092239j), (0.12694696480252873+0.053467409691387115j), (0.24263228387293803+0.08402842373379796j), (0.21591266652244698-0.05653439098578289j), (-0.27526169785804705-0.03885254310249063j), (-0.15624398531584047-0.1312547946447513j), (-0.0726522977494069+0.1168174508082596j), (-0.1979655031827051-0.19092731693766188j), (0.05280109323783226+0.07559899282823568j), (-0.1525182559512559-0.014431582789529666j), (-0.24975491488260976+0.13702817604021583j), (0.04203657378196372-0.05337784694319354j), (-0.009419326989220806-0.010980750129091383j), (0.05021167105401718+0.04897547202480532j), (0.15663958343090262-0.1672092022801005j), (0.01860075501947932+0.04790596748766369j), (0.02504561205517005-0.08432908423978032j), (-0.0932115323051455+0.11743639062047836j), (0.041734937277038066-0.20447760263016382j), (-0.15673889124864251+0.14264101358102427j), (-0.06451215618114613+0.15265778672573366j), (-0.009975937402810315-0.2087888497742197j), (-0.24483342530547897+0.10792976394279272j), (-0.10742805952970574+0.04387948397514065j), (-0.10150517179830401+0.25059115947639765j), (-0.06741387857760305-0.023604309853083802j), (0.06867651903429565-0.1397320106289373j), (0.07566478522944088+0.09137075582753362j), (0.012306803206452065-0.12703202483562817j), (0.19406824347919926-0.01263573622726564j), (0.12018153577677525-0.014029451229768012j), (-0.04862697937355754+0.02869226135741275j)]), [qreg[0], qreg[4], qreg[2], qreg[3], qreg[1]])
		
qc.reset(qr_f55541)
qc.append(SwapGate(), [qreg[2], qreg[4]])
qc.cz(2, 4)
qc.append(RXGate(5.268), [qreg[0]])
qc.cx(2, 0)
qc.append(U3Gate(4.605, 0.437, 0.991), [qreg[4]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGates()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
