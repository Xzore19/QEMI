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
subcirc0.cz(qreg_0[0],qreg_0[2])
subcirc0.rx(-0.943000, qreg_0[1])
subcirc0.y(qreg_3[0])
subcirc0.y(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cz(qreg_1[2],qreg_1[1])
subcirc1.u(pi/2,0.246000,0.898000, qreg_1[1])
subcirc1.rx(-0.503000, qreg_1[0])
subcirc1.cz(qreg_1[2],qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.cz(qreg_1[0],qreg_1[1])
subcirc2.rx(-0.008000, qreg_1[1])
subcirc2.cz(qreg_0[0],qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.rx(0.399000, qreg_1[2])
subcirc3.cz(qreg_1[0],qreg_1[1])
subcirc3.rx(-0.358000, qreg_1[2])
subcirc3.u(pi/2,0.542000,0.351000, qreg_1[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.u(pi/2,0.651000,0.319000, qreg_0[0])
main_circ.u(pi/2,-0.772000,-0.396000, qreg_0[1])
main_circ.rx(param_0, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_0[2]])
main_circ.rx(param_1, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.cz(qreg_3[0],qreg_0[2])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
main_circ.y(qreg_0[1])
main_circ.y(qreg_0[1])
main_circ.y(qreg_0[2])
main_circ.u(param_0,-0.915000,param_0, qreg_0[0])
main_circ.u(pi/2,param_0,0.246000, qreg_3[0])
main_circ.rx(param_0, qreg_0[1])
main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[2],qreg_0[0]])
main_circ.rx(-0.070000, qreg_0[0])
bindings = {param_0: 0.946000, param_1: 0.567000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "InverseCancellation")
