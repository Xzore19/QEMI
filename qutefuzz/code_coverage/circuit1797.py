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
subcirc0.s(qreg_2[0])
subcirc0.h(qreg_2[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.rz(-0.828000, qreg_2[0])
subcirc0.rz(0.807000, qreg_2[0])
subcirc0.rz(0.986000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.h(qreg_0[2])
subcirc1.h(qreg_0[1])
subcirc1.cz(qreg_0[1],qreg_3[0])
subcirc1.s(qreg_0[1])
subcirc1.cz(qreg_3[0],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.351000, qreg_0[2])
subcirc2.rz(0.343000, qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_3[0])
subcirc2.rz(0.407000, qreg_3[0])
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.s(qreg_2[1])
subcirc3.h(qreg_2[0])
subcirc3.rz(-1.000000, qreg_2[1])
subcirc3.h(qreg_2[0])
subcirc3.h(qreg_0[1])
subcirc3.rz(-0.152000, qreg_2[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_0[0],qreg_3[0])
subcirc4.s(qreg_3[0])
subcirc4.cz(qreg_0[0],qreg_0[2])
subcirc4.cz(qreg_0[1],qreg_0[0])
subcirc4.cz(qreg_0[0],qreg_3[0])
subcirc4.h(qreg_3[0])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.s(1)
main_circ.h(3)
main_circ.append(subcirc2,[1,3,0,2])
main_circ.cz(1,3)
main_circ.append(subcirc2,[1,2,0,3])
main_circ.rz(0.431000, 2)
main_circ.s(3)
main_circ.append(subcirc2,[0,3,1,2])
main_circ.rz(param_2, 0)
main_circ.rz(param_1, 0)
main_circ.s(2)
main_circ.cz(0,2)
main_circ.rz(-0.351000, 3)
main_circ.cz(3,2)
main_circ.h(0)
main_circ.h(0)
main_circ.s(1)
main_circ.cz(0,3)
main_circ.cz(1,2)
main_circ.h(1)
main_circ.h(1)
main_circ.h(0)
main_circ.cz(0,3)
main_circ.cz(3,2)
main_circ.cz(2,0)
main_circ.cz(1,0)
main_circ.cz(0,3)
main_circ.cz(1,3)
main_circ.cz(2,1)
main_circ.s(2)
main_circ.h(3)
main_circ.cz(0,1)
main_circ.h(2)
main_circ.s(1)
main_circ.rz(-0.994000, 1)
main_circ.s(0)
main_circ.h(1)
bindings = {param_1: 0.451000, param_2: 0.966000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "HoareOptimizer")
