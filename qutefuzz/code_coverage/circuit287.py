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
subcirc0.h(qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.ry(-0.856000, qreg_2[0])
subcirc0.s(qreg_3[0])
subcirc0.s(qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.h(qreg_2[1])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.ry(-0.393000, qreg_2[1])
subcirc1.s(qreg_0[1])
subcirc1.s(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[1])
subcirc2.ry(-0.110000, qreg_0[0])
subcirc2.s(qreg_0[1])
subcirc2.ry(0.398000, qreg_0[3])
subcirc2.ry(-0.599000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[0])
subcirc3.cx(qreg_0[1],qreg_0[0])
subcirc3.cx(qreg_0[2],qreg_0[1])
subcirc3.ry(-0.797000, qreg_3[0])
subcirc3.ry(0.817000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.h(3)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.append(subcirc1,[2,qreg_1[0],qreg_0[0],1])
		with else_3:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.h(3)
						main_circ.s(qreg_1[0])
						main_circ.ry(param_4, 3)
						main_circ.h(qreg_1[0])
					with case_1(1):
						main_circ.append(subcirc3,[1,3,2,qreg_1[0]])
	with case_4(1):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.ry(-0.247000, qreg_1[0])
						main_circ.ry(param_4, 0)
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],1,2,3,0])
					with else_1:
						main_circ.cx(qreg_1[0],3)
						main_circ.h(2)
						main_circ.s(1)
						main_circ.h(qreg_0[0])
				with case_2(1):
					main_circ.append(subcirc0,[qreg_0[0],0,2,1,qreg_1[0],3])
		with else_3:
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.h(0)
						main_circ.ry(param_1, 3)
						main_circ.cx(qreg_1[0],3)
						main_circ.cx(1,2)
					with else_1:
						main_circ.cx(qreg_1[0],qreg_0[0])
				with case_2(1):
					main_circ.measure(1, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.cx(qreg_0[0],qreg_1[0])
							main_circ.cx(3,1)
							main_circ.cx(qreg_0[0],2)
							main_circ.cx(qreg_0[0],2)
						with case_1(1):
							main_circ.append(subcirc3,[2,3,qreg_1[0],0])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(2)
				main_circ.h(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(2)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(3)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(3)
				main_circ.id(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_1[0])
			with case_2(1):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(3)
				main_circ.barrier(2)
		main_circ.barrier(1)
bindings = {param_1: 0.099000, param_4: 0.011000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "287")
