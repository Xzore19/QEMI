from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.rx(-0.449000, qreg_2[0])
subcirc0.z(qreg_2[1])
subcirc0.rx(-0.977000, qreg_0[1])
subcirc0.rz(0.896000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.105000, qreg_1[0])
subcirc1.rz(0.243000, qreg_1[1])
subcirc1.rz(-0.301000, qreg_3[0])
subcirc1.rz(-0.970000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.rz(0.903000, qreg_2[0])
subcirc2.rz(0.863000, qreg_0[0])
subcirc2.rx(-0.652000, qreg_0[0])
subcirc2.rz(-0.007000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.761000, qreg_0[1])
subcirc3.rx(0.223000, qreg_0[1])
subcirc3.z(qreg_0[1])
subcirc3.rz(-0.462000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc1,[qreg_0[1],1,qreg_0[0],2,0])
	with else_1:
		main_circ.append(subcirc1,[qreg_0[0],0,3,2,1])
with else_2:
	main_circ.append(subcirc3,[qreg_0[1],0,1,qreg_0[0]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc1,[2,1,0,qreg_0[1],qreg_0[0]])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(0.401000,-0.740000,0.120000, 2)
	with else_1:
		main_circ.id(qreg_0[0])
	main_circ.id(2)
main_circ.append(subcirc3,[3,qreg_0[0],2,qreg_0[1]])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.id(3)
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.z(3)
			main_circ.rz(param_3, qreg_0[0])
			main_circ.u(param_4,0.624000,param_4, 1)
			main_circ.z(2)
		with case_1(1):
			main_circ.barrier(qreg_0[1])
with else_2:
	main_circ.append(subcirc1,[0,qreg_0[0],1,2,3])
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.barrier(1)
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.rx(-0.211000, 2)
			main_circ.append(subcirc1,[3,1,2,qreg_0[1],0])
		with case_1(1):
			main_circ.rx(param_2, 2)
			main_circ.id(1)
main_circ.u(param_3,-0.875000,param_3, 2)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.rx(-0.112000, 1)
		main_circ.id(qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.z(0)
				main_circ.id(2)
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(-0.440000, 3)
				main_circ.append(subcirc1,[1,3,0,qreg_0[1],2])
			with case_1(1):
				main_circ.append(subcirc1,[2,0,qreg_0[1],1,qreg_0[0]])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rz(param_4, 2)
		main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],1,2])
	with else_1:
		main_circ.id(qreg_0[0])
main_circ.append(subcirc1,[0,2,3,1,qreg_0[1]])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rz(0.574000, 0)
		main_circ.u(param_3,-0.203000,param_0, 0)
		main_circ.z(qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.barrier(1)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[1])
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(3)
		with case_1(1):
			main_circ.id(0)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(1)
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(0)
		with case_1(1):
			main_circ.id(2)
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(1)
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(0)
	main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.344000, param_2: 0.012000, param_3: 0.993000, param_4: -0.286000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1687", "InverseCancellation")
