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
subcirc0.ry(-0.414000, qreg_0[0])
subcirc0.x(qreg_3[0])
subcirc0.ry(-0.035000, qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0.ry(-0.885000, qreg_0[2])
subcirc0.ry(0.061000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.372000, qreg_0[1])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,-0.228000, qreg_0[2])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.ry(-0.688000, qreg_2[0])
subcirc2.ry(-0.156000, qreg_3[0])
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.u(param_2,0,param_1, qreg_1[0])
main_circ.append(subcirc1,[qreg_1[2],qreg_1[0],qreg_1[1],qreg_0[0]])
main_circ.z(qreg_1[0])
main_circ.ry(0.403000, qreg_0[0])
main_circ.append(subcirc1,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.u(param_2,param_0,param_1, qreg_0[0])
main_circ.x(qreg_1[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[2],qreg_1[1],qreg_1[0]])
main_circ.u(param_3,0,-0.116000, qreg_1[1])
main_circ.z(qreg_1[2])
main_circ.x(qreg_0[0])
main_circ.ry(param_0, qreg_1[1])
main_circ.u(param_4,0,param_4, qreg_1[1])
main_circ.ry(-0.382000, qreg_1[1])
main_circ.u(0,0,0.493000, qreg_1[0])
main_circ.ry(param_3, qreg_0[0])
main_circ.ry(0.269000, qreg_1[1])
main_circ.ry(param_4, qreg_1[2])
main_circ.u(param_2,param_3,param_1, qreg_1[2])
main_circ.ry(0.887000, qreg_1[0])
main_circ.x(qreg_0[0])
main_circ.ry(param_0, qreg_1[1])
main_circ.z(qreg_0[0])
main_circ.ry(param_1, qreg_0[0])
main_circ.z(qreg_1[2])
bindings = {param_0: -0.127000, param_1: 0.665000, param_2: 0.145000, param_3: 0.242000, param_4: -0.181000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
