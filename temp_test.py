import cirq
from cirq.transformers import *

q = cirq.LineQubit.range(3)
circuit = cirq.Circuit()

circuit.append(cirq.X(q[2]))
circuit.append(cirq.H(q[1]).controlled_by(q[2]))

sub_circuit = cirq.Circuit()

sub_circuit.append(cirq.H(q[1]).controlled_by(q[2]))

sub_op = cirq.CircuitOperation(sub_circuit.freeze())
circuit.append(cirq.measure(q[2], key="c"))
circuit.append(sub_op.with_classical_controls("c"))

circuit.append(cirq.measure(q, key="m"))

circuit = merge_k_qubit_unitaries(circuit, k=2)
circuit = optimize_for_target_gateset(circuit)
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=500)
print(result.histogram(key='m'))