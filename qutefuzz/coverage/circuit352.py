from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cz(qreg_1[0],qreg_2[0])
subcirc0.y(qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1.u(pi/2,-0.571000,-0.195000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(2)
main_circ.y(0)
main_circ.u(param_1,param_2,-0.401000, 2)
main_circ.cz(2,0)
main_circ.s(0)
main_circ.s(1)
main_circ.cz(2,1)
main_circ.cz(1,2)
main_circ.y(2)
main_circ.append(subcirc1,[0,3,2,1])
main_circ.y(1)
main_circ.append(subcirc1,[2,1,0,3])
main_circ.append(subcirc1,[3,2,1,0])
main_circ.u(param_0,param_1,-0.895000, 0)
main_circ.u(pi/2,param_2,0.267000, 0)
main_circ.u(param_1,-0.934000,0.963000, 0)
main_circ.append(subcirc1,[1,3,0,2])
main_circ.u(pi/2,-0.658000,param_0, 0)
main_circ.u(pi/2,0.178000,param_1, 0)
main_circ.append(subcirc1,[2,3,1,0])
main_circ.append(subcirc1,[1,0,3,2])
main_circ.cz(0,1)
main_circ.cz(2,0)
main_circ.cz(2,3)
main_circ.cz(0,2)
main_circ.cz(1,3)
main_circ.cz(3,2)
main_circ.cz(0,3)
main_circ.cz(2,3)
main_circ.cz(3,2)
main_circ.cz(3,1)
main_circ.cz(0,3)
main_circ.cz(1,0)
main_circ.cz(2,1)
bindings = {param_0: 0.185000, param_1: 0.089000, param_2: 0.011000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
