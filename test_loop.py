<<<<<<< HEAD
import cirq
from cirq.transformers import *

q = cirq.LineQubit.range(2)
circuit = cirq.Circuit()

circuit.append(cirq.H(q[1]))

circuit.append(cirq.H(q[0]).controlled_by(q[1]))

circuit.append(cirq.T(q[1]))
circuit.append(cirq.H(q[1]))

# circuit.append(cirq.measure(q, key="m"))


circuit = expand_composite(circuit)
circuit = merge_k_qubit_unitaries(circuit, k=2)
circuit = optimize_for_target_gateset(circuit)

p = cirq.LineQubit.range(2)
circuit2 = cirq.Circuit()

circuit2.append(cirq.H(p[1]))

circuit2.append(cirq.H(p[0]).controlled_by(p[1]))

circuit2.append(cirq.T(p[1]))
circuit2.append(cirq.H(p[1]))

# circuit2.append(cirq.measure(q, key="m"))

# simulator = cirq.Simulator()
# result = simulator.run(circuit, repetitions=10000)
# print(result.histogram(key='m'))

# result = simulator.simulate(circuit)

# print(result.final_state_vector)

print(cirq.equal_up_to_global_phase(cirq.unitary(circuit), cirq.unitary(circuit2)))
=======
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
>>>>>>> 8faaa73adee21a64a4eddfb5ab14b7685b825347
