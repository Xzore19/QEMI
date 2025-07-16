from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.429000,-0.996000, qreg_0[0])
subcirc0.ry(-0.881000, qreg_2[0])
subcirc0.u(pi/2,-0.497000,0.136000, qreg_0[0])
subcirc0.u(pi/2,0.917000,-0.235000, qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.u(pi/2,0.916000,1.000000, qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.ry(param_2, qreg_2[1])
main_circ.u(param_0,param_2,param_2, qreg_2[1])
main_circ.u(pi/2,param_2,param_0, qreg_0[0])
main_circ.x(qreg_2[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
main_circ.x(qreg_0[1])
main_circ.x(qreg_2[1])
main_circ.u(param_2,param_0,param_0, qreg_0[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_2[1]])
main_circ.ry(-0.384000, qreg_0[1])
main_circ.u(param_0,0.171000,0.730000, qreg_2[1])
main_circ.h(qreg_2[1])
main_circ.ry(param_1, qreg_2[0])
main_circ.ry(0.727000, qreg_2[0])
main_circ.h(qreg_0[1])
main_circ.ry(-0.599000, qreg_0[0])
main_circ.x(qreg_0[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_2[1]])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_2[1],qreg_0[1]])
main_circ.x(qreg_2[1])
main_circ.ry(param_0, qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.u(pi/2,-0.464000,-0.666000, qreg_2[0])
main_circ.x(qreg_2[0])
main_circ.ry(-0.358000, qreg_2[1])
main_circ.x(qreg_2[1])
bindings = {param_0: -0.944000, param_1: -0.014000, param_2: -0.070000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
