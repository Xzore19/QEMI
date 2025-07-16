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
subcirc0.rz(-0.906000, qreg_2[0])
subcirc0.u(0,0,-0.276000, qreg_0[0])
subcirc0.x(qreg_2[1])
subcirc0.u(pi/2,0.633000,-0.101000, qreg_2[1])
subcirc0.x(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.966000, qreg_1[0])
subcirc1.rz(-0.491000, qreg_1[0])
subcirc1.rz(0.091000, qreg_0[0])
subcirc1.rz(-0.803000, qreg_1[0])
subcirc1.u(pi/2,0.485000,-0.392000, qreg_1[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
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

main_circ.rz(param_2, qreg_1[1])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[2],qreg_1[0]])
main_circ.rz(param_3, qreg_1[0])
main_circ.u(param_0,param_1,param_0, qreg_1[2])
main_circ.append(subcirc1,[qreg_1[2],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.u(pi/2,-0.986000,param_2, qreg_1[1])
main_circ.append(subcirc1,[qreg_1[2],qreg_0[0],qreg_1[1],qreg_1[0]])
main_circ.rz(param_3, qreg_1[1])
main_circ.x(qreg_0[0])
main_circ.rz(-0.081000, qreg_1[2])
main_circ.append(subcirc0,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.u(param_3,param_2,param_2, qreg_1[2])
main_circ.append(subcirc0,[qreg_1[2],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.u(param_2,param_0,param_3, qreg_1[2])
main_circ.rz(-0.716000, qreg_1[2])
main_circ.x(qreg_1[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_1[2]])
main_circ.rz(0.933000, qreg_1[1])
main_circ.x(qreg_1[1])
main_circ.x(qreg_1[1])
main_circ.u(pi/2,0.610000,param_0, qreg_1[1])
main_circ.rz(param_0, qreg_0[0])
main_circ.u(param_2,0.379000,-0.606000, qreg_1[0])
main_circ.rz(-0.471000, qreg_0[0])
main_circ.x(qreg_1[0])
bindings = {param_0: -0.805000, param_1: 0.041000, param_2: 0.128000, param_3: -0.824000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
