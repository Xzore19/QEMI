from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_0[0])
subcirc0.y(qreg_1[1])
subcirc0.y(qreg_0[0])
subcirc0.h(qreg_1[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_0[2])
subcirc1.h(qreg_0[0])
subcirc1.u(0,0,0.980000, qreg_0[1])
subcirc1.u(0,0,-0.135000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.182000, qreg_3[0])
subcirc2.h(qreg_0[0])
subcirc2.u(0,0,-0.560000, qreg_2[0])
subcirc2.y(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0,0,0.409000, qreg_3[0])
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.y(qreg_2[0])
subcirc3.y(qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.h(1)
					main_circ.h(0)
					main_circ.y(1)
					main_circ.y(0)
					main_circ.y(3)
			with case_2(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.h(2)
						main_circ.id(1)
					with case_1(1):
						main_circ.h(2)
						main_circ.barrier(0)
				main_circ.u(param_1,0,0.344000, 1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.append(subcirc1,[0,2,1,3])
	with case_3(1):
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.append(subcirc1,[1,0,2,3])
			with case_2(1):
				main_circ.measure(2, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(param_3,param_0,-0.520000, 0)
					main_circ.u(param_0,0,-0.817000, 3)
					main_circ.id(2)
				with else_1:
					main_circ.u(param_0,0,0.715000, 2)
					main_circ.cy(3,1)
					main_circ.id(3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.cy(3,1)
		main_circ.id(2)
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.y(1)
				main_circ.barrier(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc3,[3,1,0,2])
				with case_1(1):
					main_circ.h(3)
					main_circ.append(subcirc1,[0,3,1,2])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0,0,-0.424000, 0)
				main_circ.barrier(3)
			with else_1:
				main_circ.barrier(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.append(subcirc3,[1,0,3,2])
	with case_3(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.append(subcirc1,[3,2,1,0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.cy(2,1)
					main_circ.cy(0,1)
					main_circ.cy(2,0)
					main_circ.cy(3,0)
				with case_1(1):
					main_circ.cy(3,2)
					main_circ.cy(1,0)
					main_circ.cy(0,1)
					main_circ.cy(3,1)
		with case_2(1):
			main_circ.cy(0,1)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(2,0)
					main_circ.cy(1,2)
					main_circ.cy(2,3)
					main_circ.h(2)
				with case_1(1):
					main_circ.id(2)
with else_3:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.h(3)
			main_circ.cy(2,3)
			main_circ.id(1)
		with else_1:
			main_circ.id(3)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(1)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(1)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(1)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.id(2)
		main_circ.barrier(1)
	with else_2:
		main_circ.barrier(1)
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.id(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.id(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(3)
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(2)
			main_circ.barrier(1)
		with case_2(1):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.id(2)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(0)
			main_circ.id(2)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(2)
		main_circ.id(3)
	with else_2:
		main_circ.barrier(3)
	main_circ.barrier(3)
bindings = {param_0: -0.476000, param_1: -0.785000, param_3: -0.015000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1067")
