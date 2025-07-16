from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.u(param_3,param_0,0.819000, 1)
main_circ.ry(-0.858000, 3)
main_circ.u(0,0,-0.731000, 1)
main_circ.s(1)
main_circ.s(3)
main_circ.s(1)
main_circ.h(1)
main_circ.u(param_1,param_1,-0.883000, 2)
main_circ.u(0,0,-0.599000, 2)
main_circ.u(0,param_3,param_1, 2)
main_circ.u(0,param_0,0.432000, 3)
main_circ.ry(param_1, 3)
main_circ.s(1)
main_circ.s(0)
main_circ.u(0,param_0,param_1, 1)
main_circ.ry(param_2, 0)
main_circ.ry(-0.799000, 3)
main_circ.ry(-0.253000, 0)
main_circ.u(param_0,0,param_1, 0)
main_circ.s(3)
main_circ.u(param_3,param_1,param_2, 2)
main_circ.s(1)
main_circ.ry(param_1, 0)
main_circ.ry(param_2, 2)
main_circ.s(3)
main_circ.h(1)
main_circ.u(0,param_2,0.344000, 0)
main_circ.u(0,param_2,0.280000, 3)
main_circ.ry(0.717000, 1)
main_circ.ry(0.925000, 3)
main_circ.u(0,param_3,0.188000, 2)
main_circ.u(0,param_0,param_1, 0)
main_circ.h(0)
main_circ.ry(0.626000, 0)
main_circ.u(0,0,param_0, 1)
main_circ.ry(0.849000, 0)
main_circ.s(0)
main_circ.s(3)
main_circ.ry(param_2, 2)
main_circ.ry(0.990000, 3)
bindings = {param_0: -0.744000, param_1: 0.920000, param_2: 0.728000, param_3: 0.337000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
