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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.u(0,param_3,param_1, 3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,param_3,-0.157000, 2)
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(param_1,param_1,param_0, 0)
		main_circ.y(2)
		main_circ.y(2)
		main_circ.u(param_0,param_0,param_3, 2)
	with else_1:
		main_circ.u(-0.798000,0.398000,param_2, 2)
		main_circ.u(pi/2,param_3,-0.519000, 0)
		main_circ.u(0.044000,param_0,-0.149000, 1)
		main_circ.u(0,0,param_2, 2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.y(0)
			main_circ.u(param_0,0,-0.324000, 0)
			main_circ.u(-0.414000,param_2,param_1, 3)
			main_circ.u(0,param_2,0.585000, 0)
		with case_1(1):
			main_circ.u(param_0,param_0,0.572000, 2)
			main_circ.u(param_3,0,param_3, 3)
			main_circ.u(param_2,0.382000,param_3, 3)
			main_circ.u(param_1,0,0.852000, 1)
with else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(0,0,0.281000, 0)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(param_0,param_3,-0.030000, 2)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.y(1)
				main_circ.u(param_0,param_2,0.315000, 2)
				main_circ.u(param_3,param_3,-0.456000, 0)
				main_circ.u(param_3,0.458000,param_0, 0)
			with case_1(1):
				main_circ.u(param_0,0,0.325000, 3)
				main_circ.y(2)
				main_circ.y(3)
				main_circ.y(1)
	with case_2(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(pi/2,param_3,0.148000, 3)
			main_circ.y(0)
			main_circ.u(pi/2,param_1,-0.428000, 3)
			main_circ.u(param_2,param_2,0.453000, 0)
		with else_1:
			main_circ.y(1)
			main_circ.y(0)
			main_circ.u(pi/2,0.430000,param_3, 0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(param_1,0.899000,0.651000, 2)
		main_circ.y(1)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,param_3,-0.194000, 2)
				main_circ.y(1)
				main_circ.u(0.067000,param_2,0.129000, 2)
				main_circ.y(3)
			with case_1(1):
				main_circ.u(param_3,param_1,0.767000, 2)
				main_circ.u(0,param_0,-0.672000, 0)
				main_circ.u(param_1,param_0,-0.472000, 0)
				main_circ.u(-0.183000,param_3,0.874000, 3)
	with case_2(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.u(param_0,param_2,param_3, 1)
				main_circ.y(1)
				main_circ.u(param_1,0.236000,0.633000, 0)
				main_circ.y(0)
			with case_1(1):
				main_circ.id(0)
bindings = {param_0: 0.616000, param_1: 0.742000, param_2: 0.984000, param_3: -0.758000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "307")
