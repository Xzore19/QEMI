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
subcirc0.s(qreg_0[0])
subcirc0.rz(0.404000, qreg_2[0])
subcirc0.s(qreg_0[1])
subcirc0.u(pi/2,0.415000,-0.772000, qreg_0[0])
subcirc0.rz(-0.140000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[3])
subcirc1.s(qreg_0[0])
subcirc1.rz(0.200000, qreg_0[1])
subcirc1.u(pi/2,-0.258000,-0.165000, qreg_0[2])
subcirc1.s(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_2[0])
subcirc2.x(qreg_0[0])
subcirc2.rz(-0.457000, qreg_3[0])
subcirc2.rz(0.976000, qreg_3[0])
subcirc2.rz(0.448000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.453000, qreg_0[0])
subcirc3.s(qreg_2[0])
subcirc3.u(pi/2,0.318000,0.481000, qreg_0[1])
subcirc3.rz(-0.063000, qreg_0[1])
subcirc3.x(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.x(1)
main_circ.append(subcirc1,[qreg_0[0],0,2,3])
main_circ.rz(0.792000, qreg_0[1])
main_circ.x(qreg_0[0])
main_circ.append(subcirc3,[qreg_0[0],3,2,0,1,qreg_0[1]])
main_circ.append(subcirc2,[0,2,qreg_0[1],1,3])
main_circ.append(subcirc2,[1,qreg_0[1],0,qreg_0[0],3])
main_circ.append(subcirc2,[3,qreg_0[0],2,0,qreg_0[1]])
main_circ.u(pi/2,0.206000,param_1, 2)
main_circ.append(subcirc1,[0,1,3,qreg_0[0]])
main_circ.append(subcirc2,[1,qreg_0[1],2,qreg_0[0],3])
main_circ.u(param_1,-0.762000,0.068000, 2)
main_circ.append(subcirc3,[1,3,0,2,qreg_0[1],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],0,1,qreg_0[1],2])
main_circ.append(subcirc1,[1,qreg_0[1],3,0])
main_circ.u(pi/2,param_2,param_2, qreg_0[1])
bindings = {param_1: -0.603000, param_2: 0.229000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
