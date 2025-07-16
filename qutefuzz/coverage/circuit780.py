from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.cx(qreg_3[0],qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_3[0])
subcirc0.y(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_0[0])
subcirc1.h(qreg_0[0])
subcirc1.y(qreg_1[0])
subcirc1.cx(qreg_1[0],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[2],qreg_0[3])
subcirc2.y(qreg_0[0])
subcirc2.h(qreg_0[2])
subcirc2.cz(qreg_0[1],qreg_0[2])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.cz(0,qreg_1[1])
main_circ.append(subcirc0,[qreg_3[0],0,qreg_1[0],qreg_1[1]])
main_circ.append(subcirc1,[qreg_1[1],0,qreg_1[0],qreg_0[0]])
main_circ.cz(0,qreg_1[1])
main_circ.cz(qreg_1[1],qreg_3[0])
main_circ.h(qreg_0[0])
main_circ.append(subcirc1,[qreg_1[0],qreg_3[0],qreg_1[1],qreg_0[0]])
main_circ.y(qreg_1[1])
main_circ.h(0)
main_circ.cz(0,qreg_1[1])
main_circ.h(qreg_1[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_1[1],0])
main_circ.cx(qreg_1[1],qreg_0[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_1[0],qreg_1[1]])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.append(subcirc1,[qreg_1[0],0,qreg_3[0],qreg_1[1]])
main_circ.y(qreg_1[0])
main_circ.cx(0,qreg_1[0])
main_circ.append(subcirc1,[qreg_1[1],qreg_3[0],qreg_1[0],qreg_0[0]])
main_circ.cx(qreg_1[1],0)
main_circ.h(qreg_1[0])
main_circ.h(qreg_0[0])
main_circ.y(qreg_1[0])
main_circ.h(0)
main_circ.append(subcirc0,[qreg_1[1],qreg_1[0],qreg_0[0],qreg_3[0]])
main_circ.y(0)
main_circ.cz(0,qreg_0[0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
