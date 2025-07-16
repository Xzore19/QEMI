from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(pi/2,-0.388000,0.229000, qreg_1[2])
subcirc0.s(qreg_1[1])
subcirc0.u(pi/2,0.469000,-0.267000, qreg_1[2])
subcirc0.s(qreg_1[1])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[2])
subcirc1.s(qreg_3[0])
subcirc1.u(pi/2,-0.803000,0.932000, qreg_0[0])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.u(param_2,0.001000,param_4, qreg_0[3])
main_circ.u(pi/2,-0.075000,-0.468000, qreg_0[2])
main_circ.s(qreg_0[2])
main_circ.s(qreg_0[3])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1],0])
main_circ.s(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2],0])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[2],0,qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],qreg_0[0],0,qreg_0[1]])
main_circ.s(qreg_0[3])
main_circ.z(qreg_0[2])
main_circ.s(qreg_0[2])
main_circ.x(qreg_0[2])
main_circ.s(qreg_0[1])
main_circ.z(qreg_0[2])
main_circ.u(param_1,param_4,0.407000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1],0])
main_circ.s(qreg_0[0])
main_circ.s(qreg_0[2])
main_circ.u(param_2,param_4,0.749000, qreg_0[0])
main_circ.x(qreg_0[0])
bindings = {param_1: 0.359000, param_2: -0.357000, param_4: -0.391000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
