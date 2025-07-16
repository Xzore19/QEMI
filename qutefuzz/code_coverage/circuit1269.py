from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.s(qreg_0[0])
subcirc0.u(0,0,0.476000, qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_2[0])
subcirc0.cz(qreg_2[0],qreg_0[1])
subcirc0.u(0,0,-0.553000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.rx(-0.430000, qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.u(0,0,-0.505000, qreg_2[0])
subcirc1.u(0,0,-0.517000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.399000, qreg_0[1])
subcirc2.u(0,0,-0.536000, qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2.u(0,0,0.560000, qreg_0[0])
subcirc2.s(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(1)
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

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rx(-0.592000, 0)
				main_circ.u(0,param_1,param_3, 0)
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.rx(param_3, 0)
				main_circ.barrier(qreg_0[1])
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.rx(param_1, qreg_0[2])
				main_circ.u(param_2,0,0.142000, 0)
				main_circ.cz(qreg_0[3],qreg_0[2])
				main_circ.cz(qreg_0[2],qreg_0[1])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.id(qreg_0[3])
		with else_2:
			main_circ.u(param_4,0,param_4, qreg_0[1])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.rx(param_2, qreg_0[0])
			main_circ.u(param_2,param_0,param_0, qreg_0[2])
		with else_2:
			main_circ.s(qreg_0[3])
			main_circ.u(param_2,0,0.814000, qreg_0[0])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[1])
			with case_1(1):
				main_circ.cz(qreg_0[1],0)
				main_circ.cz(qreg_0[2],qreg_0[0])
				main_circ.rx(param_3, qreg_0[2])
				main_circ.id(0)
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(qreg_0[1],qreg_0[3])
			main_circ.rx(-0.464000, qreg_0[3])
			main_circ.cz(qreg_0[0],qreg_0[1])
			main_circ.rx(0.715000, 0)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(qreg_0[1])
			main_circ.id(qreg_0[0])
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0,0,param_4, 0)
			main_circ.s(qreg_0[3])
			main_circ.cz(qreg_0[0],qreg_0[1])
			main_circ.rx(-0.754000, 0)
			main_circ.barrier(qreg_0[1])
		with else_1:
			main_circ.cz(0,qreg_0[1])
			main_circ.id(qreg_0[0])
	with else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.s(0)
				main_circ.id(qreg_0[2])
			with case_1(1):
				main_circ.id(qreg_0[3])
with else_3:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(0,qreg_0[2])
				main_circ.cz(qreg_0[1],qreg_0[3])
				main_circ.id(qreg_0[2])
			with case_1(1):
				main_circ.barrier(qreg_0[2])
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[1])
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.rx(param_0, qreg_0[1])
				main_circ.id(qreg_0[2])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.cz(qreg_0[1],qreg_0[3])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0,0,param_4, qreg_0[3])
			main_circ.u(0,param_2,param_4, qreg_0[2])
			main_circ.rx(param_4, qreg_0[0])
			main_circ.barrier(qreg_0[2])
	with else_2:
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_0[2],qreg_0[1])
				main_circ.u(0,param_1,param_0, qreg_0[3])
				main_circ.barrier(qreg_0[3])
			with case_1(1):
				main_circ.s(qreg_0[2])
				main_circ.s(qreg_0[3])
				main_circ.id(0)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.s(qreg_0[0])
						main_circ.s(qreg_0[0])
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cz(qreg_0[3],qreg_0[2])
					main_circ.rx(0.184000, qreg_0[0])
					main_circ.cz(0,qreg_0[0])
					main_circ.cz(qreg_0[2],qreg_0[1])
					main_circ.cz(qreg_0[1],qreg_0[2])
			with case_2(1):
				main_circ.cz(qreg_0[0],qreg_0[2])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cz(qreg_0[2],qreg_0[0])
						main_circ.id(qreg_0[2])
					with case_1(1):
						main_circ.s(qreg_0[3])
						main_circ.s(qreg_0[0])
						main_circ.rx(0.414000, qreg_0[0])
						main_circ.rx(param_2, qreg_0[0])
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.rx(0.657000, qreg_0[1])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.rx(param_3, qreg_0[1])
					main_circ.cz(qreg_0[3],qreg_0[0])
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.rx(param_1, qreg_0[2])
						main_circ.u(0,0,0.119000, qreg_0[0])
						main_circ.rx(0.145000, qreg_0[0])
						main_circ.s(0)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(qreg_0[2])
						main_circ.cz(qreg_0[2],0)
						main_circ.s(0)
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_0[1])
bindings = {param_0: -0.082000, param_1: -0.538000, param_2: 0.025000, param_3: -0.719000, param_4: 0.478000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1269")
