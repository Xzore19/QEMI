from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(0.371000,0.761000,0.575000, qreg_2[0])
subcirc0.u(pi/2,-0.266000,0.920000, qreg_0[1])
subcirc0.s(qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.485000,0.259000, qreg_0[0])
subcirc1.s(qreg_0[0])
subcirc1.s(qreg_2[0])
subcirc1.u(-0.552000,0.780000,-0.588000, qreg_1[0])
subcirc1.s(qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.u(pi/2,-0.077000,-0.240000, qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.u(0.678000,-0.716000,-0.259000, qreg_2[0])
subcirc2.u(0.833000,-0.859000,-0.782000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.721000,0.871000,-0.229000, qreg_0[1])
subcirc3.u(0.954000,0.919000,0.854000, qreg_3[0])
subcirc3.z(qreg_0[2])
subcirc3.z(qreg_3[0])
subcirc3.u(pi/2,0.640000,0.335000, qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.z(qreg_0[2])
subcirc4.z(qreg_0[1])
subcirc4.z(qreg_0[0])
subcirc4.u(-0.001000,0.595000,0.656000, qreg_0[1])
subcirc4.s(qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(qreg_3[0])
main_circ.u(param_0,0.830000,param_0, qreg_0[0])
main_circ.u(param_0,param_0,param_0, qreg_0[2])
main_circ.z(qreg_3[0])
main_circ.z(qreg_3[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.u(param_1,param_0,param_2, qreg_0[1])
main_circ.z(qreg_3[0])
main_circ.z(qreg_3[0])
main_circ.u(param_2,param_2,param_2, qreg_0[1])
main_circ.z(qreg_0[1])
main_circ.append(subcirc3,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.u(-0.407000,param_2,param_0, qreg_0[1])
main_circ.u(param_0,-0.925000,param_0, qreg_0[2])
main_circ.u(pi/2,0.938000,param_1, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.z(qreg_0[2])
main_circ.z(qreg_3[0])
main_circ.u(param_0,param_2,param_0, qreg_0[2])
main_circ.u(pi/2,0.291000,0.693000, qreg_0[1])
main_circ.z(qreg_0[2])
main_circ.u(param_2,-0.014000,0.520000, qreg_0[2])
main_circ.z(qreg_0[1])
bindings = {param_0: 0.424000, param_1: -0.279000, param_2: 0.932000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
