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

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(1,2)
with else_1:
	main_circ.y(3)
	main_circ.x(1)
	main_circ.cy(0,3)
	main_circ.cy(2,3)
main_circ.ry(0.552000, 1)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.x(3)
		main_circ.x(1)
		main_circ.cy(2,1)
		main_circ.x(0)
	with case_1(1):
		main_circ.ry(param_0, 2)
		main_circ.ry(-0.558000, 2)
		main_circ.cy(1,0)
		main_circ.y(1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(param_0, 3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.861000, 2)
	main_circ.cy(3,2)
	main_circ.y(2)
	main_circ.cy(1,3)
	main_circ.y(1)
with else_1:
	main_circ.cy(0,2)
	main_circ.ry(param_0, 0)
	main_circ.x(3)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.y(1)
	main_circ.ry(param_0, 3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(0)
	main_circ.cy(2,1)
	main_circ.ry(-0.449000, 0)
	main_circ.y(2)
	main_circ.ry(-0.152000, 2)
with else_1:
	main_circ.y(2)
	main_circ.ry(param_0, 3)
	main_circ.cy(1,2)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_0, 1)
		main_circ.ry(param_0, 2)
		main_circ.y(2)
		main_circ.cy(3,1)
	with case_1(1):
		main_circ.cy(0,2)
		main_circ.cy(1,0)
		main_circ.cy(2,0)
		main_circ.cy(3,1)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.y(2)
	main_circ.x(3)
	main_circ.cy(2,0)
	main_circ.cy(1,0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.x(2)
	main_circ.cy(1,2)
with else_1:
	main_circ.cy(1,2)
	main_circ.cy(1,0)
	main_circ.cy(3,1)
main_circ.x(3)
bindings = {param_0: 0.716000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1996", "Collect1qRuns")
