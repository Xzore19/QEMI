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
subcirc0.u(pi/2,-0.909000,-0.305000, qreg_0[1])
subcirc0.u(0,0,-0.907000, qreg_2[0])
subcirc0.u(pi/2,0.540000,-0.363000, qreg_2[0])
subcirc0.u(-0.256000,-0.689000,0.667000, qreg_3[0])

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

main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.u(param_3,0.238000,0.002000, qreg_0[2])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(0.882000,0.722000,param_2, 0)
					main_circ.u(param_4,param_1,param_1, 1)
					main_circ.u(param_4,-0.583000,param_3, qreg_0[2])
					main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[1],qreg_0[0]])
		with else_3:
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.u(param_0,param_1,-0.418000, 0)
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.u(param_2,param_2,-0.527000, qreg_0[3])
						main_circ.u(0.229000,0.148000,0.000000, qreg_0[3])
						main_circ.append(subcirc0,[qreg_0[0],0,1,qreg_0[3]])
					with case_1(1):
						main_circ.u(param_4,param_0,param_4, qreg_0[0])
						main_circ.append(subcirc0,[0,1,qreg_0[1],qreg_0[0]])
			with else_2:
				main_circ.u(param_2,0.010000,param_4, 0)
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.y(qreg_0[1])
				main_circ.u(0,0,param_4, qreg_0[2])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.u(0,param_2,param_0, qreg_0[3])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(param_4,param_2,param_3, qreg_0[1])
	with case_4(1):
		main_circ.u(pi/2,0.192000,param_3, 1)
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_0[3], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.u(0,0,param_4, qreg_0[2])
						main_circ.u(param_0,param_4,0.989000, qreg_0[2])
						main_circ.u(0.032000,-0.375000,param_2, qreg_0[2])
						main_circ.y(qreg_0[0])
						main_circ.u(param_0,param_3,param_2, 0)
					with else_1:
						main_circ.u(param_4,-0.018000,param_0, qreg_0[0])
						main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],1])
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.switch(creg_0[0]) as case_1:
							with case_1(0):
								main_circ.u(0.007000,param_2,0.758000, qreg_0[3])
								main_circ.u(param_0,param_4,0.139000, qreg_0[1])
								main_circ.y(0)
								main_circ.u(param_2,param_3,param_1, qreg_0[3])
							with case_1(1):
								main_circ.u(pi/2,0.171000,-0.486000, qreg_0[3])
								main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[3],qreg_0[2]])
					with case_2(1):
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.u(pi/2,-0.412000,0.493000, 1)
							main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],0,qreg_0[3]])
						with else_1:
							main_circ.u(0,param_2,param_2, 1)
							main_circ.id(qreg_0[3])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.u(0,0,0.799000, qreg_0[1])
					main_circ.y(qreg_0[0])
					main_circ.id(qreg_0[2])
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[2])
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[3])
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[2])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[3])
				with case_1(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.id(qreg_0[1])
		with else_2:
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.id(1)
			main_circ.barrier(0)
		with else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.barrier(1)
			main_circ.id(qreg_0[3])
		main_circ.barrier(0)
	main_circ.barrier(1)
with else_4:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.barrier(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.barrier(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.barrier(1)
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.id(qreg_0[2])
	with else_3:
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[2])
			main_circ.id(1)
		with else_2:
			main_circ.barrier(1)
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(1)
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[3])
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.barrier(1)
		main_circ.barrier(qreg_0[3])
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.barrier(0)
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[3])
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[3])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[3])
				with else_1:
					main_circ.id(0)
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(0)
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.barrier(1)
			main_circ.id(qreg_0[3])
	main_circ.id(0)
bindings = {param_0: -0.380000, param_1: -0.752000, param_2: -0.266000, param_3: 0.010000, param_4: 0.490000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1953", "NormalizeRXAngle")
