from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.806000,0.088000, qreg_2[0])
subcirc0.h(qreg_1[0])
subcirc0.h(qreg_2[0])
subcirc0.cz(qreg_3[0],qreg_2[0])
subcirc0.u(pi/2,0.917000,-0.810000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(pi/2,0.569000,0.396000, qreg_1[1])
subcirc1.s(qreg_1[2])
subcirc1.s(qreg_1[0])
subcirc1.h(qreg_1[0])
subcirc1.u(pi/2,0.475000,0.363000, qreg_1[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_0[2])
subcirc2.u(pi/2,-0.468000,-0.420000, qreg_0[2])
subcirc2.s(qreg_0[2])
subcirc2.h(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_0[2],qreg_0[1])
subcirc3.h(qreg_0[1])
subcirc3.s(qreg_0[0])
subcirc3.h(qreg_0[1])
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.append(subcirc0,[3,0,qreg_1[0],qreg_0[0]])
		with else_2:
			main_circ.s(1)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[1,3,2,qreg_1[0],0])
				with case_1(1):
					main_circ.u(pi/2,-0.462000,-0.136000, 1)
					main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],2,0])
	with else_3:
		main_circ.append(subcirc1,[qreg_1[0],1,2,0,qreg_0[0]])
with else_4:
	main_circ.append(subcirc0,[0,qreg_0[0],3,1])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.append(subcirc2,[3,2,qreg_1[0],0])
				with else_2:
					main_circ.cz(0,qreg_1[0])
					main_circ.cz(3,qreg_1[0])
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.cz(1,2)
						main_circ.cz(3,1)
					with else_1:
						main_circ.cz(0,3)
						main_circ.cz(0,1)
						main_circ.cz(1,2)
						main_circ.cz(qreg_1[0],2)
						main_circ.id(qreg_1[0])
			with case_3(1):
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_1[0])
						main_circ.measure(qreg_1[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.u(param_1,param_2,0.844000, 3)
							main_circ.barrier(2)
						with else_1:
							main_circ.u(pi/2,-0.354000,param_3, 2)
							main_circ.id(3)
						main_circ.barrier(2)
					with case_2(1):
						main_circ.h(3)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(qreg_1[0])
						main_circ.measure(3, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.id(3)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(3)
						main_circ.barrier(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.id(qreg_1[0])
				with else_2:
					main_circ.id(qreg_1[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(1)
					main_circ.barrier(1)
				with else_2:
					main_circ.barrier(1)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.measure(3, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(qreg_1[0])
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(0)
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(1)
							with case_1(1):
								main_circ.barrier(qreg_1[0])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_1[0])
						with else_1:
							main_circ.barrier(0)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_1[0])
						with else_1:
							main_circ.id(1)
						main_circ.id(3)
					with case_2(1):
						main_circ.barrier(2)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(2)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.id(0)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(2)
						with else_1:
							main_circ.id(0)
						main_circ.measure(2, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_1[0])
							with case_1(1):
								main_circ.id(qreg_0[0])
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.id(0)
						main_circ.measure(3, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.id(2)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.id(0)
						main_circ.id(qreg_1[0])
					with case_2(1):
						main_circ.id(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.id(2)
				with else_2:
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_1[0])
						main_circ.id(2)
					with case_2(1):
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.measure(qreg_1[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(2)
						main_circ.measure(1, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[0])
							with case_1(1):
								main_circ.id(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(0)
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(1)
							with case_1(1):
								main_circ.barrier(2)
						main_circ.measure(qreg_1[0], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_1[0])
							with case_1(1):
								main_circ.id(2)
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.barrier(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(2)
						with else_1:
							main_circ.id(1)
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.id(qreg_0[0])
						main_circ.barrier(qreg_1[0])
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.id(0)
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(0)
					main_circ.id(0)
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(2)
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(3)
						main_circ.measure(2, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(0)
							with case_1(1):
								main_circ.barrier(0)
						main_circ.measure(qreg_1[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.barrier(qreg_1[0])
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(2)
							with case_1(1):
								main_circ.barrier(0)
						main_circ.barrier(3)
					with case_2(1):
						main_circ.barrier(2)
				main_circ.barrier(2)
	with case_4(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(2)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_1[0])
					with else_1:
						main_circ.barrier(2)
					main_circ.id(2)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(3)
					main_circ.measure(qreg_1[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.barrier(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_1[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(0)
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(3)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.id(2)
					main_circ.id(2)
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(0, creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(3)
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.barrier(1)
						main_circ.id(qreg_1[0])
					with case_2(1):
						main_circ.id(0)
				main_circ.barrier(qreg_1[0])
			with case_3(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(2)
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(1)
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(2)
					main_circ.barrier(0)
				main_circ.id(0)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(3)
					main_circ.measure(qreg_1[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(3)
					main_circ.id(qreg_1[0])
				with else_2:
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.barrier(3)
					main_circ.barrier(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.barrier(3)
				with else_2:
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(2)
					main_circ.barrier(qreg_1[0])
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.id(0)
						main_circ.barrier(0)
					with case_2(1):
						main_circ.id(qreg_1[0])
				main_circ.barrier(0)
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.id(qreg_0[0])
				with else_2:
					main_circ.barrier(qreg_1[0])
				main_circ.barrier(qreg_0[0])
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_3:
			main_circ.id(qreg_0[0])
		with else_3:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.barrier(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(0)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(3)
				main_circ.id(2)
			with else_2:
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(qreg_1[0])
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(3)
				main_circ.barrier(0)
			with else_2:
				main_circ.barrier(1)
			main_circ.barrier(1)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.barrier(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(2)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(0)
				main_circ.id(2)
			main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_1[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.id(1)
			main_circ.id(3)
		main_circ.barrier(0)
bindings = {param_1: 0.333000, param_2: -0.640000, param_3: 0.197000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1720")
