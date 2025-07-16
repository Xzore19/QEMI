from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rz(param_2, 2)
main_circ.cz(3,qreg_0[0])
main_circ.s(2)
main_circ.ry(param_1, 1)
main_circ.cz(1,3)
main_circ.rz(param_1, 3)
main_circ.cz(qreg_0[0],1)
main_circ.s(2)
main_circ.ry(param_1, 0)
main_circ.rz(param_2, 0)
main_circ.rz(param_2, qreg_0[0])
main_circ.ry(0.251000, 1)
main_circ.s(2)
main_circ.ry(0.933000, 2)
main_circ.ry(param_0, 2)
main_circ.rz(-0.915000, qreg_0[0])
main_circ.cz(1,qreg_0[0])
main_circ.cz(0,1)
main_circ.ry(param_0, 0)
main_circ.cz(3,0)
main_circ.ry(param_0, qreg_0[0])
main_circ.rz(param_0, 3)
main_circ.s(1)
main_circ.cz(3,2)
main_circ.rz(param_1, 0)
main_circ.ry(param_1, 3)
main_circ.cz(1,qreg_0[0])
main_circ.rz(-0.573000, 1)
main_circ.rz(param_0, 2)
main_circ.cz(3,1)
main_circ.cz(3,0)
main_circ.cz(1,2)
main_circ.cz(2,3)
main_circ.rz(param_0, qreg_0[0])
main_circ.cz(0,2)
main_circ.s(1)
main_circ.s(3)
main_circ.cz(2,qreg_0[0])
main_circ.ry(-0.043000, 2)
main_circ.ry(param_1, 2)
main_circ.cz(1,0)
bindings = {param_0: 0.398000, param_1: -0.637000, param_2: 0.529000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesSimpleCommutation")
