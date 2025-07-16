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
subcirc0.y(qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.s(qreg_3[0])
subcirc0.h(qreg_0[1])
subcirc0.rz(-0.659000, qreg_3[0])
subcirc0.rz(-0.487000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(-0.399000, qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1.y(qreg_0[2])
subcirc1.s(qreg_0[2])
subcirc1.h(qreg_0[2])
subcirc1.s(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.append(subcirc1,[2,qreg_0[1],1,0])
main_circ.rz(param_1, 1)
main_circ.append(subcirc0,[qreg_0[0],1,qreg_0[1],3])
main_circ.append(subcirc1,[1,3,2,qreg_0[0]])
main_circ.append(subcirc1,[1,qreg_0[0],qreg_0[1],0])
main_circ.s(qreg_0[1])
main_circ.rz(param_0, qreg_0[0])
main_circ.rz(param_1, 0)
main_circ.s(2)
main_circ.append(subcirc1,[qreg_0[0],2,0,1])
main_circ.append(subcirc1,[qreg_0[1],0,1,2])
main_circ.h(1)
main_circ.h(qreg_0[1])
main_circ.s(0)
main_circ.s(qreg_0[0])
main_circ.s(qreg_0[1])
main_circ.s(qreg_0[0])
main_circ.y(3)
bindings = {param_0: -0.151000, param_1: 0.763000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "OptimizeAnnotated")
