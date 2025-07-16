from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cy(qreg_2[0],qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_1[0])
subcirc0.u(-0.276000,-0.814000,-0.763000, qreg_0[0])
subcirc0.cy(qreg_1[0],qreg_0[0])
subcirc0.cy(qreg_2[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.cy(qreg_0[3],qreg_0[0])
subcirc1.u(-0.344000,0.255000,-0.490000, qreg_0[3])
subcirc1.cx(qreg_0[3],qreg_0[0])
subcirc1.u(-0.929000,-0.337000,-0.645000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.102000,-0.519000,0.633000, qreg_0[1])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.rz(0.979000, qreg_0[3])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

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

main_circ.cy(2,qreg_0[0])
main_circ.u(param_0,0.770000,-0.217000, qreg_1[0])
main_circ.cy(1,qreg_0[0])
main_circ.u(-0.306000,param_1,0.133000, qreg_0[0])
main_circ.cx(qreg_0[0],0)
main_circ.append(subcirc1,[2,3,0,qreg_0[0]])
main_circ.append(subcirc1,[3,0,qreg_0[0],1])
main_circ.cy(qreg_1[0],2)
main_circ.rz(0.593000, 1)
main_circ.u(param_2,param_0,param_0, 3)
main_circ.append(subcirc1,[qreg_0[0],0,3,1])
main_circ.append(subcirc1,[1,2,qreg_1[0],3])
main_circ.cy(qreg_1[0],1)
main_circ.u(-0.994000,param_1,-0.556000, 0)
main_circ.rz(param_0, 0)
main_circ.cy(qreg_1[0],2)
main_circ.u(-0.196000,-0.827000,param_0, qreg_0[0])
main_circ.cx(qreg_1[0],1)
main_circ.cx(qreg_0[0],3)
main_circ.cy(qreg_1[0],0)
main_circ.rz(-0.038000, 0)
main_circ.cy(0,qreg_1[0])
main_circ.cy(qreg_1[0],3)
main_circ.rz(param_1, 2)
main_circ.cx(0,qreg_0[0])
main_circ.rz(param_2, 3)
main_circ.cy(1,2)
main_circ.rz(-0.351000, 0)
main_circ.rz(-0.822000, 3)
main_circ.rz(param_2, 3)
main_circ.u(param_1,param_2,-0.941000, 1)
main_circ.rz(param_1, 1)
main_circ.append(subcirc1,[1,0,qreg_1[0],2])
main_circ.cx(3,qreg_0[0])
main_circ.cx(qreg_1[0],0)
bindings = {param_0: 0.337000, param_1: -0.433000, param_2: -0.654000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutationAnalysis")
