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
subcirc0.s(qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.ry(0.432000, qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[3])
subcirc0.s(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.172000, qreg_3[0])
subcirc1.s(qreg_3[0])
subcirc1.u(0,0,0.848000, qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.s(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.s(qreg_1[1])
subcirc2.cy(qreg_1[1],qreg_1[0])
subcirc2.cy(qreg_0[0],qreg_1[2])
subcirc2.cy(qreg_0[0],qreg_1[1])
subcirc2.ry(-0.470000, qreg_1[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[0],qreg_0[1])
subcirc3.ry(-0.468000, qreg_0[0])
subcirc3.cy(qreg_0[3],qreg_0[2])
subcirc3.ry(-0.858000, qreg_0[2])
subcirc3.u(0,0,-0.974000, qreg_0[3])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cy(qreg_1[0],qreg_1[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_1[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_1[2])
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.s(qreg_1[2])
			main_circ.append(subcirc2,[qreg_1[0],qreg_0[0],qreg_1[2],0])
		with else_1:
			main_circ.cy(qreg_0[0],0)
			main_circ.s(qreg_1[0])
			main_circ.id(qreg_0[0])
	with else_2:
		main_circ.barrier(qreg_1[2])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_1[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.ry(param_2, qreg_1[1])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.cy(0,qreg_1[0])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cy(0,qreg_1[1])
			with else_1:
				main_circ.id(qreg_1[0])
			main_circ.append(subcirc2,[0,qreg_1[1],qreg_1[0],qreg_0[0]])
		with case_2(1):
			main_circ.append(subcirc3,[0,qreg_0[0],qreg_1[2],qreg_1[0],qreg_1[1]])
main_circ.measure(qreg_1[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc3,[qreg_1[0],qreg_1[1],0,qreg_1[2],qreg_0[0]])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_1[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc2,[qreg_1[0],0,qreg_0[0],qreg_1[1]])
			with else_1:
				main_circ.cy(qreg_1[0],0)
				main_circ.append(subcirc3,[qreg_1[0],qreg_1[1],qreg_0[0],0,qreg_1[2]])
		with else_2:
			main_circ.u(0,param_0,-0.533000, qreg_1[1])
			main_circ.id(qreg_0[0])
main_circ.measure(qreg_1[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_1[2])
				with case_1(1):
					main_circ.append(subcirc3,[qreg_1[0],qreg_1[2],0,qreg_1[1],qreg_0[0]])
	with case_3(1):
		main_circ.cy(qreg_1[0],qreg_1[2])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc2,[qreg_1[0],qreg_1[2],0,qreg_0[0]])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.id(qreg_1[0])
	with case_3(1):
		main_circ.measure(qreg_1[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.barrier(0)
			with case_2(1):
				main_circ.measure(qreg_1[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.cy(qreg_1[1],qreg_1[2])
						main_circ.barrier(qreg_1[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.id(qreg_1[2])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_1[2])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[1])
				main_circ.measure(qreg_1[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[1])
					with case_1(1):
						main_circ.barrier(qreg_1[1])
				main_circ.measure(qreg_1[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_1[2])
				main_circ.measure(qreg_1[2], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_1[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[2])
				main_circ.id(qreg_1[0])
			with case_2(1):
				main_circ.measure(qreg_1[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(0)
				main_circ.measure(qreg_1[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.id(qreg_1[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_1[2])
				with else_1:
					main_circ.barrier(0)
				main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_1[0])
bindings = {param_0: -0.651000, param_2: 0.851000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "874", "InverseCancellation")
