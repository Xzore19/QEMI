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

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.ry(param_3, 3)
		main_circ.y(0)
		main_circ.cy(1,2)
		main_circ.cy(2,0)
	with else_1:
		main_circ.ry(param_2, 1)
		main_circ.y(2)
		main_circ.y(2)
main_circ.cy(1,0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.y(2)
	with else_1:
		main_circ.rx(0.815000, 3)
		main_circ.rx(param_3, 3)
		main_circ.y(2)
		main_circ.ry(0.808000, 0)
		main_circ.rx(-0.927000, 2)
with else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(2)
			main_circ.y(3)
			main_circ.ry(param_2, 2)
			main_circ.ry(param_1, 3)
		with case_1(1):
			main_circ.y(0)
			main_circ.ry(-0.432000, 2)
			main_circ.cy(0,3)
			main_circ.cy(3,2)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_2, 1)
			main_circ.ry(0.950000, 1)
			main_circ.cy(1,0)
			main_circ.ry(0.137000, 1)
		with case_1(1):
			main_circ.cy(3,2)
			main_circ.ry(param_2, 3)
			main_circ.ry(-0.708000, 2)
			main_circ.y(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.ry(param_4, 1)
		main_circ.y(2)
		main_circ.y(3)
with else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(1)
			main_circ.y(3)
			main_circ.y(3)
			main_circ.ry(-0.722000, 2)
		with case_1(1):
			main_circ.rx(param_0, 1)
			main_circ.rx(param_0, 0)
			main_circ.y(2)
			main_circ.cy(2,3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cy(1,3)
			main_circ.cy(2,3)
			main_circ.cy(2,0)
			main_circ.cy(1,2)
		with case_1(1):
			main_circ.cy(0,3)
			main_circ.cy(0,1)
			main_circ.cy(3,2)
			main_circ.cy(0,2)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rx(param_3, 0)
		main_circ.rx(param_0, 1)
		main_circ.y(1)
		main_circ.y(0)
		main_circ.y(2)
	with else_1:
		main_circ.ry(0.465000, 2)
		main_circ.y(1)
bindings = {param_0: -0.800000, param_1: -0.078000, param_2: 0.811000, param_3: -0.020000, param_4: -0.634000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "881")
