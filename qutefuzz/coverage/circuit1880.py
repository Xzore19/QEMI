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
subcirc0.u(0,0,0.391000, qreg_0[0])
subcirc0.rz(0.952000, qreg_0[0])
subcirc0.rz(0.043000, qreg_3[0])
subcirc0.u(-0.871000,0.267000,0.088000, qreg_0[0])
subcirc0.rz(0.883000, qreg_3[0])
subcirc0.cy(qreg_0[0],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.751000, qreg_0[3])
subcirc1.u(0.533000,-0.897000,-0.933000, qreg_0[3])
subcirc1.u(0,0,-0.288000, qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[3])
subcirc1.u(0.498000,0.746000,-0.672000, qreg_0[2])
subcirc1.cy(qreg_0[2],qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.017000,0.108000,-0.710000, qreg_0[0])
subcirc2.u(-0.368000,0.466000,-0.452000, qreg_0[1])
subcirc2.u(0,0,-0.673000, qreg_0[3])
subcirc2.u(0,0,-0.952000, qreg_0[3])
subcirc2.rz(-0.019000, qreg_0[3])
subcirc2.u(-0.315000,-0.461000,0.591000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(0.544000,-0.354000,0.446000, qreg_0[0])
subcirc3.u(0.762000,0.927000,0.138000, qreg_2[1])
subcirc3.cy(qreg_2[0],qreg_1[0])
subcirc3.u(-0.063000,0.770000,0.190000, qreg_2[0])
subcirc3.u(0,0,-0.962000, qreg_2[0])
subcirc3.cy(qreg_2[0],qreg_1[0])

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
param_5 = Parameter("param_5")

main_circ.u(0,param_0,param_3, 1)
main_circ.append(subcirc2,[2,qreg_0[0],1,0,3])
main_circ.cy(1,0)
main_circ.u(0.767000,param_4,param_3, 1)
main_circ.cy(2,qreg_0[0])
main_circ.u(0,0,param_2, 1)
main_circ.rz(-0.727000, 0)
main_circ.u(0,0,param_3, 0)
main_circ.rz(param_0, 3)
main_circ.u(param_3,param_2,-0.630000, 0)
main_circ.append(subcirc0,[1,2,3,qreg_0[0]])
main_circ.cy(0,1)
main_circ.u(-0.535000,param_1,param_1, 1)
main_circ.cy(qreg_0[0],0)
main_circ.cy(qreg_0[0],0)
main_circ.rz(param_4, 2)
main_circ.append(subcirc2,[2,0,3,qreg_0[0],1])
main_circ.append(subcirc3,[0,2,3,qreg_0[0]])
main_circ.cy(2,3)
main_circ.cy(2,3)
main_circ.cy(3,1)
main_circ.cy(0,2)
main_circ.cy(0,3)
main_circ.cy(3,0)
main_circ.cy(0,2)
main_circ.cy(1,2)
main_circ.u(param_1,0,param_1, 1)
main_circ.rz(param_3, 2)
main_circ.u(param_5,param_5,0.420000, 3)
main_circ.rz(0.721000, 0)
main_circ.rz(param_1, 3)
main_circ.u(param_5,0,0.015000, qreg_0[0])
main_circ.rz(param_1, qreg_0[0])
bindings = {param_0: 0.401000, param_1: -0.899000, param_2: -0.043000, param_3: 0.972000, param_4: -0.123000, param_5: -0.359000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesSimpleCommutation")
