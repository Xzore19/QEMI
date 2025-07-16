from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
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

main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.ry(param_0, qreg_0[2])
			main_circ.h(qreg_0[2])
			main_circ.ry(-0.037000, qreg_0[0])
			main_circ.h(qreg_0[0])
			main_circ.ry(-0.646000, qreg_0[2])
		with else_1:
			main_circ.cy(qreg_0[2],qreg_0[3])
	with case_2(1):
		main_circ.cy(qreg_0[3],qreg_0[1])
		main_circ.ry(0.106000, qreg_0[1])
		main_circ.u(pi/2,0.510000,-0.056000, qreg_0[1])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.ry(-0.481000, qreg_0[0])
				main_circ.u(param_0,0.182000,-0.851000, qreg_0[0])
				main_circ.h(qreg_0[0])
				main_circ.h(qreg_0[0])
			with case_1(1):
				main_circ.cy(qreg_0[1],qreg_0[2])
				main_circ.h(qreg_0[1])
				main_circ.cy(qreg_0[0],qreg_0[3])
				main_circ.ry(-0.268000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cy(qreg_0[1],qreg_0[3])
		main_circ.ry(-0.792000, qreg_0[1])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.cy(qreg_0[1],qreg_0[3])
		main_circ.h(qreg_0[0])
		main_circ.h(qreg_0[3])
		main_circ.h(qreg_0[1])
		main_circ.cy(qreg_0[0],qreg_0[3])
	with else_1:
		main_circ.h(qreg_0[1])
		main_circ.ry(param_0, qreg_0[2])
with else_2:
	main_circ.u(pi/2,0.224000,param_0, qreg_0[2])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_0[2],qreg_0[1])
			main_circ.cy(qreg_0[2],qreg_0[3])
			main_circ.cy(qreg_0[0],qreg_0[1])
			main_circ.h(qreg_0[0])
		with case_1(1):
			main_circ.u(param_0,param_0,0.663000, qreg_0[1])
			main_circ.cy(qreg_0[1],qreg_0[3])
			main_circ.h(qreg_0[2])
			main_circ.cy(qreg_0[2],qreg_0[1])
main_circ.u(pi/2,param_0,-0.825000, qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_0[2],qreg_0[0])
			main_circ.h(qreg_0[0])
			main_circ.cy(qreg_0[2],qreg_0[1])
			main_circ.cy(qreg_0[0],qreg_0[2])
		with case_1(1):
			main_circ.cy(qreg_0[0],qreg_0[1])
			main_circ.u(pi/2,param_0,param_0, qreg_0[2])
			main_circ.h(qreg_0[0])
			main_circ.u(pi/2,0.819000,-0.757000, qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(pi/2,0.514000,0.456000, qreg_0[2])
		main_circ.h(qreg_0[1])
		main_circ.u(param_0,-0.916000,param_0, qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(qreg_0[1])
	with else_1:
		main_circ.h(qreg_0[0])
		main_circ.cy(qreg_0[3],qreg_0[0])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_0,0.968000,0.218000, qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(qreg_0[3],qreg_0[1])
	with else_1:
		main_circ.u(param_0,0.596000,param_0, qreg_0[0])
		main_circ.cy(qreg_0[2],qreg_0[0])
bindings = {param_0: -0.620000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "489")
