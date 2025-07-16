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
subcirc0.s(qreg_0[2])
subcirc0.u(pi/2,-0.342000,0.165000, qreg_3[0])
subcirc0.rx(0.499000, qreg_0[1])
subcirc0.s(qreg_0[2])
subcirc0.rx(-0.928000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.u(param_0,param_0,param_0, qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(param_0,param_2,param_0, qreg_2[1])
						main_circ.u(param_0,0,param_0, qreg_0[0])
						main_circ.u(param_2,param_0,0.094000, qreg_0[0])
						main_circ.u(param_0,0.685000,param_1, qreg_2[1])
					with case_1(1):
						main_circ.rx(param_2, qreg_0[0])
						main_circ.id(qreg_2[0])
		with case_3(1):
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.u(pi/2,param_0,0.157000, qreg_0[0])
						main_circ.u(param_2,0,-0.211000, qreg_2[1])
						main_circ.rx(0.542000, qreg_1[0])
						main_circ.s(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
				with case_2(1):
					main_circ.id(qreg_2[0])
with else_4:
	main_circ.u(0,param_2,param_0, qreg_2[1])
	main_circ.barrier(qreg_2[1])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.rx(param_1, qreg_1[0])
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.u(param_2,param_0,-0.520000, qreg_1[0])
					main_circ.u(pi/2,-0.035000,param_1, qreg_1[0])
				with else_1:
					main_circ.rx(param_2, qreg_1[0])
					main_circ.s(qreg_2[0])
					main_circ.rx(-0.147000, qreg_2[0])
		with else_3:
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.u(pi/2,-0.831000,param_2, qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(param_2,0,param_1, qreg_2[1])
				with else_1:
					main_circ.u(param_1,0,-0.016000, qreg_2[0])
					main_circ.s(qreg_2[0])
					main_circ.s(qreg_1[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(param_0,0.180000,0.012000, qreg_2[1])
					main_circ.u(param_1,param_2,param_1, qreg_2[0])
					main_circ.u(pi/2,0.598000,param_2, qreg_0[0])
	with case_4(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.s(qreg_1[0])
						main_circ.id(qreg_1[0])
					with else_1:
						main_circ.u(0,param_2,param_0, qreg_1[0])
				with else_2:
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.u(pi/2,0.096000,param_0, qreg_1[0])
						main_circ.u(param_1,0.887000,0.768000, qreg_2[0])
						main_circ.u(0,0,param_2, qreg_1[0])
						main_circ.s(qreg_2[1])
					with else_1:
						main_circ.s(qreg_1[0])
						main_circ.barrier(qreg_2[1])
			with case_3(1):
				main_circ.u(pi/2,param_0,param_1, qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[1])
							with case_1(1):
								main_circ.u(0,param_0,-0.710000, qreg_0[0])
								main_circ.rx(param_0, qreg_2[1])
								main_circ.u(0,0,param_1, qreg_2[1])
								main_circ.s(qreg_0[0])
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.rx(param_2, qreg_2[0])
							main_circ.barrier(qreg_0[0])
						main_circ.rx(param_0, qreg_0[0])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.s(qreg_2[1])
						with else_1:
							main_circ.id(qreg_1[0])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.rx(0.489000, qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.u(param_0,param_2,0.377000, qreg_1[0])
			with else_1:
				main_circ.u(0,0,-0.924000, qreg_2[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,0,param_1, qreg_0[0])
					main_circ.u(param_2,0,-0.897000, qreg_1[0])
					main_circ.u(param_0,param_1,param_2, qreg_2[0])
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.u(pi/2,0.424000,0.903000, qreg_2[1])
					main_circ.barrier(qreg_1[0])
		with else_2:
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rx(0.874000, qreg_2[1])
			with else_1:
				main_circ.u(param_0,param_0,param_2, qreg_1[0])
				main_circ.u(param_1,-0.852000,param_0, qreg_2[0])
				main_circ.u(0,param_1,0.915000, qreg_2[1])
				main_circ.u(0,param_1,param_0, qreg_0[0])
main_circ.u(pi/2,param_1,-0.310000, qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.u(param_1,0.853000,0.177000, qreg_2[0])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.rx(-0.272000, qreg_2[0])
						main_circ.rx(param_1, qreg_1[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.id(qreg_2[0])
		with else_3:
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.id(qreg_2[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_2[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_2[0])
				with case_2(1):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.id(qreg_2[0])
			main_circ.id(qreg_2[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[0])
							with case_1(1):
								main_circ.barrier(qreg_2[1])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(qreg_0[0])
						main_circ.id(qreg_2[0])
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[0])
							with case_1(1):
								main_circ.id(qreg_1[0])
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_2[1])
			with case_3(1):
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(qreg_1[0])
				with else_2:
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_1[0])
							with case_1(1):
								main_circ.id(qreg_2[1])
						main_circ.id(qreg_2[1])
					with case_2(1):
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_2[0])
				with else_2:
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.id(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_1[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[1])
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[1])
							with case_1(1):
								main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_2[0])
						with else_1:
							main_circ.id(qreg_2[0])
						main_circ.barrier(qreg_2[0])
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[0])
						with else_1:
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_1[0])
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_1[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_2[1])
				with else_2:
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.id(qreg_2[1])
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_1[0])
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.id(qreg_2[0])
				with case_2(1):
					main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_2[1])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.id(qreg_1[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_1[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.id(qreg_2[1])
				with case_2(1):
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.id(qreg_2[1])
			main_circ.barrier(qreg_2[0])
		with else_3:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.id(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.id(qreg_1[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.barrier(qreg_2[1])
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.id(qreg_0[0])
		with else_3:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.id(qreg_2[1])
			main_circ.id(qreg_1[0])
		main_circ.id(qreg_2[1])
	with case_4(1):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_2[1])
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_2[1])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[1])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.barrier(qreg_1[0])
			with else_2:
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_1[0])
			main_circ.barrier(qreg_2[0])
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.id(qreg_2[1])
				with case_2(1):
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.id(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.barrier(qreg_2[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_2[0])
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.id(qreg_0[0])
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.barrier(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_2[1])
				main_circ.id(qreg_2[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.id(qreg_2[1])
			with case_3(1):
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_2[0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_2[1])
				main_circ.id(qreg_2[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.barrier(qreg_1[0])
			with else_2:
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.id(qreg_2[0])
			with else_2:
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_2[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_0[0])
			main_circ.barrier(qreg_2[0])
		with else_3:
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.id(qreg_2[1])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_2[0])
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.id(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.id(qreg_2[1])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.id(qreg_2[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.id(qreg_1[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_1[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.id(qreg_1[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.id(qreg_2[1])
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.id(qreg_2[1])
				with else_2:
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.id(qreg_2[0])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[1])
							with case_1(1):
								main_circ.id(qreg_1[0])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[0])
							with case_1(1):
								main_circ.id(qreg_2[1])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[1])
							with case_1(1):
								main_circ.barrier(qreg_1[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(qreg_1[0])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[1])
						with else_1:
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_1[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[0])
							with case_1(1):
								main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_1[0])
							with case_1(1):
								main_circ.id(qreg_1[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[1])
							with case_1(1):
								main_circ.barrier(qreg_1[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_2[1])
						main_circ.id(qreg_2[1])
					with case_2(1):
						main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.id(qreg_1[0])
			with case_3(1):
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_1[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_2[0])
				with else_2:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[0])
							with case_1(1):
								main_circ.id(qreg_2[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_2[1])
						main_circ.barrier(qreg_0[0])
					with case_2(1):
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_1[0])
							with case_1(1):
								main_circ.id(qreg_1[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[1])
							with case_1(1):
								main_circ.id(qreg_0[0])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[0])
							with case_1(1):
								main_circ.barrier(qreg_2[1])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(qreg_1[0])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_2[0])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.id(qreg_1[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[1])
							with case_1(1):
								main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[0])
							with case_1(1):
								main_circ.id(qreg_1[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_1[0])
						with else_1:
							main_circ.barrier(qreg_2[1])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_1[0])
						main_circ.id(qreg_2[1])
				main_circ.id(qreg_2[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.id(qreg_1[0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.id(qreg_1[0])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_1[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.barrier(qreg_2[1])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_2[1])
						with else_1:
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_2[0])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_2[1])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[0])
							with case_1(1):
								main_circ.barrier(qreg_1[0])
						main_circ.id(qreg_2[0])
					with case_2(1):
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_1[0])
							with case_1(1):
								main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_2[0])
						main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_1[0])
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[0])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_1[0])
						with else_1:
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_2[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[1])
						with else_1:
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(qreg_2[1])
							with case_1(1):
								main_circ.id(qreg_2[1])
						main_circ.barrier(qreg_2[1])
					with case_2(1):
						main_circ.id(qreg_1[0])
				main_circ.id(qreg_2[1])
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_1[0])
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(qreg_1[0])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[0])
							with case_1(1):
								main_circ.id(qreg_0[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.id(qreg_1[0])
					with case_2(1):
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.id(qreg_1[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_1[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_2[0])
						main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.barrier(qreg_2[1])
					with case_2(1):
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[1])
						with else_1:
							main_circ.barrier(qreg_2[1])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_2[1])
						with else_1:
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_2[1], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.barrier(qreg_2[1])
						main_circ.measure(qreg_2[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_2[1])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[1])
						with else_1:
							main_circ.barrier(qreg_1[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_1[0])
						with else_1:
							main_circ.barrier(qreg_1[0])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_2[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_2[0])
							with case_1(1):
								main_circ.id(qreg_0[0])
						main_circ.measure(qreg_1[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.id(qreg_2[1])
						with else_1:
							main_circ.id(qreg_2[0])
						main_circ.measure(qreg_1[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_1[0])
							with case_1(1):
								main_circ.barrier(qreg_2[1])
						main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_2[1])
			with case_3(1):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[1])
					main_circ.id(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.id(qreg_1[0])
				main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.id(qreg_0[0])
			with case_3(1):
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_2[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_1[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_1[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.barrier(qreg_1[0])
			main_circ.id(qreg_2[1])
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.id(qreg_2[0])
		with else_3:
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.barrier(qreg_2[0])
			with case_3(1):
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.barrier(qreg_2[0])
				with else_2:
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[1])
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_2[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_2[1])
					main_circ.barrier(qreg_1[0])
				main_circ.id(qreg_2[0])
		main_circ.barrier(qreg_2[1])
bindings = {param_0: -0.210000, param_1: -0.880000, param_2: 0.056000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "886", "Optimize1qGatesSimpleCommutation")
