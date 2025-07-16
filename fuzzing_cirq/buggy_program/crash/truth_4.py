import cirq
from cirq.transformers import *

q = cirq.LineQubit.range(6) 
circuit = cirq.Circuit()


sub_circuit = cirq.Circuit()


sub_circuit.append(cirq.Z(q[0]))



sub_op = cirq.CircuitOperation(sub_circuit.freeze()) 
circuit.append(cirq.measure(q[5], key="c")) 
circuit.append(cirq.measure([q[0],q[1]], key="ca")) 
dc_cond = cirq.BitMaskKeyCondition.create_equal_mask('ca', bitmask=1)
circuit.append(sub_op.with_classical_controls("c", dc_cond)) 


cirq.contrib.acquaintance.AcquaintanceOperation([q[2],q[0]], [2, 0]) 
cirq.contrib.acquaintance.CircularShiftGate(shift=1, num_qubits=4).on(q[0],q[4],q[1],q[3]) 
circuit.append(cirq.measure(q, key="m")) 
circuit = optimize_for_target_gateset(circuit)
circuit = eject_z(circuit)
circuit = stratified_circuit(circuit)
simulator = cirq.Simulator() 
result = simulator.run(circuit, repetitions=5)
print(result.histogram(key='m'))