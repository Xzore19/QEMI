from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.z(qreg_0[1])
subcirc0.u(pi/2,0.594000,0.331000, qreg_3[0])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.u(pi/2,-0.942000,0.069000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.h(qreg_1[0])
subcirc1.h(qreg_0[0])
subcirc1.cy(qreg_1[1],qreg_1[0])
subcirc1.h(qreg_1[1])
subcirc1 = subcirc1.to_gate().control(3)

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

main_circ.u(param_0,param_1,param_2, 1)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.cy(3,2)
		main_circ.id(0)
	with case_3(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.h(1)
				main_circ.h(0)
				main_circ.h(1)
				main_circ.append(subcirc0,[qreg_0[1],1,2,0])
		with else_2:
			main_circ.z(qreg_0[1])
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[0],3)
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.h(qreg_0[1])
					main_circ.z(3)
					main_circ.h(3)
					main_circ.h(3)
				with case_1(1):
					main_circ.u(pi/2,param_0,0.861000, qreg_0[0])
					main_circ.append(subcirc0,[0,1,2,qreg_0[1]])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.h(qreg_0[1])
						main_circ.cy(qreg_0[0],qreg_0[1])
						main_circ.append(subcirc0,[3,0,2,1])
					with case_1(1):
						main_circ.z(2)
						main_circ.barrier(qreg_0[0])
			with case_2(1):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],1])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[0],1)
					main_circ.u(pi/2,param_1,param_0, 2)
					main_circ.cy(0,2)
					main_circ.cy(2,0)
				with case_1(1):
					main_circ.cy(qreg_0[1],0)
					main_circ.cy(3,1)
					main_circ.cy(qreg_0[1],3)
					main_circ.cy(3,2)
main_circ.append(subcirc0,[1,2,qreg_0[1],qreg_0[0]])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(2,qreg_0[1])
			with else_1:
				main_circ.h(qreg_0[0])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.h(0)
					main_circ.z(qreg_0[0])
					main_circ.barrier(1)
		with case_2(1):
			main_circ.barrier(1)
with else_3:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.id(qreg_0[1])
	with else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(0)
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(3)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.barrier(0)
		main_circ.barrier(0)
	main_circ.id(2)
bindings = {param_0: 0.598000, param_1: 0.215000, param_2: -0.907000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "226", "Collect1qRuns")
