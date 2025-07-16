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
subcirc0.rz(-0.273000, qreg_3[0])
subcirc0.z(qreg_0[0])
subcirc0.u(0.500000,-0.900000,-0.388000, qreg_0[2])
subcirc0.u(0.539000,-0.205000,-0.028000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.z(qreg_0[0])
subcirc1.u(-0.524000,-0.510000,-0.333000, qreg_3[0])
subcirc1.y(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_3[0])
subcirc2.rz(0.101000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(0.104000, qreg_0[2])
subcirc3.z(qreg_0[1])
subcirc3.rz(0.260000, qreg_0[2])
subcirc3.rz(-0.445000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc2,[qreg_1[2],qreg_1[0],qreg_0[0],qreg_1[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_1[0],qreg_1[2],qreg_1[1]])
main_circ.y(qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.append(subcirc2,[qreg_1[2],qreg_0[0],qreg_1[1],qreg_1[0]])
main_circ.y(qreg_1[2])
main_circ.rz(0.425000, qreg_0[0])
main_circ.append(subcirc1,[qreg_1[0],qreg_1[1],qreg_0[0],qreg_1[2]])
main_circ.append(subcirc2,[qreg_1[1],qreg_1[2],qreg_1[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_1[2]])
main_circ.append(subcirc1,[qreg_1[1],qreg_1[2],qreg_0[0],qreg_1[0]])
main_circ.y(qreg_1[1])
main_circ.append(subcirc2,[qreg_1[1],qreg_1[0],qreg_1[2],qreg_0[0]])
main_circ.u(0.573000,0.472000,-0.241000, qreg_1[1])
main_circ.append(subcirc2,[qreg_1[0],qreg_0[0],qreg_1[2],qreg_1[1]])
main_circ.y(qreg_0[0])
main_circ.y(qreg_1[0])
main_circ.y(qreg_1[1])
main_circ.u(-0.290000,-0.503000,-0.445000, qreg_1[0])
main_circ.z(qreg_1[0])
main_circ.y(qreg_1[2])
main_circ.y(qreg_0[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[2],qreg_1[1],qreg_0[0]])
main_circ.z(qreg_1[1])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
