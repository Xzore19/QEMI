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
subcirc0.u(0.431000,0.890000,0.981000, qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0.rz(-0.029000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.u(-0.561000,0.560000,-0.847000, qreg_0[0])
subcirc1.rz(0.194000, qreg_0[3])
subcirc1.x(qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[1])
subcirc2.h(qreg_0[3])
subcirc2.u(-0.954000,-0.175000,0.015000, qreg_0[1])
subcirc2.u(-0.366000,0.670000,0.312000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.rz(0.273000, qreg_0[0])
subcirc3.h(qreg_0[1])
subcirc3.rz(-0.166000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.h(qreg_0[1])
subcirc4.rz(0.503000, qreg_0[0])
subcirc4.x(qreg_0[2])
subcirc4.rz(-0.350000, qreg_0[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.append(subcirc4,[0,qreg_0[1],qreg_0[2],qreg_0[3]])
main_circ.h(qreg_0[3])
main_circ.h(qreg_0[2])
main_circ.append(subcirc4,[0,qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.u(0.904000,param_3,0.704000, 0)
main_circ.u(-0.462000,param_0,param_2, qreg_0[2])
main_circ.append(subcirc4,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.u(param_3,0.410000,-0.909000, 0)
main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3],0])
main_circ.append(subcirc1,[qreg_0[3],qreg_0[2],0,qreg_0[0]])
main_circ.append(subcirc4,[qreg_0[2],qreg_0[0],qreg_0[3],0])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_0[2],qreg_0[1],qreg_0[3]])
main_circ.u(param_1,param_4,param_2, qreg_0[0])
main_circ.rz(-0.732000, qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
main_circ.append(subcirc4,[0,qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.h(qreg_0[3])
main_circ.rz(param_4, qreg_0[2])
main_circ.h(qreg_0[3])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[2],0,qreg_0[1]])
main_circ.u(0.622000,0.918000,0.352000, qreg_0[3])
bindings = {param_0: 0.181000, param_1: 0.377000, param_2: 0.753000, param_3: -0.204000, param_4: -0.103000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "580")
