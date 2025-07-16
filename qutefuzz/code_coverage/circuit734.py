from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(-1.000000,-0.274000,0.184000, qreg_1[1])
subcirc0.rz(0.809000, qreg_1[1])
subcirc0.u(0.801000,-0.350000,0.044000, qreg_1[0])
subcirc0.rz(0.262000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.z(qreg_0[1])
	main_circ.id(qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.barrier(qreg_2[0])
	main_circ.measure(qreg_2[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.x(qreg_2[1])
			main_circ.rz(0.324000, qreg_0[0])
			main_circ.x(qreg_2[0])
			main_circ.u(param_1,-0.784000,-0.208000, qreg_0[1])
		with case_1(1):
			main_circ.u(param_3,param_0,param_2, qreg_2[0])
			main_circ.z(qreg_2[0])
			main_circ.rz(-0.914000, qreg_0[1])
			main_circ.x(qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(qreg_2[1])
			main_circ.u(0.181000,0.417000,0.183000, qreg_2[0])
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_0,0.516000,param_2, qreg_0[1])
				main_circ.u(0.586000,-0.165000,-0.895000, qreg_2[1])
				main_circ.x(qreg_2[0])
				main_circ.rz(-0.738000, qreg_2[0])
			with case_1(1):
				main_circ.u(param_1,param_3,param_1, qreg_2[1])
				main_circ.barrier(qreg_0[0])
	with case_2(1):
		main_circ.barrier(qreg_2[0])
main_circ.z(qreg_2[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.x(qreg_0[0])
				main_circ.z(qreg_2[1])
				main_circ.rz(param_2, qreg_0[1])
				main_circ.x(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[1])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(0.583000,param_1,param_1, qreg_0[1])
		main_circ.z(qreg_0[1])
		main_circ.x(qreg_2[1])
		main_circ.measure(qreg_2[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(-0.139000,0.265000,param_1, qreg_0[0])
			main_circ.z(qreg_2[0])
			main_circ.rz(param_2, qreg_2[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.barrier(qreg_2[0])
with else_2:
	main_circ.x(qreg_2[1])
	main_circ.u(param_3,-0.622000,0.143000, qreg_0[0])
	main_circ.measure(qreg_2[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(param_3,param_0,param_2, qreg_2[1])
			main_circ.rz(param_2, qreg_2[0])
			main_circ.u(-0.645000,-0.161000,0.787000, qreg_0[0])
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.rz(-0.992000, qreg_0[1])
			main_circ.u(0.376000,param_2,0.364000, qreg_2[1])
			main_circ.u(-0.936000,param_3,-0.634000, qreg_0[1])
			main_circ.x(qreg_2[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.z(qreg_2[1])
			main_circ.x(qreg_2[0])
		main_circ.rz(param_0, qreg_2[0])
		main_circ.measure(qreg_2[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_2[0])
		with else_1:
			main_circ.id(qreg_2[1])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_2[0])
			with case_1(1):
				main_circ.u(-0.496000,param_1,param_1, qreg_0[0])
				main_circ.z(qreg_2[1])
				main_circ.x(qreg_2[1])
				main_circ.rz(param_2, qreg_0[1])
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[1])
			with case_1(1):
				main_circ.id(qreg_0[1])
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_2[0])
		main_circ.id(qreg_2[0])
bindings = {param_0: 0.667000, param_1: -0.445000, param_2: -0.996000, param_3: -0.880000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "734")
