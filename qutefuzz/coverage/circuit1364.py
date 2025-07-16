from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.s(3)
			main_circ.u(0,param_1,-0.151000, 3)
			main_circ.s(1)
			main_circ.h(1)
		with case_1(1):
			main_circ.u(-0.694000,param_0,0.432000, 3)
			main_circ.u(-0.907000,param_1,param_1, 1)
			main_circ.u(param_1,param_1,param_0, 3)
			main_circ.h(2)
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.s(0)
			main_circ.u(0,param_1,-0.397000, 0)
			main_circ.s(0)
			main_circ.h(3)
		with case_1(1):
			main_circ.s(3)
			main_circ.s(2)
			main_circ.h(3)
			main_circ.u(param_0,-0.002000,-0.086000, 2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(param_0,param_0,param_1, 2)
	main_circ.h(0)
	main_circ.s(2)
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0.622000,param_1,param_0, 1)
			main_circ.u(param_1,param_0,-0.350000, 2)
			main_circ.u(param_0,param_0,-0.416000, 2)
			main_circ.h(3)
		with case_1(1):
			main_circ.h(3)
			main_circ.h(3)
			main_circ.h(2)
			main_circ.s(3)
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0.853000,param_0,0.423000, 2)
		main_circ.h(3)
		main_circ.u(0,param_1,0.255000, 1)
		main_circ.s(1)
		main_circ.h(1)
main_circ.h(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,param_1,param_1, 2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(0,0,-0.995000, 2)
			main_circ.u(-0.015000,0.197000,-0.603000, 0)
			main_circ.u(-0.381000,param_1,param_0, 0)
			main_circ.h(3)
		with case_1(1):
			main_circ.u(0,param_1,param_1, 3)
			main_circ.s(3)
			main_circ.h(3)
			main_circ.u(param_0,param_0,0.502000, 1)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.h(2)
		main_circ.u(-0.988000,-0.425000,param_0, 3)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.s(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(0)
		main_circ.barrier(2)
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.id(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(3)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.id(1)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(1)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.barrier(3)
		main_circ.barrier(2)
bindings = {param_0: 0.583000, param_1: 0.915000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1364")
