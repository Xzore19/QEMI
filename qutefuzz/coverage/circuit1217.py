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
subcirc0.rz(-0.626000, qreg_0[1])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.rz(-0.182000, qreg_3[0])
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.u(pi/2,-0.924000,-0.652000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_1[1])
subcirc1.cz(qreg_0[0],qreg_1[0])
subcirc1.u(pi/2,0.791000,-0.859000, qreg_3[0])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
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

main_circ.cz(qreg_1[0],3)
main_circ.rz(-0.558000, 0)
main_circ.x(0)
main_circ.append(subcirc1,[0,1,qreg_0[0],2])
main_circ.x(1)
main_circ.u(pi/2,param_2,0.282000, 2)
main_circ.append(subcirc1,[3,0,2,qreg_0[0]])
main_circ.append(subcirc1,[3,qreg_1[0],qreg_0[0],0])
main_circ.cz(2,1)
main_circ.u(param_0,param_2,0.937000, qreg_1[0])
main_circ.u(pi/2,-0.959000,param_2, 2)
main_circ.x(qreg_0[0])
main_circ.rz(-0.736000, qreg_0[0])
main_circ.u(param_2,0.431000,param_1, 2)
main_circ.x(qreg_1[0])
main_circ.x(3)
main_circ.append(subcirc1,[0,qreg_1[0],1,qreg_0[0]])
main_circ.cz(3,2)
main_circ.cz(qreg_1[0],2)
main_circ.cz(2,0)
main_circ.cz(2,qreg_1[0])
main_circ.cz(1,2)
main_circ.cz(2,qreg_0[0])
main_circ.x(2)
main_circ.x(0)
main_circ.rz(-0.580000, 0)
main_circ.x(1)
main_circ.rz(0.510000, qreg_0[0])
main_circ.rz(0.037000, qreg_0[0])
main_circ.rz(param_0, 0)
bindings = {param_0: -0.042000, param_1: -0.239000, param_2: 0.660000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesSimpleCommutation")
