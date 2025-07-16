from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.u(pi/2,0.799000,param_3, 0)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(param_5,-0.991000,param_1, qreg_0[1])
			main_circ.cx(qreg_0[1],qreg_0[0])
			main_circ.u(pi/2,param_5,param_3, qreg_0[1])
		with else_1:
			main_circ.u(pi/2,0.725000,-0.084000, 3)
			main_circ.x(2)
			main_circ.x(3)
			main_circ.cx(qreg_0[1],1)
			main_circ.x(2)
	with case_2(1):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(pi/2,0.544000,-0.243000, 1)
			main_circ.cx(0,2)
			main_circ.x(2)
		with else_1:
			main_circ.h(qreg_0[1])
			main_circ.u(param_4,param_0,-0.959000, qreg_0[0])
			main_circ.u(pi/2,0.351000,param_1, 3)
			main_circ.u(pi/2,0.718000,-0.277000, 0)
			main_circ.h(qreg_0[1])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_0[1],0)
			main_circ.cx(3,qreg_0[1])
			main_circ.cx(0,qreg_0[1])
			main_circ.x(3)
		with case_1(1):
			main_circ.h(qreg_0[0])
			main_circ.h(1)
			main_circ.x(1)
			main_circ.cx(0,2)
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.h(1)
		main_circ.u(param_5,0.685000,0.375000, 0)
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(pi/2,0.643000,param_3, qreg_0[1])
			main_circ.cx(qreg_0[0],3)
			main_circ.cx(3,1)
			main_circ.h(qreg_0[0])
		with case_1(1):
			main_circ.cx(2,1)
			main_circ.u(pi/2,param_2,param_4, qreg_0[1])
			main_circ.u(pi/2,-0.858000,param_5, 0)
			main_circ.h(2)
main_circ.x(2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(pi/2,param_2,-0.304000, 1)
			main_circ.u(param_3,0.878000,0.341000, 1)
			main_circ.u(pi/2,param_0,param_1, qreg_0[0])
			main_circ.cx(3,qreg_0[1])
		with case_1(1):
			main_circ.cx(0,qreg_0[1])
			main_circ.cx(0,3)
			main_circ.cx(2,qreg_0[1])
			main_circ.cx(3,2)
with else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cx(1,qreg_0[1])
			main_circ.cx(qreg_0[0],2)
			main_circ.u(pi/2,param_4,param_4, 1)
			main_circ.h(qreg_0[0])
		with case_1(1):
			main_circ.x(3)
			main_circ.cx(1,qreg_0[0])
			main_circ.u(pi/2,0.871000,param_0, qreg_0[0])
			main_circ.h(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(pi/2,param_2,-0.557000, 2)
			main_circ.h(3)
			main_circ.h(2)
			main_circ.x(qreg_0[0])
			main_circ.h(qreg_0[1])
		with else_1:
			main_circ.barrier(2)
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[1])
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[1])
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[1])
		with else_1:
			main_circ.id(qreg_0[1])
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(0)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.id(0)
		main_circ.barrier(2)
bindings = {param_0: 0.534000, param_1: -0.966000, param_2: 0.476000, param_3: 0.011000, param_4: 0.214000, param_5: -0.982000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "55")
