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
subcirc0.y(qreg_0[2])
subcirc0.s(qreg_3[0])
subcirc0.y(qreg_0[2])
subcirc0.u(pi/2,-0.616000,0.206000, qreg_0[0])
subcirc0.u(pi/2,-0.700000,0.400000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_3[0])
subcirc1.s(qreg_1[1])
subcirc1.y(qreg_3[0])
subcirc1.y(qreg_3[0])
subcirc1.u(pi/2,0.194000,0.789000, qreg_0[0])

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

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.cz(qreg_0[0],0)
							main_circ.y(qreg_2[0])
							main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_2[1],0])
					with case_2(1):
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.append(subcirc1,[qreg_0[1],qreg_2[1],qreg_2[0],0])
						with else_1:
							main_circ.s(0)
							main_circ.y(qreg_2[1])
							main_circ.cz(qreg_0[1],0)
			with case_3(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.s(0)
							main_circ.cz(qreg_2[0],qreg_0[1])
							main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[0],0,qreg_2[1]])
						with case_1(1):
							main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[0],qreg_2[0]])
				with else_2:
					main_circ.s(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],qreg_0[1],0,qreg_0[0]])
					with else_1:
						main_circ.cz(0,qreg_2[1])
						main_circ.cz(qreg_2[1],qreg_2[0])
	with case_4(1):
		main_circ.cz(qreg_0[1],qreg_0[0])
		main_circ.cz(qreg_0[0],qreg_2[1])
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.cz(qreg_0[1],qreg_2[0])
							main_circ.cz(qreg_0[1],0)
							main_circ.cz(qreg_0[1],0)
							main_circ.cz(qreg_0[1],qreg_0[0])
						with else_1:
							main_circ.cz(0,qreg_0[1])
							main_circ.cz(qreg_2[1],qreg_0[0])
							main_circ.y(qreg_0[0])
							main_circ.barrier(qreg_0[0])
					with case_2(1):
						main_circ.measure(0, creg_0[0])
						with main_circ.if_test((creg_0[0],0)) as else_1:
							main_circ.id(qreg_0[1])
						with else_1:
							main_circ.barrier(qreg_0[0])
						main_circ.measure(qreg_2[1], creg_0[1])
						with main_circ.if_test((creg_0[1],0)) as else_1:
							main_circ.barrier(qreg_2[0])
						with else_1:
							main_circ.id(qreg_2[1])
						main_circ.measure(qreg_0[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.barrier(qreg_0[1])
						main_circ.id(qreg_2[1])
			with case_3(1):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[1])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(0)
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.barrier(qreg_0[0])
				with else_2:
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(0)
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[1])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_0[1])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1499")
