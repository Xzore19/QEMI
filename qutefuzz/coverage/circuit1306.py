from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.006000,-0.136000, qreg_2[0])
subcirc0.rx(-0.780000, qreg_0[0])
subcirc0.u(0.727000,-0.624000,0.090000, qreg_0[1])
subcirc0.u(pi/2,0.306000,0.491000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.237000,-0.968000,-0.838000, qreg_0[0])
subcirc1.u(-0.518000,-0.119000,-0.753000, qreg_3[0])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.u(-0.455000,0.337000,-0.347000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cx(qreg_2[1],qreg_1[0])
subcirc2.u(0.491000,-0.978000,-0.309000, qreg_1[0])
subcirc2.u(-0.877000,-0.748000,-0.984000, qreg_2[0])
subcirc2.u(pi/2,-0.115000,0.486000, qreg_1[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.266000,-0.919000, qreg_3[0])
subcirc3.cx(qreg_0[1],qreg_0[2])
subcirc3.u(pi/2,-0.270000,-0.009000, qreg_0[0])
subcirc3.rx(0.041000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

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

main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc1,[3,2,1,0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.append(subcirc2,[3,0,qreg_0[0],1,2])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.rx(param_0, 1)
				main_circ.cx(2,qreg_0[0])
				main_circ.rx(param_0, qreg_0[0])
				main_circ.barrier(0)
		main_circ.barrier(0)
	with case_2(1):
		main_circ.cx(2,1)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rx(param_3, 1)
				main_circ.u(param_2,-0.364000,param_0, 2)
				main_circ.u(param_3,param_2,0.317000, 1)
				main_circ.u(param_0,param_1,-0.759000, 2)
			with case_1(1):
				main_circ.barrier(1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.u(-0.808000,param_1,-0.812000, qreg_0[0])
			main_circ.rx(0.662000, 1)
			main_circ.barrier(0)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(3)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc2,[3,0,2,qreg_0[0],1])
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc1,[qreg_0[0],0,2,3])
		with else_1:
			main_circ.rx(0.107000, 2)
			main_circ.u(pi/2,0.757000,-0.176000, 0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc1,[0,1,3,2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_2,0.178000,-0.208000, 0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(0.092000,param_1,-0.401000, 3)
			main_circ.id(2)
		with case_1(1):
			main_circ.cx(3,qreg_0[0])
			main_circ.u(0.544000,-0.949000,param_3, 2)
			main_circ.append(subcirc1,[qreg_0[0],2,3,1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(pi/2,0.811000,param_1, 1)
		main_circ.u(-0.381000,0.042000,0.092000, 3)
		main_circ.cx(3,0)
		main_circ.cx(3,2)
		main_circ.cx(1,qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cx(3,2)
			main_circ.cx(2,0)
			main_circ.cx(qreg_0[0],1)
			main_circ.cx(2,1)
		with case_1(1):
			main_circ.cx(1,3)
			main_circ.cx(2,qreg_0[0])
			main_circ.u(pi/2,0.895000,param_3, 2)
			main_circ.id(2)
with else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.append(subcirc2,[qreg_0[0],2,3,0,1])
	with else_1:
		main_circ.u(param_1,param_2,0.683000, qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cx(qreg_0[0],2)
		main_circ.barrier(2)
	main_circ.barrier(0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(param_0,param_3,param_2, 2)
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.u(param_3,-0.996000,-0.887000, 0)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.id(0)
		main_circ.id(1)
	with case_2(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(1)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(0)
		main_circ.id(0)
bindings = {param_0: -0.354000, param_1: 0.579000, param_2: 0.068000, param_3: 0.271000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1306")
