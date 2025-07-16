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
subcirc0.u(pi/2,-0.698000,-0.515000, qreg_0[0])
subcirc0.u(pi/2,0.376000,-0.222000, qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.rz(-0.441000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,0.277000,-0.293000, qreg_2[1])
subcirc1.z(qreg_0[1])
subcirc1.rz(-0.887000, qreg_0[0])
subcirc1.s(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.457000, qreg_0[2])
subcirc2.rz(0.886000, qreg_0[2])
subcirc2.u(pi/2,-0.785000,-0.555000, qreg_0[0])
subcirc2.rz(-0.033000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

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

main_circ.append(subcirc0,[qreg_0[0],3,1,0])
main_circ.u(pi/2,param_1,0.916000, 2)
main_circ.z(3)
main_circ.rz(param_1, 2)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.rz(0.148000, 3)
main_circ.append(subcirc0,[qreg_0[0],2,3,0])
main_circ.rz(param_4, 2)
main_circ.u(pi/2,-0.220000,0.403000, 2)
main_circ.append(subcirc0,[qreg_0[0],3,2,1])
main_circ.u(param_1,0.920000,0.161000, 2)
main_circ.u(param_0,-0.944000,param_0, 2)
main_circ.s(3)
main_circ.append(subcirc1,[qreg_0[0],3,1,2])
main_circ.s(qreg_0[0])
main_circ.s(1)
main_circ.rz(-0.401000, 3)
main_circ.u(pi/2,0.147000,param_3, qreg_0[0])
main_circ.append(subcirc0,[0,qreg_0[0],1,2])
main_circ.u(pi/2,0.411000,param_1, 2)
main_circ.append(subcirc0,[qreg_0[0],0,1,3])
main_circ.append(subcirc0,[qreg_0[0],2,1,0])
main_circ.append(subcirc1,[2,0,1,3])
main_circ.u(pi/2,0.522000,0.940000, 0)
main_circ.u(param_1,param_3,param_0, 3)
main_circ.s(1)
main_circ.s(3)
main_circ.s(qreg_0[0])
bindings = {param_0: 0.439000, param_1: 0.522000, param_3: -0.717000, param_4: -0.908000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
