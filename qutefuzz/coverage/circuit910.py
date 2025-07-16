from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.354000,-0.774000, qreg_0[0])
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.u(0.378000,0.780000,0.443000, qreg_0[0])
subcirc0.u(0.756000,0.741000,-0.971000, qreg_2[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(-0.782000,0.098000,param_0, 0)
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.x(1)
				main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],1,qreg_0[0]])
			with case_1(1):
				main_circ.cz(qreg_0[3],qreg_0[2])
				main_circ.x(qreg_0[1])
				main_circ.u(param_1,param_0,-0.991000, 0)
				main_circ.u(0.083000,param_0,param_0, qreg_0[2])
	with else_2:
		main_circ.u(pi/2,-0.510000,param_0, qreg_0[1])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(-0.791000,0.330000,0.286000, qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.x(qreg_0[2])
					main_circ.u(-0.394000,param_1,-0.281000, qreg_0[1])
					main_circ.cz(qreg_0[2],0)
					main_circ.u(0.774000,0.924000,param_1, 0)
				with case_1(1):
					main_circ.x(qreg_0[1])
					main_circ.u(param_0,-0.548000,param_0, 0)
					main_circ.u(0.961000,-0.537000,param_0, qreg_0[0])
					main_circ.x(qreg_0[3])
		with case_2(1):
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.u(pi/2,param_1,0.212000, qreg_0[0])
					main_circ.x(1)
					main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[0],1])
				with case_1(1):
					main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],0,qreg_0[1]])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.cz(0,1)
		main_circ.cz(qreg_0[1],qreg_0[2])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cz(qreg_0[0],1)
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.cz(qreg_0[0],0)
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cz(1,qreg_0[0])
						main_circ.cz(1,0)
						main_circ.cz(qreg_0[1],qreg_0[3])
						main_circ.u(pi/2,param_0,0.895000, 0)
					with case_1(1):
						main_circ.cz(1,qreg_0[1])
						main_circ.u(pi/2,param_0,param_0, qreg_0[2])
						main_circ.barrier(qreg_0[1])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(1,0)
					main_circ.u(pi/2,param_0,0.514000, 0)
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[3])
				with else_1:
					main_circ.id(0)
				main_circ.id(1)
	with case_3(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.id(1)
bindings = {param_0: 0.718000, param_1: -0.567000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "910", "Collect2qBlocks")
