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
subcirc0.u(pi/2,-0.686000,0.454000, qreg_0[1])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_0[1])
subcirc0.rz(0.834000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[2])
subcirc1.y(qreg_0[2])
subcirc1.u(pi/2,-0.001000,-0.972000, qreg_0[1])
subcirc1.rz(0.312000, qreg_0[2])

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

main_circ.rz(0.284000, 3)
main_circ.y(2)
main_circ.u(param_0,-0.052000,param_0, qreg_0[0])
main_circ.append(subcirc1,[3,1,qreg_0[1],qreg_0[0]])
main_circ.append(subcirc0,[3,0,2,qreg_0[1]])
main_circ.x(qreg_0[1])
main_circ.x(2)
main_circ.append(subcirc0,[3,qreg_0[1],1,0])
main_circ.append(subcirc0,[3,2,qreg_0[0],1])
main_circ.append(subcirc1,[qreg_0[1],1,0,3])
main_circ.x(1)
main_circ.u(pi/2,-0.433000,-0.843000, 1)
main_circ.x(0)
main_circ.y(3)
main_circ.append(subcirc1,[1,3,2,0])
main_circ.y(1)
main_circ.u(pi/2,-0.324000,param_0, qreg_0[0])
main_circ.rz(param_2, qreg_0[0])
main_circ.rz(param_0, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],1,qreg_0[0],3])
main_circ.rz(-0.093000, 0)
main_circ.x(2)
main_circ.append(subcirc0,[2,3,qreg_0[1],1])
main_circ.append(subcirc0,[3,2,qreg_0[0],1])
main_circ.u(pi/2,param_2,-0.804000, 0)
main_circ.rz(param_1, qreg_0[1])
main_circ.x(1)
bindings = {param_0: 0.224000, param_1: 0.482000, param_2: 0.325000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "TemplateOptimization")
