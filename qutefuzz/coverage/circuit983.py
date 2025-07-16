from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(pi/2,0.462000,-0.677000, qreg_0[0])
subcirc0.rx(0.731000, qreg_0[0])
subcirc0.s(qreg_1[1])
subcirc0.cx(qreg_0[0],qreg_1[1])
subcirc0.cx(qreg_1[1],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.261000, qreg_0[0])
subcirc1.rx(-0.771000, qreg_3[0])
subcirc1.cx(qreg_3[0],qreg_1[0])
subcirc1.u(pi/2,0.542000,0.187000, qreg_1[0])
subcirc1.rx(-0.979000, qreg_1[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_3[0],qreg_0[0]])
with else_2:
	main_circ.s(qreg_2[0])
main_circ.cx(qreg_0[0],qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.rx(-0.605000, qreg_0[0])
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.s(qreg_0[0])
			main_circ.u(param_2,-0.123000,-0.008000, qreg_0[0])
			main_circ.cx(qreg_2[0],qreg_3[0])
			main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_3[0]])
		with else_1:
			main_circ.cx(qreg_0[0],qreg_2[0])
			main_circ.append(subcirc0,[qreg_3[0],qreg_2[0],qreg_0[0],qreg_0[1]])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cx(qreg_0[0],qreg_2[0])
			main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.cx(qreg_0[0],qreg_3[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rx(param_1, qreg_3[0])
			main_circ.s(qreg_0[1])
			main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_3[0],qreg_0[0]])
	with case_2(1):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.s(qreg_3[0])
				main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[1],qreg_0[0]])
			with case_1(1):
				main_circ.cx(qreg_3[0],qreg_2[0])
				main_circ.u(pi/2,param_1,param_0, qreg_3[0])
				main_circ.s(qreg_0[1])
				main_circ.u(pi/2,param_2,-0.435000, qreg_0[1])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.s(qreg_2[0])
	with else_1:
		main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.rx(param_1, qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.s(qreg_2[0])
	with else_1:
		main_circ.u(param_2,-0.537000,param_2, qreg_3[0])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[1])
		with case_1(1):
			main_circ.barrier(qreg_2[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_3[0])
		with case_1(1):
			main_circ.id(qreg_2[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_3[0])
		with case_1(1):
			main_circ.barrier(qreg_2[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_2[0])
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[1])
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.id(qreg_0[0])
	main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_3[0])
		with case_1(1):
			main_circ.id(qreg_2[0])
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(qreg_2[0])
	with else_1:
		main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.830000, param_1: -0.053000, param_2: -0.752000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "983")
