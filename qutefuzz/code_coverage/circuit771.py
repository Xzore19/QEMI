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
subcirc0.u(pi/2,-0.189000,-0.080000, qreg_2[0])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_2[0])
subcirc0.ry(-0.593000, qreg_0[1])
subcirc0.u(pi/2,-0.598000,0.249000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.ry(0.920000, qreg_0[0])
subcirc1.u(0,0,0.894000, qreg_0[0])
subcirc1.u(0,0,-0.551000, qreg_1[0])
subcirc1.ry(-0.369000, qreg_1[2])
subcirc1.ry(0.183000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_1[1])
subcirc2.y(qreg_1[0])
subcirc2.u(0,0,-0.637000, qreg_1[1])
subcirc2.u(pi/2,-0.567000,0.230000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.541000, qreg_1[1])
subcirc3.u(0,0,0.730000, qreg_3[0])
subcirc3.u(0,0,0.411000, qreg_1[1])
subcirc3.ry(0.349000, qreg_1[1])
subcirc3.u(pi/2,-0.840000,-0.772000, qreg_1[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,0.269000,0.925000, qreg_0[2])
subcirc4.ry(0.587000, qreg_3[0])
subcirc4.u(pi/2,-0.419000,-0.661000, qreg_0[2])
subcirc4.u(0,0,0.085000, qreg_3[0])
subcirc4.u(pi/2,-1.000000,0.602000, qreg_0[0])

main_circ = QuantumCircuit(1)
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

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.y(qreg_0[2])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3],0])
						with case_1(1):
							main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
				with case_2(1):
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.u(param_1,0,0.649000, qreg_0[3])
						main_circ.y(0)
						main_circ.append(subcirc2,[qreg_0[1],0,qreg_0[3],qreg_0[0]])
					with else_1:
						main_circ.ry(param_2, qreg_0[1])
	with case_4(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.u(0,param_1,param_2, 0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.append(subcirc4,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
		with else_3:
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[3],qreg_0[0]])
				with else_1:
					main_circ.ry(param_0, qreg_0[1])
					main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[3],qreg_0[1]])
			with else_2:
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.u(pi/2,0.121000,0.185000, qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(pi/2,0.015000,param_1, qreg_0[1])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],0,qreg_0[0]])
				with else_1:
					main_circ.u(param_2,0,0.801000, qreg_0[2])
					main_circ.u(pi/2,-0.212000,param_0, qreg_0[3])
					main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.u(0,0,-0.142000, qreg_0[0])
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[3])
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.id(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.id(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(0)
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.id(0)
			with else_2:
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.barrier(0)
			main_circ.barrier(qreg_0[2])
		with case_3(1):
			main_circ.barrier(qreg_0[2])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(0)
				main_circ.id(qreg_0[3])
			main_circ.barrier(qreg_0[0])
		with case_3(1):
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[3])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(0)
			main_circ.barrier(qreg_0[3])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.id(0)
		with case_3(1):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.barrier(qreg_0[3])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(0)
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[3])
					with case_1(1):
						main_circ.id(qreg_0[3])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[3])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_0[1])
			with case_2(1):
				main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.barrier(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.barrier(qreg_0[3])
			main_circ.barrier(qreg_0[2])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[3])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.barrier(qreg_0[2])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.id(0)
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_0[3])
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.id(qreg_0[1])
			with case_2(1):
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[3])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.barrier(qreg_0[3])
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[3])
			main_circ.id(qreg_0[2])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[3])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[2])
				with case_1(1):
					main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[2])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[3])
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(0)
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(qreg_0[2])
			main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[3])
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[3])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[3])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[3])
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[3])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[2])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.id(qreg_0[1])
		with else_2:
			main_circ.id(qreg_0[2])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_0[3])
		with else_2:
			main_circ.barrier(qreg_0[1])
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.barrier(0)
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.id(qreg_0[3])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[2])
			main_circ.id(0)
		with else_2:
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[2])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[2])
				with case_1(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.barrier(qreg_0[3])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[3])
		main_circ.barrier(qreg_0[2])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.barrier(qreg_0[1])
		main_circ.barrier(qreg_0[3])
	main_circ.id(qreg_0[3])
bindings = {param_0: -0.979000, param_1: 0.804000, param_2: -0.316000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "771")
