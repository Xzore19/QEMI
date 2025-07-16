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
subcirc0.cx(qreg_0[0],qreg_0[2])
subcirc0.u(0,0,0.129000, qreg_0[1])
subcirc0.u(0,0,-0.818000, qreg_0[2])
subcirc0.u(0,0,-0.279000, qreg_0[0])
subcirc0.u(0,0,-0.491000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.u(0,0,0.566000, qreg_0[2])
subcirc1.x(qreg_0[2])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.u(param_1,0,-0.112000, 1)
main_circ.cx(qreg_1[0],qreg_2[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.u(0,0,0.381000, 0)
main_circ.u(0,param_1,param_0, qreg_3[0])
main_circ.rz(-0.175000, qreg_3[0])
main_circ.cx(qreg_3[0],1)
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],0,1])
main_circ.rz(param_2, qreg_2[0])
main_circ.x(1)
main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],1,qreg_0[0]])
main_circ.rz(param_1, qreg_2[0])
main_circ.append(subcirc0,[0,qreg_3[0],qreg_1[0],qreg_2[0]])
main_circ.rz(param_4, 0)
main_circ.cx(1,qreg_0[0])
main_circ.x(0)
main_circ.x(qreg_0[0])
main_circ.append(subcirc0,[qreg_2[0],1,qreg_3[0],0])
main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.cx(qreg_1[0],qreg_3[0])
main_circ.cx(0,qreg_2[0])
main_circ.cx(qreg_0[0],1)
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.u(param_0,param_4,0.878000, qreg_3[0])
main_circ.x(qreg_0[0])
main_circ.rz(-0.256000, 1)
main_circ.x(0)
main_circ.x(qreg_3[0])
bindings = {param_0: -0.060000, param_1: -0.169000, param_2: 0.508000, param_4: 0.510000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesDecomposition")
