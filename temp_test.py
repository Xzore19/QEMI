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

qc.t(0)
qc.ry(1.5707963267948966, 4)
qc.ccx(4, 2, 1)
qc.rx(0.39269908169872414, 4)

def luo(qc):
	qc.y(1)
	qc.y(2)
	qc.y(3)
	qc.ccx(4, 2, 1)


with qc.for_loop(range(5)) as i:
	luo(qc)

qc.cry(0.39269908169872414, 0, 3)
qc.x(0)
qc.crx(1.5707963267948966, 1, 3)

qc.measure(qreg[0], creg[0])
qc.measure(qreg[1], creg[1])
qc.measure(qreg[2], creg[2])
qc.measure(qreg[3], creg[3])
qc.measure(qreg[4], creg[4])


simulator = Aer.get_backend("aer_simulator")

p = PassManager(Optimize1qGates())
qc = p.run(qc)

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "sabre", layout_method = "noise_adaptive", approximation_degree = 1 )
job = simulator.run(compiled_circuit, shots=10000)
result = job.result().get_counts()
print(result)
