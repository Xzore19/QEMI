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
subcirc0.u(pi/2,0.241000,0.436000, qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0.x(qreg_2[1])
subcirc0.u(pi/2,-0.786000,-0.367000, qreg_0[1])
subcirc0.x(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.u(0,0,0.453000, qreg_0[1])
subcirc1.x(qreg_0[1])
subcirc1.u(0,0,-0.258000, qreg_0[1])
subcirc1.z(qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.x(qreg_0[0])
				main_circ.z(qreg_0[0])
				main_circ.u(pi/2,param_0,-0.645000, qreg_3[0])
				main_circ.u(param_0,param_0,param_0, qreg_0[1])
			with case_1(1):
				main_circ.u(param_0,0,0.713000, qreg_0[1])
				main_circ.append(subcirc1,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_3[0]])
	with else_2:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_0,0,-0.682000, qreg_0[0])
with else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_0,0,param_0, qreg_2[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.x(qreg_2[0])
				main_circ.append(subcirc1,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_2[0]])
			with case_1(1):
				main_circ.u(0,0,param_0, qreg_3[0])
				main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],qreg_3[0],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0,0,0.045000, qreg_2[0])
			main_circ.z(qreg_0[0])
			main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[1],qreg_0[0]])
		with else_1:
			main_circ.u(param_0,0.076000,-0.152000, qreg_2[0])
			main_circ.z(qreg_0[0])
			main_circ.z(qreg_0[0])
			main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[1],qreg_0[0]])
	with else_2:
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_2[0]])
		with else_1:
			main_circ.z(qreg_0[1])
			main_circ.barrier(qreg_3[0])
main_circ.z(qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0,0,param_0, qreg_0[0])
				main_circ.u(pi/2,-0.959000,-0.878000, qreg_2[0])
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.u(pi/2,0.689000,param_0, qreg_3[0])
				main_circ.id(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_3[0])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_2[0])
			with else_1:
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_3[0])
			with else_1:
				main_circ.barrier(qreg_2[0])
			main_circ.id(qreg_2[0])
		with else_2:
			main_circ.barrier(qreg_0[1])
		main_circ.barrier(qreg_2[0])
	with case_3(1):
		main_circ.id(qreg_2[0])
bindings = {param_0: 0.845000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1266", "TemplateOptimization")
