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
subcirc0.u(0,0,0.055000, qreg_0[0])
subcirc0.u(0,0,0.414000, qreg_0[3])
subcirc0.u(pi/2,0.143000,-0.294000, qreg_0[0])
subcirc0.ry(0.123000, qreg_0[3])
subcirc0.u(pi/2,0.404000,0.823000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.123000,-0.631000, qreg_0[0])
subcirc1.rz(-0.250000, qreg_3[0])
subcirc1.rz(0.330000, qreg_0[1])
subcirc1.u(0,0,0.551000, qreg_0[0])
subcirc1.ry(0.861000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
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

main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_0,0.323000,param_2, qreg_1[1])
		main_circ.id(qreg_1[0])
	main_circ.id(qreg_1[2])
with else_2:
	main_circ.barrier(qreg_1[1])
main_circ.ry(param_2, qreg_1[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(param_1,param_3,-0.299000, qreg_1[1])
		main_circ.ry(param_2, qreg_1[0])
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[1])
			with case_1(1):
				main_circ.ry(-0.426000, qreg_1[1])
				main_circ.u(param_3,param_3,param_2, qreg_1[0])
				main_circ.u(param_1,param_0,0.432000, qreg_1[0])
				main_circ.barrier(qreg_1[1])
	with case_2(1):
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_3,-0.271000,-0.608000, qreg_0[0])
			main_circ.u(0,0,-0.496000, qreg_0[0])
			main_circ.u(param_3,param_2,-0.142000, qreg_1[2])
			main_circ.ry(0.816000, qreg_0[0])
			main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(param_0,param_3,param_2, qreg_1[0])
			main_circ.u(param_2,param_3,param_1, qreg_1[2])
			main_circ.u(0,param_0,-0.285000, qreg_1[1])
			main_circ.u(param_1,param_1,-0.787000, qreg_1[0])
		with else_1:
			main_circ.id(qreg_1[1])
	with case_2(1):
		main_circ.u(pi/2,param_3,-0.771000, qreg_1[0])
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.barrier(qreg_1[2])
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[2])
			with case_1(1):
				main_circ.barrier(qreg_1[1])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rz(-0.162000, qreg_1[2])
			main_circ.barrier(qreg_1[2])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[1])
			with case_1(1):
				main_circ.barrier(qreg_1[2])
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rz(-0.185000, qreg_0[0])
			main_circ.ry(param_3, qreg_0[0])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(qreg_1[0])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.rz(-0.004000, qreg_0[0])
		main_circ.u(pi/2,-0.941000,-0.827000, qreg_1[1])
		main_circ.u(pi/2,-0.796000,-0.601000, qreg_1[1])
		main_circ.ry(0.615000, qreg_1[2])
	with else_1:
		main_circ.ry(param_2, qreg_0[0])
		main_circ.u(0,param_0,0.031000, qreg_1[1])
		main_circ.id(qreg_1[0])
with else_2:
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_1[1])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(-0.885000, qreg_1[1])
		main_circ.u(param_2,0,param_3, qreg_1[0])
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(qreg_1[1])
	with else_1:
		main_circ.rz(0.740000, qreg_1[1])
		main_circ.ry(param_3, qreg_1[0])
		main_circ.ry(param_3, qreg_1[2])
		main_circ.u(param_1,-0.996000,0.808000, qreg_1[2])
		main_circ.ry(0.693000, qreg_1[0])
main_circ.measure(qreg_1[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_1[1])
	with else_1:
		main_circ.rz(-0.976000, qreg_1[1])
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(0,0,param_0, qreg_0[0])
				main_circ.id(qreg_1[0])
			with case_1(1):
				main_circ.rz(-0.559000, qreg_1[2])
				main_circ.barrier(qreg_1[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(param_0, qreg_1[0])
				main_circ.barrier(qreg_1[1])
			with case_1(1):
				main_circ.u(pi/2,-0.652000,param_3, qreg_1[0])
				main_circ.u(0,0,0.449000, qreg_0[0])
				main_circ.id(qreg_1[2])
	with case_2(1):
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_1[1])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.ry(0.159000, qreg_0[0])
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.barrier(qreg_1[1])
		main_circ.measure(qreg_1[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.ry(param_0, qreg_1[2])
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.barrier(qreg_1[2])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[2])
			with case_1(1):
				main_circ.ry(param_1, qreg_0[0])
				main_circ.rz(param_3, qreg_0[0])
				main_circ.rz(-0.413000, qreg_1[1])
				main_circ.barrier(qreg_1[1])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_1[1])
	main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(pi/2,-0.538000,-0.507000, qreg_1[2])
		main_circ.u(param_0,param_2,param_2, qreg_1[2])
		main_circ.u(0,param_2,param_3, qreg_1[2])
bindings = {param_0: 0.826000, param_1: -0.406000, param_2: 0.634000, param_3: -0.856000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1959", "Collect2qBlocks")
