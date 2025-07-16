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

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.h(3)
with else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(0)
				main_circ.h(0)
				main_circ.rx(param_3, 1)
				main_circ.s(3)
			with case_1(1):
				main_circ.s(0)
				main_circ.h(0)
				main_circ.s(0)
				main_circ.s(1)
	with else_2:
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(1,2)
				main_circ.s(1)
				main_circ.h(1)
				main_circ.rx(param_0, 3)
			with case_1(1):
				main_circ.h(0)
				main_circ.cx(0,3)
				main_circ.h(2)
				main_circ.h(0)
main_circ.cx(3,0)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.h(0)
		main_circ.cx(0,1)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.s(0)
			with else_1:
				main_circ.h(2)
				main_circ.s(3)
	with case_3(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(2)
						main_circ.h(1)
						main_circ.s(0)
						main_circ.h(3)
					with case_1(1):
						main_circ.h(0)
						main_circ.h(2)
						main_circ.h(3)
						main_circ.s(2)
			with case_2(1):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(2)
				with else_1:
					main_circ.h(3)
					main_circ.cx(2,1)
					main_circ.cx(1,0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cx(1,0)
				main_circ.cx(1,3)
				main_circ.cx(1,2)
				main_circ.cx(3,2)
			with case_1(1):
				main_circ.cx(1,3)
				main_circ.cx(3,0)
				main_circ.cx(3,0)
				main_circ.s(2)
with else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.h(1)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rx(param_0, 2)
				main_circ.h(1)
				main_circ.barrier(0)
			with case_1(1):
				main_circ.barrier(3)
	with else_2:
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(2)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(1)
		main_circ.barrier(1)
bindings = {param_0: -0.552000, param_3: -0.279000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1004", "CollectMultiQBlocks")
