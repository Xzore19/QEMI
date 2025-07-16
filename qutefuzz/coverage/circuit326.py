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
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.y(qreg_0[0])
				with else_1:
					main_circ.y(2)
					main_circ.y(1)
					main_circ.cy(qreg_0[0],1)
				main_circ.h(2)
			with else_2:
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.ry(param_0, 3)
						main_circ.ry(0.708000, 3)
						main_circ.ry(0.363000, 0)
						main_circ.y(3)
					with case_1(1):
						main_circ.y(2)
						main_circ.cy(3,1)
						main_circ.y(1)
						main_circ.cy(0,1)
	with case_4(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.cy(0,2)
						main_circ.y(2)
						main_circ.cy(2,0)
						main_circ.h(0)
						main_circ.ry(-0.687000, 2)
					with else_1:
						main_circ.y(3)
				with case_2(1):
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.y(1)
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.cy(qreg_0[0],3)
						main_circ.cy(0,3)
						main_circ.h(1)
						main_circ.ry(0.434000, 0)
					with else_1:
						main_circ.y(qreg_0[0])
						main_circ.h(qreg_0[0])
						main_circ.cy(3,0)
main_circ.ry(param_0, 2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(3,2)
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.y(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.h(1)
						main_circ.cy(qreg_0[0],2)
					main_circ.measure(2, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.y(0)
					with else_1:
						main_circ.y(qreg_0[0])
						main_circ.cy(1,qreg_0[0])
						main_circ.cy(0,1)
				with case_2(1):
					main_circ.measure(2, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.cy(2,3)
						main_circ.cy(3,1)
						main_circ.cy(qreg_0[0],3)
					with else_1:
						main_circ.y(3)
						main_circ.cy(2,3)
		with case_3(1):
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.h(qreg_0[0])
				main_circ.h(3)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.cy(3,1)
					main_circ.cy(2,0)
					main_circ.h(qreg_0[0])
					main_circ.h(0)
					main_circ.h(2)
				with else_1:
					main_circ.h(2)
					main_circ.barrier(1)
			with else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(2)
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(0)
				main_circ.barrier(0)
bindings = {param_0: -0.387000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "326")
