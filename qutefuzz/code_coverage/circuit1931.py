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
subcirc0.rx(0.102000, qreg_1[1])
subcirc0.rx(0.087000, qreg_1[1])
subcirc0.u(0.194000,-0.588000,-0.643000, qreg_1[0])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.739000, qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.rx(0.920000, qreg_0[1])
subcirc1.u(0.880000,-0.054000,0.104000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0.104000,0.054000,0.649000, qreg_1[1])
subcirc2.rx(0.866000, qreg_1[0])
subcirc2.rz(-0.909000, qreg_1[1])
subcirc2.rx(0.294000, qreg_1[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.545000, qreg_0[0])
subcirc3.rx(0.279000, qreg_1[1])
subcirc3.rx(0.707000, qreg_1[0])
subcirc3.y(qreg_1[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(-0.889000, qreg_1[0])
subcirc4.y(qreg_3[0])
subcirc4.rz(-0.897000, qreg_1[1])
subcirc4.u(-0.789000,-0.081000,0.320000, qreg_1[0])
subcirc4 = subcirc4.to_gate().control(2)

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

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.append(subcirc4,[0,qreg_1[0],2,3,1,qreg_0[0]])
		with else_2:
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rz(0.911000, 2)
					main_circ.y(0)
					main_circ.append(subcirc4,[qreg_1[0],qreg_0[0],2,0,1,3])
				with case_1(1):
					main_circ.append(subcirc4,[0,qreg_0[0],qreg_1[0],2,3,1])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(-0.604000,-0.391000,param_0, qreg_0[0])
						main_circ.append(subcirc4,[qreg_0[0],qreg_1[0],0,3,2,1])
					with case_1(1):
						main_circ.u(param_1,0.795000,param_3, 3)
						main_circ.rz(param_2, 1)
						main_circ.u(-0.307000,-0.287000,param_3, qreg_1[0])
						main_circ.append(subcirc0,[2,qreg_1[0],3,0,1,qreg_0[0]])
		with else_3:
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(2)
						with case_1(1):
							main_circ.rz(-0.080000, 3)
							main_circ.append(subcirc3,[1,qreg_0[0],2,3,0])
				with case_2(1):
					main_circ.append(subcirc0,[1,qreg_0[0],3,2,0,qreg_1[0]])
	with case_4(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.rx(0.545000, 0)
						main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],0,1,2,3])
				with else_2:
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.append(subcirc4,[0,1,qreg_0[0],2,3,qreg_1[0]])
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],1,0,2])
					with else_1:
						main_circ.y(2)
						main_circ.barrier(qreg_1[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.id(1)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(2)
			main_circ.barrier(2)
		main_circ.rz(param_2, 0)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.barrier(0)
		with else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.y(3)
				main_circ.barrier(qreg_1[0])
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(0)
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.barrier(1)
	with else_3:
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_1[0])
			main_circ.id(3)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.barrier(1)
		with else_2:
			main_circ.id(0)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(3)
			main_circ.barrier(qreg_1[0])
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.barrier(0)
			with case_2(1):
				main_circ.id(1)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(3)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(1)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.barrier(qreg_1[0])
			with case_2(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.barrier(2)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.barrier(3)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_1[0])
			main_circ.barrier(2)
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_1[0])
			with else_1:
				main_circ.id(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(0)
			main_circ.id(1)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.barrier(2)
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(1)
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(1)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(1)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(3)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(2)
					with case_1(1):
						main_circ.barrier(qreg_1[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.id(qreg_0[0])
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(2)
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.id(2)
			main_circ.id(3)
		with else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.id(qreg_1[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_1[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(2)
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_1[0])
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.id(1)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(1)
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(2)
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.id(0)
		with else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_1[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.id(2)
		main_circ.barrier(2)
bindings = {param_0: 0.943000, param_1: 0.900000, param_2: 0.491000, param_3: -0.305000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1931")
