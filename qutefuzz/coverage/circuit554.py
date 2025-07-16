from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(0.765000, qreg_3[0])
subcirc0.ry(0.242000, qreg_0[0])
subcirc0.h(qreg_2[0])
subcirc0.rz(0.821000, qreg_1[0])

main_circ = QuantumCircuit(0)
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
param_1 = Parameter("param_1")

main_circ.h(qreg_3[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.h(qreg_3[0])
main_circ.y(qreg_3[0])
main_circ.rz(-0.092000, qreg_3[0])
main_circ.h(qreg_0[1])
main_circ.ry(param_1, qreg_3[0])
main_circ.h(qreg_0[0])
main_circ.y(qreg_3[0])
main_circ.y(qreg_0[0])
main_circ.rz(param_0, qreg_0[0])
main_circ.y(qreg_3[0])
main_circ.y(qreg_0[1])
main_circ.rz(0.863000, qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.rz(param_1, qreg_0[1])
main_circ.y(qreg_3[0])
main_circ.h(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.h(qreg_0[2])
main_circ.h(qreg_0[2])
main_circ.ry(param_1, qreg_0[2])
main_circ.y(qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.h(qreg_0[1])
main_circ.rz(param_1, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
main_circ.ry(0.691000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_3[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.rz(-0.968000, qreg_0[0])
main_circ.rz(-0.278000, qreg_3[0])
main_circ.ry(0.425000, qreg_0[2])
main_circ.rz(0.168000, qreg_3[0])
main_circ.rz(param_1, qreg_0[2])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.ry(param_0, qreg_0[0])
main_circ.h(qreg_0[1])
bindings = {param_0: -0.858000, param_1: 0.961000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
