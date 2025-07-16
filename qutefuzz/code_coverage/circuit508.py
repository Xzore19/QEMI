from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.u(param_1,param_3,-0.862000, qreg_1[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_1[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.u(param_1,-0.313000,param_2, qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.s(qreg_0[0])
					with else_1:
						main_circ.s(qreg_0[0])
						main_circ.y(qreg_1[0])
						main_circ.y(qreg_1[1])
				with else_2:
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.y(qreg_0[0])
							main_circ.u(0,param_2,param_3, qreg_3[0])
							main_circ.u(0,0,param_0, qreg_0[0])
							main_circ.u(param_2,0,param_0, qreg_1[0])
						with case_1(1):
							main_circ.u(param_1,0,param_0, qreg_3[0])
							main_circ.u(pi/2,0.664000,-0.077000, qreg_3[0])
							main_circ.u(pi/2,param_2,0.632000, qreg_3[0])
							main_circ.u(param_3,0,-0.222000, qreg_1[1])
			with case_3(1):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(pi/2,0.991000,param_2, qreg_1[1])
							main_circ.u(param_3,0,0.132000, qreg_3[0])
							main_circ.u(param_2,0,param_2, qreg_0[0])
							main_circ.u(pi/2,-0.170000,-0.516000, qreg_1[0])
						with case_1(1):
							main_circ.u(param_0,param_0,-0.430000, qreg_0[0])
							main_circ.y(qreg_3[0])
							main_circ.u(pi/2,0.227000,param_3, qreg_3[0])
							main_circ.u(param_2,param_2,0.184000, qreg_3[0])
	with case_4(1):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.s(qreg_0[0])
					main_circ.s(qreg_1[1])
					main_circ.u(pi/2,param_0,param_2, qreg_1[1])
				with else_1:
					main_circ.u(param_2,-0.852000,-0.722000, qreg_0[0])
					main_circ.y(qreg_1[0])
					main_circ.s(qreg_0[0])
			with else_2:
				main_circ.y(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.s(qreg_0[0])
				with else_1:
					main_circ.y(qreg_1[1])
					main_circ.u(param_1,param_2,0.534000, qreg_1[1])
					main_circ.u(param_3,0.719000,param_2, qreg_1[1])
		with else_3:
			main_circ.u(param_3,param_0,-0.227000, qreg_0[0])
			main_circ.s(qreg_1[0])
main_circ.u(param_2,param_2,param_2, qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(param_0,param_1,param_3, qreg_3[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.u(param_0,0,-0.619000, qreg_0[0])
					main_circ.u(pi/2,0.652000,param_0, qreg_1[0])
					main_circ.s(qreg_1[0])
					main_circ.s(qreg_1[0])
				with else_1:
					main_circ.y(qreg_1[0])
					main_circ.y(qreg_1[1])
					main_circ.u(param_0,-0.973000,param_0, qreg_3[0])
					main_circ.s(qreg_1[1])
					main_circ.u(0,0,-0.609000, qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_1[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.y(qreg_1[1])
					main_circ.s(qreg_3[0])
				main_circ.u(param_2,-0.960000,param_3, qreg_3[0])
				main_circ.measure(qreg_1[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(0,param_1,param_1, qreg_1[1])
						main_circ.u(pi/2,0.414000,param_1, qreg_3[0])
						main_circ.u(param_2,param_0,param_3, qreg_1[1])
						main_circ.u(pi/2,param_0,param_1, qreg_0[0])
					with case_1(1):
						main_circ.y(qreg_0[0])
						main_circ.u(0,param_0,param_3, qreg_1[1])
						main_circ.u(param_0,param_0,0.342000, qreg_1[0])
						main_circ.y(qreg_0[0])
bindings = {param_0: 0.866000, param_1: -0.329000, param_2: -0.015000, param_3: 0.347000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "508")
