import cirq
from cirq.transformers import *

q = cirq.LineQubit.range(6) 
circuit = cirq.Circuit()


cirq.contrib.acquaintance.CircularShiftGate(shift=1, num_qubits=2).on(q[4],q[2]) 
circuit.append(cirq.PhasedFSimGate(theta=1.5707963267948966, zeta=0.0030679615757712823, chi=0.0030679615757712823, gamma=1.5707963267948966, phi=0.006135923151542565).on(q[3], q[1]).controlled_by(q[2]))
circuit.append(cirq.CCZ(q[2], q[3], q[0]).controlled_by(q[1]))
circuit.append(cirq.ZZPowGate(exponent=0.0030679615757712823).on(q[0], q[2]))
circuit.append(cirq.CSwapGate().on(q[2], q[1], q[0]))
circuit.append(cirq.H(q[2]))
circuit.append(cirq.rx(0.01227184630308513).on(q[4]).controlled_by(q[2]))
circuit.append(cirq.SWAP(q[4], q[0]))
circuit.append(cirq.X(q[2]))
circuit.append(cirq.CCZ(q[4], q[3], q[1]))
circuit.append(cirq.SWAP(q[3], q[1]).controlled_by(q[2]))

cirq.contrib.acquaintance.AcquaintanceOperation([q[2],q[3],q[4],q[1]], [2, 3, 4, 1]) 
cirq.contrib.acquaintance.LinearPermutationGate(num_qubits=5, permutation={3: 0, 1: 2, 0: 4, 2: 1, 4: 3}).on(q[4],q[0],q[3],q[2],q[1]) 
sub_circuit = cirq.Circuit() 
circuit.append(cirq.measure(q[5], key="c")) 

cirq.contrib.acquaintance.LinearPermutationGate(num_qubits=4, permutation={1: 0, 3: 2, 2: 1, 0: 3}).on(q[2],q[3],q[1],q[4]) 
circuit.append(cirq.PhasedFSimGate(theta=0.01227184630308513, zeta=1.5707963267948966, chi=0.02454369260617026, gamma=0.02454369260617026, phi=0.09817477042468103).on(q[4], q[0]))
circuit.append(cirq.CCZ(q[4], q[3], q[1]))
circuit.append(cirq.ZZPowGate(exponent=0.006135923151542565).on(q[4], q[0]))
circuit.append(cirq.H(q[3]))
circuit.append(cirq.CCZ(q[4], q[0], q[1]).controlled_by(q[2]))
circuit.append(cirq.CNOT(q[3], q[2]))
circuit.append(cirq.CNOT(q[4], q[0]))
circuit.append(cirq.MSGate(rads=0.04908738521234052).on(q[3], q[2]))
circuit.append(cirq.XPowGate(exponent=0.19634954084936207).on(q[1]).controlled_by(q[2]))
circuit.append(cirq.PhasedFSimGate(theta=0.006135923151542565, zeta=0.7853981633974483, chi=0.0030679615757712823, gamma=0.0030679615757712823, phi=0.19634954084936207).on(q[3], q[0]))

cirq.contrib.acquaintance.AcquaintanceOperation([q[2],q[0],q[1],q[4]], [2, 0, 1, 4]) 
circuit.append(cirq.measure(q, key="m")) 
circuit = stratified_circuit(circuit)
circuit = insertion_sort_transformer(circuit)
circuit = synchronize_terminal_measurements(circuit)
simulator = cirq.Simulator() 
result = simulator.run(circuit, repetitions=500) 
print(result.histogram(key='m'))