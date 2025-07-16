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
subcirc0.ry(0.832000, qreg_3[0])
subcirc0.u(0,0,0.484000, qreg_0[1])
subcirc0.u(pi/2,0.515000,-0.261000, qreg_3[0])
subcirc0.z(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.193000, qreg_0[2])
subcirc1.u(0,0,-0.843000, qreg_3[0])
subcirc1.ry(-0.383000, qreg_0[0])
subcirc1.ry(0.353000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.558000,0.020000, qreg_1[0])
subcirc2.z(qreg_3[0])
subcirc2.ry(0.660000, qreg_3[0])
subcirc2.u(0,0,-0.777000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.ry(0.762000, 2)
main_circ.z(1)
main_circ.append(subcirc1,[3,2,1,0])
main_circ.u(param_1,-0.773000,param_0, 1)
main_circ.u(param_0,param_1,-0.814000, 3)
main_circ.z(1)
main_circ.z(0)
main_circ.u(0,param_1,-0.274000, 0)
main_circ.ry(param_1, 0)
main_circ.z(1)
main_circ.append(subcirc1,[3,2,1,0])
main_circ.append(subcirc1,[0,2,3,1])
main_circ.ry(0.217000, 2)
main_circ.ry(-0.319000, 0)
main_circ.z(3)
main_circ.u(param_1,0.517000,param_1, 3)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.ry(param_0, 0)
main_circ.ry(-0.031000, 3)
main_circ.u(param_1,-0.019000,param_0, 2)
main_circ.u(param_0,param_1,-0.112000, 0)
main_circ.z(1)
main_circ.append(subcirc1,[3,0,2,1])
main_circ.append(subcirc1,[1,2,0,3])
main_circ.append(subcirc1,[3,2,1,0])
main_circ.append(subcirc1,[2,1,0,3])
main_circ.append(subcirc1,[3,2,1,0])
main_circ.u(param_1,-0.476000,param_1, 3)
main_circ.u(param_0,0,param_1, 1)
main_circ.u(pi/2,-0.856000,-0.113000, 3)
main_circ.ry(-0.793000, 1)
main_circ.u(param_0,0,0.855000, 1)
main_circ.ry(-0.946000, 2)
bindings = {param_0: -0.534000, param_1: -0.997000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1168")
