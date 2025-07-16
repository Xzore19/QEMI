from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.rx(0.868000, qreg_0[1])
with else_2:
	main_circ.cy(qreg_0[2],qreg_0[0])
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rx(-0.160000, qreg_0[2])
		main_circ.cy(qreg_0[0],qreg_0[2])
		main_circ.cy(qreg_0[3],qreg_0[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(0,0,0.878000, qreg_0[0])
				main_circ.u(param_2,param_1,param_2, qreg_0[0])
				main_circ.rx(-0.010000, qreg_0[2])
				main_circ.cy(qreg_0[2],qreg_0[0])
			with case_1(1):
				main_circ.rx(param_1, qreg_0[1])
				main_circ.rx(param_1, qreg_0[0])
				main_circ.u(param_2,0.091000,param_1, qreg_0[1])
				main_circ.u(-0.064000,param_3,-0.254000, qreg_0[2])
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cy(qreg_0[0],qreg_0[3])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cy(qreg_0[0],qreg_0[1])
		with else_1:
			main_circ.u(0,param_2,param_1, qreg_0[3])
			main_circ.u(param_3,param_1,param_3, qreg_0[0])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.u(0,param_3,param_1, qreg_0[1])
main_circ.cy(qreg_0[3],qreg_0[1])
main_circ.cy(qreg_0[2],qreg_0[3])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.cy(qreg_0[1],qreg_0[0])
		main_circ.cy(qreg_0[1],qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(qreg_0[1],qreg_0[2])
			main_circ.u(param_0,param_0,param_0, qreg_0[3])
			main_circ.cy(qreg_0[1],qreg_0[2])
	with case_2(1):
		main_circ.cy(qreg_0[2],qreg_0[3])
		main_circ.u(0,param_0,param_2, qreg_0[3])
		main_circ.cy(qreg_0[3],qreg_0[2])
		main_circ.cy(qreg_0[3],qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(0.622000, qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(0,0,0.402000, qreg_0[2])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0,0,0.722000, qreg_0[2])
			main_circ.u(param_2,-0.096000,param_0, qreg_0[3])
			main_circ.u(param_2,param_2,-0.456000, qreg_0[1])
			main_circ.u(param_1,param_0,-0.746000, qreg_0[1])
		with case_1(1):
			main_circ.u(param_1,0,0.667000, qreg_0[2])
			main_circ.rx(0.639000, qreg_0[0])
			main_circ.cy(qreg_0[0],qreg_0[3])
			main_circ.cy(qreg_0[3],qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.rx(param_1, qreg_0[2])
		with else_1:
			main_circ.u(param_2,0,0.802000, qreg_0[2])
			main_circ.cy(qreg_0[3],qreg_0[1])
			main_circ.rx(param_1, qreg_0[1])
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(0,0,0.505000, qreg_0[3])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0.377000,-0.880000,param_3, qreg_0[2])
			main_circ.u(param_1,param_2,param_0, qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rx(0.607000, qreg_0[1])
		with else_1:
			main_circ.cy(qreg_0[2],qreg_0[1])
			main_circ.u(param_0,param_1,param_3, qreg_0[0])
			main_circ.id(qreg_0[1])
bindings = {param_0: -0.085000, param_1: 0.064000, param_2: -0.874000, param_3: 0.299000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "695")
