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
subcirc0.y(qreg_1[0])
subcirc0.u(0.236000,0.259000,-0.403000, qreg_1[2])
subcirc0.u(0.851000,0.329000,-0.833000, qreg_1[2])
subcirc0.u(pi/2,0.151000,0.995000, qreg_1[1])
subcirc0.ry(-0.990000, qreg_1[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(pi/2,0.820000,0.814000, qreg_1[2])
subcirc1.ry(0.676000, qreg_0[0])
subcirc1.ry(0.391000, qreg_1[0])
subcirc1.u(0.485000,-0.947000,0.844000, qreg_1[2])
subcirc1.ry(0.724000, qreg_1[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.157000, qreg_0[1])
subcirc2.u(0.983000,-0.475000,-0.511000, qreg_0[2])
subcirc2.u(pi/2,-0.218000,0.215000, qreg_3[0])
subcirc2.u(-0.469000,-0.923000,-0.130000, qreg_0[0])
subcirc2.u(0.903000,-0.466000,0.814000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.ry(0.346000, 0)
main_circ.u(param_2,0.371000,param_2, 0)
main_circ.u(param_4,param_3,param_0, 0)
main_circ.u(pi/2,0.218000,-0.277000, 1)
main_circ.u(param_1,-0.823000,0.240000, 3)
main_circ.u(param_4,-0.613000,param_2, 0)
main_circ.ry(param_1, 3)
main_circ.append(subcirc1,[1,2,3,0])
main_circ.u(param_4,param_4,param_0, 0)
main_circ.u(param_1,param_3,param_1, 2)
main_circ.y(1)
main_circ.ry(param_2, 2)
main_circ.u(pi/2,param_0,0.343000, 3)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.y(0)
main_circ.ry(param_1, 1)
main_circ.y(0)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.ry(0.766000, 3)
main_circ.ry(-0.512000, 2)
main_circ.ry(param_4, 0)
main_circ.append(subcirc1,[0,1,3,2])
main_circ.u(param_2,-0.609000,0.632000, 0)
main_circ.u(param_4,0.283000,param_2, 0)
main_circ.append(subcirc1,[3,2,1,0])
main_circ.ry(param_0, 1)
main_circ.u(pi/2,-0.731000,param_2, 0)
main_circ.u(pi/2,param_2,param_3, 1)
main_circ.y(1)
main_circ.y(3)
main_circ.ry(0.992000, 3)
main_circ.u(param_0,param_3,param_3, 0)
bindings = {param_0: -0.096000, param_1: -0.875000, param_2: 0.116000, param_3: -0.967000, param_4: 0.492000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "767")
