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
param_3 = Parameter("param_3")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.rx(0.228000, 0)
					main_circ.s(1)
					main_circ.rx(-0.854000, 2)
					main_circ.rx(-0.232000, 1)
					main_circ.rz(param_3, 1)
				with else_1:
					main_circ.h(1)
		with case_3(1):
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.rz(-0.536000, 2)
						main_circ.rz(param_1, 0)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.s(1)
						main_circ.rx(0.047000, 0)
						main_circ.rx(0.084000, 0)
						main_circ.rx(-0.654000, 3)
					with else_1:
						main_circ.s(3)
						main_circ.s(3)
						main_circ.rx(param_2, 3)
						main_circ.rz(param_2, 3)
						main_circ.h(2)
				with case_2(1):
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.s(0)
							main_circ.rz(-0.371000, 2)
							main_circ.s(3)
							main_circ.rz(param_1, 3)
						with case_1(1):
							main_circ.s(0)
							main_circ.h(3)
							main_circ.h(2)
							main_circ.rx(0.337000, 0)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.rz(0.159000, 0)
		main_circ.rz(0.742000, 2)
		main_circ.s(1)
		main_circ.rx(0.662000, 1)
	with case_4(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.h(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.rz(param_2, 2)
				with else_2:
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.rx(-0.258000, 2)
						main_circ.s(2)
						main_circ.rz(0.862000, 2)
					with else_1:
						main_circ.s(1)
						main_circ.h(2)
						main_circ.rz(0.928000, 0)
						main_circ.s(1)
						main_circ.rx(-0.261000, 2)
			with case_3(1):
				main_circ.h(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(2)
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(3)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(1)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(1)
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(2)
						with else_1:
							main_circ.barrier(3)
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.id(0)
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(3)
						with else_1:
							main_circ.id(2)
						main_circ.measure(2, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(2)
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(2)
						with else_1:
							main_circ.id(2)
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(2)
						with else_1:
							main_circ.barrier(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(3)
						main_circ.measure(1, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(3)
							with case_1(1):
								main_circ.barrier(1)
						main_circ.id(3)
					with case_2(1):
						main_circ.barrier(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.id(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(0)
							with case_1(1):
								main_circ.barrier(2)
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(3)
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.id(2)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.id(2)
						main_circ.measure(0, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.barrier(0)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(2)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(3, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.id(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.id(2)
					with case_2(1):
						main_circ.measure(3, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(3)
						with else_1:
							main_circ.id(0)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.barrier(1)
						main_circ.barrier(0)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(2)
						with else_1:
							main_circ.barrier(0)
						main_circ.measure(2, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(3)
						with else_1:
							main_circ.barrier(0)
						main_circ.measure(3, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.barrier(3)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(2)
							with case_1(1):
								main_circ.barrier(0)
						main_circ.id(1)
					with case_2(1):
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(0)
						main_circ.id(0)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(3)
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(0)
					main_circ.id(1)
				main_circ.barrier(0)
bindings = {param_1: 0.123000, param_2: -0.934000, param_3: 0.511000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1899")
