from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rx(-0.569000, 2)
				main_circ.u(param_1,param_1,param_0, 1)
				main_circ.ry(param_0, 2)
				main_circ.ry(param_1, 2)
			with case_1(1):
				main_circ.ry(0.018000, 0)
				main_circ.rz(param_1, 0)
				main_circ.rx(0.203000, 2)
				main_circ.rx(param_1, 3)
	with else_2:
		main_circ.u(param_1,-0.239000,0.849000, 0)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rz(param_0, 0)
			main_circ.rx(0.236000, 1)
			main_circ.u(param_0,param_1,-0.984000, 2)
		with else_1:
			main_circ.u(param_1,param_0,0.124000, 2)
			main_circ.rx(0.585000, 3)
			main_circ.rz(param_0, 2)
			main_circ.ry(0.333000, 0)
			main_circ.ry(-0.175000, 3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.rx(param_0, 0)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rx(param_1, 1)
				main_circ.u(param_1,0.887000,0.714000, 0)
				main_circ.rx(param_1, 2)
				main_circ.u(0.970000,-0.530000,param_0, 2)
			with else_1:
				main_circ.rx(param_1, 2)
				main_circ.ry(param_0, 0)
		with else_2:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rx(0.265000, 0)
				main_circ.rz(-0.253000, 1)
				main_circ.ry(param_0, 0)
			with else_1:
				main_circ.rz(param_0, 1)
				main_circ.rx(0.429000, 2)
				main_circ.u(param_0,0.115000,param_1, 2)
				main_circ.rx(0.924000, 1)
				main_circ.rz(0.831000, 2)
	with case_3(1):
		main_circ.u(-0.588000,0.794000,param_1, 0)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rx(param_0, 3)
				main_circ.u(param_0,param_0,-0.910000, 3)
				main_circ.u(-0.317000,param_0,param_1, 3)
				main_circ.rz(param_1, 2)
				main_circ.ry(0.075000, 3)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.rz(0.234000, 1)
				main_circ.u(-0.656000,param_1,-0.353000, 2)
				main_circ.u(param_0,-0.621000,param_0, 2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(param_0, 3)
				main_circ.ry(param_0, 1)
				main_circ.rx(param_0, 3)
				main_circ.rx(-0.081000, 3)
		with case_2(1):
			main_circ.rx(0.429000, 1)
			main_circ.rz(-0.050000, 3)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.ry(0.217000, 2)
				main_circ.rx(param_0, 2)
				main_circ.rz(-0.418000, 3)
			with else_1:
				main_circ.u(0.263000,param_1,param_0, 1)
				main_circ.ry(param_1, 2)
				main_circ.u(param_0,-0.139000,-0.604000, 3)
				main_circ.u(0.218000,param_0,-0.926000, 1)
				main_circ.rx(param_1, 1)
with else_3:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.ry(param_1, 3)
				main_circ.id(1)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(2)
			main_circ.barrier(2)
		with case_2(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.barrier(1)
bindings = {param_0: -0.516000, param_1: -0.147000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "382")
