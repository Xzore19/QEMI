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
subcirc0.z(qreg_3[0])
subcirc0.rz(0.229000, qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.rz(-0.433000, qreg_0[0])

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
subcirc1.rz(-0.179000, qreg_1[0])
subcirc1.cx(qreg_1[0],qreg_3[0])
subcirc1.rz(0.522000, qreg_2[0])
subcirc1.rz(0.739000, qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.346000, qreg_0[1])
subcirc2.ry(0.901000, qreg_3[0])
subcirc2.cx(qreg_0[1],qreg_2[0])
subcirc2.cx(qreg_0[1],qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.rz(0.244000, 2)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc0,[qreg_0[0],0,2,3])
		main_circ.rz(param_0, 1)
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rz(0.005000, 2)
			main_circ.append(subcirc2,[3,0,qreg_0[0],1])
		with case_1(1):
			main_circ.ry(-0.005000, 1)
			main_circ.rz(param_0, 3)
			main_circ.cx(1,3)
			main_circ.ry(param_2, qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.ry(param_2, 0)
		main_circ.cx(1,3)
	with else_1:
		main_circ.append(subcirc2,[3,2,0,qreg_0[0]])
		main_circ.z(2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.append(subcirc0,[0,qreg_0[0],3,2])
with else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.append(subcirc1,[0,3,1,2])
	with else_1:
		main_circ.rz(-0.341000, qreg_0[0])
		main_circ.cx(0,qreg_0[0])
		main_circ.z(qreg_0[0])
		main_circ.cx(3,2)
		main_circ.append(subcirc2,[3,0,qreg_0[0],2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(1,0)
			main_circ.cx(0,1)
			main_circ.cx(3,1)
			main_circ.cx(0,3)
		with case_1(1):
			main_circ.append(subcirc1,[qreg_0[0],1,0,2])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.ry(-0.900000, 1)
				main_circ.append(subcirc2,[2,0,qreg_0[0],3])
			with case_1(1):
				main_circ.id(3)
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.id(3)
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.id(3)
		main_circ.barrier(2)
bindings = {param_0: -0.517000, param_2: 0.164000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "115")
