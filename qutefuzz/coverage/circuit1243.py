from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.ry(0.411000, qreg_0[0])
subcirc0.h(qreg_2[1])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.h(qreg_2[0])
subcirc0.u(0.545000,-0.525000,-0.380000, qreg_0[0])
subcirc0.cy(qreg_2[1],qreg_0[0])

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

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.h(1)
				main_circ.append(subcirc0,[3,1,qreg_0[1],0])
with else_4:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.ry(-0.860000, qreg_0[0])
					main_circ.cy(qreg_0[1],qreg_0[0])
					main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],2,1])
				with case_1(1):
					main_circ.append(subcirc0,[2,qreg_0[0],3,0])
		with else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(0.046000,param_3,-0.088000, 0)
				main_circ.h(qreg_0[1])
				main_circ.append(subcirc0,[1,3,0,2])
	with else_3:
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.u(0.491000,-0.298000,0.750000, 2)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],2])
			with else_1:
				main_circ.cy(1,0)
				main_circ.cy(1,0)
				main_circ.cy(qreg_0[0],3)
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cy(qreg_0[1],3)
				main_circ.cy(qreg_0[0],2)
				main_circ.h(qreg_0[0])
				main_circ.h(qreg_0[1])
				main_circ.id(3)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.u(-0.063000,-0.702000,param_1, 2)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.u(param_2,-0.254000,param_2, 3)
		main_circ.barrier(qreg_0[1])
	with else_3:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.cy(qreg_0[1],qreg_0[0])
					main_circ.cy(3,2)
					main_circ.h(2)
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(2)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(1)
				main_circ.barrier(0)
			with case_2(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.id(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(2)
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(1)
				main_circ.barrier(2)
with else_4:
	main_circ.barrier(0)
bindings = {param_1: 0.610000, param_2: 0.773000, param_3: -0.269000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1243", "CollectMultiQBlocks")
