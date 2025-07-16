from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.z(qreg_0[1])
subcirc0.u(0.678000,0.276000,0.383000, qreg_0[2])
subcirc0.u(0.482000,-0.807000,0.335000, qreg_0[3])
subcirc0.rx(0.323000, qreg_0[1])
subcirc0.rz(-0.656000, qreg_0[1])
subcirc0.z(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(-0.213000, qreg_0[3])
subcirc1.z(qreg_0[0])
subcirc1.rx(0.780000, qreg_0[2])
subcirc1.rz(0.261000, qreg_0[3])
subcirc1.rz(0.444000, qreg_0[1])
subcirc1.rz(0.945000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.z(qreg_1[0])
subcirc2.rz(0.248000, qreg_0[0])
subcirc2.rx(-0.709000, qreg_0[0])
subcirc2.rx(-0.653000, qreg_1[2])
subcirc2.rx(-0.680000, qreg_1[1])
subcirc2.z(qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc2,[qreg_2[1],qreg_2[0],qreg_0[0],qreg_1[0]])
main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_2[1],qreg_1[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_1[0],qreg_2[1]])
			with else_1:
				main_circ.rx(0.717000, qreg_2[1])
				main_circ.rx(param_4, qreg_2[0])
				main_circ.append(subcirc1,[qreg_2[0],qreg_2[1],qreg_0[0],qreg_1[0]])
		with else_2:
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.z(qreg_0[0])
				main_circ.z(qreg_2[0])
				main_circ.rz(param_2, qreg_0[0])
				main_circ.append(subcirc1,[qreg_2[1],qreg_1[0],qreg_2[0],qreg_0[0]])
			with else_1:
				main_circ.u(0.472000,-0.585000,0.864000, qreg_2[0])
				main_circ.rz(param_2, qreg_2[0])
				main_circ.rx(0.206000, qreg_1[0])
				main_circ.u(-0.177000,-0.377000,0.555000, qreg_1[0])
				main_circ.barrier(qreg_1[0])
	with case_3(1):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.z(qreg_2[1])
				main_circ.rx(0.748000, qreg_2[1])
				main_circ.id(qreg_2[1])
			with else_1:
				main_circ.u(0.973000,param_4,-0.465000, qreg_0[0])
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[0])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_2[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_2[1])
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.barrier(qreg_2[1])
			with case_2(1):
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_2[1])
				main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.barrier(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_1[0])
			with else_1:
				main_circ.barrier(qreg_2[1])
			main_circ.id(qreg_2[0])
		main_circ.id(qreg_2[0])
bindings = {param_2: 0.886000, param_4: -0.269000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1918")
