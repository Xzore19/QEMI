from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.s(qreg_1[1])
subcirc0.s(qreg_3[0])
subcirc0.z(qreg_1[1])
subcirc0.u(-0.783000,0.401000,0.323000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.rz(-0.940000, qreg_0[0])
subcirc1.u(0.422000,-0.905000,0.227000, qreg_0[1])
subcirc1.s(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.520000,-0.748000,-0.676000, qreg_3[0])
subcirc2.s(qreg_0[0])
subcirc2.rz(0.343000, qreg_0[0])
subcirc2.rz(-0.089000, qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.s(1)
					main_circ.rz(0.100000, 2)
					main_circ.u(0.600000,0.617000,-0.758000, 1)
					main_circ.append(subcirc2,[2,3,0,1])
				with case_1(1):
					main_circ.rz(-0.742000, 2)
					main_circ.rz(param_3, 1)
					main_circ.append(subcirc1,[1,3,2,0])
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rz(-0.932000, 1)
					main_circ.id(2)
				with case_1(1):
					main_circ.u(0.980000,-0.263000,param_0, 0)
					main_circ.s(0)
					main_circ.z(2)
					main_circ.rz(-0.145000, 0)
with else_3:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.z(0)
			main_circ.s(1)
			main_circ.append(subcirc2,[2,0,1,3])
		with else_1:
			main_circ.z(0)
			main_circ.append(subcirc2,[2,0,1,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_0,-0.614000,0.051000, 3)
				main_circ.append(subcirc2,[3,2,1,0])
			with case_1(1):
				main_circ.rz(0.682000, 3)
				main_circ.z(1)
				main_circ.z(0)
				main_circ.s(0)
with else_3:
	main_circ.z(2)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc2,[1,3,2,0])
			with case_1(1):
				main_circ.append(subcirc2,[3,0,2,1])
	with else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(0)
			main_circ.u(-0.908000,-0.179000,param_1, 3)
main_circ.rz(-0.259000, 2)
main_circ.rz(-0.962000, 2)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[0,2,1,3])
				with case_1(1):
					main_circ.barrier(2)
	with case_3(1):
		main_circ.barrier(2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(3)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.s(3)
				main_circ.z(2)
				main_circ.barrier(3)
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(1)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.id(1)
		main_circ.barrier(0)
	with else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(1)
		main_circ.barrier(3)
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.id(0)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.id(3)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(0)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(3)
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(2)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(1)
			main_circ.barrier(3)
		with case_2(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.barrier(3)
			main_circ.id(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.id(1)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(3)
		with else_1:
			main_circ.barrier(1)
		main_circ.id(0)
	main_circ.barrier(0)
with else_3:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.id(0)
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(2)
			main_circ.barrier(3)
	main_circ.id(0)
bindings = {param_0: 0.224000, param_1: -0.114000, param_3: 0.669000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1450")
