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
subcirc0.x(qreg_3[0])
subcirc0.ry(0.676000, qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.x(qreg_0[1])
subcirc0.x(qreg_3[0])
subcirc0.ry(-0.803000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.116000, qreg_0[0])
subcirc1.ry(0.009000, qreg_0[0])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_3[0])
subcirc1.ry(-0.042000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.339000, qreg_3[0])
subcirc2.u(0,0,-0.656000, qreg_0[1])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.x(qreg_0[1])
subcirc2.u(0,0,-0.144000, qreg_0[2])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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

main_circ.append(subcirc0,[0,qreg_3[0],qreg_1[0],1,qreg_0[0]])
main_circ.ry(param_3, qreg_1[1])
main_circ.append(subcirc1,[0,1,qreg_3[0],qreg_1[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_1[1],qreg_1[0],0])
main_circ.append(subcirc1,[qreg_1[1],qreg_3[0],qreg_1[0],0])
main_circ.u(param_4,param_4,param_2, 1)
main_circ.cz(0,qreg_1[0])
main_circ.cz(qreg_0[0],1)
main_circ.ry(0.658000, 1)
main_circ.x(0)
main_circ.x(qreg_1[0])
main_circ.append(subcirc2,[0,1,qreg_3[0],qreg_1[1]])
main_circ.u(param_4,0,param_3, qreg_1[0])
main_circ.cz(1,0)
main_circ.cz(qreg_3[0],qreg_1[0])
main_circ.cz(1,0)
main_circ.cz(qreg_0[0],1)
main_circ.cz(qreg_1[1],qreg_0[0])
main_circ.cz(qreg_1[0],1)
main_circ.cz(qreg_0[0],1)
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cz(qreg_3[0],0)
main_circ.cz(qreg_1[1],qreg_3[0])
main_circ.cz(qreg_1[1],qreg_3[0])
main_circ.cz(0,1)
main_circ.cz(qreg_3[0],qreg_1[1])
main_circ.cz(qreg_3[0],1)
main_circ.x(qreg_1[0])
main_circ.x(qreg_1[1])
main_circ.ry(-0.424000, qreg_1[1])
bindings = {param_2: -0.253000, param_3: -0.453000, param_4: 0.344000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
