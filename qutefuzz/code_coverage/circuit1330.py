from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_3[0],qreg_0[1])
subcirc0.y(qreg_0[1])
subcirc0.ry(-0.479000, qreg_0[2])
subcirc0.y(qreg_3[0])
subcirc0.x(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.ry(param_0, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],0,qreg_0[0],qreg_0[2]])
main_circ.y(qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0],0])
main_circ.append(subcirc0,[qreg_3[0],0,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.x(qreg_0[0])
main_circ.x(qreg_0[1])
main_circ.y(qreg_3[0])
main_circ.y(qreg_3[0])
main_circ.cy(qreg_0[0],0)
main_circ.y(qreg_3[0])
main_circ.y(qreg_0[1])
main_circ.cy(qreg_0[1],qreg_3[0])
main_circ.cy(qreg_0[2],qreg_3[0])
main_circ.y(qreg_3[0])
main_circ.ry(param_0, qreg_0[1])
main_circ.y(qreg_0[2])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.ry(0.683000, qreg_0[0])
main_circ.cy(qreg_0[1],qreg_3[0])
main_circ.ry(0.813000, qreg_0[1])
main_circ.cy(qreg_3[0],qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_3[0],qreg_0[0],0])
main_circ.cy(0,qreg_3[0])
main_circ.cy(qreg_0[2],qreg_3[0])
main_circ.cy(0,qreg_0[0])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.cy(0,qreg_3[0])
main_circ.ry(0.250000, qreg_0[1])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],0,qreg_0[0]])
main_circ.cy(0,qreg_3[0])
main_circ.cy(0,qreg_0[1])
bindings = {param_0: -0.590000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesDecomposition")
