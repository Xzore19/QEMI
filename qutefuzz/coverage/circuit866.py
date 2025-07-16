from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
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

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.x(qreg_2[1])
			main_circ.x(qreg_0[0])
		with else_1:
			main_circ.s(qreg_0[1])
	with else_2:
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.s(qreg_0[0])
				main_circ.u(0.112000,-0.484000,param_1, 0)
				main_circ.x(0)
				main_circ.rz(param_1, 0)
			with case_1(1):
				main_circ.u(0.688000,param_0,-0.398000, qreg_0[1])
				main_circ.s(0)
				main_circ.x(qreg_0[0])
				main_circ.u(param_1,-0.116000,-0.060000, 0)
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rz(param_0, qreg_0[1])
			main_circ.rz(0.372000, qreg_2[0])
			main_circ.u(-0.344000,param_1,0.248000, qreg_2[0])
			main_circ.rz(0.269000, qreg_2[1])
			main_circ.u(0.211000,param_1,param_1, qreg_0[0])
	with else_2:
		main_circ.s(qreg_2[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0.305000,param_0,0.252000, 0)
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(param_1,0.032000,param_0, qreg_2[1])
			main_circ.rz(0.467000, qreg_2[0])
			main_circ.x(qreg_2[1])
			main_circ.x(qreg_2[1])
main_circ.u(-0.557000,param_1,-0.714000, 0)
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.s(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(param_1, qreg_2[1])
				main_circ.u(0.234000,0.722000,0.036000, qreg_2[1])
				main_circ.rz(0.862000, qreg_2[1])
				main_circ.u(param_1,param_1,param_0, qreg_0[1])
			with case_1(1):
				main_circ.s(qreg_2[0])
				main_circ.x(0)
				main_circ.rz(param_1, qreg_2[0])
				main_circ.rz(0.821000, qreg_2[1])
	with else_2:
		main_circ.s(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(qreg_2[1])
			main_circ.s(0)
			main_circ.rz(param_0, qreg_0[1])
		main_circ.u(-0.279000,param_0,0.753000, qreg_2[1])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.u(param_1,-0.773000,-0.035000, qreg_0[1])
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.rz(param_1, 0)
	with else_2:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(param_1, qreg_0[0])
				main_circ.rz(param_0, 0)
				main_circ.rz(param_0, qreg_2[1])
				main_circ.rz(-0.563000, qreg_2[0])
			with case_1(1):
				main_circ.s(0)
				main_circ.u(-0.804000,-0.243000,0.482000, qreg_0[0])
				main_circ.rz(param_0, qreg_0[0])
				main_circ.rz(-0.132000, 0)
with else_3:
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.s(qreg_0[1])
					main_circ.s(qreg_0[0])
					main_circ.u(param_1,param_0,param_0, qreg_2[0])
					main_circ.u(0.441000,0.554000,param_1, qreg_0[0])
				with case_1(1):
					main_circ.rz(param_1, 0)
					main_circ.s(qreg_0[0])
					main_circ.u(param_1,-0.200000,param_0, 0)
					main_circ.x(qreg_0[1])
		with case_2(1):
			main_circ.rz(-0.349000, 0)
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.u(param_0,0.777000,param_0, qreg_0[0])
					main_circ.s(qreg_0[1])
					main_circ.x(qreg_0[1])
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.145000, param_1: -0.658000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "866", "CollectLinearFunctions")
