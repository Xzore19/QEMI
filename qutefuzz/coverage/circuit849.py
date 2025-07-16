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
subcirc0.ry(0.355000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.cy(qreg_1[0],qreg_1[1])
subcirc0.cy(qreg_0[0],qreg_1[0])

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

main_circ.ry(0.643000, 3)
main_circ.cz(3,0)
main_circ.cy(3,0)
main_circ.s(3)
main_circ.ry(param_2, 3)
main_circ.s(3)
main_circ.ry(param_0, 3)
main_circ.cz(3,2)
main_circ.cz(2,0)
main_circ.ry(0.209000, 2)
main_circ.cy(1,3)
main_circ.ry(param_2, 3)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.ry(param_1, 0)
main_circ.append(subcirc0,[0,3,1,2])
main_circ.ry(param_0, 1)
main_circ.cz(0,3)
main_circ.append(subcirc0,[3,2,0,1])
main_circ.cy(0,3)
main_circ.append(subcirc0,[3,0,2,1])
main_circ.ry(param_0, 3)
main_circ.cy(2,1)
main_circ.ry(-0.325000, 2)
main_circ.cy(0,2)
main_circ.s(2)
main_circ.cz(1,3)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.append(subcirc0,[1,0,3,2])
main_circ.s(0)
main_circ.cy(3,0)
main_circ.s(1)
main_circ.s(0)
main_circ.s(0)
main_circ.cy(1,2)
main_circ.s(1)
main_circ.ry(-0.750000, 0)
main_circ.append(subcirc0,[1,2,0,3])
bindings = {param_0: 0.625000, param_1: -0.313000, param_2: -0.794000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ElidePermutations")
