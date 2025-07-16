from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.z(qreg_1[1])
subcirc0.rz(0.973000, qreg_3[0])
subcirc0.h(qreg_1[0])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_3[0])
subcirc0.rz(0.182000, qreg_1[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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
param_4 = Parameter("param_4")

main_circ.append(subcirc0,[qreg_2[1],0,qreg_0[1],qreg_0[0]])
main_circ.x(1)
main_circ.rz(0.938000, qreg_0[0])
main_circ.append(subcirc0,[1,qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.append(subcirc0,[1,qreg_2[1],qreg_0[1],qreg_2[0]])
main_circ.x(qreg_2[0])
main_circ.z(qreg_2[0])
main_circ.x(qreg_2[0])
main_circ.z(1)
main_circ.z(qreg_2[1])
main_circ.rz(0.248000, qreg_0[1])
main_circ.h(qreg_2[0])
main_circ.h(1)
main_circ.rz(-0.773000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],0,qreg_2[1]])
main_circ.rz(0.523000, qreg_2[0])
main_circ.rz(0.103000, qreg_0[1])
main_circ.z(0)
main_circ.append(subcirc0,[qreg_2[1],1,qreg_2[0],0])
main_circ.rz(param_4, qreg_2[1])
main_circ.rz(0.890000, qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.z(qreg_2[0])
main_circ.h(qreg_2[0])
main_circ.rz(-0.573000, qreg_0[0])
main_circ.h(1)
main_circ.rz(0.198000, qreg_0[1])
main_circ.x(1)
bindings = {param_4: 0.501000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Optimize1qGatesDecomposition")
