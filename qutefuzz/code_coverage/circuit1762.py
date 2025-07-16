from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.h(qreg_0[0])
			with else_1:
				main_circ.h(qreg_0[1])
				main_circ.cy(1,qreg_0[0])
				main_circ.cy(qreg_0[0],1)
		with else_2:
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.s(qreg_0[2])
				main_circ.h(qreg_0[1])
				main_circ.s(qreg_0[3])
				main_circ.s(qreg_0[3])
				main_circ.cy(qreg_0[0],qreg_0[2])
	with else_3:
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.u(pi/2,param_1,0.360000, qreg_0[0])
					main_circ.s(qreg_0[0])
					main_circ.cy(qreg_0[2],1)
					main_circ.cy(0,qreg_0[3])
				with case_1(1):
					main_circ.s(qreg_0[3])
					main_circ.s(qreg_0[1])
					main_circ.u(pi/2,-0.701000,0.219000, 1)
					main_circ.u(pi/2,param_2,param_2, qreg_0[1])
main_circ.cy(1,qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.h(1)
						main_circ.cy(qreg_0[3],qreg_0[1])
						main_circ.s(qreg_0[0])
						main_circ.u(pi/2,param_1,param_1, 0)
					with case_1(1):
						main_circ.h(0)
						main_circ.u(pi/2,param_0,-0.293000, 1)
						main_circ.u(param_2,0.240000,param_2, qreg_0[1])
						main_circ.cy(1,qreg_0[3])
			with else_2:
				main_circ.u(param_2,0.196000,param_2, 0)
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(qreg_0[1])
						main_circ.h(qreg_0[1])
						main_circ.u(pi/2,param_0,param_0, qreg_0[1])
						main_circ.cy(qreg_0[1],qreg_0[2])
					with case_1(1):
						main_circ.h(0)
						main_circ.cy(0,qreg_0[1])
						main_circ.u(pi/2,param_1,-0.707000, 0)
						main_circ.h(0)
		with case_3(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.cy(0,qreg_0[1])
					main_circ.s(qreg_0[3])
				with else_1:
					main_circ.cy(1,qreg_0[3])
					main_circ.cy(qreg_0[2],0)
					main_circ.cy(0,1)
					main_circ.cy(1,qreg_0[3])
main_circ.u(pi/2,param_1,0.223000, 0)
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(0)
					main_circ.cy(0,qreg_0[3])
					main_circ.u(pi/2,param_2,-0.035000, 1)
				with else_1:
					main_circ.cy(qreg_0[3],qreg_0[2])
					main_circ.h(qreg_0[3])
					main_circ.cy(1,0)
					main_circ.s(qreg_0[2])
	with case_4(1):
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.h(qreg_0[2])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.s(0)
						main_circ.cy(qreg_0[3],0)
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(0)
				with else_2:
					main_circ.measure(1, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(1)
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(0)
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(1)
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[2])
					with else_1:
						main_circ.id(0)
					main_circ.id(qreg_0[2])
				main_circ.id(0)
			with case_3(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(1)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.id(0)
				with else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(1)
					with else_1:
						main_circ.barrier(qreg_0[3])
					main_circ.id(1)
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(1)
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[2])
							with case_1(1):
								main_circ.barrier(0)
						main_circ.measure(qreg_0[3], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[2])
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[3], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[2])
						with else_1:
							main_circ.barrier(qreg_0[2])
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[0])
							with case_1(1):
								main_circ.barrier(qreg_0[0])
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(1)
						main_circ.measure(0, creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[2])
							with case_1(1):
								main_circ.id(qreg_0[3])
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(qreg_0[1])
						with else_1:
							main_circ.id(qreg_0[3])
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(0)
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(0)
						main_circ.id(qreg_0[3])
					with case_2(1):
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(0)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(1)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(1)
						with else_1:
							main_circ.id(1)
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[2])
							with case_1(1):
								main_circ.id(qreg_0[1])
						main_circ.measure(qreg_0[3], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[2])
							with case_1(1):
								main_circ.barrier(1)
						main_circ.measure(1, creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(qreg_0[3])
						main_circ.measure(1, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.id(qreg_0[0])
							with case_1(1):
								main_circ.id(0)
						main_circ.measure(qreg_0[3], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.barrier(qreg_0[1])
							with case_1(1):
								main_circ.barrier(qreg_0[0])
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_0[3])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.id(1)
				main_circ.id(qreg_0[0])
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[3])
				with else_1:
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[3])
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[3])
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(0)
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[2])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(0, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.barrier(qreg_0[2])
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.barrier(qreg_0[2])
			with else_2:
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(0)
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(1)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[2])
				main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[3])
					main_circ.barrier(1)
				with else_2:
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(1)
					main_circ.id(qreg_0[3])
				main_circ.id(qreg_0[1])
			with case_3(1):
				main_circ.id(0)
		main_circ.id(qreg_0[3])
bindings = {param_0: 0.883000, param_1: 0.238000, param_2: 0.074000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1762", "HoareOptimizer")
