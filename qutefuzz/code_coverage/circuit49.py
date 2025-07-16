from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.988000,0.883000, qreg_1[0])
subcirc0.cx(qreg_0[0],qreg_3[0])
subcirc0.u(pi/2,-0.187000,0.238000, qreg_1[0])
subcirc0.u(pi/2,-0.284000,-0.559000, qreg_3[0])
subcirc0.cx(qreg_0[0],qreg_1[0])
subcirc0.cx(qreg_0[0],qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_2[1])
subcirc1.u(pi/2,-0.431000,-0.042000, qreg_2[0])
subcirc1.ry(0.169000, qreg_2[1])
subcirc1.ry(-0.582000, qreg_0[0])
subcirc1.u(0.402000,-0.925000,-0.071000, qreg_2[0])
subcirc1.cx(qreg_2[1],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.100000, qreg_0[2])
subcirc2.ry(-0.799000, qreg_0[2])
subcirc2.u(-0.114000,0.978000,-0.533000, qreg_0[2])
subcirc2.u(0.064000,0.553000,-0.924000, qreg_3[0])
subcirc2.u(-0.274000,0.718000,-0.388000, qreg_0[2])
subcirc2.cx(qreg_3[0],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cx(qreg_1[0],qreg_2[0])
subcirc3.ry(0.209000, qreg_0[0])
subcirc3.ry(-0.400000, qreg_0[0])
subcirc3.ry(-0.633000, qreg_0[0])
subcirc3.u(-0.531000,0.195000,-0.787000, qreg_0[0])
subcirc3.cx(qreg_1[0],qreg_2[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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
param_3 = Parameter("param_3")

main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[0],0)
main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_3[0],1])
main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.u(param_2,0.572000,param_0, 1)
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.ry(param_0, 1)
main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],qreg_3[0],0,1,qreg_0[1]])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.u(param_1,param_3,-0.803000, qreg_0[1])
main_circ.ry(0.042000, qreg_0[0])
main_circ.cx(qreg_0[1],0)
main_circ.u(param_3,param_1,param_2, 0)
main_circ.u(param_2,param_3,0.605000, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[2],0])
main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.append(subcirc1,[qreg_0[0],1,qreg_3[0],qreg_0[1]])
main_circ.u(pi/2,-0.544000,param_1, 0)
main_circ.u(-0.703000,param_2,0.661000, qreg_0[0])
main_circ.u(0.746000,-0.753000,param_1, qreg_3[0])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.cx(0,qreg_0[1])
bindings = {param_0: -0.567000, param_1: 0.289000, param_2: 0.370000, param_3: -0.097000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
