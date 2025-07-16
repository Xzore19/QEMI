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
param_4 = Parameter("param_4")

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(2,3)
		main_circ.u(pi/2,0.967000,param_2, 3)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cz(2,1)
	with else_1:
		main_circ.rx(param_1, 3)
		main_circ.u(pi/2,param_3,-0.391000, 2)
		main_circ.rx(param_2, 2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_3, 2)
			main_circ.rx(param_0, 0)
			main_circ.x(1)
			main_circ.cz(1,3)
		with case_1(1):
			main_circ.u(param_0,0.929000,param_1, 0)
			main_circ.u(pi/2,0.647000,param_4, 3)
			main_circ.cz(3,2)
			main_circ.u(pi/2,0.259000,param_4, 3)
with else_2:
	main_circ.cz(3,1)
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_3, 1)
			main_circ.x(1)
			main_circ.rx(param_3, 3)
			main_circ.x(3)
		with case_1(1):
			main_circ.cz(3,1)
			main_circ.x(2)
			main_circ.cz(2,3)
			main_circ.x(2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.x(0)
		main_circ.rx(param_2, 2)
	with else_1:
		main_circ.cz(3,2)
		main_circ.cz(1,2)
		main_circ.cz(1,3)
		main_circ.rx(param_1, 2)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_3, 3)
			main_circ.x(1)
			main_circ.u(param_0,param_1,param_2, 2)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(pi/2,param_3,0.875000, 2)
			main_circ.x(2)
			main_circ.x(0)
			main_circ.cz(1,0)
		with else_1:
			main_circ.cz(3,0)
			main_circ.u(pi/2,param_0,0.079000, 2)
			main_circ.cz(3,1)
			main_circ.cz(1,0)
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(3,0)
				main_circ.cz(0,2)
				main_circ.cz(1,3)
				main_circ.cz(0,3)
			with case_1(1):
				main_circ.u(pi/2,param_0,param_1, 0)
				main_circ.rx(0.876000, 1)
				main_circ.cz(2,1)
				main_circ.x(2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(pi/2,-0.763000,0.284000, 0)
			main_circ.u(pi/2,param_1,param_0, 1)
			main_circ.cz(2,1)
			main_circ.cz(2,1)
		with case_1(1):
			main_circ.cz(2,1)
			main_circ.id(2)
with else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(2)
	with else_1:
		main_circ.id(0)
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.id(2)
		with case_1(1):
			main_circ.barrier(1)
	main_circ.id(2)
bindings = {param_0: -0.881000, param_1: 0.706000, param_2: 0.893000, param_3: -0.637000, param_4: -0.463000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "40")
