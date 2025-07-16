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
subcirc0.ry(0.911000, qreg_2[1])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_2[0])
subcirc0.s(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(-0.883000, qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.ry(-0.032000, qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(-0.436000, qreg_0[1])
subcirc2.rx(0.418000, qreg_0[0])
subcirc2.s(qreg_0[1])
subcirc2.rx(0.932000, qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc0,[0,1,qreg_0[0],qreg_1[0]])
main_circ.append(subcirc0,[0,qreg_1[0],1,qreg_1[2]])
main_circ.ry(param_0, 1)
main_circ.s(qreg_1[0])
main_circ.y(1)
main_circ.y(qreg_0[0])
main_circ.s(qreg_1[1])
main_circ.y(qreg_0[0])
main_circ.y(qreg_1[1])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_1[1],qreg_1[2]])
main_circ.append(subcirc0,[qreg_1[2],0,qreg_1[0],qreg_1[1]])
main_circ.y(qreg_0[0])
main_circ.s(qreg_1[1])
main_circ.ry(param_1, qreg_1[0])
main_circ.ry(param_3, qreg_1[2])
main_circ.rx(param_3, 0)
main_circ.s(0)
main_circ.ry(param_2, 1)
main_circ.append(subcirc0,[qreg_1[2],qreg_0[0],1,0])
main_circ.ry(param_3, 1)
main_circ.append(subcirc2,[qreg_1[2],1,0,qreg_1[1]])
main_circ.y(1)
main_circ.ry(-0.054000, qreg_1[0])
main_circ.y(qreg_1[2])
main_circ.rx(param_1, qreg_1[2])
main_circ.s(qreg_1[0])
main_circ.s(qreg_1[2])
main_circ.y(qreg_0[0])
main_circ.append(subcirc2,[qreg_1[0],qreg_1[1],1,qreg_1[2]])
bindings = {param_0: 0.755000, param_1: -0.175000, param_2: -0.427000, param_3: 0.430000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
