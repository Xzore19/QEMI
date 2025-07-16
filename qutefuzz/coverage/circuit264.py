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
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.x(qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rx(param_2, qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cy(0,qreg_0[1])
					main_circ.u(pi/2,0.959000,param_0, qreg_0[1])
					main_circ.cy(qreg_0[2],qreg_3[0])
				with else_1:
					main_circ.x(0)
					main_circ.x(qreg_0[1])
	with case_4(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.cy(qreg_0[2],0)
							main_circ.rx(-0.385000, 0)
							main_circ.rx(param_1, qreg_0[0])
							main_circ.u(param_1,-0.636000,param_0, qreg_0[1])
						with case_1(1):
							main_circ.rx(0.738000, qreg_0[1])
							main_circ.x(qreg_0[1])
							main_circ.u(param_3,-0.541000,-0.772000, 0)
							main_circ.x(qreg_0[1])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.x(qreg_3[0])
							main_circ.rx(param_0, qreg_3[0])
							main_circ.x(qreg_0[1])
							main_circ.u(pi/2,-0.620000,param_2, 0)
						with case_1(1):
							main_circ.u(param_1,-0.698000,param_1, 0)
							main_circ.cy(qreg_3[0],0)
							main_circ.cy(qreg_3[0],0)
							main_circ.u(pi/2,-0.950000,param_0, qreg_3[0])
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.rx(param_1, qreg_3[0])
							main_circ.x(0)
							main_circ.rx(0.926000, 0)
							main_circ.cy(qreg_0[1],qreg_0[0])
						with else_1:
							main_circ.x(qreg_0[1])
					with case_2(1):
						main_circ.measure(qreg_0[2], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.x(qreg_0[0])
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.u(param_3,-0.645000,0.731000, qreg_0[2])
							main_circ.rx(-0.362000, qreg_0[1])
							main_circ.u(param_0,0.521000,param_0, 0)
						with else_1:
							main_circ.rx(param_3, qreg_0[0])
							main_circ.cy(qreg_0[0],0)
							main_circ.x(qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_0, qreg_3[0])
			main_circ.u(param_3,param_1,param_2, qreg_0[0])
			main_circ.cy(0,qreg_0[1])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[2],qreg_3[0])
					main_circ.cy(0,qreg_0[2])
					main_circ.cy(qreg_0[1],qreg_3[0])
					main_circ.cy(0,qreg_0[2])
				with case_1(1):
					main_circ.cy(0,qreg_0[0])
					main_circ.cy(0,qreg_0[2])
					main_circ.cy(qreg_0[0],qreg_0[2])
					main_circ.x(qreg_0[2])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.cy(qreg_0[0],qreg_3[0])
				main_circ.u(param_1,-0.261000,param_0, 0)
				main_circ.cy(qreg_0[0],qreg_3[0])
				main_circ.cy(qreg_3[0],qreg_0[2])
				main_circ.u(pi/2,-0.933000,-0.755000, qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.x(qreg_0[1])
				main_circ.id(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_3[0])
		main_circ.id(qreg_0[2])
	main_circ.barrier(qreg_3[0])
bindings = {param_0: -0.083000, param_1: -0.814000, param_2: 0.658000, param_3: -0.437000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "264")
