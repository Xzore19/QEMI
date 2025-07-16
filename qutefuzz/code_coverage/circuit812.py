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
subcirc0.u(pi/2,0.456000,0.652000, qreg_0[3])
subcirc0.rz(0.235000, qreg_0[3])
subcirc0.y(qreg_0[0])
subcirc0.u(pi/2,-0.836000,0.684000, qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.y(qreg_1[2])
subcirc1.u(pi/2,0.041000,0.479000, qreg_1[2])
subcirc1.u(pi/2,0.238000,0.279000, qreg_1[2])
subcirc1.u(pi/2,0.817000,0.692000, qreg_1[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[3])
subcirc2.y(qreg_0[0])
subcirc2.u(0.344000,0.803000,0.116000, qreg_0[1])
subcirc2.y(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.386000,-0.890000,-0.780000, qreg_0[0])
subcirc3.rz(0.860000, qreg_1[1])
subcirc3.u(pi/2,-0.070000,0.601000, qreg_3[0])
subcirc3.u(pi/2,0.320000,0.162000, qreg_1[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc3,[qreg_0[0],3,2,1])
main_circ.append(subcirc1,[0,1,3,2])
main_circ.append(subcirc1,[3,qreg_0[0],0,1])
main_circ.append(subcirc1,[0,2,qreg_0[0],3])
main_circ.append(subcirc3,[3,1,qreg_0[0],0])
main_circ.u(param_1,param_0,0.490000, 2)
main_circ.append(subcirc2,[2,1,3,qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],3,0,1])
main_circ.append(subcirc2,[qreg_0[0],2,3,0])
main_circ.y(1)
main_circ.append(subcirc2,[3,2,0,qreg_0[0]])
main_circ.append(subcirc1,[2,3,0,qreg_0[0]])
main_circ.u(pi/2,param_4,0.855000, 2)
main_circ.u(param_4,param_2,-0.050000, 0)
main_circ.rz(param_4, qreg_0[0])
main_circ.u(0.807000,-0.977000,0.420000, 3)
main_circ.u(0.648000,param_2,param_3, 3)
bindings = {param_0: -0.982000, param_1: 0.425000, param_2: -0.280000, param_3: -0.540000, param_4: -0.817000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesDecomposition")
