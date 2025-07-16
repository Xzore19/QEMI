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
subcirc0.rx(-0.503000, qreg_0[0])
subcirc0.ry(-0.444000, qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.rx(0.040000, qreg_0[1])
subcirc0.rx(0.921000, qreg_3[0])
subcirc0.h(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.x(qreg_3[0])
subcirc1.x(qreg_3[0])
subcirc1.ry(-0.388000, qreg_3[0])
subcirc1.x(qreg_0[0])
subcirc1.rx(0.181000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_3[0])
subcirc2.h(qreg_2[0])
subcirc2.h(qreg_0[1])
subcirc2.h(qreg_2[0])
subcirc2.rx(0.528000, qreg_2[0])
subcirc2.rx(0.228000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.rx(-0.062000, qreg_1[2])
subcirc3.h(qreg_1[1])
subcirc3.h(qreg_1[1])
subcirc3.x(qreg_0[0])
subcirc3.rx(-0.805000, qreg_0[0])
subcirc3.ry(-0.190000, qreg_1[0])
subcirc3 = subcirc3.to_gate().control(3)

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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],1,qreg_0[2]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(qreg_0[2])
			main_circ.x(qreg_0[2])
			main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[2],qreg_0[0]])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(qreg_0[0])
				main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],1,0])
			with case_1(1):
				main_circ.ry(param_0, qreg_0[0])
				main_circ.x(qreg_0[1])
				main_circ.ry(param_2, qreg_0[0])
				main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[0],0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc2,[qreg_0[2],1,qreg_0[0],qreg_0[1]])
	with else_1:
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.ry(param_1, qreg_0[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[2])
		with else_1:
			main_circ.rx(0.175000, qreg_0[2])
			main_circ.id(qreg_0[2])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.x(qreg_0[2])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc2,[qreg_0[3],1,qreg_0[0],qreg_0[2]])
		with else_1:
			main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],0,qreg_0[1]])
	with case_2(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.ry(param_1, 0)
				main_circ.x(qreg_0[0])
				main_circ.ry(0.752000, qreg_0[0])
				main_circ.h(qreg_0[3])
			with case_1(1):
				main_circ.x(qreg_0[3])
				main_circ.id(0)
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.x(qreg_0[0])
	with else_1:
		main_circ.x(1)
		main_circ.rx(param_2, qreg_0[3])
		main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.x(qreg_0[1])
	with else_1:
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.id(qreg_0[2])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(0)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.barrier(0)
bindings = {param_0: 0.470000, param_1: -0.203000, param_2: -0.723000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "505", "InverseCancellation")
