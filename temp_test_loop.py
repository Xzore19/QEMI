import cirq

q = cirq.LineQubit.range(2)
circuit1 = cirq.Circuit(cirq.X(q[1]),
                        cirq.PhasedXPowGate(exponent=-0.5, phase_exponent=0.25).on(q[0]),
                        cirq.CZ(q[1], q[0]),
                        cirq.PhasedXPowGate(exponent=0.5, phase_exponent=0.25).on(q[0]))


p = cirq.LineQubit.range(2)
circuit2 = cirq.Circuit(cirq.X(p[1]),
                        cirq.PhasedXPowGate(exponent=0.5, phase_exponent=0.75).on(p[0]),
                        cirq.CZ(p[1], p[0]),
                        cirq.PhasedXPowGate(exponent=-0.5, phase_exponent=0.75).on(p[0]),
                        cirq.Z(p[1]))

print(cirq.equal_up_to_global_phase(cirq.unitary(circuit1), cirq.unitary(circuit2)))