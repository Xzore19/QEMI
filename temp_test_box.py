import cirq
from cirq.transformers import *

q = cirq.LineQubit.range(2)
circuit = cirq.Circuit()

c = cirq.Circuit()
c.append([
    cirq.S(q[0]),
    cirq.XPowGate(exponent=0.25)(q[0]),
    cirq.S(q[0])**-1,
    cirq.CZ(q[0], q[1]),
    cirq.S(q[0])**-1,
    cirq.XPowGate(exponent=0.25)(q[0]),
    cirq.S(q[0]),
])

p = cirq.LineQubit.range(2)
circuit1 = cirq.Circuit()

c1 = cirq.Circuit()
c1.append([
    cirq.S(p[0])**-1,
    cirq.XPowGate(exponent=0.75)(p[0]),
    cirq.S(p[0]),
    cirq.CZ(p[0], p[1]),
    cirq.S(p[0]),
    cirq.XPowGate(exponent=0.75)(p[0]),
    cirq.S(p[0])**-1,
    cirq.Z(p[1])
])


print(cirq.equal_up_to_global_phase(cirq.unitary(c), cirq.unitary(c1)))