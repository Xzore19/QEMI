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
subcirc0.u(pi/2,0.577000,-0.088000, qreg_0[0])
subcirc0.u(pi/2,-0.764000,-0.740000, qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.cx(qreg_0[2],qreg_0[1])
subcirc0.u(pi/2,0.850000,0.678000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_3[0])
subcirc1.s(qreg_0[1])
subcirc1.s(qreg_3[0])
subcirc1.s(qreg_0[0])
subcirc1.s(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(3)
main_circ.cx(qreg_1[0],3)
main_circ.u(pi/2,param_0,-0.998000, 2)
main_circ.s(qreg_1[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.u(param_0,0.411000,0.548000, 1)
main_circ.u(pi/2,param_0,param_0, 3)
main_circ.cx(2,qreg_1[0])
main_circ.z(qreg_0[0])
main_circ.s(0)
main_circ.u(param_1,param_2,-0.006000, 1)
main_circ.cx(1,0)
main_circ.cx(3,1)
main_circ.append(subcirc0,[1,qreg_0[0],3,qreg_1[0],0,2])
main_circ.cx(0,qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[0,qreg_1[0],2,3,qreg_0[0],1])
main_circ.s(0)
main_circ.append(subcirc0,[3,1,qreg_1[0],qreg_0[0],2,0])
main_circ.s(qreg_0[0])
main_circ.cx(2,1)
main_circ.u(param_1,0.930000,0.651000, 2)
main_circ.s(2)
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],0,3,2,1])
main_circ.u(pi/2,-0.281000,0.563000, 1)
main_circ.cx(1,3)
main_circ.cx(qreg_1[0],0)
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.cx(3,qreg_1[0])
main_circ.cx(3,0)
main_circ.cx(1,2)
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[0,1,qreg_0[0],3,qreg_1[0],2])
main_circ.append(subcirc0,[2,0,3,qreg_0[0],qreg_1[0],1])
bindings = {param_0: 0.742000, param_1: -0.207000, param_2: 0.834000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
