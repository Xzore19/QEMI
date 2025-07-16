from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0,0,0.171000, qreg_3[0])
subcirc0.u(pi/2,0.100000,-0.505000, qreg_1[1])
subcirc0.ry(-0.167000, qreg_0[0])
subcirc0.u(0,0,0.149000, qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.248000,0.618000, qreg_0[0])
subcirc1.u(pi/2,0.882000,-0.236000, qreg_0[0])
subcirc1.rz(-0.304000, qreg_0[0])
subcirc1.u(pi/2,0.555000,0.327000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.500000,0.590000, qreg_1[0])
subcirc2.u(pi/2,0.689000,-0.717000, qreg_1[0])
subcirc2.rz(0.114000, qreg_0[0])
subcirc2.ry(0.862000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.886000, qreg_2[0])
subcirc3.ry(0.110000, qreg_2[0])
subcirc3.rz(0.524000, qreg_3[0])
subcirc3.rz(-0.286000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(0,0,0.254000, qreg_0[1])
subcirc4.u(0,0,0.018000, qreg_0[2])
subcirc4.ry(-0.597000, qreg_0[1])
subcirc4.rz(0.369000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.ry(-0.352000, qreg_0[0])
			main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],0,qreg_0[1]])
		with case_3(1):
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.append(subcirc1,[qreg_0[2],0,qreg_3[0],1])
					main_circ.ry(param_3, 0)
				with else_1:
					main_circ.ry(param_1, 0)
			with else_2:
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.append(subcirc0,[qreg_3[0],1,qreg_0[1],0])
					main_circ.append(subcirc1,[qreg_3[0],1,qreg_0[2],qreg_0[0]])
				with else_1:
					main_circ.rz(-0.821000, qreg_3[0])
					main_circ.u(0,0,0.152000, qreg_0[2])
					main_circ.u(pi/2,-0.469000,-0.936000, qreg_0[0])
					main_circ.ry(-0.418000, qreg_0[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.ry(param_2, 1)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.ry(param_2, 1)
							main_circ.append(subcirc4,[qreg_3[0],qreg_0[2],qreg_0[0],0,qreg_0[1]])
					with case_2(1):
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.append(subcirc3,[qreg_0[2],qreg_3[0],1,0,qreg_0[0]])
						with else_1:
							main_circ.u(pi/2,-0.302000,param_4, qreg_0[2])
							main_circ.u(param_4,param_3,param_3, qreg_3[0])
							main_circ.ry(param_3, qreg_0[2])
							main_circ.ry(0.145000, 1)
							main_circ.u(0,param_1,param_4, qreg_0[1])
			with case_3(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[0],1])
							main_circ.append(subcirc3,[qreg_0[1],0,1,qreg_0[2],qreg_0[0]])
						with else_1:
							main_circ.u(param_3,0,0.370000, qreg_3[0])
							main_circ.u(0,param_2,param_4, 1)
							main_circ.append(subcirc4,[qreg_3[0],0,qreg_0[1],qreg_0[2],1])
					with case_2(1):
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.append(subcirc0,[1,qreg_3[0],0,qreg_0[2]])
							with case_1(1):
								main_circ.barrier(qreg_0[2])
	with case_4(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.barrier(1)
			with case_3(1):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[1])
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(qreg_3[0])
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.u(pi/2,-0.493000,-0.412000, qreg_0[0])
								main_circ.id(1)
							with case_1(1):
								main_circ.id(qreg_0[1])
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[1])
							with case_1(1):
								main_circ.barrier(qreg_0[1])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[1])
						main_circ.id(qreg_0[1])
					with case_2(1):
						main_circ.barrier(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.id(qreg_0[1])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.id(0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_3[0])
			main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.barrier(qreg_0[0])
			with case_3(1):
				main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(qreg_3[0])
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.id(qreg_0[2])
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[2])
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(qreg_3[0], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[1])
							with case_1(1):
								main_circ.barrier(0)
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(0)
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_3[0])
							with case_1(1):
								main_circ.barrier(1)
						main_circ.barrier(qreg_0[0])
					with case_2(1):
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(1)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(1)
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(0)
						main_circ.barrier(0)
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(0, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_3[0])
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_3[0])
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[2])
						with else_1:
							main_circ.id(0)
						main_circ.measure(qreg_3[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.id(qreg_0[2])
					with case_2(1):
						main_circ.barrier(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.barrier(0)
				with else_2:
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.id(qreg_3[0])
				main_circ.id(qreg_0[1])
			with case_3(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.id(qreg_3[0])
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(0)
							with case_1(1):
								main_circ.id(qreg_0[2])
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(1)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(1)
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.id(qreg_0[2])
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[1])
						with else_1:
							main_circ.barrier(qreg_0[2])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[1])
						main_circ.id(qreg_0[1])
					with case_2(1):
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[1])
						with else_1:
							main_circ.barrier(0)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(0)
						main_circ.id(0)
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.barrier(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.id(1)
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.barrier(1)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.barrier(1)
		main_circ.barrier(qreg_3[0])
bindings = {param_1: -0.336000, param_2: -0.493000, param_3: -0.681000, param_4: -0.586000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "947")
