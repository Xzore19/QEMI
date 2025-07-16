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
subcirc0.u(-0.658000,0.561000,0.046000, qreg_0[0])
subcirc0.cy(qreg_1[1],qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_1[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.450000,0.376000,-0.034000, qreg_0[0])
subcirc1.s(qreg_0[2])
subcirc1.u(pi/2,0.374000,-0.204000, qreg_0[1])
subcirc1.u(0.326000,0.182000,-0.130000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(-0.881000,-0.615000,-0.315000, qreg_0[0])
subcirc2.cy(qreg_2[0],qreg_2[1])
subcirc2.u(-0.603000,0.510000,-0.423000, qreg_2[1])
subcirc2.u(-0.493000,-0.365000,0.177000, qreg_1[0])

main_circ = QuantumCircuit(1)
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

main_circ.append(subcirc2,[qreg_2[0],0,qreg_2[1],qreg_0[1]])
main_circ.u(pi/2,param_1,param_1, qreg_2[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_2[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cy(qreg_0[1],0)
		main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_2[1],0])
main_circ.u(pi/2,param_0,param_0, qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_2[1])
	main_circ.barrier(0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],qreg_0[0],0])
		with else_1:
			main_circ.s(0)
	with else_2:
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.u(param_1,0.577000,-0.155000, qreg_2[1])
			main_circ.s(qreg_0[0])
			main_circ.u(-0.862000,0.118000,0.844000, qreg_0[1])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_2[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.u(param_1,-0.362000,0.244000, qreg_2[0])
		main_circ.append(subcirc2,[qreg_2[1],qreg_0[1],qreg_0[0],qreg_2[0]])
	with else_2:
		main_circ.u(0.726000,-0.999000,0.107000, qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.append(subcirc2,[qreg_2[1],qreg_2[0],qreg_0[1],0])
with else_3:
	main_circ.measure(qreg_2[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.id(0)
	with else_2:
		main_circ.u(pi/2,param_0,param_2, qreg_0[1])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(pi/2,0.421000,param_0, 0)
			main_circ.cy(0,qreg_2[1])
		with else_1:
			main_circ.id(qreg_2[0])
	main_circ.measure(qreg_2[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(param_1,-0.753000,param_1, 0)
		with else_1:
			main_circ.u(param_1,param_1,param_0, 0)
			main_circ.cy(qreg_0[0],qreg_0[1])
			main_circ.cy(qreg_2[1],0)
			main_circ.cy(qreg_0[1],qreg_0[0])
			main_circ.cy(0,qreg_0[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(0,qreg_0[1])
				main_circ.cy(qreg_0[0],0)
				main_circ.cy(0,qreg_2[0])
				main_circ.u(param_1,-0.285000,param_1, qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc2,[qreg_0[0],0,qreg_2[0],qreg_0[1]])
				with case_1(1):
					main_circ.s(qreg_2[0])
					main_circ.u(0.046000,param_2,0.798000, qreg_2[1])
					main_circ.barrier(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(0)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_2[1])
				with case_1(1):
					main_circ.id(qreg_2[1])
			main_circ.id(0)
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_2[1])
			with else_1:
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_2[1])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_2[1])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_2[0])
			main_circ.id(qreg_2[0])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_2[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.barrier(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.id(qreg_2[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_2[1])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.barrier(qreg_2[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.barrier(qreg_2[0])
			with case_2(1):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(qreg_2[1])
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.id(0)
			with case_2(1):
				main_circ.id(qreg_0[1])
		main_circ.barrier(qreg_2[0])
bindings = {param_0: 0.651000, param_1: -0.873000, param_2: 0.198000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1742")
