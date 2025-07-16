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
subcirc0.y(qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.y(qreg_0[2])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.y(qreg_1[2])
subcirc1.x(qreg_0[0])
subcirc1.s(qreg_1[2])
subcirc1.x(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.s(qreg_2[1])
subcirc2.z(qreg_0[1])
subcirc2.y(qreg_0[0])
subcirc2.s(qreg_2[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_3[0])
subcirc3.y(qreg_3[0])
subcirc3.z(qreg_3[0])
subcirc3.s(qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.z(2)
main_circ.s(2)
main_circ.append(subcirc3,[1,3,2,0])
main_circ.y(1)
main_circ.append(subcirc3,[3,0,2,1])
main_circ.x(0)
main_circ.x(2)
main_circ.x(0)
main_circ.y(3)
main_circ.s(2)
main_circ.x(3)
main_circ.x(3)
main_circ.x(0)
main_circ.z(3)
main_circ.append(subcirc3,[3,1,2,0])
main_circ.y(1)
main_circ.x(0)
main_circ.y(1)
main_circ.x(3)
main_circ.s(0)
main_circ.z(0)
main_circ.z(0)
main_circ.x(0)
main_circ.z(0)
main_circ.append(subcirc3,[2,0,3,1])
main_circ.z(0)
main_circ.s(2)
main_circ.append(subcirc3,[3,0,1,2])
main_circ.append(subcirc3,[2,1,3,0])
main_circ.y(2)
main_circ.x(0)
main_circ.s(3)
main_circ.x(3)
main_circ.z(2)
main_circ.x(0)
main_circ.s(3)
main_circ.z(1)
main_circ.z(1)
main_circ.s(2)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
