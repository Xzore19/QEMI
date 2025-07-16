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
subcirc0.u(0.016000,0.654000,0.569000, qreg_0[0])
subcirc0.x(qreg_1[1])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_1[1])
subcirc0.u(pi/2,0.113000,0.217000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[1])
subcirc1.u(0.445000,0.275000,0.347000, qreg_0[1])
subcirc1.x(qreg_0[0])
subcirc1.u(0.810000,-0.123000,0.386000, qreg_0[2])
subcirc1.x(qreg_0[1])

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
param_4 = Parameter("param_4")

main_circ.append(subcirc1,[qreg_0[3],0,qreg_0[2],1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.h(qreg_0[3])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],1,qreg_0[2],qreg_0[1],0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.u(-0.497000,param_4,0.518000, qreg_0[3])
						main_circ.u(param_4,param_4,param_4, qreg_0[1])
						main_circ.append(subcirc0,[1,0,qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
					with else_1:
						main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[2],qreg_0[3],qreg_0[0],1])
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.u(param_3,param_1,param_4, qreg_0[1])
					main_circ.u(0.637000,0.402000,param_1, qreg_0[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.x(qreg_0[2])
						main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],0,qreg_0[0],1,qreg_0[3]])
				with else_2:
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.x(qreg_0[1])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],0,qreg_0[0]])
					with else_1:
						main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],0,qreg_0[3],qreg_0[1],1])
	with case_4(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[3])
						with case_1(1):
							main_circ.h(1)
							main_circ.barrier(qreg_0[1])
					main_circ.barrier(qreg_0[1])
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[3])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[3])
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.id(qreg_0[3])
				with else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(1)
			with case_3(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[3])
						with else_1:
							main_circ.barrier(qreg_0[1])
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(qreg_0[3])
						with else_1:
							main_circ.id(1)
						main_circ.barrier(0)
					with case_2(1):
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_0[2])
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[3])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[3])
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(0)
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(0)
					main_circ.id(0)
				with else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.id(qreg_0[1])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(1)
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[3])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.barrier(qreg_0[2])
				with else_2:
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(1)
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(1)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.barrier(qreg_0[3])
				with else_2:
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.barrier(0)
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.barrier(qreg_0[2])
				with else_2:
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[3])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.id(0)
				main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(1)
					main_circ.barrier(qreg_0[3])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.barrier(qreg_0[3])
				with else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.barrier(1)
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.barrier(qreg_0[2])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.id(0)
				with else_2:
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(1)
					main_circ.barrier(0)
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.id(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(qreg_0[1])
						main_circ.measure(0, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[3])
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(0)
							with case_1(1):
								main_circ.id(qreg_0[1])
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.barrier(1)
						main_circ.id(1)
					with case_2(1):
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(1)
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(qreg_0[1])
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[0])
							with case_1(1):
								main_circ.barrier(1)
						main_circ.id(qreg_0[1])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[3])
						with case_1(1):
							main_circ.id(0)
					main_circ.id(0)
				with else_2:
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[2])
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.id(qreg_0[3])
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(1)
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.barrier(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[3])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(qreg_0[3])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.id(1)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(0)
					main_circ.barrier(qreg_0[0])
				main_circ.barrier(qreg_0[2])
			with case_3(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(1)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.id(0)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_0[2])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(0)
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[3])
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.id(qreg_0[1])
				with else_2:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[3], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(0)
						main_circ.id(qreg_0[2])
					with case_2(1):
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(qreg_0[2])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[2])
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[1])
							with case_1(1):
								main_circ.id(qreg_0[1])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[2])
						main_circ.barrier(qreg_0[3])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.id(qreg_0[1])
				with else_2:
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[2])
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.id(qreg_0[3])
				main_circ.id(qreg_0[1])
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_0[2])
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(qreg_0[2])
						with else_1:
							main_circ.barrier(qreg_0[1])
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[3], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.id(qreg_0[3])
						main_circ.barrier(qreg_0[2])
					with case_2(1):
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[3])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[2])
						with else_1:
							main_circ.barrier(qreg_0[1])
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.barrier(0)
						main_circ.measure(qreg_0[3], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(0)
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(qreg_0[1])
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(0)
						main_circ.id(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(0)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[3])
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[3])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(1)
					main_circ.barrier(qreg_0[2])
				with else_2:
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[2])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[3])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[3])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.id(qreg_0[0])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.id(qreg_0[2])
				main_circ.id(qreg_0[1])
			with case_3(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(0)
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_0[1])
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.id(1)
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.barrier(qreg_0[3])
					with case_2(1):
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(0)
						main_circ.measure(qreg_0[3], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[3])
						main_circ.id(qreg_0[2])
				main_circ.barrier(1)
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_3:
			main_circ.barrier(qreg_0[3])
		with else_3:
			main_circ.id(qreg_0[2])
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_3:
			main_circ.barrier(qreg_0[2])
		with else_3:
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_0[1])
			with else_2:
				main_circ.barrier(0)
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_0[1])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.id(qreg_0[3])
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.id(1)
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(qreg_0[3])
				main_circ.id(0)
			with else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(1)
				main_circ.barrier(qreg_0[1])
			with else_2:
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.barrier(qreg_0[3])
				with case_2(1):
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(1)
					main_circ.barrier(qreg_0[1])
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.id(qreg_0[3])
					main_circ.id(qreg_0[2])
				with case_2(1):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(qreg_0[3])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[3])
					with else_1:
						main_circ.barrier(qreg_0[3])
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(1)
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[3])
				with else_1:
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.id(qreg_0[3])
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(0)
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_0[1])
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.id(qreg_0[3])
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[3])
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_0[3])
					main_circ.barrier(0)
				with case_2(1):
					main_circ.barrier(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[3])
				with else_1:
					main_circ.id(1)
				main_circ.barrier(qreg_0[1])
			main_circ.barrier(0)
		main_circ.barrier(qreg_0[3])
bindings = {param_1: 0.942000, param_3: -0.503000, param_4: -0.475000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "694", "ConsolidateBlocks")
