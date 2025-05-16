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

qc.append(NLocal(4, reps=1, parameter_prefix='theta_46ca3a'), [qreg[3], qreg[0], qreg[4], qreg[1]])
qc.append(SwapGate(), [qreg[1], qreg[4]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=3), [qreg[4], qreg[1], qreg[2], qreg[0]])
qc.append(Initialize([(-0.022818241789192385-0.017627949778080645j), (0.03543908832829437+0.0003647356800496602j), (0.005748683068965417-0.11558350539544832j), (-0.2550851912285812-0.13296013581888835j), (0.004860646016645763-0.10371380274090523j), (0.002233105008671352-0.15224280859412326j), (0.029884356497051765-0.054560072838964455j), (-0.23696728623554272+0.2829705952504447j), (0.0392399441402888-0.009677701346870645j), (0.07719035827925284-0.11998163462255049j), (0.1415602477110923-0.04662585225914955j), (-0.11353048464782309+0.021376695743698274j), (-0.13785297924538478-0.01021226587083271j), (-0.26851296699569194-0.14224423319873872j), (-0.12281536242236522-0.010368426061162894j), (0.026136768632806562-0.05536356247672421j), (-0.14031464862309342+0.15547289626117355j), (0.09093082335898542-0.21207908113723956j), (-0.008770396796186927-0.031161333261418404j), (-0.15555459204923605+0.16808078767081447j), (0.247939966320635+0.1426475674925254j), (-0.12576066263753513+0.12632730163352487j), (0.04122088179083724+0.008326603741984965j), (0.021100128946557703+0.20408820571652436j), (-0.12609989239074718+0.030253953984268417j), (-0.1669339694845874+0.06616056339545315j), (0.0326840606082218-0.12477172041943467j), (0.02508229256834729+0.12671425774499623j), (-0.1771492202819308-0.043763269105752296j), (0.17593741745612004-0.16942389986036954j), (-0.1300488818089005+0.10843026004993818j), (-0.16436905796323767-0.026416939735469627j)]), [qreg[3], qreg[2], qreg[1], qreg[0], qreg[4]])
qc.append(CRXGate(6.002), [qreg[1], qreg[3]])
qc.append(CUGate(4.454, 2.908, 1.408, 4.331), [qreg[2], qreg[0]])
qc.append(HGate(), [qreg[4]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[4], qreg[1], qreg[3]])
qc.append(StatePreparation([(0.027467693223088056-0.06723483278852185j), (0.14167956940598397+0.08198252053344673j), (-0.4208826162097185+0.14722725746201085j), (0.10360314148367424-0.08643672308645325j), (0.10198025758139954+0.1148895591294259j), (0.16868034863521783+0.2588983975542402j), (-0.14077185281469995-0.04200866679175034j), (0.11737375053604833+0.10036745519364716j), (-0.16017820789261977+0.1334535290448588j), (0.18185888441365716+0.19260869152604296j), (0.3152043855802326-0.015663624102159043j), (-0.14729264511242657+0.177135264419932j), (-0.03775713887772779-0.2770651198803155j), (-0.0913223395617666-0.01599806071413092j), (0.33517992303128513+0.013090965516267749j), (-0.3276427621628252-0.11590147454740794j)]), [qreg[3], qreg[1], qreg[4], qreg[2]])
qc.append(HGate(), [qreg[4]])
with qc.for_loop(range(5)) as i:
	qc.append(RXGate(0.248), [qreg[2]])
	qc.append(AND(3), [qreg[1], qreg[4], qreg[2], qreg[3]])
	qc.append(RZGate(1.733), [qreg[2]])
	qc.append(RZGate(1.472), [qreg[3]])
	qc.append(U3Gate(2.758, 5.469, 3.891), [qreg[4]])
	qc.append(RealAmplitudes(5, reps=1, parameter_prefix='theta_1885d1'), [qreg[1], qreg[4], qreg[2], qreg[0], qreg[3]])
	qc.append(C3XGate(), [qreg[1], qreg[2], qreg[4], qreg[3]])
	qc.append(CUGate(4.264, 5.606, 3.308, 5.658), [qreg[4], qreg[3]])
	qc.append(XOR(1), [qreg[1]])
	qc.append(C3XGate(), [qreg[4], qreg[2], qreg[3], qreg[0]])
	qc.break_loop()
	qc.ch(3, 1)
	qc.ccx(4, 2, 0)
	qc.ry(0.39269908169872414, 2)
	qc.rz(1.5707963267948966, 3)
	qc.ccz(4, 2, 1)
	qc.x(1)
	qc.ry(0.39269908169872414, 4)
	qc.ch(4, 1)
	qc.crz(1.5707963267948966, 4, 1)
	qc.swap(4, 0)
qc.append(RXGate(3.678), [qreg[3]])
qc.append(CUGate(3.747, 0.76, 6.233, 3.054), [qreg[3], qreg[2]])
qc.append(StatePreparation([(0.7277782219705242-0.23408404841892846j), (-0.1998489284806281-0.43875019438907875j), (-0.2977394272730092-0.18552253564076976j), (-0.15631512220335397+0.18868067043825004j)]), [qreg[2], qreg[1]])
qc.append(MCXGate(1), [qreg[1], qreg[3]])
qc.append(U3Gate(5.871, 0.018, 2.726), [qreg[2]])
qc.append(CXGate(), [qreg[3], qreg[2]])
qc.append(CXGate(), [qreg[4], qreg[1]])
qc.append(OR(3), [qreg[1], qreg[2], qreg[3], qreg[4]])
qc.append(HGate(), [qreg[4]])
qc.append(AND(3), [qreg[2], qreg[3], qreg[4], qreg[0]])
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
