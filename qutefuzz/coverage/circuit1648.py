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
subcirc0.z(qreg_3[0])
subcirc0.z(qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0.z(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.942000,-0.536000, qreg_2[0])
subcirc1.rz(0.767000, qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1.u(pi/2,0.870000,0.771000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.695000, qreg_3[0])
subcirc2.rz(0.938000, qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2.s(qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.s(2)
main_circ.u(pi/2,param_1,0.503000, 0)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.append(subcirc2,[3,1,2,0])
main_circ.rz(0.193000, 0)
main_circ.s(3)
main_circ.append(subcirc2,[1,0,3,2])
main_circ.s(3)
main_circ.rz(0.604000, 0)
main_circ.s(0)
main_circ.u(param_3,param_0,param_1, 3)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.z(2)
main_circ.z(3)
main_circ.rz(param_1, 2)
main_circ.append(subcirc2,[1,0,2,3])
main_circ.s(1)
main_circ.u(pi/2,param_2,0.425000, 2)
main_circ.rz(0.306000, 0)
main_circ.u(pi/2,-0.092000,0.282000, 0)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.z(1)
main_circ.u(pi/2,param_1,param_1, 1)
main_circ.u(param_2,0.829000,-0.700000, 1)
main_circ.u(pi/2,param_2,0.149000, 0)
main_circ.z(3)
main_circ.u(param_0,param_0,-0.259000, 2)
main_circ.u(param_2,-0.604000,0.736000, 1)
main_circ.u(pi/2,param_3,0.373000, 1)
main_circ.z(0)
bindings = {param_0: 0.220000, param_1: -0.200000, param_2: 0.455000, param_3: -0.692000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
