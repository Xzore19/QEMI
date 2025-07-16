from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(qreg_3[0],qreg_0[2])
		main_circ.cy(qreg_3[0],qreg_0[0])
		main_circ.y(qreg_3[0])
	with else_1:
		main_circ.rz(-0.526000, qreg_3[0])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.rz(0.725000, qreg_0[2])
		main_circ.cx(qreg_0[2],qreg_0[0])
		main_circ.y(qreg_0[2])
		main_circ.rz(param_1, qreg_3[0])
main_circ.cx(qreg_0[2],qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(qreg_0[1],qreg_3[0])
		main_circ.cy(qreg_0[0],qreg_3[0])
		main_circ.cx(qreg_0[1],qreg_0[0])
		main_circ.cx(qreg_3[0],qreg_0[2])
		main_circ.cy(qreg_0[0],qreg_3[0])
	with else_1:
		main_circ.rz(-0.709000, qreg_0[2])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cx(qreg_0[0],qreg_0[2])
		main_circ.rz(-0.177000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(-0.776000, qreg_0[1])
				main_circ.cy(qreg_3[0],qreg_0[0])
				main_circ.y(qreg_3[0])
				main_circ.cx(qreg_3[0],qreg_0[2])
			with case_1(1):
				main_circ.cx(qreg_3[0],qreg_0[2])
				main_circ.rz(0.924000, qreg_0[0])
				main_circ.cy(qreg_0[1],qreg_0[2])
				main_circ.y(qreg_0[1])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rz(param_1, qreg_0[0])
			main_circ.cy(qreg_0[0],qreg_0[2])
			main_circ.rz(0.268000, qreg_0[0])
		with else_1:
			main_circ.cy(qreg_0[0],qreg_0[2])
			main_circ.y(qreg_0[0])
			main_circ.rz(0.067000, qreg_0[1])
			main_circ.rz(-0.039000, qreg_3[0])
main_circ.rz(0.326000, qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cy(qreg_0[0],qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(qreg_0[0],qreg_0[1])
			main_circ.cx(qreg_3[0],qreg_0[0])
			main_circ.cx(qreg_0[0],qreg_0[2])
			main_circ.cx(qreg_0[1],qreg_3[0])
	with case_2(1):
		main_circ.y(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.y(qreg_3[0])
			main_circ.y(qreg_0[1])
			main_circ.cx(qreg_0[1],qreg_3[0])
		with else_1:
			main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cx(qreg_0[2],qreg_3[0])
		main_circ.y(qreg_0[2])
		main_circ.cx(qreg_0[0],qreg_0[1])
		main_circ.rz(param_2, qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(qreg_3[0],qreg_0[1])
		main_circ.y(qreg_0[1])
		main_circ.cx(qreg_0[0],qreg_3[0])
	with else_1:
		main_circ.y(qreg_0[2])
		main_circ.rz(param_0, qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(qreg_3[0])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_0[1],qreg_0[2])
			main_circ.cx(qreg_0[1],qreg_0[2])
			main_circ.rz(0.644000, qreg_0[1])
			main_circ.cy(qreg_0[1],qreg_0[0])
		with case_1(1):
			main_circ.y(qreg_0[0])
			main_circ.rz(-0.902000, qreg_0[2])
			main_circ.y(qreg_0[0])
			main_circ.id(qreg_3[0])
bindings = {param_0: -0.434000, param_1: -0.079000, param_2: 0.387000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1161")
