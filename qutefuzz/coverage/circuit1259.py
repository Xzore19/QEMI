from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.ry(-0.641000, qreg_1[0])
subcirc0.ry(0.755000, qreg_1[1])
subcirc0.u(pi/2,-0.060000,-0.071000, qreg_1[0])
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0.cz(qreg_0[0],qreg_1[1])
subcirc0.cz(qreg_0[0],qreg_1[2])
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
subcirc1.u(pi/2,-0.403000,-0.632000, qreg_3[0])
subcirc1.cz(qreg_2[0],qreg_0[0])
subcirc1.cy(qreg_3[0],qreg_0[0])
subcirc1.ry(-0.156000, qreg_0[1])
subcirc1.u(pi/2,0.676000,-0.279000, qreg_3[0])
subcirc1.cy(qreg_3[0],qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_1[1],qreg_0[0])
subcirc2.cy(qreg_1[1],qreg_3[0])
subcirc2.cz(qreg_1[1],qreg_3[0])
subcirc2.ry(-0.728000, qreg_1[0])
subcirc2.cy(qreg_1[1],qreg_0[0])
subcirc2.ry(0.425000, qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.ry(0.015000, qreg_0[1])
subcirc3.cz(qreg_2[0],qreg_0[1])
subcirc3.ry(0.125000, qreg_0[0])
subcirc3.cy(qreg_2[1],qreg_0[0])
subcirc3.ry(-0.593000, qreg_0[0])
subcirc3.ry(0.224000, qreg_2[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.append(subcirc2,[2,qreg_1[0],0,3])
main_circ.cy(qreg_0[0],1)
main_circ.cz(3,qreg_0[0])
main_circ.cy(3,1)
main_circ.append(subcirc2,[1,0,2,qreg_1[0]])
main_circ.append(subcirc1,[qreg_1[0],3,0,2,1,qreg_0[0]])
main_circ.append(subcirc3,[2,1,qreg_1[0],qreg_0[0]])
main_circ.append(subcirc1,[0,2,1,qreg_1[0],3,qreg_0[0]])
main_circ.cy(1,qreg_1[0])
main_circ.cz(0,3)
main_circ.append(subcirc3,[0,qreg_0[0],1,qreg_1[0]])
main_circ.ry(0.968000, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],1,qreg_1[0],0])
main_circ.append(subcirc3,[2,1,qreg_1[0],qreg_0[0]])
main_circ.append(subcirc2,[2,0,3,qreg_0[0]])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
