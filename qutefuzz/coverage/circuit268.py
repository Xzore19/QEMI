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

main_circ.y(3)
main_circ.y(3)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.s(3)
	main_circ.y(0)
	main_circ.rx(param_1, 0)
	main_circ.s(3)
with else_1:
	main_circ.rx(0.816000, 1)
	main_circ.rx(-0.921000, 2)
	main_circ.ry(0.582000, 2)
	main_circ.rx(param_0, 2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.832000, 3)
with else_1:
	main_circ.rx(0.884000, 0)
	main_circ.y(0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(0)
		main_circ.ry(0.997000, 1)
		main_circ.s(3)
		main_circ.ry(-0.888000, 1)
	with case_1(1):
		main_circ.rx(param_0, 0)
		main_circ.ry(param_1, 1)
		main_circ.rx(param_2, 3)
		main_circ.rx(-0.599000, 3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(3)
	main_circ.ry(-0.347000, 0)
	main_circ.ry(param_0, 1)
with else_1:
	main_circ.ry(0.285000, 3)
	main_circ.y(2)
	main_circ.s(0)
	main_circ.rx(param_1, 1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(-0.597000, 0)
	main_circ.rx(0.976000, 3)
	main_circ.s(1)
	main_circ.y(0)
	main_circ.rx(-0.051000, 1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(param_1, 0)
		main_circ.ry(-0.385000, 2)
		main_circ.s(0)
		main_circ.rx(-0.016000, 3)
	with case_1(1):
		main_circ.rx(param_0, 0)
		main_circ.ry(param_0, 0)
		main_circ.s(3)
		main_circ.y(0)
bindings = {param_0: -0.451000, param_1: -0.330000, param_2: 0.781000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "268", "HoareOptimizer")
