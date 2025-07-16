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
subcirc0.h(qreg_0[1])
subcirc0.u(pi/2,-0.495000,0.991000, qreg_0[1])
subcirc0.u(-0.027000,0.500000,0.729000, qreg_0[1])
subcirc0.s(qreg_3[0])
subcirc0.u(-0.863000,-0.230000,0.492000, qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_0,-0.249000,0.645000, qreg_2[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,param_2,param_1, qreg_2[1])
				main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[0],qreg_2[1]])
			with case_1(1):
				main_circ.s(qreg_2[1])
				main_circ.s(qreg_0[1])
				main_circ.h(qreg_0[0])
				main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[1],qreg_2[0]])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.u(param_3,param_3,param_1, qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(0.458000,-0.536000,-0.749000, qreg_0[0])
				with else_1:
					main_circ.h(qreg_0[1])
					main_circ.s(qreg_0[0])
					main_circ.h(qreg_2[0])
					main_circ.append(subcirc0,[qreg_0[1],qreg_2[1],qreg_2[0],qreg_0[0]])
			with case_2(1):
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.u(param_2,param_3,param_3, qreg_0[1])
					main_circ.u(pi/2,0.728000,param_3, qreg_0[0])
					main_circ.s(qreg_0[0])
					main_circ.append(subcirc0,[qreg_0[1],qreg_2[1],qreg_2[0],qreg_0[0]])
	with case_3(1):
		main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_0[1],qreg_0[0]])
main_circ.u(param_3,param_3,param_3, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(-0.884000,-0.598000,-0.218000, qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(qreg_2[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.h(qreg_2[0])
						main_circ.u(-0.546000,param_3,param_1, qreg_2[0])
						main_circ.id(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_2[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.barrier(qreg_2[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_2[0])
				with case_1(1):
					main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_2[1])
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_0[1])
		main_circ.id(qreg_0[0])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.id(qreg_0[1])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_2[1])
			with case_2(1):
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.id(qreg_0[0])
		main_circ.id(qreg_2[1])
bindings = {param_0: -0.086000, param_1: -0.319000, param_2: 0.828000, param_3: -0.959000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "462", "Optimize1qGatesSimpleCommutation")
