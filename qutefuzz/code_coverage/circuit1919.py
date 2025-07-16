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

main_circ.cy(1,0)
main_circ.rx(param_0, 3)
main_circ.cy(1,0)
main_circ.cy(2,0)
main_circ.rx(param_1, 1)
main_circ.rx(param_1, 1)
main_circ.s(1)
main_circ.u(param_0,0.059000,0.105000, 3)
main_circ.rx(-0.862000, 0)
main_circ.u(param_1,param_0,param_1, 2)
main_circ.cy(0,3)
main_circ.u(param_1,param_1,-0.439000, 1)
main_circ.s(0)
main_circ.rx(-0.062000, 2)
main_circ.u(0.147000,-0.377000,0.567000, 0)
main_circ.rx(-0.739000, 3)
main_circ.rx(param_0, 2)
main_circ.u(0.593000,param_0,param_1, 0)
main_circ.s(1)
main_circ.cy(2,3)
main_circ.u(0.241000,param_0,param_0, 3)
main_circ.rx(0.684000, 2)
main_circ.cy(3,0)
main_circ.u(-0.426000,param_0,0.387000, 1)
main_circ.u(-0.035000,param_0,0.925000, 3)
main_circ.rx(param_1, 0)
main_circ.s(1)
main_circ.u(param_1,0.355000,param_1, 2)
main_circ.cy(2,1)
main_circ.cy(0,1)
main_circ.cy(3,0)
main_circ.cy(3,0)
main_circ.cy(1,0)
main_circ.cy(1,3)
main_circ.cy(1,2)
main_circ.rx(param_0, 2)
main_circ.u(param_0,0.574000,-0.506000, 0)
main_circ.cy(1,0)
main_circ.u(param_1,param_0,-0.722000, 2)
main_circ.u(param_0,param_0,param_0, 0)
bindings = {param_0: -0.739000, param_1: -0.218000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectCliffords")
