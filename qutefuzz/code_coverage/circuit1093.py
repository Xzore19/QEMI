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

main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.x(2)
		main_circ.ry(param_0, 3)
		main_circ.ry(param_1, 1)
		main_circ.y(3)
	with case_1(1):
		main_circ.y(0)
		main_circ.u(0.094000,0.790000,-0.873000, 0)
		main_circ.y(0)
		main_circ.x(3)
main_circ.x(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(param_0, 2)
	main_circ.u(param_0,param_1,param_1, 2)
	main_circ.ry(param_1, 2)
	main_circ.u(param_0,0.059000,0.132000, 1)
with else_1:
	main_circ.ry(0.536000, 3)
	main_circ.x(1)
	main_circ.y(2)
	main_circ.ry(param_1, 0)
	main_circ.ry(0.455000, 2)
main_circ.x(1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,param_0,param_1, 2)
	main_circ.u(param_1,0.668000,-0.801000, 1)
	main_circ.x(0)
	main_circ.x(1)
with else_1:
	main_circ.y(2)
	main_circ.y(2)
	main_circ.ry(param_0, 1)
	main_circ.u(param_1,0.025000,param_0, 2)
	main_circ.y(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(0)
	main_circ.ry(0.900000, 0)
	main_circ.u(param_0,-0.265000,0.231000, 1)
	main_circ.ry(-0.297000, 3)
	main_circ.ry(param_1, 2)
main_circ.x(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(2)
	main_circ.y(3)
	main_circ.x(0)
	main_circ.y(3)
with else_1:
	main_circ.ry(param_0, 3)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(-0.536000, 1)
		main_circ.y(1)
		main_circ.y(0)
		main_circ.x(3)
	with case_1(1):
		main_circ.u(0.967000,0.584000,0.226000, 1)
		main_circ.ry(0.840000, 0)
		main_circ.u(param_0,param_0,param_0, 0)
		main_circ.u(0.565000,param_0,param_0, 0)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(3)
	main_circ.y(1)
	main_circ.ry(param_1, 0)
	main_circ.ry(0.279000, 1)
	main_circ.ry(param_0, 3)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(1)
		main_circ.x(1)
		main_circ.id(2)
	with case_1(1):
		main_circ.id(3)
bindings = {param_0: -0.912000, param_1: -0.562000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1093", "Optimize1qGatesDecomposition")
