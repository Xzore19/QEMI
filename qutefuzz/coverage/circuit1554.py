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
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_3[0])
subcirc0.u(0,0,-0.621000, qreg_3[0])
subcirc0.h(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.335000, qreg_2[0])
subcirc1.h(qreg_3[0])
subcirc1.u(0.126000,0.495000,0.128000, qreg_0[0])
subcirc1.z(qreg_2[0])
subcirc1.u(0,0,0.161000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,0.216000, qreg_0[0])
subcirc2.u(-0.862000,0.610000,0.149000, qreg_0[1])
subcirc2.u(0.229000,0.821000,0.532000, qreg_0[2])
subcirc2.u(0,0,-0.337000, qreg_0[2])
subcirc2.z(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(-0.708000,-0.158000,-0.988000, qreg_0[1])
subcirc3.z(qreg_0[3])
subcirc3.u(0,0,-0.196000, qreg_0[1])
subcirc3.h(qreg_0[2])
subcirc3.h(qreg_0[2])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.z(qreg_1[2])
subcirc4.u(0,0,-0.431000, qreg_1[1])
subcirc4.u(-0.965000,-0.477000,0.916000, qreg_1[2])
subcirc4.u(0,0,0.327000, qreg_1[2])
subcirc4.z(qreg_0[0])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(0,param_2,0.145000, 1)
		main_circ.u(0,0,0.575000, 1)
		main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[2],0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.h(qreg_0[2])
		main_circ.h(qreg_3[0])
		main_circ.z(qreg_0[1])
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.z(0)
		main_circ.h(0)
		main_circ.u(0.058000,-0.657000,-0.073000, qreg_0[1])
		main_circ.append(subcirc3,[qreg_0[2],1,qreg_0[0],qreg_3[0],0])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_3[0])
		with case_1(1):
			main_circ.h(qreg_3[0])
			main_circ.append(subcirc2,[0,qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.h(0)
		with else_1:
			main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[0],1])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0],0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.h(qreg_0[2])
		main_circ.append(subcirc1,[1,qreg_3[0],0,qreg_0[1],qreg_0[0],qreg_0[2]])
	with else_1:
		main_circ.append(subcirc2,[qreg_0[0],1,qreg_0[1],0])
with else_2:
	main_circ.u(param_3,param_0,param_1, 1)
main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],0,qreg_3[0],1])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.z(0)
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(1)
	main_circ.id(qreg_3[0])
with else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.id(qreg_3[0])
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.h(qreg_0[0])
			main_circ.id(0)
		with case_1(1):
			main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.z(qreg_0[1])
			main_circ.id(1)
		with case_1(1):
			main_circ.barrier(qreg_3[0])
with else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.id(0)
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.id(0)
		with case_1(1):
			main_circ.h(qreg_0[2])
			main_circ.barrier(1)
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(qreg_0[1])
	with else_1:
		main_circ.id(1)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.id(qreg_0[1])
bindings = {param_0: -0.274000, param_1: 0.958000, param_2: 0.961000, param_3: -0.476000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1554")
