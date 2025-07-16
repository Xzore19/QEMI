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
subcirc0.u(pi/2,0.712000,0.987000, qreg_0[0])
subcirc0.h(qreg_2[0])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cz(1,2)
					main_circ.u(param_1,-0.690000,-0.610000, 1)
					main_circ.ry(-0.697000, qreg_0[0])
					main_circ.h(3)
		with case_3(1):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.append(subcirc0,[3,qreg_0[0],1,0])
						main_circ.ry(param_1, 1)
				with case_2(1):
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.cz(qreg_0[0],2)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.append(subcirc0,[2,1,3,0])
with else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.ry(param_2, 1)
				main_circ.h(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cz(2,0)
						main_circ.h(qreg_0[0])
						main_circ.u(pi/2,-0.645000,0.258000, 1)
						main_circ.ry(param_1, qreg_0[0])
					with case_1(1):
						main_circ.ry(-0.597000, qreg_0[0])
						main_circ.u(pi/2,0.937000,-0.393000, 2)
						main_circ.h(qreg_0[0])
						main_circ.ry(0.770000, 3)
			with case_2(1):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.append(subcirc0,[3,qreg_0[0],2,0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(0,2)
	main_circ.ry(0.271000, 0)
	main_circ.u(param_0,param_0,param_1, 1)
main_circ.ry(0.425000, 1)
main_circ.cz(qreg_0[0],2)
main_circ.cz(qreg_0[0],1)
main_circ.cz(0,qreg_0[0])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.cz(3,0)
with else_4:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.cz(2,3)
	with else_3:
		main_circ.cz(qreg_0[0],2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(2,0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cz(qreg_0[0],0)
			with else_1:
				main_circ.cz(qreg_0[0],1)
				main_circ.cz(0,qreg_0[0])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_3:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,param_2,-0.361000, 2)
						main_circ.h(qreg_0[0])
						main_circ.cz(qreg_0[0],2)
						main_circ.barrier(1)
					with case_1(1):
						main_circ.h(1)
						main_circ.ry(param_2, 1)
						main_circ.id(3)
		with else_3:
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.id(0)
				with case_2(1):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.id(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(2)
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.barrier(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(3)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(1)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.barrier(2)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.id(qreg_0[0])
			with else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(2)
				main_circ.id(2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.id(3)
				with case_2(1):
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(2)
					with else_1:
						main_circ.id(0)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.id(1)
					main_circ.id(0)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.id(0)
				main_circ.barrier(1)
			with else_2:
				main_circ.id(1)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(1)
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.id(qreg_0[0])
	with case_4(1):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_3:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(0)
					main_circ.id(0)
				with case_2(1):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.id(1)
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(2)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(0)
					main_circ.barrier(qreg_0[0])
			main_circ.id(1)
		with else_3:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(1)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(2)
			main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(2)
				main_circ.id(3)
			main_circ.id(3)
		with else_3:
			main_circ.barrier(3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(3)
				main_circ.id(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(3)
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.id(0)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(1)
				main_circ.barrier(0)
			with else_2:
				main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_0[0])
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(2)
					main_circ.id(1)
				with else_2:
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(1)
				main_circ.id(0)
			with case_3(1):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(3)
					main_circ.barrier(3)
				with else_2:
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(3)
						with else_1:
							main_circ.id(2)
						main_circ.measure(2, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.barrier(1)
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(2)
							with case_1(1):
								main_circ.barrier(1)
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(2)
						main_circ.measure(2, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(3)
							with case_1(1):
								main_circ.barrier(qreg_0[0])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(0)
						with else_1:
							main_circ.id(2)
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(1)
						with else_1:
							main_circ.id(0)
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(2)
						with else_1:
							main_circ.barrier(3)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(2)
						main_circ.barrier(1)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.id(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(2)
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(3, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(3)
							with case_1(1):
								main_circ.id(3)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(0)
							with case_1(1):
								main_circ.id(3)
						main_circ.barrier(3)
					with case_2(1):
						main_circ.barrier(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.barrier(3)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(1)
						main_circ.measure(1, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.barrier(1)
						main_circ.id(2)
					with case_2(1):
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.id(2)
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(2)
						main_circ.id(0)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.barrier(1)
				main_circ.id(2)
		main_circ.id(3)
bindings = {param_0: -0.583000, param_1: -0.328000, param_2: 0.316000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1883", "RemoveFinalReset")
