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

main_circ.x(qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.u(param_0,param_1,-0.989000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.u(0,param_1,param_1, qreg_0[1])
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.cz(qreg_0[3],1)
					main_circ.cz(qreg_0[2],qreg_0[3])
					main_circ.u(param_0,0,param_0, qreg_0[2])
					main_circ.x(qreg_0[3])
				with case_1(1):
					main_circ.cz(qreg_0[0],qreg_0[3])
					main_circ.cz(0,qreg_0[2])
					main_circ.y(1)
					main_circ.y(qreg_0[2])
		with case_2(1):
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0,0,0.925000, qreg_0[3])
				main_circ.x(0)
			with else_1:
				main_circ.y(qreg_0[2])
			main_circ.cz(qreg_0[3],qreg_0[2])
with else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.cz(qreg_0[3],0)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(0,0,0.737000, qreg_0[0])
			main_circ.u(param_1,0,0.989000, 0)
			main_circ.u(param_1,param_0,param_1, 0)
			main_circ.y(qreg_0[1])
			main_circ.x(1)
		with else_1:
			main_circ.x(qreg_0[2])
	with else_2:
		main_circ.x(1)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.cz(qreg_0[0],qreg_0[3])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.u(param_0,0,param_1, 1)
					main_circ.y(qreg_0[0])
					main_circ.u(param_1,param_1,0.762000, 0)
			with case_2(1):
				main_circ.x(qreg_0[1])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.u(param_0,0,0.647000, qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(0,param_1,param_1, qreg_0[3])
					main_circ.y(qreg_0[0])
					main_circ.cz(qreg_0[2],qreg_0[3])
					main_circ.cz(qreg_0[3],1)
					main_circ.cz(qreg_0[0],qreg_0[3])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.cz(1,0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cz(qreg_0[1],0)
					main_circ.cz(qreg_0[3],qreg_0[0])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cz(0,qreg_0[3])
					main_circ.u(0,0,-0.028000, 0)
			with case_2(1):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(qreg_0[3],qreg_0[0])
					main_circ.u(0,param_0,param_0, qreg_0[3])
				with else_1:
					main_circ.cz(0,qreg_0[1])
					main_circ.x(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.cz(1,0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.y(0)
						main_circ.u(0,param_1,0.451000, qreg_0[3])
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[3])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.barrier(qreg_0[0])
			with case_2(1):
				main_circ.barrier(1)
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.barrier(1)
			with case_2(1):
				main_circ.barrier(0)
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.id(0)
			with case_2(1):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[3])
					with case_1(1):
						main_circ.id(0)
				main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.barrier(qreg_0[0])
		main_circ.barrier(qreg_0[1])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.id(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[2])
				with case_1(1):
					main_circ.id(qreg_0[2])
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.id(1)
		main_circ.id(1)
bindings = {param_0: 0.827000, param_1: -0.003000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "622")
