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
subcirc0.z(qreg_0[1])
subcirc0.rz(-0.110000, qreg_0[2])
subcirc0.z(qreg_0[2])
subcirc0.u(pi/2,-0.979000,-0.488000, qreg_0[1])
subcirc0.u(pi/2,-0.620000,-0.501000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.ry(-0.256000, qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.u(pi/2,-0.743000,-0.876000, qreg_0[0])
subcirc1.z(qreg_1[0])
subcirc1.u(pi/2,-0.650000,-0.654000, qreg_1[0])

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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.u(param_0,-0.645000,0.382000, 2)
main_circ.rz(-0.597000, 1)
main_circ.append(subcirc0,[3,1,0,qreg_0[0]])
main_circ.z(1)
main_circ.rz(param_4, qreg_0[0])
main_circ.append(subcirc1,[1,0,3,2])
main_circ.append(subcirc0,[1,3,0,qreg_0[0]])
main_circ.rz(param_3, qreg_0[0])
main_circ.ry(-0.406000, 1)
main_circ.rz(param_4, 3)
main_circ.u(param_1,param_5,-0.005000, qreg_0[0])
main_circ.u(pi/2,param_0,0.175000, 1)
main_circ.append(subcirc0,[2,3,qreg_0[0],1])
main_circ.rz(-0.086000, 2)
main_circ.rz(param_0, 2)
main_circ.z(qreg_0[0])
main_circ.u(param_3,param_5,param_3, 1)
main_circ.z(qreg_0[0])
main_circ.z(1)
main_circ.u(param_5,param_0,param_6, qreg_0[0])
main_circ.u(param_1,param_5,param_6, 3)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.ry(-0.002000, 2)
main_circ.u(pi/2,param_0,0.058000, 3)
main_circ.z(0)
bindings = {param_0: -0.218000, param_1: 0.286000, param_3: 0.960000, param_4: -0.754000, param_5: 0.355000, param_6: -0.063000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "203")
