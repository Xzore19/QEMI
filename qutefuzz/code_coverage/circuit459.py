from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_1[0])
subcirc0.x(qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_1[0])
subcirc0.u(pi/2,-0.079000,0.104000, qreg_1[0])
subcirc0.ry(0.997000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.u(pi/2,0.974000,0.188000, qreg_1[0])
subcirc1.u(pi/2,-0.324000,0.784000, qreg_1[2])
subcirc1.ry(-0.522000, qreg_1[1])
subcirc1.ry(0.787000, qreg_0[0])
subcirc1.x(qreg_1[2])
subcirc1.u(pi/2,-0.173000,0.481000, qreg_1[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.h(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.x(0)
		main_circ.h(qreg_3[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(param_0,0.876000,param_1, qreg_0[2])
					main_circ.h(qreg_0[2])
				with else_1:
					main_circ.h(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.ry(-0.908000, qreg_0[0])
					main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],0])
				with else_1:
					main_circ.h(qreg_0[1])
					main_circ.h(qreg_3[0])
					main_circ.x(qreg_0[2])
					main_circ.ry(-0.220000, 0)
					main_circ.ry(param_1, qreg_3[0])
			with case_2(1):
				main_circ.ry(param_0, qreg_0[1])
				main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[1],qreg_0[2]])
with else_4:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.h(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[2],qreg_0[0]])
			with else_1:
				main_circ.h(0)
				main_circ.u(pi/2,-0.047000,-0.231000, qreg_0[2])
				main_circ.ry(0.360000, 0)
				main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],0,qreg_0[0]])
	with else_3:
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.ry(param_1, 0)
			main_circ.h(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.x(qreg_0[1])
				main_circ.x(0)
				main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[0],qreg_0[2]])
			with else_1:
				main_circ.barrier(qreg_3[0])
		with else_2:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(pi/2,-0.979000,param_1, 0)
				main_circ.id(qreg_3[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_3[0])
			with else_1:
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_3[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_0[2])
			main_circ.id(qreg_0[0])
bindings = {param_0: 0.296000, param_1: 0.796000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "459", "CommutativeInverseCancellation")
