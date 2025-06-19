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

qreg = QuantumRegister(4)
creg = ClassicalRegister(4)
qc = QuantumCircuit(qreg, creg)

qc.z(3)
qc.swap(1, 0)
qc.ch(2, 1)
qc.z(2)
qc.t(1)

qr_5f5257 = QuantumRegister(2)
cr_5f5257 = ClassicalRegister(2)
qc.add_register(qr_5f5257)
qc.add_register(cr_5f5257)
qc.x(qr_5f5257[0])
qc.x(qr_5f5257[1])
qc.measure(qr_5f5257[0], cr_5f5257[0])
qc.measure(qr_5f5257[1], cr_5f5257[1])
with qc.while_loop((cr_5f5257, 0b11)):
    qc.measure(qr_5f5257[0], cr_5f5257[0])
    qc.measure(qr_5f5257[1], cr_5f5257[1])

    qr_81e73d = QuantumRegister(2)
    cr_81e73d = ClassicalRegister(2)
    qc.add_register(qr_81e73d)
    qc.add_register(cr_81e73d)
    qc.x(qr_81e73d[0])
    qc.x(qr_81e73d[1])
    qc.measure(qr_81e73d[0], cr_81e73d[0])
    qc.measure(qr_81e73d[1], cr_81e73d[1])
    with qc.if_test((cr_81e73d, 0b11)) as else_81e73d:
        pass
    with else_81e73d:
        qc.crz(1.5707963267948966, 3, 0)
        qc.h(0)
        qc.t(0)
        qc.z(0)
        qc.ch(2, 0)
    qc.reset(qr_81e73d)

    qc.break_loop()
qc.reset(qr_5f5257)
qc.cx(1, 0)
qc.swap(3, 2)
qc.y(3)
qc.tdg(0)
qc.iswap(3, 0)
qc.measure(qreg[0], creg[0])
qc.measure(qreg[1], creg[1])
qc.measure(qreg[2], creg[2])
qc.measure(qreg[3], creg[3])

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})

simulator = Aer.get_backend("aer_simulator")

p = PassManager([Optimize1qGatesDecomposition(), Optimize1qGates()])
qc = p.run(qc)

compiled_circuit = transpile(qc, backend=simulator, optimization_level=3, routing_method="default",
                             layout_method="noise_adaptive", approximation_degree=1)

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=500)
result = job.result().get_counts()
print(result)
