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
subcirc0.u(-0.378000,0.631000,0.149000, qreg_0[0])
subcirc0.s(qreg_3[0])
subcirc0.s(qreg_3[0])
subcirc0.s(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.165000,0.564000,0.243000, qreg_2[0])
subcirc1.s(qreg_2[0])
subcirc1.cz(qreg_2[0],qreg_0[0])
subcirc1.cz(qreg_3[0],qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.199000,-0.052000,-0.073000, qreg_1[0])
subcirc2.s(qreg_3[0])
subcirc2.s(qreg_1[1])
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(0)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.u(param_6,param_0,param_2, qreg_0[1])
			main_circ.u(0.264000,0.306000,0.537000, qreg_0[0])
			main_circ.s(qreg_0[1])
			main_circ.u(-0.619000,0.292000,param_1, qreg_0[3])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[3])
			with case_1(1):
				main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.s(qreg_0[1])
		main_circ.u(param_5,param_5,param_6, qreg_0[3])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_3,0.368000,param_4, qreg_0[2])
			main_circ.u(param_2,param_5,0.742000, qreg_0[1])
			main_circ.barrier(qreg_0[2])
		with case_1(1):
			main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[2])
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[3],qreg_0[1]])
		with case_1(1):
			main_circ.u(pi/2,0.333000,param_2, qreg_0[0])
			main_circ.u(pi/2,param_5,-0.681000, qreg_0[0])
			main_circ.u(pi/2,param_4,-0.729000, qreg_0[1])
			main_circ.u(param_5,-0.063000,-0.867000, qreg_0[0])
with else_2:
	main_circ.u(0.460000,0.635000,param_6, qreg_0[1])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cz(qreg_0[2],qreg_0[3])
			main_circ.barrier(qreg_0[2])
		with case_1(1):
			main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.s(qreg_0[2])
		main_circ.cz(qreg_0[3],qreg_0[0])
		main_circ.s(qreg_0[3])
		main_circ.cz(qreg_0[1],qreg_0[2])
	with else_1:
		main_circ.id(qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.id(qreg_0[3])
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(-0.651000,param_3,0.327000, qreg_0[3])
			main_circ.cz(qreg_0[1],qreg_0[2])
		with else_1:
			main_circ.s(qreg_0[3])
			main_circ.u(-0.010000,-0.577000,0.806000, qreg_0[2])
			main_circ.id(qreg_0[2])
main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_0[3]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.s(qreg_0[1])
			main_circ.cz(qreg_0[0],qreg_0[3])
			main_circ.id(qreg_0[3])
		with case_1(1):
			main_circ.s(qreg_0[1])
			main_circ.cz(qreg_0[0],qreg_0[2])
			main_circ.cz(qreg_0[1],qreg_0[2])
			main_circ.cz(qreg_0[2],qreg_0[3])
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cz(qreg_0[0],qreg_0[3])
			main_circ.u(pi/2,0.088000,0.066000, qreg_0[0])
			main_circ.cz(qreg_0[0],qreg_0[1])
			main_circ.cz(qreg_0[3],qreg_0[2])
		with case_1(1):
			main_circ.s(qreg_0[0])
			main_circ.u(pi/2,param_3,param_3, qreg_0[3])
			main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[3])
		with case_1(1):
			main_circ.id(qreg_0[3])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[3])
		with case_1(1):
			main_circ.id(qreg_0[3])
	main_circ.cz(qreg_0[0],qreg_0[2])
with else_2:
	main_circ.u(pi/2,param_6,-0.614000, qreg_0[2])
bindings = {param_0: -0.909000, param_1: -0.361000, param_2: 0.274000, param_3: -0.390000, param_4: -0.066000, param_5: 0.376000, param_6: -0.860000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1444")
