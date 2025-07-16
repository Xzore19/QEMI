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
subcirc0.rx(0.346000, qreg_3[0])
subcirc0.u(-0.151000,0.738000,0.727000, qreg_0[1])
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_3[0])
subcirc0.u(0.129000,-0.937000,-0.432000, qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.u(param_0,0,0.167000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.rx(param_5, qreg_0[1])
			main_circ.u(param_1,param_4,0.181000, qreg_3[0])
			main_circ.rx(-0.713000, qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.u(0.758000,param_3,-0.852000, qreg_0[1])
							main_circ.u(param_4,param_4,param_5, qreg_0[1])
							main_circ.rx(0.312000, qreg_0[1])
							main_circ.u(-0.581000,param_2,param_0, qreg_3[0])
						with case_1(1):
							main_circ.rx(-0.731000, qreg_3[0])
							main_circ.x(qreg_0[0])
							main_circ.x(qreg_0[1])
							main_circ.x(qreg_0[2])
				with case_2(1):
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
					with else_1:
						main_circ.x(qreg_0[1])
						main_circ.rx(0.142000, qreg_0[2])
		with case_3(1):
			main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
with else_4:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.rx(-0.015000, qreg_0[1])
				main_circ.rx(0.476000, qreg_0[2])
				main_circ.u(param_0,0.928000,-0.760000, qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rx(param_0, qreg_0[1])
				main_circ.x(qreg_0[0])
			with else_1:
				main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.u(0.202000,param_3,-0.972000, qreg_0[1])
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_0[2])
	with case_4(1):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[2])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[2])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[2])
					main_circ.id(qreg_3[0])
			main_circ.barrier(qreg_0[2])
		with else_3:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.id(qreg_3[0])
			with case_3(1):
				main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_3[0])
bindings = {param_0: 0.399000, param_1: 0.122000, param_2: 0.096000, param_3: 0.736000, param_4: -0.568000, param_5: -0.518000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1314", "HoareOptimizer")
