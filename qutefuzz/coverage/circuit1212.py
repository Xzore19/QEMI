from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.964000,0.718000, qreg_0[0])
subcirc0.u(0.001000,0.658000,0.176000, qreg_0[2])
subcirc0.ry(-0.523000, qreg_0[1])
subcirc0.u(0.510000,-0.201000,-0.760000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.621000, qreg_1[1])
subcirc1.u(-0.490000,-0.541000,0.898000, qreg_1[0])
subcirc1.ry(-0.554000, qreg_3[0])
subcirc1.u(0.265000,-0.059000,0.421000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.313000, qreg_0[1])
subcirc2.u(0,0,-0.373000, qreg_2[0])
subcirc2.ry(0.705000, qreg_0[1])
subcirc2.u(0,0,-0.538000, qreg_2[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.u(param_0,param_3,param_0, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(0,0,0.989000, 1)
		main_circ.u(0.737000,0.845000,-0.213000, 0)
	with else_1:
		main_circ.u(param_2,-0.670000,-0.410000, 2)
		main_circ.id(1)
main_circ.u(pi/2,0.833000,param_0, 0)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.barrier(1)
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.id(3)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(1)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(1)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0,0,-0.974000, 0)
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.u(0.821000,param_3,param_3, qreg_0[0])
			main_circ.barrier(2)
		main_circ.u(param_2,0,param_2, 3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(-0.152000,param_2,param_1, 2)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(0.002000,param_2,0.161000, 3)
			main_circ.ry(param_0, 1)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.ry(param_1, qreg_0[0])
			main_circ.u(param_3,param_1,param_0, 3)
			main_circ.ry(param_1, 0)
	with case_2(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.ry(param_1, 2)
			main_circ.u(pi/2,-0.635000,param_0, 3)
			main_circ.id(3)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.u(param_1,-0.321000,param_0, 0)
				main_circ.ry(param_1, 0)
				main_circ.ry(0.120000, 3)
				main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(0,param_0,-0.762000, 1)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.u(0.004000,param_2,-0.346000, 3)
				main_circ.ry(param_1, qreg_0[0])
				main_circ.id(2)
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.ry(0.386000, 3)
				main_circ.barrier(2)
	with case_2(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.ry(param_3, qreg_0[0])
				main_circ.u(param_1,param_1,-0.571000, 1)
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.u(0.195000,-0.112000,param_2, qreg_0[0])
				main_circ.ry(0.129000, qreg_0[0])
				main_circ.id(1)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(param_1,0,param_3, qreg_0[0])
		main_circ.id(0)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(pi/2,-0.967000,-0.184000, 2)
		main_circ.u(param_1,param_3,param_2, qreg_0[0])
		main_circ.u(0,0,-0.591000, 3)
		main_circ.u(param_2,param_2,0.634000, qreg_0[0])
		main_circ.u(-0.132000,-0.805000,param_3, 3)
	with else_1:
		main_circ.barrier(1)
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(2)
		with case_1(1):
			main_circ.u(param_1,0.006000,0.786000, 3)
			main_circ.u(param_0,0.702000,param_0, 3)
			main_circ.barrier(3)
main_circ.u(0.987000,-0.044000,param_1, 3)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_1,param_3,0.904000, 2)
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.id(qreg_0[0])
with else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(pi/2,param_2,-0.171000, 1)
		main_circ.id(3)
	with else_1:
		main_circ.u(param_3,-0.676000,0.156000, 2)
		main_circ.u(param_2,param_1,0.090000, 2)
		main_circ.barrier(0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.ry(param_0, qreg_0[0])
			main_circ.ry(-0.187000, 1)
			main_circ.barrier(0)
		with case_1(1):
			main_circ.barrier(3)
with else_2:
	main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.324000, param_1: -0.890000, param_2: -0.559000, param_3: 0.525000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1212")
