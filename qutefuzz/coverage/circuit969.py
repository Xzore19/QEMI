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
subcirc0.z(qreg_1[1])
subcirc0.u(-0.675000,-0.713000,0.990000, qreg_1[0])
subcirc0.cz(qreg_1[2],qreg_1[1])
subcirc0.cz(qreg_1[1],qreg_0[0])
subcirc0.u(pi/2,0.692000,-0.143000, qreg_1[0])
subcirc0.cz(qreg_1[0],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.666000,-0.655000,-0.755000, qreg_0[1])
subcirc1.u(pi/2,0.100000,-0.687000, qreg_0[1])
subcirc1.u(0.350000,0.658000,0.002000, qreg_0[2])
subcirc1.u(-0.323000,-0.893000,-0.495000, qreg_0[2])
subcirc1.cz(qreg_0[1],qreg_0[2])
subcirc1.u(pi/2,0.821000,-0.998000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.cz(1,2)
main_circ.z(qreg_0[0])
main_circ.append(subcirc1,[1,qreg_0[0],2,0])
main_circ.append(subcirc0,[qreg_0[0],2,3,qreg_0[1]])
main_circ.u(-0.606000,param_0,param_2, 3)
main_circ.z(1)
main_circ.append(subcirc1,[qreg_0[1],3,0,qreg_0[0]])
main_circ.z(qreg_0[1])
main_circ.append(subcirc1,[qreg_0[0],1,0,qreg_0[1]])
main_circ.u(param_2,param_0,param_1, 2)
main_circ.z(0)
main_circ.u(pi/2,param_0,-0.810000, qreg_0[0])
main_circ.append(subcirc1,[2,qreg_0[1],qreg_0[0],0])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],3)
main_circ.cz(3,1)
main_circ.cz(0,3)
main_circ.cz(qreg_0[0],3)
main_circ.cz(3,2)
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.cz(qreg_0[1],3)
main_circ.u(param_0,0.183000,-0.207000, 3)
main_circ.z(0)
main_circ.u(param_1,param_2,param_0, 0)
main_circ.cz(qreg_0[0],3)
main_circ.z(2)
main_circ.u(param_1,param_1,param_0, 2)
main_circ.u(param_2,param_2,-0.870000, qreg_0[1])
bindings = {param_0: -0.227000, param_1: -0.684000, param_2: 0.171000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "969")
