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
subcirc0.h(qreg_0[0])
subcirc0.cy(qreg_3[0],qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.u(pi/2,0.145000,-0.597000, qreg_0[0])
subcirc0.ry(-0.591000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.u(pi/2,-0.641000,-0.815000, qreg_1[1])
subcirc1.ry(-0.544000, qreg_3[0])
subcirc1.u(pi/2,0.720000,0.800000, qreg_0[0])
subcirc1.ry(0.003000, qreg_3[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.cy(qreg_0[1],qreg_2[1])
main_circ.ry(-0.229000, qreg_0[1])
main_circ.append(subcirc1,[qreg_2[1],0,qreg_0[1],qreg_0[0]])
main_circ.ry(param_3, qreg_2[0])
main_circ.append(subcirc1,[qreg_2[1],qreg_2[0],qreg_0[0],qreg_0[1]])
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.u(param_3,param_2,param_2, qreg_0[1])
main_circ.ry(0.591000, qreg_2[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[1],0])
main_circ.ry(0.264000, qreg_0[1])
main_circ.ry(-0.181000, qreg_2[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_2[0],0,qreg_2[1]])
main_circ.cy(qreg_2[1],qreg_0[1])
main_circ.cy(qreg_2[0],qreg_0[0])
main_circ.cy(qreg_2[1],qreg_2[0])
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.cy(qreg_0[1],qreg_2[1])
main_circ.cy(qreg_2[1],0)
main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.cy(qreg_2[1],qreg_2[0])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.h(qreg_2[1])
main_circ.u(pi/2,param_1,0.442000, qreg_2[0])
main_circ.u(pi/2,-0.930000,param_2, qreg_2[0])
main_circ.cy(0,qreg_2[0])
bindings = {param_1: 0.070000, param_2: 0.501000, param_3: 0.807000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
