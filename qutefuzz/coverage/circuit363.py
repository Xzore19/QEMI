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
subcirc0.z(qreg_0[2])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[1])
subcirc0.s(qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.rz(-0.228000, qreg_0[1])

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

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[0],3])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(0.394000, 3)
	main_circ.z(3)
	main_circ.rz(0.895000, 1)
	main_circ.h(qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(-0.826000, qreg_0[0])
	main_circ.rz(0.973000, 3)
	main_circ.rz(-0.372000, 1)
with else_1:
	main_circ.rz(0.754000, qreg_0[1])
	main_circ.append(subcirc0,[2,1,0,qreg_0[1]])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.z(qreg_0[0])
	main_circ.rz(0.467000, 1)
	main_circ.rz(-0.404000, qreg_0[0])
	main_circ.z(qreg_0[1])
	main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],2])
with else_1:
	main_circ.h(2)
	main_circ.s(qreg_0[0])
main_circ.s(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(param_2, qreg_0[0])
	main_circ.s(qreg_0[0])
	main_circ.h(qreg_0[0])
with else_1:
	main_circ.z(2)
	main_circ.s(1)
	main_circ.append(subcirc0,[2,0,1,qreg_0[0]])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(1)
	main_circ.h(0)
with else_1:
	main_circ.id(0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.h(3)
	main_circ.id(3)
with else_1:
	main_circ.barrier(0)
bindings = {param_2: 0.812000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "363")
