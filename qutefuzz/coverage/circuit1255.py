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
subcirc0.u(pi/2,-0.166000,0.378000, qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0.u(-0.087000,0.420000,-0.351000, qreg_0[0])
subcirc0.u(pi/2,-0.054000,-0.958000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.169000,-0.209000,-0.697000, qreg_0[1])
subcirc1.u(pi/2,-0.019000,0.725000, qreg_0[1])
subcirc1.u(0,0,0.236000, qreg_3[0])
subcirc1.u(0,0,-0.361000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.378000,0.486000,0.893000, qreg_3[0])
subcirc2.u(0,0,0.722000, qreg_3[0])
subcirc2.u(0.504000,-0.547000,0.831000, qreg_0[1])
subcirc2.u(pi/2,0.729000,-0.188000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.s(qreg_0[0])
subcirc3.s(qreg_0[0])
subcirc3.u(0,0,0.513000, qreg_0[1])
subcirc3.s(qreg_0[3])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,-0.651000,0.732000, qreg_0[1])
subcirc4.s(qreg_0[2])
subcirc4.u(pi/2,-0.857000,0.477000, qreg_3[0])
subcirc4.u(pi/2,-0.352000,-0.092000, qreg_0[2])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc4,[qreg_0[1],0,qreg_0[2],qreg_0[0]])
					with case_1(1):
						main_circ.append(subcirc3,[qreg_0[1],0,qreg_0[3],1])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(param_0,param_0,param_1, qreg_0[1])
						main_circ.append(subcirc4,[qreg_0[2],0,1,qreg_0[1]])
					with case_1(1):
						main_circ.u(param_1,-0.750000,param_1, 1)
						main_circ.append(subcirc2,[qreg_0[3],0,qreg_0[2],1])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[3], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.u(param_1,param_0,param_0, qreg_0[3])
						main_circ.u(0,0,-0.582000, qreg_0[2])
					main_circ.u(0.575000,param_0,param_1, 0)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.append(subcirc1,[qreg_0[2],1,qreg_0[1],qreg_0[3]])
					with else_1:
						main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],qreg_0[0],0])
				with case_2(1):
					main_circ.u(pi/2,param_1,-0.151000, qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.u(pi/2,0.414000,param_0, 1)
						main_circ.u(0,0,0.817000, qreg_0[2])
						main_circ.append(subcirc0,[qreg_0[3],1,qreg_0[1],0])
					with else_1:
						main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],0,qreg_0[0]])
with else_4:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.s(1)
					main_circ.u(param_1,0.035000,-0.649000, qreg_0[2])
					main_circ.u(param_1,param_0,-0.114000, 1)
					main_circ.u(pi/2,-0.899000,0.992000, 0)
				with case_1(1):
					main_circ.barrier(qreg_0[3])
		with else_2:
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.u(pi/2,param_0,param_0, 0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.s(1)
					main_circ.u(param_0,0,-0.132000, 0)
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.id(1)
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(1)
				main_circ.barrier(qreg_0[1])
			with case_2(1):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[3])
				main_circ.id(0)
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.id(qreg_0[2])
		with else_2:
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(0)
			main_circ.id(qreg_0[2])
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.barrier(qreg_0[3])
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[2])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.barrier(1)
		main_circ.id(qreg_0[2])
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.id(qreg_0[0])
		with case_3(1):
			main_circ.id(qreg_0[0])
	main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.779000, param_1: 0.585000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1255", "Optimize1qGatesSimpleCommutation")
