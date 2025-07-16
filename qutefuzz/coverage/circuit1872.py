from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.ry(0.644000, qreg_0[0])
subcirc0.ry(-0.822000, qreg_0[2])
subcirc0.ry(-0.432000, qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0.s(qreg_0[3])
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
subcirc1.z(qreg_1[0])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.s(qreg_1[0])
subcirc1.z(qreg_2[1])
subcirc1.z(qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_3[0])
subcirc2.z(qreg_0[1])
subcirc2.s(qreg_3[0])
subcirc2.u(pi/2,-0.763000,-0.981000, qreg_0[0])
subcirc2.u(pi/2,-0.653000,0.297000, qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.u(pi/2,param_0,param_0, qreg_2[1])
main_circ.append(subcirc1,[qreg_2[0],qreg_2[1],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_2[1],0])
main_circ.z(qreg_2[0])
main_circ.s(qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.s(0)
main_circ.z(0)
main_circ.append(subcirc1,[qreg_2[1],qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.u(param_1,0.069000,param_0, 0)
main_circ.append(subcirc1,[qreg_2[1],0,qreg_0[0],qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[1],qreg_0[1],qreg_2[0]])
main_circ.z(qreg_2[1])
main_circ.u(pi/2,0.296000,param_2, qreg_0[0])
main_circ.u(pi/2,0.171000,-0.529000, qreg_2[0])
main_circ.append(subcirc1,[qreg_2[1],0,qreg_2[0],qreg_0[1]])
main_circ.u(pi/2,0.838000,0.547000, 0)
main_circ.u(pi/2,-0.153000,-0.271000, qreg_2[1])
main_circ.u(param_2,param_0,0.477000, qreg_2[0])
bindings = {param_0: 0.233000, param_1: -0.786000, param_2: 0.824000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "InverseCancellation")
