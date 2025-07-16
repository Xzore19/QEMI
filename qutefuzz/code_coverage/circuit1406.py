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
subcirc0.cy(qreg_0[0],qreg_1[1])
subcirc0.s(qreg_1[2])
subcirc0.s(qreg_0[0])
subcirc0.cx(qreg_1[0],qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[2],qreg_3[0])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.cy(qreg_0[2],qreg_3[0])
subcirc1.s(qreg_3[0])

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

main_circ.cy(2,0)
main_circ.append(subcirc0,[0,3,1,2])
main_circ.append(subcirc0,[1,2,0,3])
main_circ.cy(2,1)
main_circ.cy(3,0)
main_circ.z(3)
main_circ.append(subcirc0,[2,0,1,3])
main_circ.s(0)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.append(subcirc1,[0,2,3,1])
main_circ.cx(0,2)
main_circ.cy(0,1)
main_circ.cy(0,2)
main_circ.s(0)
main_circ.cy(2,1)
main_circ.s(0)
main_circ.z(2)
main_circ.cy(3,0)
main_circ.append(subcirc0,[0,1,2,3])
main_circ.cy(3,0)
main_circ.z(3)
main_circ.z(0)
main_circ.s(3)
main_circ.append(subcirc1,[1,0,2,3])
main_circ.cx(3,2)
main_circ.append(subcirc0,[1,3,2,0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "InverseCancellation")
