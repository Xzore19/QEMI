from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(param_0,-0.146000,param_0, qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(0)
				with else_1:
					main_circ.u(pi/2,param_0,param_0, qreg_0[0])
					main_circ.u(0,0,0.759000, qreg_0[0])
					main_circ.u(param_0,param_0,param_0, qreg_0[0])
	with case_4(1):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.u(pi/2,param_0,-0.267000, qreg_0[1])
					main_circ.u(param_0,0.554000,-0.644000, qreg_0[2])
					main_circ.h(qreg_0[2])
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.rz(-0.500000, qreg_3[0])
						main_circ.h(qreg_3[0])
						main_circ.u(param_0,param_0,0.263000, qreg_3[0])
					with else_1:
						main_circ.h(qreg_0[1])
						main_circ.u(0,0,0.994000, qreg_0[0])
						main_circ.u(pi/2,param_0,-0.206000, qreg_0[2])
						main_circ.u(0,0,-0.249000, qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(pi/2,param_0,0.569000, qreg_0[2])
							main_circ.h(qreg_0[2])
							main_circ.u(pi/2,-0.174000,param_0, qreg_3[0])
							main_circ.u(param_0,0,-0.284000, qreg_0[2])
						with case_1(1):
							main_circ.rz(0.065000, qreg_3[0])
							main_circ.h(qreg_0[2])
							main_circ.u(0,param_0,-0.571000, qreg_0[1])
							main_circ.u(0,param_0,param_0, qreg_3[0])
		with else_3:
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(param_0,0.566000,param_0, qreg_0[2])
					main_circ.u(param_0,0,param_0, qreg_3[0])
				with else_1:
					main_circ.u(param_0,0.394000,0.281000, qreg_0[2])
					main_circ.u(param_0,param_0,param_0, qreg_3[0])
					main_circ.rz(0.999000, qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.switch(creg_1[0]) as case_1:
							with case_1(0):
								main_circ.u(param_0,param_0,-0.736000, qreg_3[0])
								main_circ.u(0,0,param_0, qreg_0[1])
								main_circ.h(qreg_0[0])
								main_circ.u(pi/2,0.512000,-0.225000, qreg_3[0])
							with case_1(1):
								main_circ.rz(0.125000, qreg_0[0])
								main_circ.rz(0.323000, qreg_3[0])
								main_circ.h(qreg_0[2])
								main_circ.rz(0.692000, qreg_3[0])
					with case_2(1):
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.rz(param_0, qreg_3[0])
							main_circ.h(qreg_0[1])
							main_circ.rz(param_0, 0)
						with else_1:
							main_circ.rz(param_0, 0)
			with case_3(1):
				main_circ.measure(qreg_3[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.rz(param_0, qreg_0[1])
							main_circ.u(0,param_0,-0.845000, qreg_0[2])
							main_circ.rz(-0.428000, 0)
							main_circ.h(qreg_0[0])
						with case_1(1):
							main_circ.u(param_0,param_0,param_0, 0)
							main_circ.u(0,param_0,-0.550000, qreg_3[0])
							main_circ.h(qreg_3[0])
							main_circ.u(param_0,-0.151000,param_0, qreg_0[1])
	with case_4(1):
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.barrier(qreg_0[2])
			with case_3(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(0)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.id(qreg_0[2])
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.barrier(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.barrier(qreg_0[1])
				with else_2:
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(qreg_3[0])
						main_circ.measure(qreg_0[1], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.barrier(0)
						with else_1:
							main_circ.barrier(qreg_0[2])
						main_circ.measure(0, creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.barrier(0)
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[0])
						main_circ.measure(qreg_0[2], creg_1[0])
						with main_circ.if_test((creg_1[0],0)) as else_1:
							main_circ.barrier(qreg_0[0])
						with else_1:
							main_circ.barrier(qreg_0[2])
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_3[0])
						with else_1:
							main_circ.id(qreg_0[2])
						main_circ.barrier(qreg_0[2])
					with case_2(1):
						main_circ.measure(qreg_0[0], creg_1[0])
						with main_circ.if_test((creg_1[0],0)):
							main_circ.id(0)
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.id(qreg_0[2])
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_3:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(qreg_3[0])
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.id(qreg_0[2])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_3[0])
					main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_3[0])
		with else_3:
			main_circ.barrier(qreg_0[0])
		main_circ.barrier(qreg_0[2])
bindings = {param_0: -0.942000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "308", "InverseCancellation")
