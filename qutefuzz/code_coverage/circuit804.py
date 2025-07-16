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
subcirc0.z(qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.rz(0.463000, qreg_0[0])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(-0.401000, qreg_0[1])
subcirc1.h(qreg_0[1])
subcirc1.u(pi/2,0.740000,-0.488000, qreg_0[3])
subcirc1.h(qreg_0[3])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_3[0])
subcirc2.u(pi/2,-0.480000,-0.491000, qreg_3[0])
subcirc2.z(qreg_3[0])
subcirc2.u(pi/2,0.203000,0.049000, qreg_1[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.rz(param_1, 3)
main_circ.rz(0.825000, 2)
main_circ.rz(param_1, 1)
main_circ.h(0)
main_circ.u(pi/2,-0.789000,param_1, 1)
main_circ.z(0)
main_circ.rz(-0.276000, 3)
main_circ.z(1)
main_circ.h(1)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.h(0)
main_circ.append(subcirc0,[3,2,1,0])
main_circ.append(subcirc0,[2,3,0,1])
main_circ.h(3)
main_circ.rz(-0.162000, 2)
main_circ.h(0)
main_circ.rz(0.328000, 2)
main_circ.z(1)
main_circ.h(3)
main_circ.rz(param_0, 3)
main_circ.rz(-0.887000, 1)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.z(2)
main_circ.rz(-0.430000, 3)
main_circ.u(param_0,0.525000,0.154000, 1)
main_circ.h(2)
main_circ.u(param_1,-0.616000,param_0, 1)
main_circ.u(pi/2,param_0,-0.925000, 3)
main_circ.u(param_1,param_0,-0.011000, 0)
main_circ.append(subcirc0,[1,2,3,0])
main_circ.rz(-0.179000, 2)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.z(1)
main_circ.rz(param_0, 0)
main_circ.z(1)
bindings = {param_0: -0.906000, param_1: -0.162000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "804")
