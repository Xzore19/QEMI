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
subcirc0.rz(0.624000, qreg_0[0])
subcirc0.u(0,0,-0.851000, qreg_0[1])
subcirc0.rz(-0.932000, qreg_0[1])
subcirc0.rz(-0.437000, qreg_0[2])
subcirc0.u(0,0,0.414000, qreg_0[1])
subcirc0.rz(0.375000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_0[3])
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.cx(qreg_0[2],qreg_0[3])
subcirc1.rz(0.328000, qreg_0[1])
subcirc1.cx(qreg_0[3],qreg_0[0])
subcirc1.u(0,0,-0.282000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(param_3,param_2,-0.957000, 0)
		main_circ.cx(qreg_0[0],qreg_3[0])
		main_circ.id(0)
with else_2:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(-0.811000, 0)
		main_circ.y(qreg_0[0])
		main_circ.y(qreg_0[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.y(0)
main_circ.cx(qreg_1[0],qreg_3[0])
main_circ.u(param_2,0,0.405000, 0)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.y(qreg_0[0])
		with else_1:
			main_circ.rz(param_2, 0)
			main_circ.y(qreg_0[0])
			main_circ.cx(0,qreg_3[0])
	with case_2(1):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_0[0],qreg_1[1])
				main_circ.cx(qreg_0[0],qreg_3[0])
				main_circ.id(qreg_3[0])
			with case_1(1):
				main_circ.y(qreg_1[0])
				main_circ.y(qreg_3[0])
				main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(qreg_3[0])
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_1[0])
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(0,param_0,param_0, qreg_3[0])
		main_circ.barrier(qreg_1[1])
	with else_1:
		main_circ.barrier(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(0,qreg_1[1])
			main_circ.u(0,param_1,-0.545000, qreg_1[0])
			main_circ.u(0,0,param_1, qreg_0[0])
			main_circ.u(param_2,0,param_4, qreg_1[1])
		with case_1(1):
			main_circ.cx(qreg_1[0],qreg_0[0])
			main_circ.barrier(qreg_1[0])
main_circ.y(0)
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.y(0)
		main_circ.u(0,0,param_1, qreg_1[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.rz(-0.878000, qreg_1[1])
				main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.rz(param_0, qreg_3[0])
				main_circ.id(qreg_3[0])
	with case_2(1):
		main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.y(0)
		main_circ.cx(qreg_1[1],qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_1[1])
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(param_4,param_0,-0.250000, 0)
		main_circ.u(0,param_3,param_4, qreg_3[0])
	with else_1:
		main_circ.barrier(qreg_0[0])
	main_circ.id(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cx(qreg_0[0],0)
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(param_2,0,-0.492000, qreg_0[0])
		main_circ.cx(qreg_1[1],0)
		main_circ.cx(qreg_1[1],0)
		main_circ.cx(0,qreg_1[1])
	with else_1:
		main_circ.cx(qreg_3[0],qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.cx(qreg_1[0],0)
	main_circ.id(qreg_3[0])
with else_2:
	main_circ.u(0,0,0.595000, 0)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.rz(param_4, qreg_0[0])
		main_circ.u(0,0,param_3, qreg_1[1])
		main_circ.u(0,param_1,param_3, qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_1[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.y(qreg_0[0])
	with else_1:
		main_circ.barrier(qreg_3[0])
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.y(qreg_1[1])
		main_circ.u(0,0,0.853000, qreg_3[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(0,qreg_1[1])
		main_circ.rz(0.710000, 0)
		main_circ.u(0,param_0,-0.421000, qreg_1[1])
	with else_1:
		main_circ.id(qreg_1[0])
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(0)
	with else_1:
		main_circ.barrier(qreg_3[0])
	main_circ.id(qreg_0[0])
bindings = {param_0: 0.295000, param_1: 0.412000, param_2: 0.074000, param_3: -0.295000, param_4: 0.953000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1158", "InverseCancellation")
