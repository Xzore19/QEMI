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
subcirc0.u(0,0,0.780000, qreg_3[0])
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.ry(-0.232000, qreg_0[0])
subcirc0.cz(qreg_3[0],qreg_0[2])
subcirc0.cz(qreg_3[0],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rz(-0.651000, qreg_0[1])
subcirc1.ry(0.732000, qreg_0[0])
subcirc1.cz(qreg_2[0],qreg_2[1])
subcirc1.u(0,0,-0.374000, qreg_2[1])
subcirc1.u(0,0,-0.695000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_1[0],qreg_2[0])
subcirc2.ry(0.724000, qreg_0[0])
subcirc2.u(0,0,0.316000, qreg_0[0])
subcirc2.cz(qreg_1[0],qreg_3[0])
subcirc2.u(0,0,-0.709000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0,0,0.069000, qreg_0[3])
subcirc3.rz(0.390000, qreg_0[3])
subcirc3.cz(qreg_0[3],qreg_0[1])
subcirc3.ry(-0.046000, qreg_0[2])
subcirc3.rz(-0.110000, qreg_0[3])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(-0.420000, qreg_0[2])
subcirc4.rz(0.954000, qreg_0[2])
subcirc4.cz(qreg_0[0],qreg_3[0])
subcirc4.rz(-0.506000, qreg_0[0])
subcirc4.ry(-0.449000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc3,[1,qreg_0[0],3,qreg_1[0],2])
					with case_1(1):
						main_circ.ry(0.638000, 2)
						main_circ.rz(-0.635000, 2)
						main_circ.append(subcirc3,[0,1,qreg_1[0],2,3])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.append(subcirc0,[3,2,qreg_0[0],0])
				with else_1:
					main_circ.ry(-0.628000, 2)
					main_circ.append(subcirc4,[3,0,1,qreg_0[0],2])
		with else_3:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.append(subcirc2,[qreg_1[0],1,qreg_0[0],0])
					with else_1:
						main_circ.append(subcirc1,[qreg_0[0],3,2,0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.u(param_1,0,param_0, qreg_1[0])
						main_circ.append(subcirc0,[0,3,qreg_0[0],qreg_1[0]])
	with case_4(1):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cz(1,0)
					main_circ.cz(2,0)
		with else_3:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.cz(2,1)
					main_circ.rz(0.284000, qreg_1[0])
					main_circ.append(subcirc1,[0,2,1,qreg_0[0]])
				with else_1:
					main_circ.u(0,0,0.494000, 3)
			with else_2:
				main_circ.barrier(1)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rz(param_1, 2)
				main_circ.barrier(1)
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cz(1,qreg_0[0])
				main_circ.cz(1,qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
		with else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(3)
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.id(0)
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(0)
			main_circ.barrier(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.id(3)
		with else_2:
			main_circ.id(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.id(2)
		main_circ.barrier(qreg_0[0])
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.barrier(qreg_1[0])
		with case_3(1):
			main_circ.id(0)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(3)
				with case_1(1):
					main_circ.id(2)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.id(1)
		with else_2:
			main_circ.barrier(0)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(3)
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.id(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(3)
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(3)
			main_circ.barrier(3)
		with else_2:
			main_circ.id(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(3)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(1)
				main_circ.barrier(3)
		main_circ.barrier(1)
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(2)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.barrier(1)
			with case_2(1):
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(2)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_1[0])
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(3)
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(2)
				with else_1:
					main_circ.barrier(0)
				main_circ.barrier(3)
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(2)
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.id(0)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(2)
				main_circ.id(qreg_1[0])
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.id(3)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(3)
		main_circ.barrier(0)
	with else_3:
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(3)
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.barrier(1)
		with case_3(1):
			main_circ.barrier(qreg_1[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.id(0)
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.barrier(3)
			with case_2(1):
				main_circ.id(qreg_1[0])
		main_circ.id(qreg_0[0])
	with else_3:
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(2)
				main_circ.barrier(qreg_1[0])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.id(3)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(1)
				main_circ.barrier(1)
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.barrier(1)
			main_circ.barrier(0)
		with else_2:
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(2)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_1[0])
				with case_1(1):
					main_circ.barrier(3)
			main_circ.id(0)
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(2)
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(1)
			main_circ.id(2)
		main_circ.barrier(1)
	main_circ.barrier(qreg_1[0])
bindings = {param_0: -0.228000, param_1: 0.155000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1988", "ElidePermutations")
