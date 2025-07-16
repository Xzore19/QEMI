from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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
param_4 = Parameter("param_4")

main_circ.x(2)
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.h(3)
		main_circ.h(qreg_0[0])
		main_circ.s(qreg_0[0])
		main_circ.s(qreg_0[0])
	with case_1(1):
		main_circ.rx(-0.932000, 0)
		main_circ.rx(0.887000, 3)
		main_circ.x(0)
		main_circ.s(3)
main_circ.s(qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.h(0)
		main_circ.s(qreg_0[0])
		main_circ.s(0)
		main_circ.rx(-0.751000, 0)
	with case_1(1):
		main_circ.h(qreg_0[0])
		main_circ.rx(0.996000, 3)
		main_circ.rx(param_1, 0)
		main_circ.h(1)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rx(0.747000, 0)
		main_circ.rx(param_3, 2)
		main_circ.s(2)
		main_circ.s(2)
	with case_1(1):
		main_circ.s(1)
		main_circ.x(0)
		main_circ.s(3)
		main_circ.x(3)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rx(0.234000, 0)
	main_circ.rx(param_4, 1)
	main_circ.s(qreg_0[0])
	main_circ.s(1)
	main_circ.s(qreg_0[0])
with else_1:
	main_circ.x(3)
main_circ.rx(param_1, 2)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rx(-0.709000, 2)
	main_circ.s(0)
	main_circ.h(1)
	main_circ.x(qreg_0[0])
	main_circ.x(3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.h(1)
		main_circ.h(qreg_0[0])
		main_circ.h(2)
		main_circ.x(1)
	with case_1(1):
		main_circ.rx(param_4, 1)
		main_circ.id(qreg_0[0])
bindings = {param_1: -0.580000, param_3: -0.819000, param_4: -0.403000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1976", "Optimize1qGatesSimpleCommutation")
