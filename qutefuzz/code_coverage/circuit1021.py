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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.u(param_5,param_5,-0.493000, 1)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cx(1,2)
					main_circ.u(pi/2,-0.293000,param_0, 0)
			with else_2:
				main_circ.cx(0,3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cz(2,0)
					main_circ.h(3)
					main_circ.u(pi/2,param_2,0.801000, 0)
		with case_3(1):
			main_circ.cx(0,2)
			main_circ.cx(3,1)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cx(2,3)
						main_circ.h(0)
						main_circ.h(0)
						main_circ.h(3)
					with case_1(1):
						main_circ.h(2)
						main_circ.cz(3,0)
						main_circ.u(pi/2,0.016000,param_1, 2)
						main_circ.u(pi/2,param_0,-0.357000, 2)
with else_4:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,param_1,param_4, 2)
						main_circ.cx(1,2)
						main_circ.h(1)
						main_circ.h(0)
					with case_1(1):
						main_circ.u(param_5,-0.843000,param_2, 1)
						main_circ.h(2)
						main_circ.cz(1,0)
						main_circ.cz(2,3)
			with case_2(1):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.h(0)
					main_circ.cz(2,1)
					main_circ.u(pi/2,param_2,-0.229000, 1)
					main_circ.cx(0,3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.cx(2,3)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.cz(1,3)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.cx(0,2)
							main_circ.cx(0,1)
							main_circ.u(param_1,param_0,param_2, 1)
							main_circ.cx(0,1)
						with case_1(1):
							main_circ.h(3)
							main_circ.cz(3,1)
							main_circ.h(3)
							main_circ.u(param_1,param_1,-0.144000, 3)
				with case_2(1):
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.h(1)
						main_circ.cz(1,2)
						main_circ.cz(1,3)
						main_circ.u(pi/2,-0.100000,param_2, 2)
		with case_3(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.u(pi/2,-0.768000,param_2, 1)
						main_circ.cx(0,1)
						main_circ.cx(1,0)
						main_circ.h(3)
						main_circ.h(2)
					with else_1:
						main_circ.h(3)
						main_circ.u(param_2,-0.194000,param_5, 1)
				with case_2(1):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.h(2)
						main_circ.cx(3,0)
					with else_1:
						main_circ.cz(2,0)
						main_circ.cx(3,2)
						main_circ.cz(0,3)
main_circ.cx(3,2)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.cz(2,3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.h(1)
					with else_1:
						main_circ.h(3)
						main_circ.id(3)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(2)
					main_circ.id(3)
				with case_2(1):
					main_circ.id(2)
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.id(1)
				with case_2(1):
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.id(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(3)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.barrier(1)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(3)
				main_circ.id(0)
			with else_2:
				main_circ.barrier(0)
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(2)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(2)
					main_circ.id(2)
				with case_2(1):
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(0)
					main_circ.id(2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.barrier(3)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(1)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(2)
							with case_1(1):
								main_circ.barrier(0)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(3)
						main_circ.id(2)
					with case_2(1):
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(2)
						with else_1:
							main_circ.id(0)
						main_circ.id(1)
				main_circ.barrier(2)
			with case_3(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(2)
						main_circ.id(1)
					with case_2(1):
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.barrier(3)
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(0)
					main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(3)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(0)
							with case_1(1):
								main_circ.id(2)
						main_circ.measure(2, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.id(3)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.measure(1, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(3)
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(2)
						main_circ.measure(1, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(3)
						main_circ.measure(2, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(2)
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(1, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(3)
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(2)
							with case_1(1):
								main_circ.barrier(2)
						main_circ.measure(0, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(2)
							with case_1(1):
								main_circ.barrier(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(2)
						with else_1:
							main_circ.id(1)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(1)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(1, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(3)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(2)
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(0)
						main_circ.measure(3, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(1)
						main_circ.id(1)
					with case_2(1):
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.id(3)
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(0)
						main_circ.id(0)
				main_circ.id(3)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.barrier(3)
			with case_3(1):
				main_circ.barrier(1)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(3)
				main_circ.id(3)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.id(1)
			with else_2:
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(2)
					main_circ.id(3)
				with case_2(1):
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(3)
					main_circ.id(1)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(3)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(3)
				main_circ.id(0)
			with else_2:
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.id(0)
				main_circ.barrier(3)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(0)
				main_circ.id(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(1)
				main_circ.id(1)
			main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(3)
				main_circ.barrier(3)
			main_circ.barrier(0)
		main_circ.id(0)
	with case_4(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.barrier(1)
			with case_3(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(2)
					main_circ.id(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.barrier(2)
						main_circ.id(3)
					with case_2(1):
						main_circ.id(3)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(1)
					main_circ.id(2)
				with else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.id(1)
				main_circ.id(0)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(3)
					main_circ.barrier(2)
				with case_2(1):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(3)
					main_circ.id(1)
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.barrier(3)
					main_circ.barrier(3)
				with case_2(1):
					main_circ.barrier(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(2)
					main_circ.barrier(2)
				with case_2(1):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.barrier(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.id(2)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.id(3)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(2)
				main_circ.id(0)
			with else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(1)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.id(2)
			main_circ.id(3)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(2)
			with else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(3)
				main_circ.barrier(0)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.id(3)
			with else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(1)
				main_circ.id(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(1)
				main_circ.id(3)
			with else_2:
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.id(2)
				main_circ.id(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(3)
				main_circ.id(3)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.id(0)
				with case_2(1):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.barrier(1)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(3)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.id(1)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(3)
				main_circ.barrier(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(2)
				main_circ.id(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(3)
				main_circ.id(2)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(0)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(2)
				main_circ.barrier(0)
			with else_2:
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.id(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.id(0)
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.id(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.id(2)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(2)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(3)
					main_circ.id(0)
				with case_2(1):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.id(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.barrier(1)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(0)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(1)
				main_circ.barrier(0)
			with else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(1)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(3)
				main_circ.id(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.id(2)
				main_circ.id(1)
			with else_2:
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.id(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(0)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(3)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(3)
				main_circ.id(1)
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(1)
				main_circ.id(1)
			main_circ.id(2)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.id(2)
						main_circ.barrier(1)
					with case_2(1):
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(0)
							with case_1(1):
								main_circ.barrier(2)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.barrier(2)
						main_circ.id(3)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.id(1)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.id(1)
					main_circ.id(1)
				with else_2:
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(2)
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.barrier(1)
						main_circ.id(2)
					with case_2(1):
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(0)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(3)
						main_circ.measure(2, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(0)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(3)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.id(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.id(2)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(2)
						with else_1:
							main_circ.id(0)
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(3)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.id(3)
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(2)
						main_circ.measure(0, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(3)
							with case_1(1):
								main_circ.id(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(2)
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.id(0)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(0)
							with case_1(1):
								main_circ.barrier(3)
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.id(2)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(0)
							with case_1(1):
								main_circ.id(3)
						main_circ.barrier(3)
					with case_2(1):
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.barrier(3)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(3)
						main_circ.id(3)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.measure(1, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.id(3)
						main_circ.measure(1, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(1)
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(3)
						with else_1:
							main_circ.id(2)
						main_circ.measure(3, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(2)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.id(2)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.id(1)
					with case_2(1):
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(0)
							with case_1(1):
								main_circ.barrier(2)
						main_circ.measure(2, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(0)
							with case_1(1):
								main_circ.barrier(3)
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(1)
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.id(3)
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(3)
							with case_1(1):
								main_circ.barrier(1)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(2)
						with else_1:
							main_circ.barrier(2)
						main_circ.barrier(0)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(1)
					main_circ.id(3)
				with else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.id(2)
					main_circ.barrier(0)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(0)
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.id(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(3)
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.id(0)
					main_circ.id(0)
				with else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(0)
					main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(2)
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.id(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(2)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(2)
					main_circ.barrier(0)
				main_circ.id(3)
			with case_3(1):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.id(3)
					main_circ.barrier(0)
				with else_2:
					main_circ.id(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.barrier(2)
					with case_2(1):
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(3)
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(0)
						main_circ.measure(3, creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(2)
							with case_1(1):
								main_circ.id(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.id(3)
						main_circ.measure(2, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(2)
						with else_1:
							main_circ.id(2)
						main_circ.measure(1, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(0)
						main_circ.barrier(1)
				main_circ.barrier(1)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(0)
				main_circ.barrier(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.barrier(3)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.barrier(3)
			with else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(1)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(0)
				main_circ.id(2)
			main_circ.id(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(2)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.barrier(0)
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(3)
					main_circ.barrier(2)
				main_circ.barrier(1)
			with case_3(1):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(1)
					main_circ.id(3)
				with else_2:
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.id(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(2)
					main_circ.barrier(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.id(3)
					main_circ.barrier(2)
				with else_2:
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(0)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(0)
					main_circ.barrier(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.id(3)
					with case_2(1):
						main_circ.barrier(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.barrier(2)
				main_circ.barrier(3)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(1)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.barrier(3)
				main_circ.id(1)
			with case_3(1):
				main_circ.id(2)
		main_circ.id(1)
bindings = {param_0: -0.881000, param_1: -0.326000, param_2: -0.769000, param_4: 0.356000, param_5: -0.877000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1021", "Optimize1qGatesSimpleCommutation")
