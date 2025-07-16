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
subcirc0.ry(-0.506000, qreg_0[0])
subcirc0.u(pi/2,0.507000,0.556000, qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[1])
subcirc0.s(qreg_0[2])
subcirc0.ry(-0.622000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(0.048000, qreg_0[0])
subcirc1.s(qreg_2[0])
subcirc1.s(qreg_2[1])
subcirc1.s(qreg_0[0])
subcirc1.ry(0.091000, qreg_2[1])
subcirc1.ry(0.667000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.cx(qreg_0[2],qreg_0[1])
subcirc2.u(pi/2,-0.457000,0.634000, qreg_0[3])
subcirc2.s(qreg_0[2])
subcirc2.u(pi/2,-0.577000,0.809000, qreg_0[1])
subcirc2.u(pi/2,-0.198000,-0.677000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,-0.941000,-0.471000, qreg_0[1])
subcirc3.s(qreg_3[0])
subcirc3.u(pi/2,-0.462000,0.748000, qreg_3[0])
subcirc3.s(qreg_0[1])
subcirc3.cx(qreg_2[0],qreg_0[1])
subcirc3.ry(-0.194000, qreg_3[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.s(qreg_0[2])
subcirc4.cx(qreg_0[2],qreg_0[3])
subcirc4.u(pi/2,0.468000,0.447000, qreg_0[2])
subcirc4.u(pi/2,0.811000,0.176000, qreg_0[1])
subcirc4.ry(-0.701000, qreg_0[0])
subcirc4.ry(0.190000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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
param_5 = Parameter("param_5")

main_circ.append(subcirc4,[qreg_0[0],0,qreg_0[1],1])
main_circ.ry(-0.629000, 0)
main_circ.ry(0.919000, qreg_0[1])
main_circ.ry(param_4, qreg_0[0])
main_circ.ry(0.472000, 2)
main_circ.cx(qreg_0[0],0)
main_circ.s(1)
main_circ.append(subcirc2,[3,qreg_0[0],1,2])
main_circ.append(subcirc4,[qreg_0[0],3,2,0])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],3,0])
main_circ.append(subcirc4,[2,0,3,1])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],0,1])
main_circ.cx(0,3)
main_circ.cx(0,3)
main_circ.cx(1,2)
main_circ.cx(qreg_0[0],1)
main_circ.cx(qreg_0[0],1)
main_circ.cx(3,1)
main_circ.cx(qreg_0[0],1)
main_circ.cx(0,1)
main_circ.cx(qreg_0[1],0)
main_circ.cx(2,0)
main_circ.u(pi/2,param_1,-0.539000, 1)
main_circ.s(1)
main_circ.ry(param_0, 1)
main_circ.cx(0,1)
bindings = {param_0: -0.966000, param_1: 0.900000, param_4: 0.664000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
