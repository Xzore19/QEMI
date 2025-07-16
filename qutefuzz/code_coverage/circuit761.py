from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cx(qreg_2[1],qreg_0[1])
subcirc0.z(qreg_2[1])
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

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
param_3 = Parameter("param_3")

main_circ.cx(0,2)
main_circ.u(param_3,-0.527000,-0.768000, 3)
main_circ.u(0.392000,0.382000,-0.111000, 0)
main_circ.cx(1,3)
main_circ.z(3)
main_circ.u(param_3,param_1,-0.700000, 2)
main_circ.z(3)
main_circ.u(pi/2,param_0,param_3, 3)
main_circ.z(1)
main_circ.u(param_1,0.561000,-0.841000, 0)
main_circ.u(param_3,0.204000,-0.464000, 2)
main_circ.u(param_3,0.686000,0.141000, 1)
main_circ.cx(1,3)
main_circ.u(param_1,0.889000,-0.755000, 3)
main_circ.u(-0.365000,param_3,-0.544000, 0)
main_circ.u(param_2,param_0,param_2, 0)
main_circ.cx(3,2)
main_circ.u(pi/2,0.642000,0.538000, 3)
main_circ.u(param_3,0.803000,-0.275000, 1)
main_circ.z(2)
main_circ.u(pi/2,param_0,param_0, 1)
main_circ.z(1)
main_circ.z(1)
main_circ.u(pi/2,param_1,param_0, 2)
main_circ.u(param_2,0.404000,param_2, 0)
main_circ.z(1)
main_circ.z(2)
main_circ.z(2)
main_circ.cx(0,1)
main_circ.cx(3,1)
main_circ.cx(2,0)
main_circ.cx(1,0)
main_circ.cx(0,1)
main_circ.cx(2,0)
main_circ.cx(3,2)
main_circ.cx(1,2)
main_circ.u(param_2,param_3,0.276000, 0)
main_circ.u(param_0,param_2,param_1, 2)
main_circ.u(param_0,param_0,-0.471000, 1)
main_circ.u(pi/2,0.100000,param_1, 2)
bindings = {param_0: 0.139000, param_1: -0.863000, param_2: 0.146000, param_3: -0.394000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeCliffords")
