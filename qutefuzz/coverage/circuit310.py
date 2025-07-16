from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.rx(param_2, qreg_2[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.ry(param_5, qreg_0[1])
					main_circ.rx(param_2, qreg_2[0])
					main_circ.u(0.630000,0.269000,param_1, qreg_0[1])
					main_circ.cy(qreg_0[1],qreg_2[0])
				with case_1(1):
					main_circ.u(-0.629000,param_1,0.242000, qreg_0[1])
					main_circ.cy(qreg_2[0],qreg_0[0])
					main_circ.rx(0.973000, qreg_0[1])
					main_circ.u(param_1,param_5,-0.902000, qreg_2[1])
		with else_2:
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.ry(param_4, qreg_2[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(param_4,param_4,param_0, qreg_2[0])
			with else_1:
				main_circ.u(param_3,-0.014000,param_4, qreg_0[0])
				main_circ.rx(0.582000, qreg_0[0])
	with case_3(1):
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.ry(param_1, qreg_2[0])
				main_circ.rx(-0.233000, qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cy(qreg_0[1],qreg_2[0])
					main_circ.ry(param_5, qreg_0[0])
				with else_1:
					main_circ.u(0.283000,param_4,param_0, qreg_2[0])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.rx(param_4, qreg_0[0])
						main_circ.u(param_5,param_0,0.389000, qreg_0[1])
						main_circ.cy(qreg_0[0],qreg_2[0])
						main_circ.ry(param_3, qreg_0[1])
					with case_1(1):
						main_circ.cy(qreg_2[0],qreg_0[1])
						main_circ.u(param_0,param_0,param_0, qreg_0[1])
						main_circ.ry(-0.439000, qreg_0[1])
						main_circ.u(param_5,param_3,-0.205000, qreg_0[1])
main_circ.u(0.612000,param_2,param_0, qreg_2[1])
main_circ.rx(0.472000, qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cy(qreg_0[1],qreg_2[1])
				main_circ.u(param_4,-0.375000,param_2, qreg_2[0])
				main_circ.u(param_2,0.466000,param_0, qreg_0[1])
				main_circ.ry(param_1, qreg_0[1])
				main_circ.cy(qreg_0[1],qreg_2[0])
			with else_1:
				main_circ.cy(qreg_2[0],qreg_0[0])
				main_circ.cy(qreg_2[0],qreg_0[0])
				main_circ.cy(qreg_0[1],qreg_2[0])
		with case_2(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cy(qreg_2[1],qreg_2[0])
				main_circ.cy(qreg_0[0],qreg_2[1])
				main_circ.cy(qreg_2[1],qreg_0[1])
				main_circ.rx(param_4, qreg_2[1])
				main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.cy(qreg_2[0],qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[1],qreg_0[0])
					main_circ.ry(param_3, qreg_0[1])
					main_circ.cy(qreg_2[1],qreg_0[1])
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_2[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[1])
				with case_1(1):
					main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_2[0])
			main_circ.barrier(qreg_0[0])
	with case_3(1):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_2[1])
			with else_1:
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_2[0])
			with else_1:
				main_circ.id(qreg_2[1])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_2[1])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.barrier(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.id(qreg_2[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.barrier(qreg_2[0])
			with case_2(1):
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_0[1])
		main_circ.barrier(qreg_2[0])
bindings = {param_0: -0.321000, param_1: 0.317000, param_2: -0.659000, param_3: 0.705000, param_4: -0.297000, param_5: -0.153000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "310", "CommutativeCancellation")
