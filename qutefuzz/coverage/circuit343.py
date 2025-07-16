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
subcirc0.u(pi/2,-0.590000,0.810000, qreg_0[1])
subcirc0.u(pi/2,0.212000,-0.050000, qreg_3[0])
subcirc0.ry(-0.675000, qreg_3[0])
subcirc0.u(pi/2,0.759000,0.476000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.295000,0.845000, qreg_0[2])
subcirc1.u(pi/2,0.448000,-0.010000, qreg_0[1])
subcirc1.ry(0.831000, qreg_0[1])
subcirc1.ry(-0.551000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.752000,-0.601000, qreg_0[0])
subcirc2.x(qreg_3[0])
subcirc2.ry(-0.432000, qreg_2[0])
subcirc2.ry(-0.461000, qreg_2[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.ry(-0.633000, qreg_0[1])
main_circ.u(param_0,param_2,param_0, qreg_0[1])
main_circ.y(qreg_0[1])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_3[0],1])
main_circ.append(subcirc1,[qreg_3[0],qreg_2[0],1,0])
main_circ.u(pi/2,0.231000,0.673000, 0)
main_circ.append(subcirc0,[qreg_0[0],1,qreg_3[0],qreg_0[1]])
main_circ.u(pi/2,0.520000,-0.595000, qreg_2[0])
main_circ.append(subcirc1,[1,qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.y(qreg_0[0])
main_circ.append(subcirc2,[qreg_3[0],1,0,qreg_0[1]])
main_circ.y(qreg_0[1])
main_circ.ry(-0.260000, qreg_2[0])
main_circ.y(qreg_2[0])
main_circ.append(subcirc0,[qreg_0[1],1,qreg_3[0],qreg_0[0]])
main_circ.y(qreg_0[1])
main_circ.y(qreg_0[0])
main_circ.x(qreg_3[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],0,1])
main_circ.y(qreg_3[0])
main_circ.y(qreg_3[0])
main_circ.ry(0.771000, qreg_3[0])
main_circ.y(1)
bindings = {param_0: 0.777000, param_2: -0.997000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
