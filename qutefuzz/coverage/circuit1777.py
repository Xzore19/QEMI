from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.rz(0.995000, qreg_0[0])
		main_circ.h(0)
		main_circ.h(qreg_3[0])
	with else_1:
		main_circ.x(qreg_3[0])
		main_circ.x(1)
		main_circ.x(qreg_2[0])
		main_circ.rz(param_5, 0)
		main_circ.rz(0.864000, qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.s(0)
		main_circ.rz(param_4, qreg_0[1])
		main_circ.h(1)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.x(0)
			main_circ.rz(-0.237000, qreg_0[0])
			main_circ.x(qreg_0[0])
			main_circ.h(0)
		with case_1(1):
			main_circ.s(1)
			main_circ.s(qreg_0[1])
			main_circ.h(1)
			main_circ.x(qreg_2[0])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.s(qreg_2[0])
	with else_1:
		main_circ.h(0)
		main_circ.s(qreg_3[0])
		main_circ.h(0)
		main_circ.x(qreg_0[0])
		main_circ.s(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.s(qreg_0[1])
		main_circ.h(qreg_3[0])
		main_circ.s(qreg_0[0])
		main_circ.rz(0.817000, qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.rz(0.583000, qreg_0[1])
		main_circ.s(qreg_0[0])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(param_1, qreg_3[0])
		main_circ.x(1)
		main_circ.h(1)
		main_circ.s(qreg_2[0])
		main_circ.rz(-0.291000, qreg_0[0])
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.h(qreg_0[1])
			main_circ.x(qreg_2[0])
			main_circ.rz(param_4, qreg_0[0])
			main_circ.rz(param_4, qreg_0[1])
		with case_1(1):
			main_circ.rz(param_4, qreg_3[0])
			main_circ.rz(-0.801000, qreg_0[0])
			main_circ.x(qreg_0[0])
			main_circ.rz(0.456000, 0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.s(0)
		main_circ.rz(0.394000, 0)
		main_circ.x(qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.s(0)
		main_circ.h(qreg_0[1])
		main_circ.h(qreg_0[0])
		main_circ.x(qreg_0[1])
		main_circ.x(qreg_0[0])
	with else_1:
		main_circ.s(qreg_3[0])
		main_circ.barrier(0)
with else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[0])
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.id(qreg_0[1])
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[1])
		with case_1(1):
			main_circ.barrier(1)
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_2[0])
	main_circ.barrier(1)
bindings = {param_1: 0.864000, param_4: -0.725000, param_5: -0.864000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1777", "CollectMultiQBlocks")
