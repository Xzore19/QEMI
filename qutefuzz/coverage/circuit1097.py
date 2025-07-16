from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.u(pi/2,-0.662000,0.852000, 2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,param_0,0.954000, 0)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.rz(0.558000, 1)
				main_circ.u(pi/2,0.515000,param_1, qreg_0[0])
				main_circ.s(qreg_0[0])
				main_circ.rz(-0.100000, 3)
			with case_1(1):
				main_circ.h(qreg_0[0])
				main_circ.s(3)
				main_circ.h(qreg_0[1])
				main_circ.rz(param_2, qreg_0[1])
	with else_2:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,0.677000,param_2, 1)
				main_circ.h(qreg_0[0])
				main_circ.h(3)
				main_circ.rz(param_0, 0)
			with case_1(1):
				main_circ.h(3)
				main_circ.u(param_1,0.904000,param_3, 0)
				main_circ.h(qreg_0[1])
				main_circ.s(qreg_0[1])
main_circ.s(0)
main_circ.u(pi/2,0.580000,param_3, qreg_0[0])
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.s(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.h(1)
					main_circ.u(param_2,-0.778000,0.690000, 1)
					main_circ.u(param_2,param_3,param_0, 1)
			with case_2(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.rz(0.505000, qreg_0[1])
				with else_1:
					main_circ.rz(0.235000, qreg_0[0])
					main_circ.u(param_1,-0.488000,-0.950000, 3)
					main_circ.s(3)
					main_circ.rz(0.394000, 3)
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rz(param_1, qreg_0[1])
				main_circ.rz(-0.440000, qreg_0[1])
				main_circ.rz(param_3, 0)
			with else_1:
				main_circ.s(1)
				main_circ.s(0)
		with else_2:
			main_circ.rz(0.261000, 3)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.h(3)
				main_circ.h(3)
				main_circ.u(pi/2,param_0,-0.920000, 2)
			with else_1:
				main_circ.u(param_1,0.117000,param_0, qreg_0[0])
				main_circ.u(param_0,-0.391000,param_1, qreg_0[1])
				main_circ.h(qreg_0[0])
				main_circ.rz(param_1, 0)
main_circ.u(param_3,0.003000,param_1, qreg_0[1])
main_circ.u(pi/2,0.394000,-0.345000, 0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.s(qreg_0[1])
			main_circ.h(1)
		with else_1:
			main_circ.s(3)
			main_circ.rz(param_2, qreg_0[0])
			main_circ.s(qreg_0[1])
			main_circ.h(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(qreg_0[0])
			main_circ.h(2)
			main_circ.h(1)
			main_circ.rz(-0.333000, qreg_0[0])
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.h(0)
				main_circ.s(2)
				main_circ.u(pi/2,param_1,param_0, 3)
				main_circ.s(3)
			with case_1(1):
				main_circ.barrier(qreg_0[1])
	with else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(0)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(3)
		main_circ.id(0)
bindings = {param_0: 0.165000, param_1: -0.740000, param_2: -0.646000, param_3: 0.136000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1097")
