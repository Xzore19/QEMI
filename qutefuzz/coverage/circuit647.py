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

main_circ.rz(param_0, 2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cx(2,0)
				main_circ.rx(param_1, 1)
		with else_2:
			main_circ.u(param_0,param_1,0.132000, 2)
			main_circ.u(-0.139000,0.940000,0.116000, 0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(param_1,param_0,param_0, 1)
				main_circ.rx(0.045000, 0)
				main_circ.rz(0.491000, 3)
				main_circ.u(param_0,-0.430000,param_1, 2)
				main_circ.u(param_0,0.632000,param_1, 1)
	with else_3:
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(2,1)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(0.124000,param_0,param_0, 0)
				main_circ.rz(param_1, 2)
				main_circ.rz(param_1, 1)
				main_circ.u(-0.568000,param_1,-0.280000, 1)
			with else_1:
				main_circ.cx(3,2)
				main_circ.cx(1,2)
				main_circ.cx(1,0)
with else_4:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rx(-0.027000, 0)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cx(0,2)
					main_circ.u(param_0,-0.231000,0.161000, 3)
					main_circ.cx(3,2)
					main_circ.cx(3,0)
				with case_1(1):
					main_circ.rz(0.852000, 1)
					main_circ.u(param_1,param_0,-0.229000, 1)
					main_circ.rz(param_1, 2)
					main_circ.rz(param_1, 0)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.cx(3,2)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.cx(0,3)
				with else_1:
					main_circ.rx(param_0, 1)
					main_circ.cx(3,0)
					main_circ.cx(2,3)
					main_circ.cx(1,2)
			with case_2(1):
				main_circ.rx(param_1, 0)
				main_circ.rx(param_0, 3)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cx(1,2)
						main_circ.rz(-0.977000, 3)
						main_circ.cx(1,3)
						main_circ.cx(1,0)
					with case_1(1):
						main_circ.rz(-0.069000, 2)
						main_circ.cx(1,0)
						main_circ.u(param_0,0.960000,-0.708000, 3)
						main_circ.rx(param_0, 3)
	with else_3:
		main_circ.cx(0,3)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(param_0,param_0,param_0, 1)
				main_circ.rz(param_1, 3)
			with else_1:
				main_circ.u(-0.864000,param_0,param_0, 0)
				main_circ.rz(param_0, 1)
				main_circ.cx(3,0)
				main_circ.cx(1,0)
				main_circ.rx(-0.999000, 0)
with else_4:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.u(0.860000,-0.188000,param_1, 0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cx(0,1)
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(0)
				main_circ.barrier(2)
			with else_2:
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(3)
				main_circ.barrier(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(2)
				with case_2(1):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(3)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(2)
					main_circ.id(2)
			main_circ.id(1)
		with case_3(1):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(2)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(2)
				main_circ.id(0)
			with else_2:
				main_circ.id(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.barrier(1)
			with else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(0)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.barrier(3)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(1)
					main_circ.barrier(2)
				with case_2(1):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(0)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(0)
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(0)
					main_circ.barrier(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.id(3)
			main_circ.barrier(2)
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.id(0)
		with case_3(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(3)
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
							main_circ.id(3)
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(3)
					main_circ.barrier(0)
				with case_2(1):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.id(1)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.id(0)
				with case_2(1):
					main_circ.barrier(3)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(2)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.barrier(3)
				main_circ.barrier(1)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(0)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.id(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.barrier(0)
			with else_2:
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(0)
				main_circ.id(0)
			main_circ.id(0)
	main_circ.barrier(1)
bindings = {param_0: -0.396000, param_1: -0.381000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "647")
