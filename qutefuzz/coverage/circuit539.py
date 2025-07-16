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
subcirc0.y(qreg_0[2])
subcirc0.u(pi/2,-0.397000,-0.658000, qreg_0[2])
subcirc0.y(qreg_0[1])
subcirc0.u(pi/2,-0.613000,-0.899000, qreg_0[0])
subcirc0.y(qreg_0[2])
subcirc0.rz(-0.659000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_1[0])
subcirc1.u(0,0,-0.744000, qreg_1[1])
subcirc1.y(qreg_1[0])
subcirc1.rz(0.009000, qreg_3[0])
subcirc1.rz(0.723000, qreg_0[0])
subcirc1.u(pi/2,-0.797000,0.320000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_1[0])
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_1[0])
subcirc2.y(qreg_1[0])
subcirc2.u(pi/2,0.317000,0.704000, qreg_0[0])
subcirc2.y(qreg_1[0])

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

main_circ.y(3)
main_circ.append(subcirc2,[1,2,3,0])
main_circ.append(subcirc0,[3,1,qreg_0[1],qreg_0[0],0])
main_circ.u(param_0,param_3,param_1, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],2,3,0])
main_circ.append(subcirc0,[qreg_0[1],3,qreg_0[0],0,2])
main_circ.u(pi/2,-0.740000,-0.386000, 2)
main_circ.rz(0.040000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[1],3,0,qreg_0[0],1])
main_circ.u(0,0,0.707000, qreg_0[1])
main_circ.append(subcirc0,[0,qreg_0[1],3,2,1])
main_circ.rz(-0.817000, qreg_0[1])
main_circ.u(pi/2,0.168000,param_1, qreg_0[1])
main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[0],3])
main_circ.y(0)
main_circ.y(qreg_0[1])
main_circ.y(qreg_0[1])
main_circ.u(param_0,-0.563000,param_3, 2)
main_circ.u(pi/2,-0.552000,param_3, 1)
main_circ.rz(0.064000, 2)
bindings = {param_0: -0.792000, param_1: -0.150000, param_3: 0.510000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
