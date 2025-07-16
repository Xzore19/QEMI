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
subcirc0.ry(0.608000, qreg_3[0])
subcirc0.u(-0.173000,-0.475000,0.017000, qreg_0[2])
subcirc0.u(0.121000,0.391000,-0.853000, qreg_0[2])
subcirc0.z(qreg_3[0])
subcirc0.u(0.756000,0.572000,-0.274000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.u(-0.019000,0.391000,0.514000, qreg_0[1])
						main_circ.s(1)
					with else_1:
						main_circ.s(1)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.z(0)
							main_circ.u(param_0,param_1,param_0, 1)
							main_circ.ry(param_2, qreg_2[0])
							main_circ.ry(param_3, qreg_0[1])
						with case_1(1):
							main_circ.s(qreg_0[0])
							main_circ.u(-0.015000,0.667000,param_4, qreg_2[0])
							main_circ.s(0)
							main_circ.u(param_3,0.337000,0.399000, 0)
				with case_2(1):
					main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_0[0],0,qreg_2[1],1])
		with else_3:
			main_circ.ry(param_0, 1)
			main_circ.z(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.ry(param_3, qreg_0[1])
						main_circ.u(0.019000,-0.887000,0.658000, 0)
						main_circ.z(0)
						main_circ.s(qreg_0[1])
					with case_1(1):
						main_circ.ry(-0.784000, qreg_2[1])
						main_circ.s(qreg_2[1])
						main_circ.u(0.752000,0.736000,param_2, qreg_2[0])
						main_circ.ry(-0.637000, qreg_0[1])
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.z(0)
						main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[1],1,qreg_2[0],0])
					with case_1(1):
						main_circ.s(qreg_2[1])
						main_circ.ry(param_0, qreg_0[0])
						main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],qreg_2[0],qreg_0[1],1,0])
	with case_4(1):
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.s(qreg_2[1])
						main_circ.u(param_2,0.560000,param_4, qreg_2[1])
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.id(1)
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(qreg_0[1])
				main_circ.id(1)
			with case_3(1):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.barrier(qreg_0[1])
				main_circ.id(0)
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.barrier(qreg_2[1])
					with case_2(1):
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[0])
							with case_1(1):
								main_circ.barrier(0)
						main_circ.barrier(1)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.barrier(qreg_0[0])
				with else_2:
					main_circ.id(1)
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_0[1])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.barrier(qreg_2[0])
						main_circ.id(qreg_2[0])
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.id(qreg_0[1])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[1])
						with else_1:
							main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[1])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.barrier(0)
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_0[1])
						with else_1:
							main_circ.id(1)
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_0[1])
						with else_1:
							main_circ.barrier(qreg_2[0])
						main_circ.barrier(qreg_2[1])
					with case_2(1):
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[1])
							with case_1(1):
								main_circ.barrier(qreg_0[1])
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[0])
							with case_1(1):
								main_circ.barrier(1)
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.id(qreg_2[0])
						main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(1)
					main_circ.id(qreg_2[0])
				with else_2:
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_2[0])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(1)
						main_circ.id(qreg_2[1])
					with case_2(1):
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.id(qreg_0[1])
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(0)
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_2[1])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.id(0)
				with else_2:
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.barrier(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_2[0])
				main_circ.id(qreg_0[0])
			with case_3(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[1])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(1)
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[0])
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[1])
							with case_1(1):
								main_circ.barrier(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.id(qreg_2[1])
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_2[1])
						main_circ.id(qreg_0[0])
					with case_2(1):
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(qreg_2[1])
						main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.barrier(qreg_0[1])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[1])
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(1)
					main_circ.barrier(0)
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.id(qreg_0[1])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_2[1])
						with else_1:
							main_circ.id(0)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[1])
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_2[0])
						with else_1:
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.barrier(qreg_0[1])
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[0])
						with else_1:
							main_circ.id(1)
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.id(1)
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.id(1)
						main_circ.barrier(1)
					with case_2(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.id(qreg_2[0])
					with case_2(1):
						main_circ.measure(1, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_2[0])
						main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.barrier(1)
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(1)
						main_circ.measure(1, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[1])
							with case_1(1):
								main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(1)
						main_circ.id(qreg_2[1])
					with case_2(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.barrier(0)
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.id(0)
				with else_2:
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.barrier(qreg_0[1])
						main_circ.measure(0, creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(1)
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_0[1])
						with else_1:
							main_circ.id(qreg_0[1])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[1])
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.id(qreg_0[0])
						main_circ.measure(1, creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(1)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.id(qreg_0[1])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[1])
						main_circ.id(qreg_2[0])
					with case_2(1):
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(1)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.id(1)
						main_circ.barrier(1)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_2[1])
			with case_3(1):
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.id(qreg_0[1])
				with else_2:
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_2[1])
				main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.barrier(0)
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_2[1])
				with case_2(1):
					main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.barrier(qreg_2[1])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.id(0)
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_0[0])
			main_circ.id(0)
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(1)
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(1)
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(qreg_0[1])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.id(qreg_0[1])
				with case_2(1):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.id(1)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(0)
				main_circ.barrier(qreg_2[1])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.id(1)
			with else_2:
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_2[1])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.barrier(1)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_2[0])
			main_circ.id(qreg_0[1])
		with else_3:
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.id(qreg_2[0])
				with case_2(1):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(1)
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_2[1])
					main_circ.barrier(qreg_2[1])
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(1)
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.barrier(qreg_2[0])
			with else_2:
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[0])
				main_circ.barrier(0)
			main_circ.barrier(1)
		main_circ.id(qreg_0[0])
bindings = {param_0: -0.344000, param_1: 0.642000, param_2: -0.043000, param_3: -0.193000, param_4: 0.969000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "545")
