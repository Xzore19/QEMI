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
param_5 = Parameter("param_5")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rz(0.166000, 1)
		main_circ.cx(2,0)
	with else_1:
		main_circ.rz(param_0, 2)
		main_circ.u(-0.014000,0.313000,param_2, qreg_0[0])
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_2,param_2,-0.391000, 1)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0.379000,0.646000,param_2, 2)
main_circ.u(param_1,-0.123000,0.854000, 3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_2,param_4,param_0, 1)
				main_circ.cx(qreg_0[0],0)
				main_circ.s(qreg_0[0])
				main_circ.s(3)
			with case_1(1):
				main_circ.u(-0.371000,param_2,param_0, 1)
				main_circ.cx(qreg_0[0],1)
				main_circ.s(0)
				main_circ.s(2)
	with case_2(1):
		main_circ.cx(3,2)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.s(2)
				main_circ.rz(-0.949000, qreg_0[0])
				main_circ.cx(qreg_0[0],1)
				main_circ.cx(0,1)
			with case_1(1):
				main_circ.u(0.042000,-0.880000,0.613000, 0)
				main_circ.rz(0.398000, 0)
				main_circ.s(2)
				main_circ.s(3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cx(2,0)
				main_circ.cx(1,3)
				main_circ.cx(qreg_0[0],0)
				main_circ.s(2)
			with case_1(1):
				main_circ.u(0.241000,param_4,0.676000, qreg_0[0])
				main_circ.rz(param_1, 1)
				main_circ.s(3)
				main_circ.cx(0,qreg_0[0])
	with case_2(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.s(qreg_0[0])
				main_circ.s(qreg_0[0])
				main_circ.u(param_2,-0.093000,param_3, 1)
				main_circ.cx(3,0)
			with case_1(1):
				main_circ.u(param_5,param_1,param_5, 2)
				main_circ.cx(3,0)
				main_circ.s(2)
				main_circ.u(param_4,-0.597000,0.894000, 3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.s(1)
			main_circ.cx(3,1)
		with else_1:
			main_circ.cx(3,0)
			main_circ.cx(1,3)
			main_circ.cx(0,1)
			main_circ.cx(1,0)
			main_circ.cx(qreg_0[0],2)
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_3,param_1,0.935000, 0)
				main_circ.cx(3,2)
				main_circ.cx(0,2)
				main_circ.rz(0.663000, 3)
			with case_1(1):
				main_circ.rz(0.455000, 3)
				main_circ.u(param_4,0.423000,0.839000, 2)
				main_circ.rz(param_5, 1)
				main_circ.u(-0.319000,0.678000,0.709000, 1)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.u(param_1,param_3,0.009000, 0)
	with else_1:
		main_circ.u(param_5,param_3,param_0, 3)
		main_circ.cx(qreg_0[0],3)
		main_circ.id(0)
bindings = {param_0: 0.610000, param_1: -0.066000, param_2: -0.659000, param_3: 0.622000, param_4: 0.438000, param_5: -0.459000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1262", "RemoveFinalReset")
