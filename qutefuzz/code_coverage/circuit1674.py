from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.z(qreg_1[1])
subcirc0.u(pi/2,0.335000,0.475000, qreg_0[0])
subcirc0.rx(-0.639000, qreg_1[0])
subcirc0.z(qreg_1[2])
subcirc0.cy(qreg_0[0],qreg_1[0])
subcirc0.cy(qreg_0[0],qreg_1[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(pi/2,0.822000,-0.243000, qreg_1[2])
subcirc1.z(qreg_1[1])
subcirc1.u(pi/2,0.004000,-0.489000, qreg_1[2])
subcirc1.u(pi/2,0.596000,-0.503000, qreg_1[2])
subcirc1.cy(qreg_0[0],qreg_1[1])
subcirc1.z(qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.rx(-0.504000, qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_3[0])
subcirc2.u(pi/2,-0.199000,-0.198000, qreg_0[2])
subcirc2.rx(-0.513000, qreg_0[0])
subcirc2.z(qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.z(qreg_2[0])
				main_circ.rx(param_0, qreg_2[0])
				main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_3[0]])
			with else_1:
				main_circ.rx(param_0, qreg_0[0])
				main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_3[0]])
		with case_2(1):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc1,[qreg_2[0],qreg_3[0],qreg_0[1],qreg_0[0]])
			with else_1:
				main_circ.barrier(qreg_2[0])
with else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(qreg_0[0],qreg_3[0])
				main_circ.u(param_0,param_0,param_0, qreg_0[1])
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.u(param_0,param_0,-0.059000, qreg_3[0])
				main_circ.barrier(qreg_2[0])
			main_circ.append(subcirc1,[qreg_0[0],qreg_3[0],qreg_2[0],qreg_0[1]])
		with case_2(1):
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rx(-0.766000, qreg_3[0])
					main_circ.rx(param_0, qreg_0[0])
					main_circ.z(qreg_3[0])
					main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_2[0]])
				with case_1(1):
					main_circ.cy(qreg_3[0],qreg_0[1])
					main_circ.cy(qreg_2[0],qreg_3[0])
					main_circ.cy(qreg_2[0],qreg_0[0])
					main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_3[0],qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.cy(qreg_0[1],qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cy(qreg_3[0],qreg_0[1])
					main_circ.cy(qreg_2[0],qreg_0[1])
					main_circ.cy(qreg_0[1],qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.cy(qreg_0[1],qreg_3[0])
				with else_1:
					main_circ.z(qreg_3[0])
					main_circ.z(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.u(pi/2,param_0,param_0, qreg_2[0])
						main_circ.u(param_0,param_0,0.501000, qreg_2[0])
						main_circ.barrier(qreg_0[0])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.u(pi/2,param_0,param_0, qreg_0[1])
					main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_3[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(qreg_2[0])
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_2[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_3[0])
				with case_1(1):
					main_circ.id(qreg_2[0])
			main_circ.barrier(qreg_2[0])
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_2[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_2[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_0[1])
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_3[0])
				with case_1(1):
					main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_3[0])
				with case_1(1):
					main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_3[0])
			with else_1:
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_3[0])
		main_circ.barrier(qreg_2[0])
bindings = {param_0: -0.573000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1674", "Collect1qRuns")
