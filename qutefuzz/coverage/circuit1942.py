from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.u(pi/2,-0.607000,0.741000, qreg_0[3])
subcirc0.h(qreg_0[1])
subcirc0.ry(-0.314000, qreg_0[1])
subcirc0.u(pi/2,-0.121000,-0.954000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.h(qreg_0[1])
subcirc1.h(qreg_2[0])
subcirc1.h(qreg_2[0])
subcirc1.h(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[2])
subcirc2.y(qreg_3[0])
subcirc2.h(qreg_0[0])
subcirc2.h(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.barrier(0)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.u(param_1,param_0,param_1, 2)
			main_circ.barrier(qreg_0[0])
	with else_2:
		main_circ.barrier(0)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,param_1,param_1, 0)
					main_circ.id(3)
				with case_1(1):
					main_circ.u(pi/2,param_1,-0.931000, 0)
					main_circ.h(0)
					main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(param_1,param_0,param_1, qreg_0[0])
		with case_2(1):
			main_circ.barrier(1)
with else_3:
	main_circ.y(qreg_0[0])
	main_circ.barrier(1)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(param_0, 2)
				main_circ.barrier(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(param_0, 0)
				main_circ.barrier(1)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.h(1)
					main_circ.ry(param_1, 3)
					main_circ.ry(param_0, qreg_0[0])
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.h(0)
					main_circ.u(param_1,-0.673000,0.600000, 2)
					main_circ.u(param_1,param_1,-0.604000, 0)
					main_circ.u(param_0,0.787000,0.733000, 2)
	with case_3(1):
		main_circ.u(param_0,param_0,0.157000, 3)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.h(0)
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(param_0, 2)
				main_circ.y(qreg_0[0])
				main_circ.y(2)
				main_circ.y(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.ry(-0.502000, 1)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.u(pi/2,param_0,param_0, 0)
				main_circ.ry(0.116000, 0)
				main_circ.h(2)
				main_circ.id(qreg_0[0])
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.h(3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_1,0.731000,0.409000, 2)
				main_circ.y(2)
				main_circ.y(1)
				main_circ.ry(-0.697000, qreg_0[0])
			with case_1(1):
				main_circ.h(qreg_0[0])
				main_circ.barrier(1)
with else_3:
	main_circ.ry(param_0, 3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(pi/2,-0.160000,param_0, 3)
					main_circ.ry(param_1, 0)
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.ry(0.121000, qreg_0[0])
					main_circ.id(2)
				main_circ.h(1)
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.y(qreg_0[0])
						main_circ.barrier(1)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.ry(0.975000, 0)
					main_circ.h(3)
					main_circ.ry(-0.238000, 2)
					main_circ.ry(0.998000, 1)
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.ry(0.212000, 3)
					main_circ.u(param_0,-0.784000,-0.201000, 1)
					main_circ.ry(0.840000, qreg_0[0])
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(1)
		main_circ.id(1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.h(3)
				main_circ.h(3)
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.y(qreg_0[0])
				main_circ.y(0)
				main_circ.ry(param_0, 2)
				main_circ.barrier(1)
	with else_2:
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(0)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.id(3)
with else_3:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_0[0])
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(3)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.id(1)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(1)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(2)
			main_circ.barrier(qreg_0[0])
	main_circ.barrier(1)
bindings = {param_0: -0.684000, param_1: 0.011000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1942")
