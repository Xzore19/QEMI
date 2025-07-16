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
subcirc0.u(-0.320000,-0.922000,0.253000, qreg_2[0])
subcirc0.cz(qreg_2[0],qreg_0[1])
subcirc0.u(-0.329000,0.593000,0.337000, qreg_3[0])
subcirc0.h(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.u(-0.407000,-0.359000,-0.351000, qreg_3[0])
subcirc1.u(0.375000,-0.477000,-0.010000, qreg_0[0])
subcirc1.h(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_0[2],qreg_3[0])
subcirc2.u(0.459000,0.025000,-0.176000, qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_3[0])
subcirc2.u(0.501000,0.628000,0.567000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.197000,0.165000, qreg_3[0])
subcirc3.h(qreg_0[1])
subcirc3.h(qreg_3[0])
subcirc3.h(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0.180000,-0.592000,-0.833000, qreg_3[0])
subcirc4.u(pi/2,-0.648000,-0.622000, qreg_1[0])
subcirc4.cz(qreg_1[0],qreg_0[0])
subcirc4.cz(qreg_3[0],qreg_1[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.append(subcirc2,[0,qreg_3[0],qreg_1[0],qreg_1[1]])
main_circ.u(param_2,0.575000,-0.801000, qreg_0[0])
main_circ.u(param_2,0.094000,-0.449000, qreg_1[1])
main_circ.append(subcirc1,[qreg_1[0],qreg_1[1],qreg_0[0],qreg_3[0]])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_3[0],qreg_1[1]])
main_circ.h(qreg_1[0])
main_circ.append(subcirc1,[qreg_3[0],0,qreg_0[0],qreg_1[0]])
main_circ.h(qreg_3[0])
main_circ.append(subcirc2,[qreg_1[0],0,qreg_0[0],qreg_1[1]])
main_circ.h(qreg_1[1])
main_circ.u(param_0,param_1,-0.298000, 0)
main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],0,qreg_1[1]])
main_circ.h(qreg_0[0])
main_circ.append(subcirc2,[0,qreg_1[0],qreg_1[1],qreg_3[0]])
main_circ.u(pi/2,param_0,0.159000, qreg_3[0])
main_circ.append(subcirc1,[qreg_1[1],qreg_1[0],qreg_3[0],qreg_0[0]])
main_circ.cz(qreg_3[0],qreg_1[1])
main_circ.cz(0,qreg_3[0])
main_circ.cz(qreg_1[1],qreg_0[0])
main_circ.cz(0,qreg_0[0])
main_circ.cz(qreg_3[0],0)
main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.append(subcirc2,[qreg_1[0],qreg_3[0],qreg_0[0],0])
main_circ.u(-0.547000,0.771000,0.030000, 0)
main_circ.u(-0.602000,-0.324000,param_2, qreg_3[0])
main_circ.cz(0,qreg_1[1])
main_circ.h(qreg_0[0])
bindings = {param_0: -0.198000, param_1: -0.472000, param_2: -0.961000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGates")
