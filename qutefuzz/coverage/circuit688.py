from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.y(0)
			main_circ.z(qreg_0[1])
			main_circ.rz(param_0, 0)
			main_circ.z(0)
		with case_1(1):
			main_circ.y(qreg_0[2])
			main_circ.y(qreg_0[0])
			main_circ.z(0)
			main_circ.rz(-0.329000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.rz(param_0, qreg_0[3])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rz(param_0, 0)
			main_circ.y(qreg_0[1])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.z(qreg_0[3])
				main_circ.u(param_0,-0.138000,-0.096000, qreg_0[3])
				main_circ.rz(param_1, qreg_0[0])
				main_circ.y(qreg_0[1])
			with case_1(1):
				main_circ.rz(param_0, 1)
				main_circ.y(qreg_0[0])
				main_circ.rz(param_1, 1)
				main_circ.rz(param_1, qreg_0[0])
	with case_2(1):
		main_circ.rz(-0.441000, 1)
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rz(0.440000, 1)
			main_circ.z(qreg_0[1])
		main_circ.y(qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_0[2])
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.z(qreg_0[2])
	with else_1:
		main_circ.rz(0.704000, 1)
		main_circ.u(param_1,param_0,-0.530000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rz(-0.269000, qreg_0[1])
		main_circ.z(qreg_0[3])
		main_circ.y(0)
		main_circ.u(param_1,param_0,0.105000, qreg_0[0])
		main_circ.y(0)
with else_2:
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(qreg_0[2])
			main_circ.y(qreg_0[2])
			main_circ.rz(0.576000, qreg_0[1])
			main_circ.z(1)
		with case_1(1):
			main_circ.u(pi/2,-0.180000,-0.158000, qreg_0[0])
			main_circ.y(qreg_0[0])
			main_circ.z(qreg_0[2])
			main_circ.y(qreg_0[3])
main_circ.z(0)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.u(param_0,param_0,param_0, qreg_0[3])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.rz(-0.721000, qreg_0[3])
			main_circ.u(param_1,param_1,param_1, 1)
			main_circ.u(param_1,param_0,0.413000, qreg_0[1])
		with else_1:
			main_circ.z(qreg_0[1])
			main_circ.z(qreg_0[1])
			main_circ.y(qreg_0[0])
			main_circ.rz(-0.549000, qreg_0[3])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.z(qreg_0[1])
			main_circ.rz(0.679000, 1)
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.barrier(0)
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[3])
		with else_1:
			main_circ.barrier(0)
		main_circ.barrier(0)
bindings = {param_0: 0.867000, param_1: 0.584000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "688", "CollectMultiQBlocks")
