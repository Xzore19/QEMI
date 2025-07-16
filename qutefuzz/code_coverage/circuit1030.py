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
subcirc0.u(0.095000,-0.181000,0.207000, qreg_0[1])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_0[2])
subcirc0.u(pi/2,0.795000,0.295000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(0.458000,-0.589000,-0.758000, qreg_1[2])
subcirc1.h(qreg_1[1])
subcirc1.u(0.832000,0.778000,-0.382000, qreg_1[1])
subcirc1.u(pi/2,-0.233000,0.547000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(2)
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

main_circ.append(subcirc1,[1,qreg_2[0],qreg_1[0],qreg_0[0],0,qreg_2[1]])
main_circ.u(param_1,-0.680000,param_1, 1)
main_circ.s(qreg_2[1])
main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],1,qreg_2[1]])
main_circ.h(qreg_2[1])
main_circ.h(0)
main_circ.append(subcirc1,[qreg_2[1],1,qreg_1[0],qreg_0[0],qreg_2[0],0])
main_circ.s(qreg_2[0])
main_circ.h(1)
main_circ.append(subcirc1,[qreg_2[1],1,qreg_2[0],qreg_1[0],0,qreg_0[0]])
main_circ.append(subcirc1,[1,0,qreg_1[0],qreg_2[0],qreg_2[1],qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],1,qreg_1[0],0,qreg_2[1]])
main_circ.append(subcirc1,[qreg_1[0],qreg_2[1],0,qreg_2[0],qreg_0[0],1])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],1,0])
main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[0,qreg_1[0],qreg_2[0],1])
main_circ.u(0.432000,0.539000,-0.947000, 1)
main_circ.u(param_1,param_0,param_0, qreg_2[1])
main_circ.u(param_0,param_0,-0.130000, qreg_2[0])
main_circ.s(0)
main_circ.h(1)
main_circ.s(1)
main_circ.u(-0.760000,param_1,-0.205000, 1)
main_circ.s(1)
main_circ.u(param_0,param_0,0.410000, qreg_2[1])
main_circ.h(0)
main_circ.u(param_0,0.327000,-0.223000, 0)
bindings = {param_0: 0.468000, param_1: 0.723000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1030")
