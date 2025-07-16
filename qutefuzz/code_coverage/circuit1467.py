from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(-0.324000, qreg_3[0])
		main_circ.ry(param_1, qreg_0[0])
		main_circ.ry(0.527000, qreg_0[1])
		main_circ.rx(0.051000, 0)
	with case_1(1):
		main_circ.rx(param_0, 1)
		main_circ.s(0)
		main_circ.rx(-0.791000, qreg_0[0])
		main_circ.rx(param_2, 0)
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(qreg_0[0])
	main_circ.s(qreg_0[1])
	main_circ.s(0)
	main_circ.s(qreg_0[0])
with else_1:
	main_circ.cy(qreg_0[2],qreg_0[0])
	main_circ.rx(param_0, qreg_0[2])
	main_circ.ry(-0.417000, qreg_0[2])
	main_circ.ry(-0.865000, qreg_0[1])
	main_circ.cy(1,0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.s(qreg_0[0])
	main_circ.s(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_0[0])
with else_1:
	main_circ.s(0)
	main_circ.rx(param_1, qreg_3[0])
	main_circ.cy(qreg_3[0],qreg_0[0])
	main_circ.rx(param_3, qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.309000, qreg_0[2])
		main_circ.rx(0.735000, qreg_0[2])
		main_circ.s(1)
		main_circ.rx(param_2, 1)
	with case_1(1):
		main_circ.ry(param_0, qreg_0[2])
		main_circ.cy(qreg_0[2],1)
		main_circ.s(qreg_0[0])
		main_circ.ry(param_0, 1)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(0,qreg_0[0])
		main_circ.cy(qreg_0[2],0)
		main_circ.cy(qreg_0[2],qreg_0[1])
		main_circ.cy(0,qreg_0[0])
	with case_1(1):
		main_circ.cy(1,0)
		main_circ.cy(qreg_0[2],qreg_0[1])
		main_circ.cy(qreg_0[1],qreg_0[0])
		main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.cy(0,qreg_0[1])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.s(0)
		main_circ.cy(1,qreg_0[0])
		main_circ.s(qreg_3[0])
		main_circ.s(qreg_0[2])
	with case_1(1):
		main_circ.cy(qreg_0[0],0)
		main_circ.id(qreg_0[0])
bindings = {param_0: -0.374000, param_1: 0.152000, param_2: 0.046000, param_3: -0.145000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1467", "Optimize1qGatesSimpleCommutation")
