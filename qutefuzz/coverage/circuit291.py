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
subcirc0.rz(-0.228000, qreg_0[2])
subcirc0.u(-0.360000,0.498000,-0.448000, qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.u(-0.360000,-0.599000,-0.661000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.209000, qreg_0[1])
subcirc1.h(qreg_0[0])
subcirc1.cz(qreg_0[2],qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.rz(-0.444000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[2])
subcirc2.u(0.218000,-0.082000,0.934000, qreg_0[2])
subcirc2.h(qreg_0[1])
subcirc2.cz(qreg_0[3],qreg_0[0])
subcirc2.cz(qreg_0[3],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.864000, qreg_2[0])
subcirc3.u(0.472000,0.381000,0.907000, qreg_0[0])
subcirc3.rz(-0.249000, qreg_2[0])
subcirc3.cz(qreg_0[1],qreg_0[0])
subcirc3.u(-0.853000,0.651000,-0.963000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.cz(qreg_2[0],qreg_0[0])
subcirc4.u(0.817000,0.105000,0.755000, qreg_1[0])
subcirc4.u(-0.027000,-0.230000,0.681000, qreg_2[0])
subcirc4.rz(-0.629000, qreg_2[0])
subcirc4.h(qreg_0[0])
subcirc4 = subcirc4.to_gate().control(2)

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

main_circ.u(-0.145000,param_2,param_2, 3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.barrier(1)
		with case_2(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.id(2)
			main_circ.id(1)
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.h(3)
				main_circ.append(subcirc1,[3,2,1,0])
			with case_1(1):
				main_circ.u(param_1,-0.206000,-0.052000, 1)
				main_circ.append(subcirc1,[3,1,2,0])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.rz(0.805000, 1)
			main_circ.u(param_2,0.916000,0.959000, 0)
			main_circ.barrier(3)
	with else_2:
		main_circ.barrier(1)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(2,3)
				main_circ.h(0)
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cz(1,3)
				main_circ.barrier(3)
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.append(subcirc1,[1,0,3,2])
			with else_1:
				main_circ.id(3)
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.h(2)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.u(param_1,param_1,0.692000, 1)
					main_circ.id(1)
				with case_1(1):
					main_circ.h(0)
					main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rz(param_0, 3)
				main_circ.id(1)
			with else_1:
				main_circ.cz(3,1)
				main_circ.append(subcirc1,[3,0,1,2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.rz(param_2, 1)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.id(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.cz(1,2)
					main_circ.id(3)
				with case_1(1):
					main_circ.h(1)
					main_circ.id(3)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cz(0,1)
				main_circ.id(3)
		with case_2(1):
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[2,1,0,3])
				with case_1(1):
					main_circ.cz(0,2)
					main_circ.h(1)
					main_circ.h(0)
					main_circ.rz(param_0, 3)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(1)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.id(1)
	with else_2:
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.rz(param_2, 1)
			main_circ.u(0.983000,-0.763000,param_2, 2)
			main_circ.id(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc1,[1,0,3,2])
			with case_1(1):
				main_circ.id(0)
with else_3:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.barrier(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_2,param_0,0.440000, 3)
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.id(3)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.id(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(3)
			main_circ.id(0)
		with case_2(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(1)
			main_circ.id(0)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.barrier(1)
	with else_2:
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(2)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.barrier(1)
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(2)
		main_circ.barrier(0)
	main_circ.id(2)
bindings = {param_0: 0.101000, param_1: 0.808000, param_2: 0.128000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "291", "Collect2qBlocks")
