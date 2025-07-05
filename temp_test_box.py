import cirq
from cirq.transformers import *

q = cirq.LineQubit.range(3)
circuit = cirq.Circuit()


sub_circuit = cirq.Circuit()

sub_circuit.append(cirq.X(q[0]).controlled_by(q[1]))

sub_op = cirq.CircuitOperation(sub_circuit.freeze())
circuit.append(cirq.measure(q[2], key="c"))
circuit.append(sub_op.with_classical_controls("c"))

circuit.append(cirq.measure(q, key="m"))

# circuit = defer_measurements(circuit)

circuit = insertion_sort_transformer(circuit)
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=500)
print(result.histogram(key='m'))
