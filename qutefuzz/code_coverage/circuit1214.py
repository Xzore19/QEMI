from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(qreg_0[3],qreg_0[0])
			main_circ.cx(qreg_0[3],qreg_0[2])
			main_circ.cx(qreg_0[1],qreg_0[0])
		main_circ.rz(-0.319000, qreg_0[0])
	with case_2(1):
		main_circ.cx(qreg_0[0],qreg_0[2])
		main_circ.cx(qreg_0[2],qreg_0[3])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.x(qreg_0[3])
		with else_1:
			main_circ.ry(param_2, qreg_0[1])
			main_circ.cx(qreg_0[3],qreg_0[2])
			main_circ.rz(param_0, qreg_0[1])
			main_circ.x(qreg_0[2])
			main_circ.ry(0.438000, qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.x(qreg_0[0])
			main_circ.ry(param_0, qreg_0[3])
			main_circ.ry(param_3, qreg_0[0])
			main_circ.cx(qreg_0[3],qreg_0[2])
		with case_1(1):
			main_circ.x(qreg_0[2])
			main_circ.ry(param_0, qreg_0[3])
			main_circ.ry(param_1, qreg_0[0])
			main_circ.rz(param_2, qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.x(qreg_0[1])
		main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.x(qreg_0[2])
			main_circ.x(qreg_0[0])
			main_circ.rz(-0.556000, qreg_0[3])
			main_circ.ry(-0.064000, qreg_0[2])
		with case_1(1):
			main_circ.rz(param_1, qreg_0[3])
			main_circ.cx(qreg_0[0],qreg_0[2])
			main_circ.ry(0.502000, qreg_0[0])
			main_circ.cx(qreg_0[2],qreg_0[3])
with else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.cx(qreg_0[2],qreg_0[1])
		main_circ.rz(param_3, qreg_0[1])
	with else_1:
		main_circ.ry(param_3, qreg_0[2])
		main_circ.cx(qreg_0[2],qreg_0[3])
		main_circ.x(qreg_0[2])
		main_circ.ry(param_1, qreg_0[1])
		main_circ.rz(param_1, qreg_0[3])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_0[2],qreg_0[1])
			main_circ.cx(qreg_0[2],qreg_0[3])
			main_circ.cx(qreg_0[2],qreg_0[3])
			main_circ.cx(qreg_0[2],qreg_0[1])
		with case_1(1):
			main_circ.ry(-0.212000, qreg_0[2])
			main_circ.ry(param_1, qreg_0[0])
			main_circ.cx(qreg_0[0],qreg_0[1])
			main_circ.rz(param_3, qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rz(param_0, qreg_0[3])
			main_circ.rz(-0.148000, qreg_0[1])
			main_circ.x(qreg_0[2])
			main_circ.x(qreg_0[1])
		with case_1(1):
			main_circ.cx(qreg_0[3],qreg_0[0])
			main_circ.ry(-0.633000, qreg_0[2])
			main_circ.x(qreg_0[1])
			main_circ.x(qreg_0[2])
main_circ.rz(-0.599000, qreg_0[0])
bindings = {param_0: -0.651000, param_1: 0.695000, param_2: 0.252000, param_3: -0.887000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1214", "CommutativeCancellation")
