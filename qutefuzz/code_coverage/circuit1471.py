from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.y(qreg_0[1])
subcirc0.ry(0.094000, qreg_0[3])
subcirc0.y(qreg_0[2])
subcirc0.s(qreg_0[3])
subcirc0.s(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_3[0])
subcirc1.ry(0.259000, qreg_0[2])
subcirc1.s(qreg_3[0])
subcirc1.ry(0.303000, qreg_0[0])
subcirc1.s(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cy(qreg_2[0],qreg_0[1])
subcirc2.y(qreg_2[0])
subcirc2.s(qreg_2[0])
subcirc2.ry(-0.644000, qreg_2[1])
subcirc2.s(qreg_2[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_0[1])
subcirc3.s(qreg_3[0])
subcirc3.ry(-0.352000, qreg_3[0])
subcirc3.ry(0.233000, qreg_0[2])
subcirc3.cy(qreg_3[0],qreg_0[2])

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

main_circ.cy(1,qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],1,0])
with else_4:
	main_circ.ry(-0.616000, 1)
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.append(subcirc2,[qreg_0[3],qreg_0[0],qreg_0[2],0])
					with else_1:
						main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],1,qreg_0[3]])
				with case_2(1):
					main_circ.barrier(1)
		with case_3(1):
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(1)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cy(qreg_0[0],qreg_0[2])
					main_circ.y(1)
				with else_1:
					main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],qreg_0[3],1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.ry(-0.673000, qreg_0[1])
						main_circ.cy(qreg_0[3],qreg_0[1])
						main_circ.y(qreg_0[3])
						main_circ.ry(param_1, qreg_0[2])
					with case_1(1):
						main_circ.cy(qreg_0[1],qreg_0[2])
						main_circ.id(qreg_0[1])
			with else_2:
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.append(subcirc3,[qreg_0[0],qreg_0[2],0,qreg_0[3]])
				with else_1:
					main_circ.append(subcirc3,[qreg_0[3],1,qreg_0[2],qreg_0[1]])
		with case_3(1):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],qreg_0[2],1])
				with case_2(1):
					main_circ.cy(qreg_0[0],0)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.cy(0,qreg_0[0])
					with else_1:
						main_circ.cy(qreg_0[1],0)
					main_circ.cy(0,qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cy(qreg_0[1],1)
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cy(qreg_0[2],0)
				main_circ.y(1)
				main_circ.cy(qreg_0[1],qreg_0[2])
				main_circ.append(subcirc3,[qreg_0[2],0,qreg_0[3],qreg_0[0]])
with else_4:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[3])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.s(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(qreg_0[3])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(1)
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.s(qreg_0[2])
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(1)
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.id(1)
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.barrier(qreg_0[1])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[3])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.barrier(qreg_0[3])
			main_circ.id(1)
		with case_3(1):
			main_circ.barrier(qreg_0[3])
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.id(qreg_0[2])
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(0)
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(0)
					main_circ.barrier(qreg_0[1])
			main_circ.id(0)
		with case_3(1):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[3])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.id(qreg_0[1])
				with case_2(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[3])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(1)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.barrier(0)
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.id(qreg_0[1])
			main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.barrier(0)
	with else_3:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.id(qreg_0[3])
			with case_2(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.id(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.barrier(1)
		with else_2:
			main_circ.id(1)
		main_circ.barrier(qreg_0[2])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(1)
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(1)
			main_circ.id(qreg_0[2])
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[3])
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[3])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.barrier(qreg_0[0])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[3])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.barrier(0)
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.id(1)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.id(1)
			main_circ.barrier(qreg_0[0])
		main_circ.id(qreg_0[1])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[2])
	main_circ.barrier(qreg_0[3])
bindings = {param_1: -0.048000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1471", "RemoveResetInZeroState")
