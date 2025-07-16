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
subcirc0.u(0,0,-0.432000, qreg_0[1])
subcirc0.u(0,0,-0.159000, qreg_0[1])
subcirc0.u(0,0,0.124000, qreg_0[0])
subcirc0.u(-0.149000,0.681000,-0.434000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.637000, qreg_0[1])
subcirc1.y(qreg_3[0])
subcirc1.rz(-0.727000, qreg_3[0])
subcirc1.rz(-0.338000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.251000,-0.238000,0.661000, qreg_0[1])
subcirc2.u(-0.042000,-0.107000,0.334000, qreg_3[0])
subcirc2.rz(0.047000, qreg_0[1])
subcirc2.u(-0.715000,-0.595000,0.491000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.u(param_0,0,0.227000, 1)
				main_circ.u(0,0,param_0, 1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0,0,param_0, 3)
				main_circ.id(3)
			with else_1:
				main_circ.u(0,0,0.954000, 0)
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,-0.511000,-0.749000, 2)
					main_circ.y(0)
					main_circ.y(2)
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rz(0.821000, 0)
				main_circ.id(3)
			with else_1:
				main_circ.barrier(1)
	with else_3:
		main_circ.id(2)
main_circ.y(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(param_0,param_0,0.893000, 1)
					main_circ.rz(param_0, 2)
					main_circ.id(1)
				with else_1:
					main_circ.u(0.772000,param_0,param_0, 1)
			main_circ.u(param_0,0,param_0, 1)
		with case_3(1):
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rz(0.200000, 2)
					main_circ.u(param_0,param_0,param_0, 3)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.u(param_0,0,param_0, 1)
					main_circ.id(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.y(2)
					main_circ.id(1)
with else_4:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.barrier(0)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(3)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(0,0,param_0, 1)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.rz(param_0, 3)
						main_circ.u(0,param_0,param_0, 0)
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.rz(param_0, 0)
					main_circ.barrier(0)
	with else_3:
		main_circ.u(param_0,0,-0.789000, 1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rz(param_0, 1)
					main_circ.barrier(3)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.y(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(0)
	main_circ.barrier(1)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.rz(param_0, 1)
						main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.rz(param_0, 1)
						main_circ.id(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.rz(-0.494000, 2)
						main_circ.y(0)
						main_circ.u(param_0,0.884000,param_0, 2)
						main_circ.y(3)
						main_circ.id(0)
				with case_2(1):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(2)
					main_circ.y(3)
					main_circ.u(param_0,param_0,param_0, 3)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(0)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.u(0.562000,0.715000,-0.828000, 1)
						main_circ.y(0)
						main_circ.rz(-0.926000, 2)
						main_circ.barrier(0)
		with else_3:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.u(param_0,0.399000,param_0, 3)
					main_circ.barrier(0)
				main_circ.id(1)
	with case_4(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(-0.878000,-0.127000,-0.801000, 3)
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.u(-0.961000,0.392000,param_0, 1)
						main_circ.barrier(3)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.y(2)
					main_circ.barrier(0)
				with case_2(1):
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.rz(param_0, 3)
						main_circ.rz(-0.981000, 1)
						main_circ.u(param_0,0,param_0, 3)
						main_circ.y(1)
					with else_1:
						main_circ.u(-0.318000,0.414000,-0.300000, 0)
						main_circ.id(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.rz(param_0, 1)
						main_circ.u(param_0,0.993000,-0.101000, 0)
						main_circ.id(2)
					with case_1(1):
						main_circ.id(3)
				main_circ.id(3)
			with else_2:
				main_circ.id(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.u(param_0,param_0,param_0, 0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.u(-0.719000,0.734000,0.813000, 0)
						main_circ.barrier(3)
					with else_1:
						main_circ.u(param_0,-0.079000,param_0, 2)
					main_circ.barrier(1)
				with case_2(1):
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.u(param_0,param_0,param_0, 3)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.id(2)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(3)
					main_circ.measure(3, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(1)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(2)
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(1)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(2)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.id(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(1)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(2)
					with else_1:
						main_circ.barrier(1)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.barrier(2)
		with case_3(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(2)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.id(1)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(3)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(0)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.barrier(0)
			with else_2:
				main_circ.barrier(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(3)
				with case_2(1):
					main_circ.barrier(0)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(3)
			with else_2:
				main_circ.barrier(2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.id(2)
			with else_2:
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.id(2)
				main_circ.barrier(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.barrier(3)
				with case_2(1):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(0)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(3)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(3)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.id(3)
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(1)
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(3)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.id(3)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(3)
					main_circ.id(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.id(1)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(3)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(3)
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(3)
						with case_1(1):
							main_circ.id(1)
					main_circ.barrier(1)
				with case_2(1):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(2)
					main_circ.id(1)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(3)
				main_circ.id(0)
			with else_2:
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(3)
				main_circ.id(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.id(0)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.barrier(3)
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(2)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(3)
				main_circ.barrier(2)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(0)
				main_circ.id(0)
			with else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(1)
				main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.id(2)
			with else_2:
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.id(1)
			main_circ.id(3)
with else_4:
	main_circ.barrier(0)
bindings = {param_0: 0.340000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "903")
