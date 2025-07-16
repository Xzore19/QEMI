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
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.s(qreg_0[2])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.s(qreg_0[3])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.h(0)
						main_circ.h(qreg_0[2])
						main_circ.u(param_0,param_2,param_1, qreg_0[1])
					with else_1:
						main_circ.u(param_0,param_1,0.862000, qreg_0[3])
						main_circ.s(qreg_0[1])
						main_circ.h(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(pi/2,param_2,0.365000, 1)
							main_circ.s(qreg_0[0])
							main_circ.s(1)
							main_circ.h(qreg_0[1])
						with case_1(1):
							main_circ.x(qreg_0[2])
							main_circ.s(1)
							main_circ.s(1)
							main_circ.x(qreg_0[0])
	with case_4(1):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.u(param_1,0.332000,-0.233000, 0)
		with else_3:
			main_circ.s(qreg_0[3])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(param_1,param_2,param_0, qreg_0[0])
						main_circ.h(qreg_0[0])
						main_circ.x(qreg_0[1])
						main_circ.u(pi/2,param_2,param_0, 0)
					with case_1(1):
						main_circ.u(param_0,param_0,0.710000, qreg_0[1])
						main_circ.x(qreg_0[1])
						main_circ.x(qreg_0[2])
						main_circ.h(qreg_0[0])
main_circ.s(qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.u(pi/2,-0.984000,param_0, qreg_0[0])
		with else_3:
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.s(qreg_0[1])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.x(qreg_0[2])
					main_circ.s(qreg_0[0])
					main_circ.s(0)
					main_circ.u(pi/2,-0.252000,param_0, qreg_0[0])
				with else_1:
					main_circ.h(qreg_0[2])
	with case_4(1):
		main_circ.x(qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[3], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.u(param_0,param_0,param_2, qreg_0[1])
						main_circ.h(1)
					with else_1:
						main_circ.u(param_2,-0.118000,-0.046000, 0)
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.u(param_2,param_2,param_1, qreg_0[2])
							main_circ.s(qreg_0[2])
							main_circ.x(0)
							main_circ.u(pi/2,-0.265000,param_2, qreg_0[1])
						with case_1(1):
							main_circ.s(qreg_0[0])
							main_circ.x(qreg_0[2])
							main_circ.u(param_0,param_0,0.744000, 0)
							main_circ.barrier(1)
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(qreg_0[3])
					main_circ.id(qreg_0[3])
bindings = {param_0: -0.850000, param_1: 0.866000, param_2: 0.648000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "239")
