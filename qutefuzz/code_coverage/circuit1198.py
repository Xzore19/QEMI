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
subcirc0.u(pi/2,0.648000,-0.560000, qreg_3[0])
subcirc0.x(qreg_1[0])
subcirc0.u(pi/2,0.742000,-0.751000, qreg_1[1])
subcirc0.u(pi/2,0.281000,-0.819000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.640000, qreg_2[0])
subcirc1.x(qreg_2[1])
subcirc1.x(qreg_0[0])
subcirc1.h(qreg_2[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,-0.234000,0.258000, qreg_2[1])
subcirc2.h(qreg_2[0])
subcirc2.h(qreg_2[0])
subcirc2.u(pi/2,-0.265000,-0.859000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.x(qreg_0[1])
subcirc3.h(qreg_2[1])
subcirc3.u(0,0,0.510000, qreg_0[1])
subcirc3.x(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc0,[qreg_0[0],0,2,3])
			with else_1:
				main_circ.append(subcirc1,[0,2,qreg_0[0],3,1])
				main_circ.append(subcirc3,[2,0,1,3])
		with else_2:
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.x(qreg_0[0])
				main_circ.id(2)
			with else_1:
				main_circ.barrier(0)
	with case_3(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.append(subcirc0,[2,1,0,qreg_0[0]])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.append(subcirc3,[0,qreg_0[0],3,2])
					main_circ.barrier(3)
				with else_1:
					main_circ.u(pi/2,param_1,param_1, 1)
					main_circ.u(pi/2,0.322000,0.409000, qreg_0[0])
					main_circ.u(param_1,param_0,-0.375000, qreg_0[0])
					main_circ.append(subcirc3,[qreg_0[0],3,1,0])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.h(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.h(qreg_0[0])
				main_circ.append(subcirc0,[2,0,1,qreg_0[0]])
			with else_1:
				main_circ.h(0)
				main_circ.u(0,param_0,param_1, 2)
				main_circ.u(0,param_0,param_1, 1)
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.u(0,0,0.884000, 1)
					main_circ.append(subcirc0,[0,1,3,2])
				with case_1(1):
					main_circ.append(subcirc3,[3,2,1,0])
main_circ.x(3)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc0,[qreg_0[0],1,2,3])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.append(subcirc1,[3,0,qreg_0[0],2,1])
			with case_2(1):
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(2)
				main_circ.id(3)
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.h(2)
				main_circ.id(1)
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.id(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(3)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(1)
			main_circ.barrier(0)
		main_circ.id(1)
bindings = {param_0: 0.198000, param_1: -0.975000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1198")
