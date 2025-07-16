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
subcirc0.s(qreg_1[0])
subcirc0.h(qreg_2[1])
subcirc0.u(pi/2,0.489000,0.642000, qreg_1[0])
subcirc0.s(qreg_2[1])
subcirc0.u(0,0,0.740000, qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.u(pi/2,-0.418000,0.583000, qreg_0[0])
subcirc1.u(pi/2,-0.793000,-0.768000, qreg_3[0])
subcirc1.s(qreg_0[0])
subcirc1.u(pi/2,-0.847000,-0.281000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.774000, qreg_3[0])
subcirc2.u(pi/2,-0.978000,0.709000, qreg_3[0])
subcirc2.s(qreg_0[0])
subcirc2.u(0,0,0.498000, qreg_0[1])
subcirc2.u(0,0,-0.045000, qreg_2[0])

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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[3,2,qreg_0[1],qreg_0[0],1,0])
main_circ.u(param_2,-0.517000,param_1, 2)
main_circ.s(qreg_0[0])
main_circ.h(3)
main_circ.append(subcirc1,[0,qreg_0[0],1,2,qreg_0[1],3])
main_circ.append(subcirc1,[1,0,qreg_0[0],qreg_0[1],2,3])
main_circ.append(subcirc0,[0,2,1,qreg_0[0]])
main_circ.u(pi/2,param_1,-0.393000, 0)
main_circ.s(3)
main_circ.append(subcirc1,[qreg_0[0],3,2,1,qreg_0[1],0])
main_circ.s(0)
main_circ.append(subcirc2,[qreg_0[0],2,3,qreg_0[1]])
main_circ.u(0,0,param_0, 3)
main_circ.h(qreg_0[1])
main_circ.h(qreg_0[1])
main_circ.s(2)
main_circ.h(3)
bindings = {param_0: 0.983000, param_1: -0.474000, param_2: -0.703000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
