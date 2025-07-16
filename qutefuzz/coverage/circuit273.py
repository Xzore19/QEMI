from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.035000,-0.360000, qreg_0[1])
subcirc0.u(pi/2,-0.720000,-0.445000, qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0.z(qreg_3[0])
subcirc0.u(pi/2,0.680000,-0.291000, qreg_0[0])
subcirc0.u(0,0,-0.013000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.u(pi/2,0.575000,0.039000, qreg_0[0])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,0.573000, qreg_0[0])
subcirc1.z(qreg_0[3])
subcirc1.z(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.z(qreg_0[0])
main_circ.u(param_1,param_1,0.965000, qreg_0[0])
main_circ.z(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.x(qreg_3[0])
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.u(pi/2,param_0,param_0, qreg_0[0])
		main_circ.u(param_1,param_1,param_1, qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0,0,-0.979000, qreg_0[1])
			main_circ.barrier(0)
		with case_1(1):
			main_circ.barrier(qreg_0[1])
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(0)
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_3[0])
		with case_1(1):
			main_circ.z(qreg_3[0])
			main_circ.u(pi/2,-0.821000,param_0, qreg_2[0])
			main_circ.id(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(pi/2,param_0,-0.375000, 0)
		main_circ.x(qreg_3[0])
		main_circ.u(param_1,0,param_0, qreg_0[1])
		main_circ.barrier(qreg_0[1])
	with else_1:
		main_circ.u(0,0,param_0, 0)
with else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.id(qreg_0[1])
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.x(0)
			main_circ.x(0)
			main_circ.z(qreg_0[1])
			main_circ.x(qreg_0[0])
		with case_1(1):
			main_circ.id(qreg_3[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_0,0,0.769000, 0)
			main_circ.z(qreg_2[0])
			main_circ.x(0)
			main_circ.u(pi/2,param_1,0.069000, qreg_2[0])
		with case_1(1):
			main_circ.z(qreg_0[0])
			main_circ.id(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.x(qreg_2[0])
			main_circ.u(param_0,param_1,0.976000, qreg_2[0])
			main_circ.u(param_0,0.241000,0.750000, qreg_0[1])
			main_circ.barrier(qreg_0[1])
		main_circ.x(0)
	with case_2(1):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0,param_0,param_1, qreg_0[1])
			main_circ.u(0,param_0,param_1, 0)
			main_circ.x(qreg_3[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_1,param_0,-0.399000, qreg_2[0])
				main_circ.u(0,param_0,param_0, qreg_0[1])
				main_circ.z(qreg_0[1])
				main_circ.x(qreg_0[0])
			with case_1(1):
				main_circ.x(qreg_3[0])
				main_circ.x(qreg_0[0])
				main_circ.u(param_1,0,param_1, qreg_3[0])
				main_circ.z(qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_2[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.x(qreg_2[0])
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(pi/2,param_0,param_0, qreg_0[0])
		with else_1:
			main_circ.z(qreg_0[1])
		main_circ.barrier(0)
	with case_2(1):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(pi/2,0.898000,param_1, qreg_0[0])
			main_circ.id(qreg_3[0])
		main_circ.z(qreg_0[1])
		main_circ.u(0,0,param_1, qreg_2[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(qreg_0[1])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.z(qreg_0[1])
				main_circ.x(0)
				main_circ.id(qreg_3[0])
			with case_1(1):
				main_circ.id(qreg_3[0])
main_circ.x(0)
main_circ.x(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(param_0,0,param_1, 0)
		main_circ.barrier(0)
	with else_1:
		main_circ.x(qreg_0[1])
		main_circ.barrier(qreg_0[1])
with else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.x(qreg_0[1])
		main_circ.u(0,param_1,param_0, 0)
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[1])
		with case_1(1):
			main_circ.z(qreg_0[0])
			main_circ.z(qreg_0[1])
			main_circ.x(qreg_2[0])
			main_circ.id(qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0,0,0.746000, qreg_2[0])
		main_circ.u(param_0,-0.015000,0.990000, qreg_0[1])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.z(qreg_2[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0,param_1,-0.237000, 0)
		main_circ.x(qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.barrier(0)
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.barrier(qreg_3[0])
bindings = {param_0: -0.073000, param_1: 0.785000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "273")
