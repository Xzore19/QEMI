from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cy(qreg_1[2],1)
			main_circ.cy(qreg_1[0],0)
			main_circ.x(qreg_1[2])
		with else_1:
			main_circ.cz(qreg_1[1],qreg_0[0])
			main_circ.u(0,param_0,param_0, qreg_1[1])
			main_circ.x(qreg_1[2])
	with case_2(1):
		main_circ.u(0,0,param_0, qreg_1[2])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cy(qreg_1[1],0)
		with else_1:
			main_circ.cz(0,qreg_1[0])
			main_circ.cy(0,qreg_1[2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_1[1],qreg_1[0])
			main_circ.x(1)
			main_circ.x(qreg_1[0])
			main_circ.cz(qreg_1[0],qreg_1[2])
		with case_1(1):
			main_circ.cz(qreg_1[0],qreg_0[0])
			main_circ.cz(1,qreg_1[2])
			main_circ.x(0)
			main_circ.cz(qreg_1[1],qreg_1[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.x(qreg_1[2])
		main_circ.cz(qreg_1[0],qreg_1[1])
		main_circ.cz(1,qreg_0[0])
		main_circ.u(0,param_2,0.588000, 1)
	with else_1:
		main_circ.x(1)
		main_circ.u(param_1,0,0.998000, qreg_1[1])
		main_circ.cy(qreg_1[2],1)
		main_circ.cy(qreg_1[0],1)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cz(0,qreg_0[0])
			main_circ.u(param_0,0,-0.862000, qreg_1[0])
			main_circ.cy(1,0)
			main_circ.u(0,0,-0.880000, qreg_0[0])
		with case_1(1):
			main_circ.x(qreg_1[0])
			main_circ.x(qreg_0[0])
			main_circ.x(qreg_0[0])
			main_circ.x(qreg_1[1])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.x(qreg_1[0])
				main_circ.u(0,param_0,param_0, 1)
				main_circ.cy(qreg_1[0],qreg_1[1])
				main_circ.cz(qreg_1[2],qreg_1[0])
			with case_1(1):
				main_circ.u(param_1,param_2,param_0, qreg_1[2])
				main_circ.u(param_0,0,param_1, qreg_1[2])
				main_circ.u(param_0,param_0,0.210000, qreg_0[0])
				main_circ.x(1)
	with case_2(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(0,1)
				main_circ.cz(qreg_1[2],qreg_1[1])
				main_circ.u(param_2,param_2,param_2, qreg_1[0])
				main_circ.cy(0,qreg_0[0])
			with case_1(1):
				main_circ.barrier(qreg_1[1])
bindings = {param_0: 0.993000, param_1: 0.015000, param_2: 0.953000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "397")
