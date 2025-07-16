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
subcirc0.s(qreg_0[3])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.y(qreg_0[2])
subcirc0.s(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.s(qreg_2[1])
subcirc1.u(0,0,0.461000, qreg_0[1])
subcirc1.u(0,0,0.041000, qreg_0[1])
subcirc1.y(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.y(qreg_1[2])
subcirc2.cz(qreg_1[1],qreg_1[2])
subcirc2.y(qreg_1[1])
subcirc2.y(qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.y(qreg_0[1])
subcirc3.y(qreg_0[1])
subcirc3.s(qreg_0[0])
subcirc3.cz(qreg_0[2],qreg_0[3])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cz(qreg_0[3],qreg_0[1])
subcirc4.u(0,0,0.517000, qreg_0[1])
subcirc4.u(0,0,0.286000, qreg_0[2])
subcirc4.s(qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(0)
main_circ.s(1)
main_circ.cz(0,1)
main_circ.cz(0,3)
main_circ.u(0,param_0,param_2, 0)
main_circ.append(subcirc2,[3,0,1,2])
main_circ.cz(3,1)
main_circ.append(subcirc4,[2,0,3,1])
main_circ.u(0,0,param_1, 1)
main_circ.s(3)
main_circ.s(0)
main_circ.cz(0,3)
main_circ.append(subcirc2,[0,3,1,2])
main_circ.s(1)
main_circ.u(0,param_1,0.162000, 0)
main_circ.u(param_2,param_0,0.059000, 3)
main_circ.append(subcirc4,[2,3,1,0])
main_circ.append(subcirc2,[2,0,3,1])
main_circ.s(3)
main_circ.y(3)
main_circ.u(0,param_2,-0.678000, 2)
main_circ.u(param_0,param_2,0.124000, 2)
main_circ.s(0)
main_circ.cz(3,2)
main_circ.cz(2,1)
main_circ.cz(1,2)
main_circ.cz(2,0)
main_circ.cz(1,2)
main_circ.cz(3,0)
main_circ.cz(0,1)
main_circ.y(3)
main_circ.u(0,0,-0.385000, 1)
main_circ.append(subcirc2,[3,0,2,1])
main_circ.y(3)
main_circ.s(0)
main_circ.s(2)
bindings = {param_0: -0.087000, param_1: 0.400000, param_2: 0.084000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveDiagonalGatesBeforeMeasure")
