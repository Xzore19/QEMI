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
subcirc0.u(pi/2,0.194000,0.232000, qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_0[1])
subcirc0.ry(0.758000, qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.ry(-0.125000, qreg_0[0])
subcirc1.u(pi/2,-0.839000,-0.157000, qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1.u(0.041000,0.222000,-0.883000, qreg_3[0])
subcirc1.u(pi/2,0.314000,0.303000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(1)
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
param_5 = Parameter("param_5")

main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[0],0])
main_circ.u(0.908000,param_4,param_0, qreg_3[0])
main_circ.u(param_2,param_5,0.582000, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_3[0],0])
main_circ.ry(-0.721000, 0)
main_circ.u(param_4,-0.143000,0.598000, qreg_1[0])
main_circ.ry(0.537000, qreg_3[0])
main_circ.u(param_2,0.752000,param_2, qreg_1[0])
main_circ.ry(-0.053000, qreg_1[0])
main_circ.append(subcirc0,[qreg_1[0],0,qreg_2[0],qreg_0[0]])
main_circ.append(subcirc0,[qreg_2[0],qreg_1[0],qreg_0[0],qreg_3[0]])
main_circ.h(0)
main_circ.ry(param_4, qreg_3[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_1[0],qreg_0[0],0])
main_circ.ry(-0.203000, qreg_0[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],0,qreg_2[0]])
main_circ.u(param_1,param_1,-0.487000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_2[0],qreg_3[0]])
main_circ.u(pi/2,param_1,-0.865000, 0)
bindings = {param_0: -0.539000, param_1: -0.882000, param_2: -0.576000, param_4: 0.562000, param_5: 0.040000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CXCancellation")
