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
subcirc0.u(0.217000,-0.083000,0.587000, qreg_0[2])
subcirc0.s(qreg_0[2])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(0.844000, qreg_0[0])
subcirc1.s(qreg_0[0])
subcirc1.u(0,0,-0.474000, qreg_2[1])
subcirc1.u(0,0,-0.069000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(-0.290000,-0.403000,0.769000, qreg_2[0])
subcirc2.ry(-0.732000, qreg_2[1])
subcirc2.u(-0.437000,-0.036000,-0.032000, qreg_0[0])
subcirc2.u(0.462000,-0.287000,-0.299000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.s(qreg_0[0])
subcirc3.u(0,0,0.542000, qreg_0[0])
subcirc3.s(qreg_0[0])
subcirc3.u(-0.175000,-0.206000,-0.862000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.u(-0.413000,-0.654000,param_3, qreg_0[1])
main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.ry(param_4, qreg_0[2])
				main_circ.u(param_5,param_0,param_4, qreg_0[2])
				main_circ.u(param_3,-0.058000,0.599000, qreg_0[1])
				main_circ.ry(-0.119000, qreg_0[0])
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
				main_circ.u(param_3,0,param_1, qreg_3[0])
with else_4:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.id(qreg_0[1])
	with else_3:
		main_circ.ry(param_2, qreg_0[2])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
				with else_1:
					main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.id(qreg_3[0])
	with case_4(1):
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.u(-0.339000,0.831000,param_0, qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.ry(-0.315000, qreg_0[2])
					main_circ.barrier(qreg_0[1])
			main_circ.u(0.432000,param_2,0.427000, qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.s(qreg_0[1])
						main_circ.u(param_3,param_3,param_1, qreg_0[2])
						main_circ.u(0.627000,param_2,0.154000, qreg_0[1])
						main_circ.u(param_2,-0.207000,param_0, qreg_0[0])
					with case_1(1):
						main_circ.u(param_1,0.470000,param_1, qreg_3[0])
						main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
	with case_4(1):
		main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.ry(-0.551000, qreg_3[0])
						main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.ry(param_0, qreg_0[0])
						main_circ.ry(0.474000, qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.s(qreg_3[0])
						main_circ.u(-0.457000,-0.991000,0.309000, qreg_0[1])
						main_circ.u(0,param_3,0.161000, qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[1])
			with case_3(1):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.ry(param_0, qreg_0[2])
							main_circ.u(param_4,param_3,-0.241000, qreg_0[1])
							main_circ.ry(param_3, qreg_0[0])
							main_circ.ry(0.156000, qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
	with case_4(1):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.id(qreg_0[1])
			with else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.s(qreg_0[2])
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_3[0])
					main_circ.id(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[2])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.barrier(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[2])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.barrier(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_0[2])
			with else_2:
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[2])
				main_circ.id(qreg_0[0])
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.barrier(qreg_0[1])
			with else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.barrier(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.barrier(qreg_0[1])
			with else_2:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.barrier(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.id(qreg_3[0])
			main_circ.barrier(qreg_0[0])
		with else_3:
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.barrier(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_3[0])
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_3[0])
					main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_3[0])
				with else_1:
					main_circ.id(qreg_3[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_3[0])
				main_circ.id(qreg_0[2])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.barrier(qreg_0[2])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.id(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.id(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.id(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.id(qreg_0[0])
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.barrier(qreg_0[0])
			with case_3(1):
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[1])
						with else_1:
							main_circ.id(qreg_0[1])
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_3[0])
						with else_1:
							main_circ.id(qreg_0[2])
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_3[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[2])
							with case_1(1):
								main_circ.id(qreg_0[2])
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[1])
							with case_1(1):
								main_circ.id(qreg_0[2])
						main_circ.id(qreg_0[2])
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[2])
							with case_1(1):
								main_circ.barrier(qreg_3[0])
						main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_3[0])
					main_circ.id(qreg_0[1])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_3[0])
		with else_3:
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.id(qreg_0[2])
			main_circ.id(qreg_0[1])
		main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.563000, param_1: 0.346000, param_2: -0.429000, param_3: -0.236000, param_4: -0.733000, param_5: -0.953000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "549", "ConsolidateBlocks")
