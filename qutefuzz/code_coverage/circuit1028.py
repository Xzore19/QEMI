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
subcirc0.s(qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0.s(qreg_3[0])
subcirc0.u(0,0,-0.153000, qreg_0[1])
subcirc0.s(qreg_0[2])
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
subcirc1.cx(qreg_2[0],qreg_0[1])
subcirc1.s(qreg_2[0])
subcirc1.u(0,0,-0.178000, qreg_3[0])
subcirc1.u(0,0,-0.563000, qreg_3[0])
subcirc1.cx(qreg_0[1],qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.h(qreg_2[1])
subcirc2.s(qreg_1[0])
subcirc2.u(0,0,-0.528000, qreg_1[0])
subcirc2.cx(qreg_2[1],qreg_2[0])
subcirc2.u(0,0,0.299000, qreg_2[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.h(qreg_1[0])
		main_circ.append(subcirc2,[qreg_2[1],qreg_1[0],qreg_2[0],qreg_0[0]])
	with else_1:
		main_circ.h(qreg_0[0])
		main_circ.append(subcirc2,[qreg_2[1],qreg_2[0],qreg_0[0],qreg_1[0]])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.s(qreg_1[0])
		main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_1[0],qreg_2[1]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(param_0,param_0,-0.568000, qreg_0[0])
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_2[1])
		with case_1(1):
			main_circ.s(qreg_2[0])
			main_circ.h(qreg_2[1])
			main_circ.h(qreg_2[0])
			main_circ.h(qreg_1[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(0,param_0,-0.850000, qreg_0[0])
			main_circ.barrier(qreg_2[0])
		with case_1(1):
			main_circ.h(qreg_2[1])
			main_circ.s(qreg_0[0])
			main_circ.u(0,param_0,param_0, qreg_1[0])
			main_circ.s(qreg_2[1])
main_circ.u(param_0,0,-0.351000, qreg_2[0])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(param_0,0,-0.395000, qreg_0[0])
		main_circ.h(qreg_0[0])
		main_circ.s(qreg_2[1])
	with else_1:
		main_circ.h(qreg_0[0])
		main_circ.cx(qreg_2[0],qreg_0[0])
		main_circ.cx(qreg_0[0],qreg_1[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(qreg_2[0],qreg_1[0])
		main_circ.cx(qreg_1[0],qreg_0[0])
		main_circ.cx(qreg_2[1],qreg_0[0])
	with else_1:
		main_circ.cx(qreg_2[1],qreg_1[0])
		main_circ.cx(qreg_0[0],qreg_2[0])
		main_circ.cx(qreg_1[0],qreg_2[0])
		main_circ.cx(qreg_1[0],qreg_2[0])
main_circ.cx(qreg_2[0],qreg_1[0])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.s(qreg_1[0])
			main_circ.id(qreg_2[0])
		with case_1(1):
			main_circ.barrier(qreg_2[1])
	main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_2[1])
			with case_1(1):
				main_circ.u(0,0,param_0, qreg_2[0])
				main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_2[1])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_2[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_2[0])
			with case_1(1):
				main_circ.id(qreg_2[1])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.barrier(qreg_1[0])
		main_circ.id(qreg_1[0])
	with case_2(1):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_2[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_2[1])
			with case_1(1):
				main_circ.barrier(qreg_2[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_2[1])
			with case_1(1):
				main_circ.id(qreg_2[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_2[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_2[0])
		main_circ.id(qreg_2[1])
bindings = {param_0: 0.793000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1028", "RemoveFinalReset")
