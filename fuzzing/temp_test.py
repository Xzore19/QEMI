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

qreg = QuantumRegister(7) 
creg = ClassicalRegister(5) 
cond_creg = ClassicalRegister(2) 
qc = QuantumCircuit(qreg, creg, cond_creg) 

qc.append(CUGate(3.258, 0.013, 2.073, 1.781), [qreg[4], qreg[1]])
qc.append(Initialize([(-0.06502556532273789-0.19509469825236567j), (-0.17387892920798098-0.009985653753050367j), (0.16685249945251648+0.09889365017642557j), (-0.1522245182214203+0.18359448739124296j), (-0.016932526914846154+0.02302209645860376j), (0.09764004116523407-0.13403631278470185j), (-0.09757637809775885-0.17789524020612502j), (-0.09239903471402872+0.20707975048544955j), (-0.17656369972305208+0.026131760223198672j), (-0.0024979413463775265-0.0813613420928353j), (-0.03769556817988178+0.02836924053036224j), (-0.11138286799791511+0.014463525984008121j), (-0.03097808460550322+0.0010043464370096385j), (0.10178562524487826-0.05942641133811023j), (-0.017848693350902636-0.0304857331440785j), (-0.038701971905106075-0.06347284589856331j), (-0.09227441317260487-0.21803331104191404j), (0.32852545046612464-0.07828751780814036j), (0.15686689811117335-0.25588465229791213j), (-0.018501136204159756+0.017380530655614963j), (0.0584466982899998-0.11521962628805849j), (-0.15152900463810517+0.01704635124439717j), (-0.023054595397380064+0.005085916288261865j), (-0.24093745037191835+0.04994073987873226j), (0.1812807602975686+0.18637000376124563j), (0.08362761743150388-0.06488810144456024j), (0.0216150902346206-0.09096529315939522j), (-0.09051786404834566+0.0013474184784506014j), (0.10995370596803238-0.32152068398588757j), (-0.14518206027277064-0.020672329698570573j), (-0.0650345748288488+0.06753287707577763j), (0.14679564645381435+0.10995229973585548j)]), [qreg[1], qreg[2], qreg[4], qreg[3], qreg[0]])
qc.append(CCXGate(), [qreg[1], qreg[2], qreg[3]])
qc.append(NLocal(3, reps=1, parameter_prefix='theta_474a72'), [qreg[1], qreg[0], qreg[2]])
qc.append(HGate(), [qreg[3]])
qc.append(TwoLocal(4, reps=1, parameter_prefix='theta_879fc4'), [qreg[1], qreg[0], qreg[2], qreg[3]])
qc.append(ZZFeatureMap(3, reps=1, parameter_prefix='x_391dde'), [qreg[1], qreg[2], qreg[0]])
qc.append(U3Gate(6.089, 0.155, 1.972), [qreg[3]])
qc.cp(0.39269908169872414, 4, 1)
qc.append(CXGate(), [qreg[4], qreg[1]])
qc.ccz(3, 2, 0)
qc.ccx(4, 3, 2)
qc.append(EfficientSU2(3, reps=1, parameter_prefix='theta_029d77'), [qreg[3], qreg[1], qreg[2]])
qc.append(Initialize([(0.1471628040920234-0.27188766909019296j), (-0.016006055303727992+0.13756215350877676j), (-0.06892502069559057-0.3081990597204823j), (0.24754594638542488-0.04188471326647321j), (0.24936522189640936-0.11301521550418865j), (0.242641908971435-0.24616953620808119j), (-0.21226125821949726+0.11612319684914346j), (0.10976529095231377-0.06653682757927817j), (-0.06408066938454926+0.09023871093361477j), (-0.07390539430885908-0.08692604457263542j), (-0.03452344009115784+0.08337530389426275j), (-0.47610715002802284+0.3884688285317501j), (0.07012244759423605+0.027278874610110762j), (0.07464876258471653+0.04138022846788172j), (-0.12252340452190152-0.10108056810743546j), (0.0614046271697869-0.009072742400103213j)]), [qreg[2], qreg[4], qreg[0], qreg[3]])
qc.append(HGate(), [qreg[0]])
qc.append(CRXGate(0.033), [qreg[0], qreg[3]])
qc.append(U3Gate(1.913, 2.299, 2.849), [qreg[1]])
qc.append(CUGate(3.97, 1.266, 2.283, 5.052), [qreg[3], qreg[0]])
qc.append(ZZFeatureMap(2, reps=1, parameter_prefix='x_599193'), [qreg[1], qreg[0]])
qc.append(CXGate(), [qreg[2], qreg[0]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(TemplateOptimization()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
