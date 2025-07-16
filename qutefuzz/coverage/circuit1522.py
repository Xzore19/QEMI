from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
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
param_4 = Parameter("param_4")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_1,param_4,param_3, qreg_0[2])
		main_circ.s(qreg_0[0])
		main_circ.u(param_1,0.120000,0.835000, qreg_0[3])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cx(1,0)
		main_circ.z(0)
		main_circ.s(0)
		main_circ.u(param_1,-0.817000,-0.688000, 1)
with else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_2,param_1,param_2, qreg_0[1])
		main_circ.u(0.362000,-0.102000,param_1, 1)
		main_circ.u(-0.453000,0.601000,0.843000, qreg_0[2])
		main_circ.u(param_1,-0.478000,-0.764000, qreg_0[0])
		main_circ.z(qreg_0[3])
main_circ.u(-0.993000,0.380000,0.844000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.cx(qreg_0[3],qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_0,0.139000,-0.720000, 1)
			main_circ.u(0.853000,param_1,-0.747000, qreg_0[0])
			main_circ.s(qreg_0[1])
	with case_2(1):
		main_circ.z(qreg_0[2])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cx(qreg_0[2],1)
			main_circ.z(qreg_0[2])
			main_circ.cx(1,qreg_0[3])
			main_circ.u(param_4,-0.166000,0.198000, 1)
		with else_1:
			main_circ.cx(1,qreg_0[1])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.s(qreg_0[2])
		main_circ.cx(qreg_0[3],0)
		main_circ.s(qreg_0[2])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(qreg_0[1])
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.z(qreg_0[3])
			main_circ.z(qreg_0[3])
			main_circ.cx(0,qreg_0[3])
			main_circ.z(0)
			main_circ.s(1)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.z(qreg_0[1])
		with else_1:
			main_circ.u(param_3,param_1,param_3, 0)
			main_circ.s(0)
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_1,param_1,0.914000, 0)
				main_circ.s(qreg_0[2])
				main_circ.u(0.029000,param_0,param_2, qreg_0[2])
				main_circ.cx(qreg_0[0],qreg_0[3])
			with case_1(1):
				main_circ.cx(0,qreg_0[0])
				main_circ.cx(0,qreg_0[0])
				main_circ.cx(qreg_0[3],1)
				main_circ.cx(1,qreg_0[0])
	with case_2(1):
		main_circ.cx(0,qreg_0[3])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(qreg_0[2],qreg_0[3])
			main_circ.cx(qreg_0[1],qreg_0[3])
			main_circ.cx(1,qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.s(qreg_0[3])
			main_circ.cx(0,qreg_0[3])
			main_circ.s(qreg_0[0])
			main_circ.cx(0,qreg_0[2])
		with case_1(1):
			main_circ.cx(qreg_0[3],qreg_0[0])
			main_circ.cx(1,0)
			main_circ.z(0)
			main_circ.u(param_2,-0.607000,param_1, 0)
with else_2:
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.barrier(1)
	with else_1:
		main_circ.id(qreg_0[2])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.barrier(qreg_0[3])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[2])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(0)
		with case_1(1):
			main_circ.barrier(1)
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[1])
	with else_1:
		main_circ.id(1)
	main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.897000, param_1: 0.686000, param_2: 0.198000, param_3: 0.737000, param_4: -0.919000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1522")
