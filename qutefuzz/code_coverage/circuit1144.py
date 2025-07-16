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
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_2[0])
subcirc0.h(qreg_2[0])
subcirc0.rz(-0.640000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.h(qreg_2[1])
subcirc1.y(qreg_0[0])
subcirc1.rz(0.563000, qreg_0[0])
subcirc1.h(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_0[3])
subcirc2.rz(-0.082000, qreg_0[0])
subcirc2.rz(0.668000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.227000, qreg_0[2])
subcirc3.h(qreg_0[1])
subcirc3.rz(-0.340000, qreg_0[0])
subcirc3.h(qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.rz(0.362000, qreg_1[2])
subcirc4.rz(0.965000, qreg_0[0])
subcirc4.x(qreg_1[1])
subcirc4.rz(-0.159000, qreg_1[2])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],1,0])
	main_circ.x(qreg_0[0])
with else_2:
	main_circ.rz(-0.357000, qreg_0[2])
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[1])
		with case_1(1):
			main_circ.append(subcirc0,[0,1,qreg_0[2],qreg_0[0]])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.y(0)
				main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],1,qreg_0[3]])
			with case_1(1):
				main_circ.id(qreg_0[2])
	with case_2(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[2])
		with else_1:
			main_circ.h(0)
		main_circ.rz(0.260000, 0)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[2])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.y(qreg_0[0])
				main_circ.append(subcirc1,[qreg_0[3],qreg_0[2],qreg_0[0],1])
			with case_1(1):
				main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
		with case_1(1):
			main_circ.h(qreg_0[2])
			main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],1,qreg_0[3]])
with else_2:
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc3,[qreg_0[1],1,qreg_0[2],qreg_0[3]])
		with case_1(1):
			main_circ.x(qreg_0[2])
			main_circ.h(qreg_0[1])
			main_circ.append(subcirc4,[qreg_0[1],qreg_0[2],1,qreg_0[3]])
main_circ.y(qreg_0[0])
main_circ.append(subcirc1,[0,qreg_0[2],1,qreg_0[0]])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[3],1])
with else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[3])
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(1)
	with else_1:
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(qreg_0[1])
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.id(0)
		with case_1(1):
			main_circ.barrier(1)
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[2])
		with case_1(1):
			main_circ.barrier(qreg_0[3])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(1)
	with else_1:
		main_circ.barrier(0)
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(qreg_0[1])
	with else_1:
		main_circ.barrier(qreg_0[3])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[2])
		with case_1(1):
			main_circ.id(1)
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(qreg_0[2])
	main_circ.id(qreg_0[2])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1144")
