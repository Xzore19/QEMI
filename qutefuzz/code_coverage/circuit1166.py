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
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.y(qreg_2[1])
subcirc0.h(qreg_0[0])
subcirc0.u(0.550000,-0.758000,0.166000, qreg_1[0])
subcirc0.h(qreg_1[0])
subcirc0.y(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.h(qreg_1[1])
subcirc1.u(0.794000,-0.614000,-0.344000, qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.y(qreg_1[2])
subcirc1.u(0.213000,0.090000,-0.966000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(0)
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

main_circ.y(qreg_0[3])
main_circ.h(qreg_0[1])
main_circ.y(qreg_0[1])
main_circ.s(qreg_0[3])
main_circ.u(-0.697000,-0.554000,param_2, qreg_0[1])
main_circ.s(qreg_0[0])
main_circ.y(qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.y(qreg_0[3])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.s(qreg_0[2])
main_circ.s(qreg_0[1])
main_circ.h(qreg_0[3])
main_circ.h(qreg_0[1])
main_circ.y(qreg_0[2])
main_circ.y(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.h(qreg_0[0])
main_circ.u(-0.627000,param_2,param_2, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.h(qreg_0[3])
main_circ.s(qreg_0[3])
main_circ.s(qreg_0[3])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.h(qreg_0[3])
main_circ.y(qreg_0[3])
main_circ.y(qreg_0[3])
main_circ.u(-0.752000,param_2,0.703000, qreg_0[0])
main_circ.h(qreg_0[0])
main_circ.y(qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.s(qreg_0[3])
main_circ.h(qreg_0[3])
main_circ.h(qreg_0[1])
main_circ.s(qreg_0[1])
bindings = {param_2: -0.164000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
