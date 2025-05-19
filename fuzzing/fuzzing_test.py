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

qc.append(ZZFeatureMap(4, reps=1, parameter_prefix='x_f4efeb'), [qreg[3], qreg[2], qreg[1], qreg[0]])
qc.cx(2, 0)
qc.append(CUGate(5.76, 5.21, 5.281, 5.429), [qreg[4], qreg[1]])
qc.append(XOR(2), [qreg[3], qreg[0]])
qc.t(0)
qc.ccx(3, 2, 1)
qc.append(CRXGate(5.371), [qreg[2], qreg[1]])
qc.append(MCPhaseGate(1.0, num_ctrl_qubits=3), [qreg[1], qreg[0], qreg[2], qreg[4]])
qc.append(C3XGate(), [qreg[0], qreg[3], qreg[1], qreg[4]])
qc.append(AND(2), [qreg[1], qreg[0], qreg[2]])
def create_oracle(qreg):
    oracle = QuantumCircuit(qreg, name='Oracle')
    oracle.x(qreg[0])
    oracle.h(qreg[1])
    oracle.mcx([qreg[0]], qreg[1])
    oracle.h(qreg[1])
    oracle.x(qreg[0])
    return oracle.to_gate(label='Oracle')

def create_diffuser(qreg):
    diffuser = QuantumCircuit(qreg, name='Diffuser')
    diffuser.h(qreg)
    diffuser.x(qreg)
    diffuser.h(qreg[1])
    diffuser.mcx([qreg[0]], qreg[1])
    diffuser.h(qreg[1])
    diffuser.x(qreg)
    diffuser.h(qreg)
    return diffuser.to_gate(label='Diffuser')

backend = Aer.get_backend('aer_simulator')
oracle_gate = create_oracle(QuantumRegister(2))
diffuser_gate = create_diffuser(QuantumRegister(2))
results = []
grdc_qreg = QuantumRegister(2)
grdc_creg = ClassicalRegister(2)
grdc_qc = QuantumCircuit(grdc_qreg, grdc_creg)
grdc_qc.h(grdc_qreg)
for _ in range(1):
    grdc_qc.append(oracle_gate, qargs=grdc_qreg)
    grdc_qc.append(diffuser_gate, qargs=grdc_qreg)

qc.compose(grdc_qc, inplace = True, qubits = [5, 6]) 
qc.append(PauliFeatureMap(4, reps=1, parameter_prefix='x_2ead34'), [qreg[4], qreg[1], qreg[2], qreg[3]])
qc.append(XOR(2), [qreg[2], qreg[0]])
qc.append(HGate(), [qreg[0]])
qc.append(HGate(), [qreg[2]])
qc.append(RXGate(5.916), [qreg[0]])
qc.append(Initialize([(-0.04452156860866316+0.2000915031944704j), (-0.13432979594110528+0.1527080105394309j), (-0.030987985936194024-0.21343803656219568j), (-0.1027793093602568+0.17466918115074848j), (-0.01069511276321954+0.129371776693634j), (-0.030188681890852644-0.21881014295648027j), (0.08917974222740903+0.10134445583152282j), (0.03342114014696869-0.15997931979210156j), (-0.18746381305438312+0.037964391640054086j), (0.015120950661461264-0.18029372379858766j), (-0.22082284690113083-0.13125837559487827j), (-0.0025259722614563926+0.1972449687905567j), (0.08606011388178841+0.10410027293783666j), (0.033717549688835016-0.2070490909268525j), (0.02553684354650782-0.07638177400462129j), (0.05522360067914986-0.23789774129866653j), (-0.16629410275021095-0.020523124147664624j), (0.010339670817939994+0.020618837756412746j), (0.10148978591790299-0.10657267912725239j), (0.059238232032337364+0.01769862157150343j), (-0.054801453470145485-0.12187989548856089j), (0.15600385830264413-0.033311732976236456j), (-0.02430281804136025-0.09766652859657562j), (0.009925682159293809-0.21121667434798908j), (0.22558567170371155-0.04791348631647873j), (0.15924225579415266-0.06670754870090904j), (-0.2257971609029432+0.15689100630512054j), (-0.08514332219351178+0.1394744669687329j), (-0.08780281523787734+0.0903938048926428j), (0.0781393015991366+0.10362223872073324j), (-0.029346151146216637+0.0032192731325631904j), (0.13489997925633412-0.16288252021527097j)]), [qreg[1], qreg[2], qreg[3], qreg[4], qreg[0]])
qc.append(NLocal(2, reps=1, parameter_prefix='theta_692beb'), [qreg[3], qreg[2]])
qc.append(CRXGate(1.118), [qreg[1], qreg[4]])
qc.append(CUGate(6.267, 1.721, 1.505, 3.433), [qreg[0], qreg[2]])
qc.append(EfficientSU2(4, reps=1, parameter_prefix='theta_d98e6b'), [qreg[1], qreg[3], qreg[0], qreg[4]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(Optimize1qGatesDecomposition()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
