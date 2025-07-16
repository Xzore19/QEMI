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
subcirc0.u(pi/2,0.852000,0.642000, qreg_1[2])
subcirc0.y(qreg_1[0])
subcirc0.u(pi/2,0.465000,0.685000, qreg_1[2])
subcirc0.cx(qreg_1[1],qreg_1[2])
subcirc0.u(pi/2,0.695000,0.024000, qreg_1[0])
subcirc0.y(qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,-0.830000,0.955000, qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.u(-0.602000,-0.104000,-0.981000, qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1.u(-0.378000,-0.753000,0.489000, qreg_0[2])
subcirc1.u(pi/2,-0.364000,-0.380000, qreg_0[2])

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

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.cx(1,qreg_0[0])
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc0,[1,0,3,qreg_0[1],2,qreg_0[0]])
		with else_1:
			main_circ.append(subcirc0,[2,3,1,qreg_0[1],0,qreg_0[0]])
with else_3:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.append(subcirc0,[0,qreg_0[1],2,1,3,qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,param_0,-0.643000, 2)
				main_circ.y(qreg_0[1])
				main_circ.u(-0.951000,param_0,0.404000, qreg_0[1])
				main_circ.u(param_1,param_3,param_4, 0)
			with case_1(1):
				main_circ.u(-0.068000,-0.388000,0.179000, qreg_0[0])
				main_circ.append(subcirc1,[3,1,0,qreg_0[0]])
	with else_2:
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc0,[3,qreg_0[1],qreg_0[0],1,0,2])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(2,qreg_0[1])
				main_circ.cx(3,0)
				main_circ.cx(1,qreg_0[1])
				main_circ.cx(qreg_0[1],qreg_0[0])
			with case_1(1):
				main_circ.cx(qreg_0[0],3)
				main_circ.cx(2,3)
				main_circ.cx(3,1)
				main_circ.id(1)
	with else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_2,param_1,-0.021000, 3)
			main_circ.barrier(qreg_0[1])
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.y(0)
			main_circ.u(param_1,-0.601000,param_0, 3)
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(qreg_0[0])
with else_3:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.barrier(2)
		with case_2(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(1)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.id(3)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.barrier(1)
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(1)
		main_circ.id(qreg_0[0])
	main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.380000, param_1: 0.185000, param_2: 0.078000, param_3: -0.756000, param_4: 0.803000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1196", "CollectLinearFunctions")
