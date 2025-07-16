from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.cy(1,2)
main_circ.cy(1,qreg_0[0])
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(1,qreg_0[0])
					main_circ.h(1)
					main_circ.s(3)
					main_circ.s(1)
				with case_1(1):
					main_circ.u(0,param_1,param_0, 2)
					main_circ.u(param_0,param_0,param_0, qreg_0[0])
					main_circ.u(0,param_1,param_1, 3)
					main_circ.s(0)
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(qreg_0[0],3)
				main_circ.h(3)
			with else_1:
				main_circ.cy(0,2)
				main_circ.s(2)
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.s(qreg_0[0])
				main_circ.cy(0,1)
				main_circ.u(param_1,param_1,param_0, 0)
				main_circ.u(param_1,param_1,-0.837000, 1)
				main_circ.cy(1,2)
			with else_1:
				main_circ.u(0,0,0.577000, 1)
				main_circ.h(qreg_0[0])
				main_circ.cy(3,1)
				main_circ.s(1)
				main_circ.u(0,0,param_1, 1)
		with else_2:
			main_circ.cy(qreg_0[0],0)
			main_circ.u(0,param_0,param_0, 0)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.s(2)
		main_circ.cy(1,3)
		main_circ.cy(1,3)
		main_circ.cy(0,2)
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_1,0,-0.012000, 1)
			main_circ.cy(qreg_0[0],1)
			main_circ.cy(2,0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(param_0,param_1,param_0, 1)
				main_circ.cy(qreg_0[0],2)
				main_circ.cy(0,1)
				main_circ.u(param_1,0,param_0, 0)
			with else_1:
				main_circ.h(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.s(2)
					main_circ.cy(2,1)
					main_circ.s(2)
					main_circ.cy(qreg_0[0],2)
				with case_1(1):
					main_circ.cy(3,1)
					main_circ.h(1)
					main_circ.s(qreg_0[0])
					main_circ.cy(qreg_0[0],2)
		with case_2(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.h(qreg_0[0])
				main_circ.cy(3,2)
				main_circ.u(param_1,param_0,param_1, 1)
				main_circ.barrier(0)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(3)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(3)
			main_circ.barrier(1)
bindings = {param_0: -0.658000, param_1: 0.612000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1313")
