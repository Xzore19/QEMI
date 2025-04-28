from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile 
from qiskit_aer import Aer 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.providers.fake_provider import GenericBackendV2 
from qiskit.circuit import Parameter, ParameterVector 
from qiskit.circuit.library import XGate 
from qiskit.transpiler.passes import * 
import z3 
from qiskit.transpiler import PassManager, generate_preset_pass_manager 
from math import pi 

qreg = QuantumRegister(7) 
creg = ClassicalRegister(5) 
cond_creg = ClassicalRegister(2) 
qc = QuantumCircuit(qreg, creg, cond_creg) 

qc.x(3)
qc.p(0.7853981633974483, 3)
qc.crz(1.5707963267948966, 2, 0)
qc.rz(0.7853981633974483, 4)
qc.y(4)
qc.cz(2, 3)
qc.t(0)
qc.cp(0.7853981633974483, 2, 4)
qc.crx(0.7853981633974483, 4, 3)
qc.y(3)

a = 1.7976931348623157e+3 
if a == 1.7976931348623157e+3 -1:
	qc.h(0) 
def create_oracle(qreg):
    oracle = QuantumCircuit(qreg, name='Oracle')
    oracle.h(qreg[1])
    oracle.mcx([qreg[0]], qreg[1])
    oracle.h(qreg[1])
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
with qc.if_test((cond_creg, 0b11)) as else_1: 
    pass
with else_1: 
    qc.h(0)

qc.measure(qreg[3], creg[3])
with qc.if_test((creg[3], 0b1)) as else_1: 
	qc.iswap(3, 2)
	qc.cx(4, 3)
	qc.y(1)
	qc.ccx(4, 3, 1)
	qc.p(1.5707963267948966, 0)
	qc.ccz(4, 3, 0)
	qc.crx(0.7853981633974483, 3, 2)
	qc.z(4)
	qc.ch(3, 0)
	qc.p(1.5707963267948966, 2)
with else_1: 
	qc.cx(4, 2)
	qc.y(0)
	qc.t(0)
	qc.cz(2, 4)
	qc.x(3)
	qc.iswap(3, 2)
	qc.cx(4, 0)
	qc.crx(1.5707963267948966, 4, 2)
	qc.cp(0.39269908169872414, 4, 2)
	qc.ccz(4, 2, 1)

qc.tdg(3)
qc.tdg(1)
qc.x(3)
qc.h(0)
qc.rz(0.39269908169872414, 0)
qc.cz(0, 4)
qc.rz(0.39269908169872414, 2)
qc.z(1)
qc.cswap(2, 1, 0)
qc.ry(0.7853981633974483, 3)
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(CollectCliffords()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 ) 
job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
