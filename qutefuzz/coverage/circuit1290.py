from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0.567000,-0.409000,0.101000, qreg_0[1])
subcirc0.u(-0.904000,-0.333000,0.932000, qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.u(0.872000,-0.713000,0.921000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.914000, qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.cy(qreg_2[0],qreg_0[1])
subcirc1.h(qreg_0[1])
subcirc1.u(0.030000,-0.691000,0.589000, qreg_2[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(param_0, qreg_0[2])
			main_circ.cy(qreg_0[3],qreg_0[1])
			main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_0[3],qreg_0[2]])
		with case_1(1):
			main_circ.ry(0.240000, qreg_0[2])
			main_circ.h(qreg_0[3])
			main_circ.barrier(qreg_0[1])
main_circ.ry(param_1, qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(qreg_0[2],qreg_0[3])
		main_circ.id(qreg_0[3])
	with else_1:
		main_circ.append(subcirc1,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
with else_2:
	main_circ.cy(qreg_0[2],qreg_0[3])
	main_circ.h(qreg_0[3])
	main_circ.h(qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.h(qreg_0[0])
				main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(qreg_0[2],qreg_0[1])
			main_circ.h(qreg_0[0])
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(param_1,param_1,param_0, qreg_0[2])
			main_circ.ry(param_0, qreg_0[3])
			main_circ.u(0.653000,param_1,param_0, qreg_0[0])
			main_circ.cy(qreg_0[2],qreg_0[0])
	with case_2(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.ry(0.216000, qreg_0[2])
			main_circ.h(qreg_0[3])
			main_circ.ry(-0.415000, qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
	with case_2(1):
		main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(qreg_0[0],qreg_0[2])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(qreg_0[3],qreg_0[0])
		main_circ.cy(qreg_0[1],qreg_0[0])
		main_circ.cy(qreg_0[2],qreg_0[3])
		main_circ.cy(qreg_0[3],qreg_0[0])
		main_circ.cy(qreg_0[3],qreg_0[1])
	with else_1:
		main_circ.cy(qreg_0[0],qreg_0[1])
		main_circ.cy(qreg_0[0],qreg_0[3])
		main_circ.u(param_1,0.894000,0.155000, qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[3])
		with case_1(1):
			main_circ.cy(qreg_0[3],qreg_0[0])
			main_circ.cy(qreg_0[2],qreg_0[0])
			main_circ.id(qreg_0[3])
	main_circ.id(qreg_0[3])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(qreg_0[1])
	with else_1:
		main_circ.id(qreg_0[3])
	main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.334000, param_1: 0.578000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1290", "CollectMultiQBlocks")
