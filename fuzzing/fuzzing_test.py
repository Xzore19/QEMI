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

qc.append(CRXGate(0.249), [qreg[2], qreg[4]])
qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[1], qreg[3]])
qc.iswap(4, 0)
qc.x(1)
qc.append(HGate(), [qreg[1]])
qc.append(CUGate(0.562, 3.292, 0.579, 0.817), [qreg[2], qreg[3]])
qc.append(XGate(), [qreg[0]])
qc.append(SwapGate(), [qreg[0], qreg[3]])
qc.rz(1.5707963267948966, 1)
qc.swap(4, 3)
def create_oracle(qreg):
    oracle = QuantumCircuit(qreg, name='Oracle')
    oracle.x(qreg[0])
    oracle.x(qreg[1])
    oracle.h(qreg[1])
    oracle.mcx([qreg[0]], qreg[1])
    oracle.h(qreg[1])
    oracle.x(qreg[0])
    oracle.x(qreg[1])
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
qc.measure(qreg[5], cond_creg[0]) 
qc.measure(qreg[6], cond_creg[1]) 
with qc.while_loop((cond_creg, 0b00)): 
	qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[2], qreg[4], qreg[1], qreg[0], qreg[3]])
	qc.iswap(2, 0)
	qc.p(0.7853981633974483, 2)
	qc.append(CXGate(), [qreg[0], qreg[2]])
	qc.cry(0.39269908169872414, 4, 2)
	qc.z(0)
	qc.append(RZGate(5.828), [qreg[1]])
	qc.cp(0.7853981633974483, 1, 4)
	qc.append(XOR(2), [qreg[3], qreg[2]])
	qc.append(AND(1), [qreg[1], qreg[4]])
	qc.measure(qreg[5], cond_creg[0]) 
	qc.measure(qreg[6], cond_creg[1]) 
	qc.break_loop()
	qc.y(0)
	qc.append(U3Gate(1.801, 2.258, 0.153), [qreg[2]])
	qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_334857'), [qreg[1], qreg[2], qreg[4], qreg[3]])
	qc.append(EfficientSU2(4, reps=1, parameter_prefix='theta_275863'), [qreg[4], qreg[3], qreg[1], qreg[2]])
	qc.append(SwapGate(), [qreg[0], qreg[3]])
	qc.append(NLocal(4, reps=1, parameter_prefix='theta_8ce978'), [qreg[1], qreg[3], qreg[2], qreg[4]])
	qc.append(CXGate(), [qreg[2], qreg[4]])
	qc.append(CUGate(4.833, 1.852, 4.003, 1.012), [qreg[1], qreg[3]])
	qc.ry(1.5707963267948966, 3)
	qc.append(U3Gate(2.487, 0.217, 5.468), [qreg[3]])
qc.crx(0.7853981633974483, 3, 2)
qc.append(CXGate(), [qreg[2], qreg[4]])
qc.rx(0.39269908169872414, 0)
qc.append(RXGate(4.019), [qreg[4]])
qc.append(C3XGate(), [qreg[0], qreg[4], qreg[3], qreg[1]])
qc.swap(4, 1)
qc.append(RXGate(0.626), [qreg[0]])
qc.append(CRXGate(2.569), [qreg[2], qreg[3]])
qc.append(SwapGate(), [qreg[0], qreg[1]])
qc.cry(1.5707963267948966, 1, 4)
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
