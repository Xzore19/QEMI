import cirq
from cirq import transformers

q = cirq.LineQubit.range(6)
circuit = cirq.Circuit()

circuit.append(cirq.PhasedXPowGate(exponent=0.04908738521234052,phase_exponent=0.006135923151542565).on(q[0]))
circuit.append(cirq.PhasedXPowGate(exponent=0.01227184630308513,phase_exponent=0.01227184630308513).on(q[0]).controlled_by(q[3]))
circuit.append(cirq.rx(0.39269908169872414).on(q[4]))
circuit.append(cirq.CSwapGate.on(q[4], q[2], q[1]))
circuit.append(cirq.YYPowGate(exponent=0.19634954084936207).on(q[1], q[4]))
sub_circuit = cirq.Circuit()
circuit.append(cirq.measure(q[5], key="c"))
circuit.append(cirq.XPowGate(exponent=0.7853981633974483).on(q[3]).controlled_by(q[4]))
circuit.append(cirq.CZ(q[1], q[4]))
circuit.append(cirq.SWAP(q[2], q[3]).controlled_by(q[4]))
circuit.append(cirq.Y(q[4]))
circuit.append(cirq.Z(q[0]).controlled_by(q[4]))
circuit.append(cirq.measure(q, key="m"))

circuit = transformers.drop_empty_moments(circuit)
circuit = transformers.defer_measurements(circuit)
circuit = transformers.expand_composite(circuit)
circuit = transformers.merge_single_qubit_gates_to_phxz(circuit)
circuit = transformers.stratified_circuit(circuit)
circuit = transformers.eject_phased_paulis(circuit)
circuit = transformers.drop_negligible_operations(circuit)
circuit = transformers.eject_z(circuit)
circuit = transformers.optimize_for_target_gateset(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=500)
print(result.histogram(key='m'))