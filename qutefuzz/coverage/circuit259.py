from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.rz(0.738000, qreg_0[1])
subcirc0.rz(0.394000, qreg_0[3])
subcirc0.u(pi/2,0.359000,-0.358000, qreg_0[0])
subcirc0.rz(0.421000, qreg_0[3])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.166000, qreg_3[0])
subcirc1.h(qreg_3[0])
subcirc1.h(qreg_2[0])
subcirc1.rz(-0.883000, qreg_0[0])
subcirc1.u(pi/2,0.764000,-0.760000, qreg_2[0])
subcirc1.u(pi/2,0.657000,0.608000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cy(qreg_1[1],qreg_1[0])
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_3[0])
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_1[0])
		with case_1(1):
			main_circ.id(0)
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_1[1])
		with case_1(1):
			main_circ.u(pi/2,param_2,-0.273000, qreg_3[0])
			main_circ.h(qreg_3[0])
			main_circ.rz(0.848000, 0)
			main_circ.rz(0.798000, 0)
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.h(qreg_1[1])
	main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.h(qreg_0[0])
		main_circ.id(qreg_1[0])
	with else_1:
		main_circ.h(0)
		main_circ.rz(0.910000, qreg_1[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_0[0],qreg_3[0])
			main_circ.h(0)
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.u(param_1,-0.260000,param_1, qreg_3[0])
			main_circ.id(qreg_1[0])
with else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.barrier(qreg_3[0])
	with else_1:
		main_circ.id(qreg_0[0])
	main_circ.u(param_2,0.332000,param_0, qreg_0[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cy(qreg_1[1],qreg_3[0])
		main_circ.id(qreg_1[1])
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.barrier(qreg_3[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(pi/2,-0.411000,-0.367000, qreg_1[0])
			main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_1[1])
		with else_1:
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_3[0])
			with case_1(1):
				main_circ.id(qreg_1[1])
		main_circ.u(pi/2,-0.098000,param_1, qreg_1[1])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(qreg_1[1],qreg_3[0])
			main_circ.rz(0.212000, qreg_0[0])
			main_circ.barrier(qreg_1[0])
	with case_2(1):
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rz(param_1, qreg_1[0])
			main_circ.h(qreg_0[0])
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_3[0])
			with case_1(1):
				main_circ.id(qreg_1[1])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_1,param_1,param_0, qreg_1[0])
				main_circ.h(qreg_3[0])
				main_circ.cy(qreg_1[0],0)
				main_circ.u(param_1,-0.221000,param_0, 0)
			with case_1(1):
				main_circ.id(qreg_1[1])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.h(qreg_3[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_3[0])
			with case_1(1):
				main_circ.h(qreg_1[1])
				main_circ.u(param_2,param_0,param_1, qreg_1[1])
				main_circ.cy(qreg_1[1],qreg_1[0])
				main_circ.id(qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[1])
			with case_1(1):
				main_circ.cy(0,qreg_3[0])
				main_circ.u(pi/2,-0.548000,param_2, qreg_1[0])
				main_circ.h(qreg_3[0])
				main_circ.id(qreg_3[0])
main_circ.rz(param_1, 0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_1,param_0,-0.595000, qreg_1[1])
			main_circ.cy(qreg_1[1],qreg_0[0])
			main_circ.rz(-0.201000, qreg_1[1])
			main_circ.h(qreg_1[0])
		with case_1(1):
			main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(pi/2,param_1,-0.208000, 0)
		main_circ.h(qreg_1[0])
		main_circ.u(pi/2,-0.909000,0.319000, 0)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_2,param_0,-0.741000, 0)
			main_circ.id(qreg_1[0])
		with case_1(1):
			main_circ.rz(param_2, qreg_1[1])
			main_circ.cy(qreg_0[0],qreg_1[0])
			main_circ.cy(qreg_0[0],0)
			main_circ.cy(qreg_1[1],qreg_3[0])
with else_2:
	main_circ.cy(qreg_3[0],0)
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(qreg_1[1],qreg_3[0])
		main_circ.cy(qreg_1[1],qreg_1[0])
		main_circ.cy(qreg_1[1],qreg_0[0])
	with else_1:
		main_circ.cy(qreg_3[0],qreg_0[0])
		main_circ.cy(qreg_3[0],0)
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_1[0])
		with else_1:
			main_circ.u(param_0,0.187000,param_1, 0)
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(qreg_3[0])
			main_circ.id(qreg_0[0])
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[0])
			with case_1(1):
				main_circ.rz(param_2, qreg_1[1])
				main_circ.cy(qreg_1[0],qreg_1[1])
				main_circ.h(qreg_3[0])
				main_circ.id(qreg_3[0])
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(qreg_0[0],qreg_1[1])
			main_circ.barrier(qreg_3[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(qreg_0[0],0)
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(qreg_1[1])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.cy(qreg_0[0],0)
				main_circ.barrier(qreg_1[0])
		main_circ.barrier(qreg_1[1])
bindings = {param_0: -0.199000, param_1: 0.817000, param_2: 0.275000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "259", "RemoveDiagonalGatesBeforeMeasure")
