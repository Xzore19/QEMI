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
subcirc0.rz(-0.128000, qreg_2[1])
subcirc0.rx(-0.445000, qreg_0[0])
subcirc0.z(qreg_2[1])
subcirc0.rz(-0.906000, qreg_0[0])
subcirc0.cy(qreg_2[0],qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_3[0],qreg_1[1])
subcirc1.rz(0.919000, qreg_1[0])
subcirc1.cy(qreg_1[1],qreg_0[0])
subcirc1.z(qreg_1[1])
subcirc1.rx(0.238000, qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[2])
subcirc2.rx(-0.121000, qreg_0[1])
subcirc2.rz(0.308000, qreg_0[1])
subcirc2.rz(-0.245000, qreg_0[2])
subcirc2.z(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_2[1])
subcirc3.z(qreg_1[0])
subcirc3.z(qreg_2[0])
subcirc3.z(qreg_2[1])
subcirc3.rz(0.874000, qreg_2[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rx(-0.255000, qreg_0[2])
subcirc4.rz(-0.746000, qreg_0[0])
subcirc4.z(qreg_0[2])
subcirc4.z(qreg_0[2])
subcirc4.rz(-0.490000, qreg_0[0])
subcirc4 = subcirc4.to_gate().control(2)

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

main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.z(qreg_0[1])
				main_circ.rz(0.908000, qreg_0[0])
				main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
			with case_1(1):
				main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
	with else_2:
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(qreg_0[1])
			main_circ.rx(-0.470000, qreg_0[2])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
			with case_1(1):
				main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.barrier(qreg_0[1])
		with case_2(1):
			main_circ.rx(-0.101000, qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cy(qreg_0[3],qreg_0[2])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[3])
				with case_1(1):
					main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[3],qreg_0[1]])
with else_3:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.append(subcirc2,[qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
		with case_2(1):
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.rx(0.585000, qreg_0[2])
					main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.rz(0.834000, qreg_0[3])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.cy(qreg_0[1],qreg_0[3])
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[3],qreg_0[0])
					main_circ.cy(qreg_0[1],qreg_0[3])
					main_circ.cy(qreg_0[2],qreg_0[3])
					main_circ.cy(qreg_0[2],qreg_0[1])
				with case_1(1):
					main_circ.cy(qreg_0[2],qreg_0[3])
					main_circ.cy(qreg_0[3],qreg_0[1])
					main_circ.cy(qreg_0[3],qreg_0[0])
					main_circ.cy(qreg_0[2],qreg_0[0])
		with case_2(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rx(-0.449000, qreg_0[0])
				main_circ.append(subcirc1,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
with else_3:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.barrier(qreg_0[0])
	with else_2:
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_0[2])
		with else_1:
			main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_0[2])
		with else_1:
			main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.barrier(qreg_0[1])
		main_circ.id(qreg_0[3])
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[2])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_0[2])
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.id(qreg_0[3])
	with else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[1])
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_0[3])
		with else_1:
			main_circ.barrier(qreg_0[3])
		main_circ.barrier(qreg_0[3])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[3])
			main_circ.id(qreg_0[2])
		with case_2(1):
			main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[1])
			with case_1(1):
				main_circ.barrier(qreg_0[3])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[3])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[1])
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[1])
		with else_1:
			main_circ.id(qreg_0[3])
		main_circ.barrier(qreg_0[1])
	with else_2:
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[3])
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[1])
			with case_1(1):
				main_circ.barrier(qreg_0[3])
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[2])
			with else_1:
				main_circ.id(qreg_0[3])
			main_circ.id(qreg_0[0])
		with case_2(1):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.barrier(qreg_0[2])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[2])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.id(qreg_0[3])
		with case_2(1):
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[3])
			with else_1:
				main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[2])
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[0])
			main_circ.id(qreg_0[3])
	main_circ.id(qreg_0[3])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "262")
