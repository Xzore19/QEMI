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

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,0.698000,-0.572000, 1)
	main_circ.u(param_1,-0.118000,0.982000, 2)
	main_circ.x(3)
	main_circ.u(param_0,param_0,param_0, 3)
main_circ.u(0.671000,param_0,param_1, 3)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.s(0)
				main_circ.s(0)
				main_circ.u(param_1,0.838000,-0.086000, 0)
				main_circ.u(param_0,0.504000,param_0, 1)
			with case_1(1):
				main_circ.x(1)
				main_circ.rz(param_1, 3)
				main_circ.x(3)
				main_circ.x(2)
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.x(1)
				main_circ.u(param_1,-0.025000,0.795000, 2)
				main_circ.s(2)
				main_circ.rz(param_1, 3)
			with case_1(1):
				main_circ.u(param_0,-0.934000,0.212000, 1)
				main_circ.x(0)
				main_circ.rz(0.490000, 2)
				main_circ.u(param_1,param_0,param_0, 0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.rz(param_0, 1)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.x(3)
		main_circ.u(0.685000,0.325000,-0.785000, 2)
	main_circ.u(-0.312000,-0.126000,-0.706000, 1)
with else_2:
	main_circ.u(param_0,0.474000,param_0, 1)
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.x(0)
		main_circ.x(1)
		main_circ.u(0.219000,-0.958000,param_1, 3)
	with else_1:
		main_circ.s(2)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.x(2)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(0.906000,-0.835000,param_0, 0)
				main_circ.rz(param_1, 2)
				main_circ.rz(0.674000, 0)
				main_circ.u(-0.750000,-0.816000,0.442000, 3)
			with case_1(1):
				main_circ.rz(param_1, 1)
				main_circ.rz(-0.964000, 2)
				main_circ.s(2)
				main_circ.u(-0.886000,0.097000,-0.069000, 0)
	with case_2(1):
		main_circ.rz(-0.499000, 3)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(3)
		with else_1:
			main_circ.id(0)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(0)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.id(3)
		main_circ.id(1)
bindings = {param_0: 0.503000, param_1: -0.605000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1649", "Optimize1qGatesSimpleCommutation")
