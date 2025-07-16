from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cy(2,0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.u(0,0,0.673000, 1)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(param_0,0,0.334000, qreg_0[1])
							main_circ.cy(2,0)
							main_circ.ry(-0.527000, 1)
							main_circ.u(0,0,param_0, 3)
						with case_1(1):
							main_circ.cy(qreg_0[1],0)
							main_circ.u(0,param_1,0.371000, qreg_0[0])
							main_circ.u(param_0,-0.674000,param_1, 0)
							main_circ.u(0,param_1,param_0, 1)
				with case_2(1):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.ry(param_1, qreg_0[0])
						main_circ.u(pi/2,0.091000,param_2, 0)
						main_circ.u(pi/2,-0.972000,param_2, qreg_0[1])
					with else_1:
						main_circ.ry(param_1, 1)
						main_circ.cy(1,qreg_0[1])
		with else_3:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(pi/2,param_1,param_0, 2)
					main_circ.u(param_2,param_2,0.685000, 1)
					main_circ.ry(param_3, 1)
					main_circ.cy(0,1)
				with else_1:
					main_circ.u(pi/2,0.470000,-0.465000, qreg_0[1])
					main_circ.ry(param_3, 1)
					main_circ.u(0,param_3,0.077000, 1)
					main_circ.cy(2,3)
	with case_4(1):
		main_circ.ry(param_3, 3)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.u(0,0,param_1, qreg_0[0])
						main_circ.cy(2,0)
						main_circ.u(0,0,param_1, 0)
					with else_1:
						main_circ.ry(param_3, qreg_0[0])
						main_circ.u(pi/2,param_0,param_3, 1)
						main_circ.u(param_1,param_1,param_3, qreg_0[0])
						main_circ.ry(param_3, qreg_0[1])
				with case_2(1):
					main_circ.ry(-0.067000, qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.cy(3,qreg_0[0])
						main_circ.u(param_2,param_3,param_3, qreg_0[1])
						main_circ.u(0,param_2,param_1, 0)
					with else_1:
						main_circ.u(0,0,-0.410000, 3)
main_circ.u(pi/2,param_0,-0.086000, 2)
main_circ.cy(qreg_0[0],0)
main_circ.u(pi/2,-0.602000,param_0, 3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.ry(0.755000, 0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_3,0.404000,param_3, 1)
				main_circ.cy(3,0)
				main_circ.cy(qreg_0[0],0)
				main_circ.cy(qreg_0[1],qreg_0[0])
				main_circ.cy(1,0)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[0],1)
					main_circ.cy(1,qreg_0[0])
					main_circ.cy(qreg_0[1],0)
					main_circ.cy(qreg_0[1],2)
				with case_1(1):
					main_circ.u(param_1,0,0.174000, qreg_0[0])
					main_circ.ry(0.392000, 2)
					main_circ.ry(-0.271000, 3)
					main_circ.u(param_2,-0.412000,param_1, qreg_0[1])
with else_4:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.u(param_0,param_3,param_1, qreg_0[0])
		main_circ.u(param_3,param_1,0.419000, qreg_0[1])
	with else_3:
		main_circ.ry(0.005000, qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(0,1)
				main_circ.u(0,0,param_3, 0)
				main_circ.cy(3,qreg_0[0])
				main_circ.id(2)
			with else_1:
				main_circ.barrier(3)
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(3)
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(1)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(3)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.barrier(3)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.id(qreg_0[1])
bindings = {param_0: 0.013000, param_1: 0.101000, param_2: -0.646000, param_3: -0.189000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1479", "OptimizeCliffords")
