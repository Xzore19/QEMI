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
subcirc0.s(qreg_3[0])
subcirc0.u(0,0,0.224000, qreg_0[0])
subcirc0.s(qreg_2[0])
subcirc0.u(0.372000,-0.925000,-0.670000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.618000, qreg_0[0])
subcirc1.u(0,0,-0.004000, qreg_2[0])
subcirc1.u(-0.967000,-0.342000,-0.094000, qreg_0[0])
subcirc1.u(0.737000,-0.390000,-0.724000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_0[1])
subcirc2.z(qreg_3[0])
subcirc2.z(qreg_0[2])
subcirc2.u(0.569000,-0.149000,0.821000, qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.z(qreg_0[1])
subcirc3.z(qreg_0[0])
subcirc3.u(0,0,0.716000, qreg_0[1])
subcirc3.u(0,0,0.554000, qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0.550000,0.026000,0.672000, qreg_0[0])
subcirc4.u(-0.715000,0.055000,0.139000, qreg_0[1])
subcirc4.z(qreg_0[0])
subcirc4.u(-0.624000,-0.473000,-0.422000, qreg_2[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(0.417000,0.363000,-0.978000, qreg_0[0])
main_circ.append(subcirc2,[qreg_2[1],qreg_2[0],qreg_0[0],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],0,qreg_2[1]])
main_circ.z(qreg_2[1])
main_circ.u(param_2,0.060000,0.003000, qreg_2[0])
main_circ.z(qreg_0[0])
main_circ.u(0.693000,0.391000,param_1, 0)
main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],qreg_2[0]])
main_circ.append(subcirc3,[qreg_0[0],qreg_2[0],0,qreg_2[1]])
main_circ.u(0.924000,param_0,-0.682000, qreg_0[1])
main_circ.append(subcirc3,[qreg_2[1],0,qreg_0[0],qreg_0[1]])
main_circ.s(qreg_2[1])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
main_circ.append(subcirc2,[0,qreg_2[0],qreg_0[0],qreg_0[1]])
main_circ.u(0.379000,-0.131000,param_2, qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[0,qreg_2[0],qreg_2[1],qreg_0[0]])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_2[1],0])
main_circ.z(qreg_2[1])
main_circ.append(subcirc3,[qreg_2[0],0,qreg_2[1],qreg_0[1]])
main_circ.s(0)
main_circ.u(param_2,param_2,0.326000, qreg_0[1])
main_circ.z(qreg_0[1])
bindings = {param_0: 0.019000, param_1: 0.831000, param_2: -0.946000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
