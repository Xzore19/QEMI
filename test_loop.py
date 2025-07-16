from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager

qc = QuantumCircuit(1, 1)

with qc.if_test((0, True)) as else_1:
    qc.x(0)
with else_1:
    qc.h(0)

simulator = Aer.get_backend("aer_simulator")

print(qc)

# compiled_circuit = transpile(qc, backend=simulator, optimization_level=3, routing_method="sabre",
#                              layout_method="noise_adaptive", approximation_degree=1)
# job = simulator.run(compiled_circuit, shots=1)
# result = job.result().get_counts()
# print(result)