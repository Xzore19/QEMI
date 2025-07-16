from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0.cy(qreg_0[0],qreg_3[0])
subcirc0.u(0,0,-0.136000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.689000, qreg_2[1])
subcirc1.u(0,0,-0.384000, qreg_0[0])
subcirc1.h(qreg_2[1])
subcirc1.h(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.553000, qreg_1[1])
subcirc2.u(0,0,-0.156000, qreg_1[0])
subcirc2.u(0,0,0.647000, qreg_1[0])
subcirc2.x(qreg_1[0])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(3)
	with else_1:
		main_circ.cy(1,2)
		main_circ.cy(2,3)
		main_circ.barrier(2)
	main_circ.append(subcirc0,[2,1,3,0])
with else_2:
	main_circ.h(1)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(2)
	with else_1:
		main_circ.h(1)
		main_circ.barrier(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(param_4,0,param_0, 1)
		main_circ.cy(3,1)
		main_circ.cy(3,2)
		main_circ.u(0,param_4,-0.725000, 0)
		main_circ.x(3)
with else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.append(subcirc0,[3,2,0,1])
		main_circ.barrier(3)
	with else_1:
		main_circ.u(0,0,param_0, 0)
		main_circ.h(0)
		main_circ.id(0)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc0,[2,1,0,3])
			main_circ.h(2)
	with case_2(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cy(0,3)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[0,1,2,3])
			with case_1(1):
				main_circ.barrier(3)
main_circ.x(1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cy(3,2)
				main_circ.h(3)
				main_circ.barrier(1)
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0,0,-0.595000, 3)
			main_circ.u(0,param_4,param_3, 0)
	with case_2(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(1,3)
				main_circ.u(0,0,param_4, 3)
				main_circ.barrier(1)
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(3)
		with else_1:
			main_circ.x(0)
			main_circ.barrier(1)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(2,1)
			main_circ.u(param_2,0,param_1, 2)
			main_circ.u(param_0,0,param_4, 0)
			main_circ.append(subcirc0,[2,3,0,1])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(3,1)
		main_circ.cy(1,2)
		main_circ.cy(1,3)
		main_circ.cy(2,0)
	with else_1:
		main_circ.x(0)
		main_circ.u(0,param_3,param_0, 2)
		main_circ.barrier(2)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc0,[1,0,2,3])
		with case_1(1):
			main_circ.barrier(2)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(2)
	with else_1:
		main_circ.h(2)
		main_circ.x(3)
main_circ.h(0)
main_circ.x(2)
main_circ.h(0)
bindings = {param_0: 0.617000, param_1: -0.281000, param_2: 0.522000, param_3: -0.477000, param_4: 0.936000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1739", "CXCancellation")
