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
subcirc0.rz(0.818000, qreg_0[0])
subcirc0.ry(0.708000, qreg_1[0])
subcirc0.cz(qreg_1[1],qreg_3[0])
subcirc0.cz(qreg_1[1],qreg_0[0])
subcirc0.ry(0.653000, qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.658000, qreg_0[1])
subcirc1.ry(-0.722000, qreg_0[0])
subcirc1.u(pi/2,-0.289000,-0.502000, qreg_3[0])
subcirc1.cz(qreg_0[1],qreg_3[0])
subcirc1.ry(-0.243000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_3[0],qreg_2[0])
subcirc2.cz(qreg_2[0],qreg_0[0])
subcirc2.cz(qreg_0[0],qreg_0[1])
subcirc2.rz(-0.955000, qreg_2[0])
subcirc2.ry(-0.581000, qreg_0[1])

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

main_circ.append(subcirc0,[qreg_1[1],qreg_1[2],qreg_0[0],qreg_1[0]])
main_circ.cz(qreg_0[0],qreg_1[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_1[1],qreg_1[0],qreg_1[2]])
main_circ.ry(0.163000, qreg_1[0])
main_circ.ry(param_0, qreg_1[2])
main_circ.u(param_1,param_0,param_2, qreg_1[1])
main_circ.u(param_2,-0.166000,param_0, qreg_1[1])
main_circ.append(subcirc1,[qreg_1[0],qreg_1[2],qreg_1[1],qreg_0[0]])
main_circ.append(subcirc2,[qreg_1[0],qreg_1[1],qreg_1[2],qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[1],qreg_1[2],qreg_1[0]])
main_circ.rz(param_1, qreg_0[0])
main_circ.cz(qreg_1[2],qreg_1[0])
main_circ.cz(qreg_1[0],qreg_1[2])
main_circ.cz(qreg_1[2],qreg_1[1])
main_circ.append(subcirc1,[qreg_1[0],qreg_1[1],qreg_0[0],qreg_1[2]])
main_circ.cz(qreg_1[2],qreg_1[0])
main_circ.rz(param_2, qreg_0[0])
main_circ.rz(-0.890000, qreg_1[0])
main_circ.cz(qreg_1[1],qreg_1[2])
main_circ.u(pi/2,-0.829000,param_0, qreg_0[0])
main_circ.append(subcirc0,[qreg_1[2],qreg_0[0],qreg_1[0],qreg_1[1]])
main_circ.rz(-0.413000, qreg_0[0])
main_circ.cz(qreg_1[1],qreg_1[0])
main_circ.rz(-0.863000, qreg_0[0])
main_circ.rz(param_1, qreg_1[1])
bindings = {param_0: 0.477000, param_1: -0.383000, param_2: -0.832000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1570")
