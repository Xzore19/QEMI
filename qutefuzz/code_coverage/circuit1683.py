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
subcirc0.u(-0.710000,0.889000,-0.121000, qreg_0[2])
subcirc0.z(qreg_0[2])
subcirc0.u(-0.647000,0.922000,0.618000, qreg_0[0])
subcirc0.u(0.027000,0.037000,-0.481000, qreg_0[1])
subcirc0.rz(0.556000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[3])
subcirc1.u(0.216000,0.466000,-0.940000, qreg_0[3])
subcirc1.z(qreg_0[2])
subcirc1.rz(0.574000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_0,param_1,0.728000, qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(param_1,param_1,0.152000, 1)
	with else_1:
		main_circ.u(param_1,param_0,0.066000, 0)
		main_circ.rz(0.170000, qreg_0[0])
		main_circ.u(pi/2,param_1,-0.945000, 0)
		main_circ.append(subcirc1,[qreg_1[0],1,0,qreg_0[0]])
with else_2:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(param_0,param_0,-0.568000, 2)
	with else_1:
		main_circ.u(pi/2,param_0,0.762000, qreg_1[0])
		main_circ.z(2)
		main_circ.u(param_0,param_0,0.191000, qreg_0[0])
		main_circ.append(subcirc1,[3,qreg_0[0],qreg_1[0],2])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(3)
	with else_1:
		main_circ.u(param_1,param_0,-0.474000, 3)
		main_circ.append(subcirc1,[0,2,1,qreg_0[0]])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.u(-0.993000,0.197000,0.038000, 3)
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.append(subcirc1,[qreg_1[0],2,3,qreg_0[0]])
with else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[2,qreg_0[0],1,0])
		with case_1(1):
			main_circ.u(pi/2,0.451000,param_0, 2)
			main_circ.rz(param_1, qreg_1[0])
			main_circ.u(param_1,param_0,param_0, qreg_0[0])
			main_circ.u(param_0,param_1,param_1, 1)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.rz(param_1, qreg_1[0])
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(1)
	with else_1:
		main_circ.append(subcirc1,[1,2,qreg_0[0],3])
with else_2:
	main_circ.u(param_0,-0.841000,param_1, 2)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc1,[0,1,2,3])
	with else_1:
		main_circ.u(pi/2,0.564000,param_1, 3)
		main_circ.id(qreg_0[0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.rz(param_0, qreg_0[0])
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(param_1,param_0,0.075000, 3)
			main_circ.u(param_1,-0.207000,param_1, 0)
			main_circ.barrier(2)
		with case_1(1):
			main_circ.id(2)
with else_2:
	main_circ.rz(param_1, qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(pi/2,0.412000,param_0, 3)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.z(1)
		main_circ.barrier(0)
	with else_1:
		main_circ.id(1)
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(2)
		with case_1(1):
			main_circ.barrier(2)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(2)
	with else_1:
		main_circ.id(qreg_0[0])
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.barrier(0)
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(0)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(2)
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(2)
	with else_1:
		main_circ.barrier(1)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(1)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.barrier(2)
	main_circ.id(qreg_0[0])
with else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(0)
	main_circ.id(3)
bindings = {param_0: 0.200000, param_1: -0.792000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1683", "CollectCliffords")
