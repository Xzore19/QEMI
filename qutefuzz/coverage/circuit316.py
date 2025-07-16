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
subcirc0.ry(0.961000, qreg_3[0])
subcirc0.u(0.519000,-0.579000,-0.180000, qreg_3[0])
subcirc0.ry(0.633000, qreg_0[2])
subcirc0.u(pi/2,-0.926000,-0.558000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,-0.351000,-0.969000, qreg_0[3])
subcirc1.u(-0.928000,-0.353000,-0.009000, qreg_0[3])
subcirc1.u(pi/2,0.459000,0.599000, qreg_0[0])
subcirc1.u(-0.537000,-0.624000,0.527000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0.986000,-0.109000,0.010000, qreg_0[0])
subcirc2.u(-0.454000,0.958000,0.570000, qreg_1[2])
subcirc2.ry(-0.988000, qreg_1[2])
subcirc2.u(0.952000,-0.029000,0.133000, qreg_1[2])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.y(0)
main_circ.u(-0.582000,-0.668000,param_2, 0)
main_circ.append(subcirc1,[1,0,3,2])
main_circ.u(0.416000,param_2,param_0, 2)
main_circ.u(pi/2,-0.727000,param_1, 2)
main_circ.y(0)
main_circ.u(param_1,param_1,-0.872000, 1)
main_circ.y(3)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.u(param_0,0.974000,-0.240000, 2)
main_circ.y(0)
main_circ.append(subcirc1,[3,0,2,1])
main_circ.ry(-0.135000, 2)
main_circ.append(subcirc1,[1,0,3,2])
main_circ.append(subcirc1,[0,1,3,2])
main_circ.ry(param_2, 1)
main_circ.u(pi/2,param_2,param_2, 0)
main_circ.append(subcirc1,[0,2,1,3])
main_circ.ry(param_1, 3)
main_circ.y(1)
main_circ.ry(0.056000, 2)
main_circ.u(pi/2,param_0,param_1, 0)
main_circ.u(param_2,0.078000,param_2, 0)
main_circ.append(subcirc1,[0,1,3,2])
main_circ.append(subcirc1,[0,2,3,1])
main_circ.ry(param_1, 2)
main_circ.u(param_1,0.833000,0.530000, 2)
main_circ.u(pi/2,param_2,param_1, 0)
main_circ.ry(param_2, 1)
bindings = {param_0: -0.925000, param_1: -0.001000, param_2: -0.244000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "316")
