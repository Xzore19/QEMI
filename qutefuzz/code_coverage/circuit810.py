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
subcirc0.u(0.200000,-0.436000,-0.969000, qreg_0[0])
subcirc0.x(qreg_2[1])
subcirc0.z(qreg_0[1])
subcirc0.u(0.021000,-0.384000,-0.796000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.013000,-0.286000,0.880000, qreg_3[0])
subcirc1.x(qreg_3[0])
subcirc1.u(0.203000,0.367000,0.394000, qreg_1[0])
subcirc1.h(qreg_3[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.x(qreg_2[1])
		main_circ.u(0.475000,0.427000,param_0, qreg_0[0])
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.h(qreg_2[1])
		main_circ.z(qreg_0[1])
	with else_1:
		main_circ.h(qreg_0[1])
		main_circ.h(qreg_0[0])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.x(qreg_2[1])
		main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_2[1]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.z(qreg_0[1])
		main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_0[1],qreg_0[0]])
	with else_1:
		main_circ.u(0.655000,param_0,param_1, qreg_0[0])
		main_circ.z(qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.x(qreg_2[0])
	with else_1:
		main_circ.z(qreg_0[1])
		main_circ.append(subcirc1,[qreg_2[1],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.x(qreg_0[0])
		with else_1:
			main_circ.x(qreg_0[0])
			main_circ.x(qreg_0[1])
			main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_2[1]])
	with case_2(1):
		main_circ.append(subcirc0,[qreg_2[1],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.x(qreg_0[1])
		main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_2[1]])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.z(qreg_0[1])
	main_circ.measure(qreg_2[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(qreg_2[0])
		main_circ.u(param_0,param_1,-0.217000, qreg_2[1])
		main_circ.u(param_1,param_1,param_0, qreg_2[1])
		main_circ.append(subcirc1,[qreg_2[0],qreg_2[1],qreg_0[0],qreg_0[1]])
	with else_1:
		main_circ.u(param_1,-0.784000,param_1, qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(-0.922000,0.078000,0.310000, qreg_2[1])
		main_circ.id(qreg_2[1])
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(qreg_2[1])
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_2[1])
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(qreg_2[1])
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.id(qreg_2[0])
bindings = {param_0: 0.604000, param_1: -0.198000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "810", "OptimizeAnnotated")
