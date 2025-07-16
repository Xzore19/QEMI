import cirq
from cirq.transformers import *

q = cirq.LineQubit.range(3)
circuit = cirq.Circuit()


sub_circuit = cirq.Circuit()


sub_circuit.append(cirq.MSGate(rads=0.19634954084936207).on(q[0], q[1]).controlled_by(q[2]))
sub_circuit.append(cirq.H(q[1]).controlled_by(q[0]))


sub_op = cirq.CircuitOperation(sub_circuit.freeze()) 
circuit.append(cirq.measure(q[1], key="c"))
circuit.append(sub_op.with_classical_controls("c"))


circuit.append(cirq.measure(q, key="m"))

circuit = optimize_for_target_gateset(circuit)
circuit = stratified_circuit(circuit)

simulator = cirq.Simulator() 
result = simulator.run(circuit, repetitions=5)
print(result.histogram(key='m'))