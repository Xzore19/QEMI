from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.s(qreg_0[0])
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.s(0)
	with else_2:
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.x(3)
				main_circ.u(param_2,param_0,param_2, 3)
				main_circ.u(0.254000,param_0,param_3, 3)
				main_circ.u(param_0,param_0,-0.113000, qreg_0[0])
			with case_1(1):
				main_circ.s(2)
				main_circ.s(0)
				main_circ.s(3)
				main_circ.u(param_2,param_3,0.325000, 3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.u(param_2,-0.797000,param_0, 0)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.x(1)
					main_circ.u(pi/2,param_3,-0.566000, 2)
					main_circ.u(param_0,param_0,param_3, 3)
				with else_1:
					main_circ.x(qreg_0[0])
					main_circ.u(pi/2,0.089000,-0.145000, 2)
					main_circ.u(0.154000,param_2,param_2, 2)
			with case_2(1):
				main_circ.s(3)
				main_circ.s(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.x(0)
					main_circ.s(1)
					main_circ.s(3)
	with case_3(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.s(1)
					main_circ.u(param_3,param_0,0.250000, qreg_0[0])
					main_circ.s(0)
					main_circ.s(2)
					main_circ.u(0.555000,param_2,param_3, 0)
				with else_1:
					main_circ.x(0)
					main_circ.s(3)
					main_circ.u(param_1,0.252000,0.479000, 2)
					main_circ.x(qreg_0[0])
					main_circ.u(param_2,0.963000,param_2, 3)
			with case_2(1):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.u(param_3,-0.051000,param_2, 1)
					main_circ.x(qreg_0[0])
					main_circ.u(pi/2,0.527000,0.965000, 1)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.u(0.402000,-0.935000,param_0, qreg_0[0])
					main_circ.s(0)
					main_circ.u(param_1,0.989000,0.473000, 0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(qreg_0[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.u(param_0,-0.654000,-0.415000, 1)
					main_circ.u(pi/2,0.190000,param_1, 1)
					main_circ.s(1)
					main_circ.x(0)
				with case_1(1):
					main_circ.s(1)
					main_circ.u(pi/2,param_0,param_2, 1)
					main_circ.u(0.717000,-0.796000,0.846000, 1)
					main_circ.x(0)
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(pi/2,-0.248000,param_3, 2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.x(qreg_0[0])
			with else_1:
				main_circ.u(pi/2,0.283000,0.712000, 1)
				main_circ.u(param_2,-0.086000,param_1, 3)
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.x(0)
				main_circ.u(param_2,param_3,param_3, 1)
				main_circ.barrier(0)
			with else_1:
				main_circ.id(2)
bindings = {param_0: -0.994000, param_1: 0.751000, param_2: 0.295000, param_3: -0.961000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "916")
