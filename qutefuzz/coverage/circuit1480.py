from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.rz(-0.957000, qreg_0[3])
subcirc0.h(qreg_0[1])
subcirc0.u(pi/2,0.693000,0.464000, qreg_0[0])
subcirc0.s(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_1[1])
subcirc1.s(qreg_1[0])
subcirc1.h(qreg_1[1])
subcirc1.h(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.h(qreg_1[1])
subcirc2.s(qreg_0[0])
subcirc2.h(qreg_0[0])
subcirc2.h(qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.914000, qreg_0[1])
subcirc3.u(pi/2,-0.530000,-0.078000, qreg_2[0])
subcirc3.s(qreg_0[1])
subcirc3.u(pi/2,0.526000,0.260000, qreg_3[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.rz(0.427000, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[2],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
main_circ.rz(-0.793000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.s(qreg_0[2])
main_circ.h(qreg_0[2])
main_circ.h(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.rz(param_2, qreg_0[3])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3]])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.u(param_1,-0.964000,0.810000, qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.h(qreg_0[2])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.rz(-0.068000, qreg_0[3])
bindings = {param_1: -0.510000, param_2: -0.501000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
