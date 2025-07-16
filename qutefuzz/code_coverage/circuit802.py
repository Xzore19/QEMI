from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.cx(0,1)
main_circ.cx(0,2)
main_circ.z(3)
main_circ.cx(1,3)
main_circ.z(1)
main_circ.cx(2,3)
main_circ.u(param_1,param_0,0.044000, 2)
main_circ.cx(2,1)
main_circ.cz(1,2)
main_circ.u(-0.597000,0.477000,param_1, 0)
main_circ.cx(2,3)
main_circ.cx(2,0)
main_circ.cz(1,0)
main_circ.u(0.915000,param_1,param_1, 2)
main_circ.cx(2,0)
main_circ.u(param_0,-0.480000,param_0, 2)
main_circ.cx(3,0)
main_circ.u(param_0,0.880000,-0.496000, 3)
main_circ.u(param_0,0.511000,-0.537000, 3)
main_circ.u(0.579000,0.785000,-0.404000, 3)
main_circ.z(2)
main_circ.u(param_0,param_0,param_0, 0)
main_circ.cx(2,0)
main_circ.cz(2,3)
main_circ.cx(3,2)
main_circ.cz(2,1)
main_circ.cz(2,1)
main_circ.cx(2,1)
main_circ.cx(3,0)
main_circ.cz(2,1)
main_circ.cz(0,2)
main_circ.u(0.521000,0.945000,0.238000, 3)
main_circ.u(0.066000,param_0,0.174000, 3)
main_circ.cz(0,1)
main_circ.z(2)
main_circ.u(0.339000,-0.194000,param_0, 1)
main_circ.u(param_1,param_1,-0.586000, 2)
main_circ.cx(2,1)
main_circ.u(param_1,param_1,0.499000, 0)
main_circ.cx(1,2)
main_circ.z(0)
main_circ.u(param_1,param_1,param_1, 1)
bindings = {param_0: 0.049000, param_1: 0.091000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
