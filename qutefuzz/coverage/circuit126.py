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
subcirc0.u(pi/2,-0.678000,-0.200000, qreg_0[1])
subcirc0.x(qreg_3[0])
subcirc0.u(0,0,0.427000, qreg_0[2])
subcirc0.u(0,0,-0.873000, qreg_0[1])
subcirc0.u(pi/2,0.884000,-0.394000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[3])
subcirc1.u(pi/2,-0.874000,-0.022000, qreg_0[2])
subcirc1.u(pi/2,0.713000,0.190000, qreg_0[2])
subcirc1.h(qreg_0[2])
subcirc1.h(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[3])
subcirc2.u(pi/2,-0.619000,0.670000, qreg_0[2])
subcirc2.u(pi/2,-0.933000,-0.905000, qreg_0[2])
subcirc2.u(0,0,-0.366000, qreg_0[1])
subcirc2.x(qreg_0[2])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.u(pi/2,param_0,0.355000, qreg_0[1])
main_circ.u(param_1,0,param_4, qreg_0[0])
main_circ.u(0,0,0.120000, qreg_0[2])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.u(param_0,param_0,0.484000, qreg_0[1])
main_circ.u(pi/2,0.700000,-0.437000, qreg_0[2])
main_circ.append(subcirc2,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.u(pi/2,param_2,param_0, qreg_0[1])
main_circ.h(qreg_0[0])
main_circ.h(qreg_3[0])
main_circ.append(subcirc2,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.x(qreg_0[2])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.u(pi/2,param_3,0.163000, qreg_0[2])
main_circ.u(param_1,param_2,-0.797000, qreg_0[1])
main_circ.u(param_0,param_3,param_5, qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.h(qreg_3[0])
main_circ.x(qreg_0[1])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_3[0],qreg_0[0]])
main_circ.u(pi/2,0.516000,param_2, qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.u(0,0,-0.438000, qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.h(qreg_3[0])
bindings = {param_0: -0.293000, param_1: -0.291000, param_2: -0.867000, param_3: 0.152000, param_4: 0.865000, param_5: 0.432000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
