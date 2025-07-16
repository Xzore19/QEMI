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
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.u(0,0,0.565000, qreg_0[0])
subcirc0.u(0,0,0.176000, qreg_0[1])
subcirc0.cx(qreg_0[2],qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.cx(qreg_2[0],qreg_2[1])
subcirc1.rz(-0.805000, qreg_2[1])
subcirc1.rz(0.959000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_0[0],qreg_3[0])
subcirc2.u(pi/2,0.992000,-0.889000, qreg_0[1])
subcirc2.u(0,0,0.685000, qreg_3[0])
subcirc2.cx(qreg_3[0],qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,-0.007000,0.586000, qreg_0[0])
subcirc3.u(pi/2,0.312000,0.500000, qreg_0[2])
subcirc3.u(0,0,0.663000, qreg_0[1])
subcirc3.rz(0.445000, qreg_0[1])

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

main_circ.cx(2,1)
main_circ.u(param_3,param_0,param_1, 2)
main_circ.cx(1,2)
main_circ.cx(2,1)
main_circ.rz(param_3, 0)
main_circ.append(subcirc2,[3,1,2,0])
main_circ.append(subcirc0,[0,3,2,1])
main_circ.u(param_3,0.482000,param_2, 2)
main_circ.u(param_3,param_3,param_2, 3)
main_circ.u(param_0,param_0,-0.409000, 2)
main_circ.cx(1,0)
main_circ.append(subcirc0,[0,2,3,1])
main_circ.cx(0,1)
main_circ.cx(3,2)
main_circ.rz(-0.296000, 3)
main_circ.append(subcirc2,[3,0,2,1])
main_circ.append(subcirc0,[1,0,3,2])
main_circ.rz(param_0, 2)
main_circ.u(0,0,0.220000, 0)
main_circ.u(pi/2,0.115000,param_3, 2)
main_circ.rz(0.361000, 2)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.rz(param_2, 2)
main_circ.cx(2,3)
main_circ.cx(0,2)
main_circ.rz(param_2, 0)
main_circ.append(subcirc0,[1,0,3,2])
bindings = {param_0: 0.905000, param_1: -0.304000, param_2: -0.044000, param_3: 0.567000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
