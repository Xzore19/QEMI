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
subcirc0.u(pi/2,-0.909000,-0.321000, qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[0])
subcirc0.u(pi/2,0.630000,-0.369000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.u(pi/2,0.017000,-0.657000, qreg_3[0])
subcirc1.y(qreg_0[0])
subcirc1.s(qreg_3[0])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[3])
subcirc2.s(qreg_0[2])
subcirc2.y(qreg_0[2])
subcirc2.s(qreg_0[0])
subcirc2.u(pi/2,0.809000,0.639000, qreg_0[0])
subcirc2.u(pi/2,-0.096000,-0.240000, qreg_0[1])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.u(param_0,-0.012000,-0.820000, qreg_2[1])
main_circ.append(subcirc2,[qreg_1[0],qreg_2[0],0,qreg_2[1]])
main_circ.append(subcirc0,[qreg_1[0],qreg_2[1],qreg_0[0],0])
main_circ.append(subcirc2,[qreg_2[1],qreg_2[0],qreg_0[0],qreg_1[0]])
main_circ.z(qreg_0[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_1[0]])
main_circ.z(qreg_2[1])
main_circ.y(qreg_1[0])
main_circ.y(qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.u(param_0,0.462000,0.067000, qreg_1[0])
main_circ.s(qreg_2[1])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_2[1],qreg_1[0]])
main_circ.z(qreg_0[0])
main_circ.u(pi/2,-0.693000,param_2, qreg_0[0])
main_circ.s(qreg_2[1])
main_circ.y(qreg_0[0])
main_circ.y(0)
bindings = {param_0: 0.616000, param_2: -0.890000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveFinalReset")
