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
subcirc0.s(qreg_0[0])
subcirc0.u(0,0,-0.011000, qreg_3[0])
subcirc0.s(qreg_0[2])
subcirc0.s(qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.844000, qreg_0[0])
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_3[0])
subcirc1.s(qreg_0[0])
subcirc1.u(0.243000,-0.807000,0.912000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.722000, qreg_0[1])
subcirc2.s(qreg_0[1])
subcirc2.u(0,0,-0.598000, qreg_0[2])
subcirc2.cx(qreg_0[0],qreg_0[2])
subcirc2.u(0.503000,0.584000,-0.343000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_3[0],qreg_1[0])
subcirc3.cx(qreg_1[1],qreg_0[0])
subcirc3.cx(qreg_1[0],qreg_1[1])
subcirc3.u(0,0,-0.477000, qreg_3[0])
subcirc3.s(qreg_1[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.s(qreg_0[1])
subcirc4.u(0,0,-0.317000, qreg_0[0])
subcirc4.u(0.113000,0.570000,0.897000, qreg_0[1])
subcirc4.u(0,0,-0.548000, qreg_0[2])
subcirc4.u(-0.329000,0.183000,-0.320000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.s(0)
main_circ.cx(1,2)
main_circ.append(subcirc0,[0,1,3,qreg_0[0],2])
main_circ.append(subcirc4,[2,3,qreg_0[0],1])
main_circ.cx(0,2)
main_circ.append(subcirc3,[1,3,2,0])
main_circ.append(subcirc3,[3,1,0,2])
main_circ.append(subcirc4,[3,qreg_0[0],2,0])
main_circ.append(subcirc2,[qreg_0[0],0,2,1])
main_circ.append(subcirc3,[1,qreg_0[0],2,0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(3,1)
main_circ.cx(qreg_0[0],2)
main_circ.append(subcirc3,[1,3,2,qreg_0[0]])
main_circ.s(2)
main_circ.u(0,0,-0.508000, qreg_0[0])
main_circ.u(param_3,param_1,param_4, 2)
main_circ.s(qreg_0[0])
bindings = {param_1: -0.628000, param_3: 0.666000, param_4: -0.056000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectLinearFunctions")
