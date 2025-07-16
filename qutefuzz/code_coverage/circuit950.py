from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(pi/2,param_0,param_1, qreg_0[1])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cy(qreg_0[2],qreg_0[1])
						main_circ.u(param_1,-0.521000,0.517000, qreg_0[0])
						main_circ.u(param_1,param_0,param_0, qreg_0[2])
						main_circ.y(qreg_0[0])
					with case_1(1):
						main_circ.ry(-0.727000, qreg_0[1])
						main_circ.u(pi/2,-0.356000,0.396000, qreg_0[2])
						main_circ.y(qreg_0[1])
						main_circ.cy(qreg_3[0],qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.ry(param_1, qreg_0[2])
					main_circ.y(qreg_0[2])
					main_circ.ry(0.196000, qreg_0[2])
				main_circ.y(qreg_0[2])
with else_4:
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.y(qreg_3[0])
						main_circ.y(qreg_0[0])
						main_circ.ry(param_1, qreg_3[0])
						main_circ.cy(qreg_3[0],qreg_0[1])
					with case_1(1):
						main_circ.y(qreg_3[0])
						main_circ.cy(qreg_0[0],qreg_0[1])
						main_circ.y(qreg_3[0])
						main_circ.y(qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.ry(-0.823000, qreg_0[0])
					main_circ.ry(0.951000, qreg_3[0])
					main_circ.ry(-0.078000, qreg_3[0])
				with else_1:
					main_circ.y(qreg_3[0])
	with else_3:
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.ry(0.819000, qreg_0[0])
			with else_1:
				main_circ.ry(param_1, qreg_0[0])
				main_circ.u(param_1,-0.457000,param_1, qreg_0[2])
				main_circ.ry(-0.408000, qreg_0[1])
				main_circ.y(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.ry(param_1, qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.ry(0.716000, qreg_0[2])
						main_circ.cy(qreg_0[2],qreg_3[0])
					with else_1:
						main_circ.cy(qreg_3[0],qreg_0[0])
						main_circ.y(qreg_0[2])
			with case_3(1):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.ry(-0.595000, qreg_0[0])
					main_circ.y(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.ry(-0.553000, qreg_3[0])
						main_circ.ry(-0.038000, qreg_0[2])
						main_circ.cy(qreg_0[1],qreg_3[0])
					with else_1:
						main_circ.cy(qreg_3[0],qreg_0[0])
				with else_2:
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.cy(qreg_0[0],qreg_3[0])
							main_circ.cy(qreg_0[2],qreg_0[1])
							main_circ.cy(qreg_3[0],qreg_0[1])
							main_circ.cy(qreg_3[0],qreg_0[1])
						with case_1(1):
							main_circ.cy(qreg_0[1],qreg_0[0])
							main_circ.cy(qreg_3[0],qreg_0[2])
							main_circ.cy(qreg_0[0],qreg_0[2])
							main_circ.cy(qreg_0[2],qreg_0[0])
	with case_4(1):
		main_circ.cy(qreg_0[2],qreg_3[0])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.y(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(pi/2,param_0,param_0, qreg_0[1])
					main_circ.y(qreg_0[2])
					main_circ.ry(0.864000, qreg_0[1])
		with else_3:
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cy(qreg_0[1],qreg_3[0])
				with else_1:
					main_circ.ry(param_1, qreg_3[0])
					main_circ.ry(param_0, qreg_0[0])
					main_circ.id(qreg_0[0])
				main_circ.id(qreg_0[0])
bindings = {param_0: -0.855000, param_1: 0.788000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "950", "Optimize1qGates")
