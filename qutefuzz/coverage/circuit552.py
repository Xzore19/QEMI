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
subcirc0.ry(0.656000, qreg_0[0])
subcirc0.u(0,0,-0.308000, qreg_0[1])
subcirc0.s(qreg_2[1])
subcirc0.u(0,0,0.633000, qreg_2[0])
subcirc0.u(pi/2,-0.285000,0.388000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.087000, qreg_0[0])
subcirc1.u(0,0,-0.480000, qreg_0[3])
subcirc1.ry(0.294000, qreg_0[3])
subcirc1.u(pi/2,-0.986000,0.944000, qreg_0[1])
subcirc1.ry(-0.826000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.448000, qreg_0[0])
subcirc2.ry(0.124000, qreg_0[2])
subcirc2.u(0,0,0.700000, qreg_3[0])
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[1])

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

main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.append(subcirc2,[3,2,0,1])
	with case_2(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(pi/2,-0.604000,param_0, 0)
		with else_1:
			main_circ.u(pi/2,-0.013000,param_0, 1)
			main_circ.append(subcirc2,[qreg_0[0],3,0,1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(0,0,-0.902000, 0)
	with else_1:
		main_circ.append(subcirc2,[1,qreg_0[0],qreg_0[1],2])
with else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.ry(0.893000, qreg_0[1])
	with else_1:
		main_circ.u(param_0,param_2,param_1, 1)
main_circ.append(subcirc1,[3,2,qreg_0[0],0])
main_circ.append(subcirc2,[1,qreg_0[1],qreg_0[0],2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.s(3)
		main_circ.append(subcirc2,[qreg_0[0],0,2,1])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(param_1,param_0,param_1, qreg_0[0])
			main_circ.u(param_1,param_0,0.734000, qreg_0[0])
			main_circ.append(subcirc2,[3,0,qreg_0[0],2])
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(0,0,param_0, 2)
				main_circ.append(subcirc2,[1,qreg_0[1],2,3])
			with case_1(1):
				main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],2,0])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.s(2)
			main_circ.s(2)
			main_circ.u(param_1,param_0,param_2, 2)
			main_circ.barrier(qreg_0[1])
		with case_1(1):
			main_circ.id(1)
	main_circ.u(pi/2,param_1,param_0, 3)
	main_circ.id(0)
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(3)
	with else_1:
		main_circ.barrier(1)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(1)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(0)
		with case_1(1):
			main_circ.id(2)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(3)
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.barrier(3)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(1)
	main_circ.barrier(3)
bindings = {param_0: -0.999000, param_1: -0.186000, param_2: -0.326000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "552")
