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
subcirc0.s(qreg_0[2])
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[0])
subcirc0.s(qreg_0[3])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.530000,0.888000,0.814000, qreg_3[0])
subcirc1.z(qreg_3[0])
subcirc1.z(qreg_0[2])
subcirc1.rz(0.623000, qreg_3[0])
subcirc1.s(qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc0,[0,qreg_1[0],3,1])
main_circ.append(subcirc0,[2,0,1,qreg_0[0]])
main_circ.rz(param_3, 0)
main_circ.z(3)
main_circ.s(qreg_0[0])
main_circ.z(2)
main_circ.append(subcirc0,[qreg_1[0],3,0,1])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],1,3])
main_circ.rz(0.662000, 3)
main_circ.s(1)
main_circ.rz(-0.009000, qreg_1[0])
main_circ.u(0.593000,-0.603000,0.893000, 1)
main_circ.append(subcirc0,[0,qreg_1[0],1,2])
main_circ.z(1)
main_circ.append(subcirc0,[qreg_0[0],0,1,2])
main_circ.z(qreg_0[0])
main_circ.z(0)
main_circ.rz(-0.780000, qreg_1[0])
main_circ.rz(param_0, qreg_0[0])
main_circ.s(1)
main_circ.append(subcirc1,[0,1,2,3])
main_circ.u(-0.577000,0.252000,param_3, qreg_1[0])
main_circ.u(0.981000,0.069000,0.387000, 1)
main_circ.u(param_4,param_0,param_3, 0)
main_circ.s(qreg_1[0])
main_circ.rz(param_3, 0)
bindings = {param_0: 0.490000, param_3: -0.077000, param_4: -0.559000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeCancellation")
