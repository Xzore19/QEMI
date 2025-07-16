from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_1[1])
subcirc0.h(qreg_3[0])
subcirc0.z(qreg_1[0])
subcirc0.z(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.779000,0.361000, qreg_3[0])
subcirc1.z(qreg_0[2])
subcirc1.h(qreg_0[1])
subcirc1.u(pi/2,0.505000,0.421000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_1[0])
subcirc2.h(qreg_0[0])
subcirc2.u(pi/2,-0.876000,-0.283000, qreg_1[0])
subcirc2.h(qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.z(qreg_0[2])
subcirc3.u(pi/2,-0.549000,-0.778000, qreg_0[2])
subcirc3.u(pi/2,0.097000,0.647000, qreg_0[2])
subcirc3.h(qreg_0[3])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.u(pi/2,param_0,-0.173000, 1)
main_circ.u(pi/2,0.166000,0.032000, qreg_0[1])
main_circ.z(1)
main_circ.append(subcirc1,[1,qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.z(qreg_3[0])
main_circ.z(qreg_0[2])
main_circ.y(qreg_3[0])
main_circ.z(1)
main_circ.append(subcirc1,[0,qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.z(qreg_0[1])
main_circ.u(param_0,-0.808000,-0.882000, qreg_0[0])
main_circ.y(qreg_0[1])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],1,qreg_0[2]])
main_circ.u(pi/2,param_2,0.139000, qreg_3[0])
main_circ.u(pi/2,param_1,-0.807000, qreg_0[1])
main_circ.u(pi/2,param_1,-0.915000, qreg_3[0])
main_circ.y(qreg_3[0])
main_circ.u(param_0,0.483000,param_2, 1)
main_circ.z(1)
main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.h(qreg_0[0])
main_circ.u(param_2,-0.668000,-0.873000, qreg_3[0])
main_circ.u(pi/2,param_1,0.467000, 1)
main_circ.z(1)
main_circ.h(0)
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],0,qreg_0[2]])
main_circ.h(qreg_3[0])
main_circ.z(qreg_0[2])
main_circ.y(0)
main_circ.append(subcirc1,[0,qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.u(param_1,param_0,-0.779000, qreg_0[0])
main_circ.y(qreg_0[2])
main_circ.h(0)
main_circ.append(subcirc2,[qreg_0[2],qreg_3[0],qreg_0[1],0])
main_circ.y(qreg_0[1])
main_circ.h(0)
bindings = {param_0: 0.582000, param_1: 0.598000, param_2: -0.071000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "274")
