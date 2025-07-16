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
param_2 = Parameter("param_2")

main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.h(3)
					with else_1:
						main_circ.u(param_1,param_0,param_1, 2)
						main_circ.u(pi/2,-0.722000,param_1, 2)
						main_circ.h(0)
						main_circ.u(pi/2,param_0,0.703000, 1)
						main_circ.u(0,0,0.348000, 0)
				with case_2(1):
					main_circ.h(3)
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.cy(0,3)
							main_circ.h(0)
							main_circ.cy(2,3)
							main_circ.h(0)
						with case_1(1):
							main_circ.u(param_0,0,param_0, 2)
							main_circ.cy(1,0)
							main_circ.cy(3,1)
							main_circ.h(0)
	with case_4(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.h(3)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.cy(0,2)
						main_circ.cy(3,1)
					with else_1:
						main_circ.cy(3,1)
						main_circ.h(0)
			with case_3(1):
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.u(param_2,param_1,0.802000, 0)
						main_circ.u(0,param_1,-0.305000, 0)
					with else_1:
						main_circ.h(2)
						main_circ.u(param_1,param_1,param_1, 0)
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.cy(2,0)
							main_circ.u(pi/2,0.710000,-0.840000, 2)
							main_circ.cy(3,0)
							main_circ.u(param_0,param_0,0.821000, 0)
						with case_1(1):
							main_circ.cy(0,2)
							main_circ.u(0,0,-0.768000, 2)
							main_circ.cy(1,3)
							main_circ.cy(1,3)
main_circ.cy(2,3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.u(param_2,-0.567000,0.655000, 1)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.h(0)
				main_circ.cy(2,1)
				main_circ.cy(3,0)
				main_circ.u(0,0,0.814000, 1)
	with else_3:
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.u(0,param_1,param_0, 3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(3)
					main_circ.u(param_2,param_0,-0.449000, 0)
					main_circ.u(pi/2,param_1,param_1, 0)
					main_circ.h(0)
					main_circ.h(2)
				with else_1:
					main_circ.u(pi/2,-0.052000,-0.816000, 1)
					main_circ.u(param_1,param_0,param_1, 1)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cy(1,3)
						main_circ.cy(2,3)
						main_circ.u(pi/2,param_1,param_2, 2)
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(2)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(3)
				main_circ.barrier(1)
bindings = {param_0: 0.734000, param_1: 0.068000, param_2: -0.459000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "105", "CollectMultiQBlocks")
