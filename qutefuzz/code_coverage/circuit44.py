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

main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.u(param_0,0,param_0, 3)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(-0.863000,0.685000,param_1, 3)
				main_circ.u(param_0,param_0,param_0, 3)
				main_circ.u(param_0,param_1,0.546000, 3)
				main_circ.ry(0.574000, 1)
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0.532000,param_0,0.435000, 1)
				main_circ.u(param_0,0,param_1, 2)
				main_circ.u(pi/2,param_0,0.395000, 1)
			with else_1:
				main_circ.u(0,0,0.601000, 1)
	with case_3(1):
		main_circ.u(param_1,0.152000,0.603000, 1)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(param_0, 3)
				main_circ.u(param_0,-0.612000,param_0, 3)
				main_circ.u(param_0,0,-0.289000, 1)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.ry(param_1, 3)
				main_circ.u(param_1,0,-0.571000, 0)
				main_circ.u(param_1,-0.444000,param_0, 1)
				main_circ.u(0,0,param_1, 3)
				main_circ.ry(param_1, 1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.u(pi/2,-0.833000,param_1, 0)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.ry(param_1, 2)
				main_circ.u(param_0,-0.473000,-0.805000, 2)
				main_circ.u(param_1,-0.697000,0.236000, 3)
				main_circ.u(-0.256000,param_0,-0.329000, 1)
			with case_1(1):
				main_circ.ry(param_0, 3)
				main_circ.u(-0.540000,param_0,-0.627000, 0)
				main_circ.u(0,0,param_1, 3)
				main_circ.u(-0.966000,param_1,param_1, 3)
	with else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,param_1,-0.379000, 1)
				main_circ.u(param_1,param_1,-0.721000, 1)
				main_circ.u(param_1,-0.956000,0.534000, 2)
				main_circ.ry(param_1, 2)
			with case_1(1):
				main_circ.ry(param_1, 3)
				main_circ.u(param_0,param_1,0.401000, 2)
				main_circ.u(pi/2,-0.609000,-0.071000, 2)
				main_circ.u(param_0,0.549000,param_0, 1)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.ry(param_1, 0)
				main_circ.u(0,param_0,0.555000, 3)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(param_0,-0.213000,-0.059000, 0)
					main_circ.u(param_1,0,-1.000000, 2)
					main_circ.u(0,0,0.368000, 1)
					main_circ.u(0,0,param_1, 1)
				with else_1:
					main_circ.u(-0.677000,0.248000,param_1, 2)
					main_circ.u(0,param_0,-0.642000, 0)
					main_circ.u(param_0,param_0,param_1, 0)
			with case_2(1):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.u(0,param_1,param_1, 3)
					main_circ.id(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(3)
	with case_3(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.id(3)
		with else_2:
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(0)
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.barrier(0)
		main_circ.id(0)
bindings = {param_0: -0.475000, param_1: -0.446000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "44", "ResetAfterMeasureSimplification")
