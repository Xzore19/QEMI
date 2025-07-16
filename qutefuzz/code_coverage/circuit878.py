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
subcirc0.z(qreg_1[0])
subcirc0.u(0,0,-0.162000, qreg_1[2])
subcirc0.u(0,0,-0.217000, qreg_1[0])
subcirc0.rx(-0.143000, qreg_0[0])
subcirc0.u(0,0,0.022000, qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rx(-0.046000, qreg_0[0])
subcirc1.u(0,0,0.644000, qreg_2[1])
subcirc1.z(qreg_0[1])
subcirc1.u(pi/2,-0.810000,-0.168000, qreg_2[0])
subcirc1.z(qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,0.650000,0.846000, qreg_0[2])
subcirc2.z(qreg_0[2])
subcirc2.rx(-0.331000, qreg_0[1])
subcirc2.u(0,0,0.327000, qreg_0[1])
subcirc2.u(0,0,-0.394000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.z(qreg_3[0])
main_circ.z(qreg_0[0])
main_circ.rx(0.121000, qreg_0[0])
main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.z(qreg_3[0])
main_circ.z(qreg_0[1])
main_circ.z(qreg_3[0])
main_circ.u(param_2,0,param_1, qreg_3[0])
main_circ.u(param_1,0,param_3, qreg_0[1])
main_circ.rx(param_0, qreg_2[0])
main_circ.u(param_3,0,0.144000, qreg_0[1])
main_circ.z(qreg_3[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.u(param_0,0.102000,param_0, qreg_2[0])
main_circ.u(pi/2,param_5,0.758000, qreg_0[0])
main_circ.u(param_4,param_7,param_0, qreg_0[1])
main_circ.u(0,param_2,0.784000, qreg_3[0])
main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_3[0]])
main_circ.rx(-0.115000, qreg_2[0])
main_circ.z(qreg_0[1])
main_circ.u(0,param_7,0.115000, qreg_2[0])
main_circ.u(pi/2,0.528000,0.116000, qreg_2[0])
main_circ.u(0,0,param_3, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_2[0]])
main_circ.u(0,0,0.926000, qreg_3[0])
main_circ.z(qreg_2[0])
main_circ.z(qreg_2[0])
main_circ.rx(-0.838000, qreg_3[0])
bindings = {param_0: 0.191000, param_1: 0.054000, param_2: -0.169000, param_3: 0.646000, param_4: 0.957000, param_5: 0.274000, param_7: 0.409000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "878")
