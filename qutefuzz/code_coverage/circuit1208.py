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
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rz(-0.309000, qreg_0[1])
			main_circ.u(0,0,param_6, qreg_0[1])
		with else_1:
			main_circ.s(2)
		main_circ.cy(0,3)
	with case_2(1):
		main_circ.u(param_4,0,param_6, 0)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(qreg_0[1],qreg_0[0])
				main_circ.u(param_1,0,0.562000, 2)
				main_circ.u(param_6,param_1,param_1, 0)
				main_circ.u(0,0,param_2, 1)
			with case_1(1):
				main_circ.u(param_5,0,param_1, 2)
				main_circ.u(0,0,0.092000, 3)
				main_circ.rz(0.503000, 1)
				main_circ.rz(-0.965000, 1)
main_circ.u(param_6,param_3,param_6, 3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.s(0)
		main_circ.u(param_5,0,param_2, 0)
	with else_1:
		main_circ.cy(2,1)
		main_circ.rz(param_6, 3)
		main_circ.rz(param_2, 3)
with else_2:
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cy(2,qreg_0[0])
			main_circ.rz(param_6, 0)
			main_circ.s(2)
			main_circ.u(param_5,0,-0.985000, 2)
		with case_1(1):
			main_circ.rz(0.715000, 3)
			main_circ.s(qreg_0[0])
			main_circ.s(qreg_0[0])
			main_circ.rz(-0.872000, qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rz(param_0, 2)
			main_circ.u(param_3,0,-0.573000, qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(0.851000, 1)
				main_circ.s(2)
				main_circ.cy(3,qreg_0[1])
				main_circ.rz(param_4, 0)
			with case_1(1):
				main_circ.s(0)
				main_circ.s(qreg_0[0])
				main_circ.u(param_6,param_3,param_5, 2)
				main_circ.s(0)
	with case_2(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.u(0,0,-0.130000, qreg_0[0])
				main_circ.s(qreg_0[1])
				main_circ.s(2)
				main_circ.s(1)
			with case_1(1):
				main_circ.rz(param_4, 3)
				main_circ.cy(3,1)
				main_circ.cy(qreg_0[0],qreg_0[1])
				main_circ.cy(qreg_0[1],1)
main_circ.cy(1,qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cy(2,1)
		main_circ.cy(0,qreg_0[1])
		main_circ.cy(2,qreg_0[1])
		main_circ.cy(0,qreg_0[1])
with else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cy(0,3)
	main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.cy(qreg_0[0],1)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(0,3)
		main_circ.u(param_4,param_5,param_2, qreg_0[0])
	with else_1:
		main_circ.cy(1,2)
		main_circ.cy(qreg_0[1],0)
		main_circ.cy(0,3)
		main_circ.cy(qreg_0[1],qreg_0[0])
		main_circ.id(3)
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(2)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(1)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(1)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(2)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(3)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.id(3)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(1)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.id(0)
	main_circ.barrier(0)
bindings = {param_0: 0.608000, param_1: -0.443000, param_2: -0.943000, param_3: -0.778000, param_4: 0.770000, param_5: 0.222000, param_6: 0.622000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1208")
