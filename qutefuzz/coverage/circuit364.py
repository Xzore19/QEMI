from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.855000,0.750000, qreg_1[1])
subcirc0.u(pi/2,0.235000,-0.895000, qreg_1[0])
subcirc0.cy(qreg_3[0],qreg_1[1])
subcirc0.u(pi/2,-0.704000,0.648000, qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.cz(qreg_0[0],qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_2[1])
subcirc1.cy(qreg_1[0],qreg_2[1])
subcirc1.cz(qreg_2[1],qreg_0[0])
subcirc1.cz(qreg_2[1],qreg_1[0])
subcirc1.cy(qreg_1[0],qreg_2[0])
subcirc1.cy(qreg_0[0],qreg_1[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cy(qreg_2[1],qreg_0[0])
subcirc2.u(pi/2,-0.082000,-0.309000, qreg_2[1])
subcirc2.u(pi/2,0.510000,-0.151000, qreg_2[0])
subcirc2.y(qreg_2[0])
subcirc2.u(pi/2,0.258000,-0.436000, qreg_2[0])
subcirc2.u(pi/2,0.744000,0.054000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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
param_5 = Parameter("param_5")

main_circ.cz(qreg_0[0],0)
main_circ.y(qreg_2[0])
main_circ.u(param_5,0.645000,param_4, qreg_0[0])
main_circ.u(pi/2,param_3,param_1, qreg_1[0])
main_circ.y(qreg_0[0])
main_circ.append(subcirc2,[0,qreg_2[0],qreg_2[1],qreg_1[0],qreg_0[0]])
main_circ.y(0)
main_circ.cy(qreg_1[0],qreg_2[1])
main_circ.cz(qreg_1[0],qreg_2[0])
main_circ.cy(qreg_1[0],0)
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],qreg_1[0],qreg_2[0]])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_2[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_2[0],0,qreg_1[0],qreg_2[1]])
main_circ.append(subcirc0,[0,qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.y(qreg_0[0])
main_circ.cy(qreg_0[0],0)
main_circ.u(param_5,param_0,param_3, 0)
main_circ.append(subcirc2,[qreg_0[0],qreg_2[1],qreg_1[0],0,qreg_2[0]])
main_circ.cy(qreg_2[1],qreg_0[0])
main_circ.append(subcirc2,[qreg_2[0],0,qreg_1[0],qreg_0[0],qreg_2[1]])
bindings = {param_0: -0.233000, param_1: -0.568000, param_3: -0.106000, param_4: 0.511000, param_5: -0.286000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
