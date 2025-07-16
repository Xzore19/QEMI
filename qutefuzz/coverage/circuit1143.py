from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.y(qreg_0[2])
subcirc0.u(0.406000,0.070000,-0.957000, qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.u(-0.697000,-0.523000,0.700000, qreg_0[1])
subcirc0.z(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.u(-0.979000,0.479000,0.697000, qreg_3[0])
subcirc1.z(qreg_0[1])
subcirc1.y(qreg_0[0])
subcirc1.u(-0.538000,-0.720000,-0.584000, qreg_3[0])

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

main_circ.y(2)
main_circ.append(subcirc0,[3,1,0,2])
main_circ.x(0)
main_circ.append(subcirc1,[1,0,2,3])
main_circ.z(0)
main_circ.u(0.716000,param_3,0.108000, 1)
main_circ.z(0)
main_circ.u(0.840000,param_1,param_3, 0)
main_circ.append(subcirc1,[0,2,3,1])
main_circ.u(0.246000,-0.909000,param_2, 2)
main_circ.x(0)
main_circ.x(2)
main_circ.u(param_0,param_0,param_3, 0)
main_circ.y(0)
main_circ.y(2)
main_circ.append(subcirc1,[3,0,1,2])
main_circ.z(1)
main_circ.u(param_1,param_1,-0.658000, 2)
main_circ.u(param_3,0.977000,-0.419000, 3)
main_circ.x(1)
main_circ.append(subcirc1,[0,3,1,2])
main_circ.u(0.124000,param_3,-0.269000, 1)
main_circ.z(2)
main_circ.x(2)
bindings = {param_0: 0.111000, param_1: -0.073000, param_2: -0.476000, param_3: -0.351000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1143")
