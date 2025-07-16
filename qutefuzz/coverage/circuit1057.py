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

main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(-0.737000,-0.651000,param_0, 3)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(param_1,0.175000,0.606000, 0)
						main_circ.y(0)
						main_circ.y(3)
						main_circ.rx(param_1, 3)
					with case_1(1):
						main_circ.rx(param_1, 2)
						main_circ.rx(-0.049000, 0)
						main_circ.h(1)
						main_circ.h(3)
	with case_4(1):
		main_circ.y(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.h(0)
					main_circ.rx(-0.608000, 3)
					main_circ.h(1)
					main_circ.rx(0.950000, 3)
				with else_1:
					main_circ.u(-0.376000,0.599000,0.689000, 0)
					main_circ.rx(param_0, 1)
					main_circ.u(-0.038000,param_1,param_0, 3)
					main_circ.u(param_0,param_0,0.900000, 1)
main_circ.rx(param_0, 2)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(0.533000,-0.229000,-0.632000, 2)
				main_circ.h(0)
				main_circ.u(-0.698000,param_1,param_0, 0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_1,0.233000,param_1, 2)
				main_circ.rx(param_1, 1)
				main_circ.rx(0.239000, 0)
				main_circ.h(3)
				main_circ.h(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.y(2)
with else_4:
	main_circ.y(1)
	main_circ.y(1)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rx(-0.614000, 3)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.h(0)
			with else_1:
				main_circ.y(2)
				main_circ.u(param_0,0.446000,param_1, 1)
				main_circ.h(3)
				main_circ.h(0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(param_1,param_0,0.139000, 0)
				main_circ.y(3)
				main_circ.u(param_1,param_0,0.369000, 3)
				main_circ.y(1)
with else_4:
	main_circ.u(-0.891000,0.571000,param_1, 1)
	main_circ.u(param_1,-0.435000,param_0, 3)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rx(-0.035000, 0)
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.rx(0.704000, 3)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.u(0.630000,param_1,0.783000, 3)
					main_circ.rx(-0.916000, 2)
			main_circ.rx(param_0, 1)
		with case_3(1):
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.h(3)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.y(2)
					with else_1:
						main_circ.rx(param_1, 1)
						main_circ.u(param_0,-0.427000,param_1, 2)
						main_circ.id(2)
				with case_2(1):
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(2)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(0)
					main_circ.barrier(0)
bindings = {param_0: -0.954000, param_1: 0.950000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1057")
