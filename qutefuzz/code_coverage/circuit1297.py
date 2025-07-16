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
subcirc0.rx(0.306000, qreg_0[2])
subcirc0.y(qreg_0[1])
subcirc0.s(qreg_0[2])
subcirc0.rx(0.389000, qreg_0[0])
subcirc0.rx(-0.394000, qreg_3[0])
subcirc0.y(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.rx(-0.934000, qreg_0[0])
subcirc1.s(qreg_0[3])
subcirc1.s(qreg_0[1])
subcirc1.rx(-0.013000, qreg_0[3])
subcirc1.s(qreg_0[3])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,0.154000,0.652000, qreg_0[1])
subcirc2.rx(0.798000, qreg_0[1])
subcirc2.u(pi/2,0.707000,0.669000, qreg_0[3])
subcirc2.rx(0.081000, qreg_0[2])
subcirc2.rx(0.938000, qreg_0[0])
subcirc2.rx(-0.531000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,0.451000,-0.478000, qreg_0[3])
subcirc3.s(qreg_0[0])
subcirc3.rx(-0.906000, qreg_0[3])
subcirc3.s(qreg_0[3])
subcirc3.y(qreg_0[0])
subcirc3.y(qreg_0[3])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.s(qreg_0[0])
subcirc4.rx(-0.726000, qreg_1[2])
subcirc4.u(pi/2,0.030000,0.805000, qreg_1[1])
subcirc4.rx(0.218000, qreg_1[2])
subcirc4.s(qreg_0[0])
subcirc4.rx(0.612000, qreg_0[0])

main_circ = QuantumCircuit(0)
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
param_3 = Parameter("param_3")

main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.append(subcirc4,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_2[1]])
with else_4:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.y(qreg_0[0])
					main_circ.id(qreg_0[0])
				main_circ.s(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.s(qreg_0[1])
						main_circ.s(qreg_0[0])
						main_circ.s(qreg_2[1])
						main_circ.append(subcirc4,[qreg_0[0],qreg_2[1],qreg_0[1],qreg_2[0]])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.rx(param_2, qreg_0[1])
						main_circ.u(pi/2,param_3,param_2, qreg_2[1])
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.append(subcirc4,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
			with else_2:
				main_circ.barrier(qreg_2[1])
main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_3:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.u(param_3,0.794000,-0.075000, qreg_2[0])
							main_circ.u(pi/2,param_1,param_2, qreg_2[0])
							main_circ.s(qreg_2[0])
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.y(qreg_2[0])
							main_circ.id(qreg_2[0])
				with case_2(1):
					main_circ.id(qreg_2[0])
		with else_3:
			main_circ.measure(qreg_2[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.s(qreg_0[0])
						main_circ.rx(0.270000, qreg_0[1])
						main_circ.u(param_3,0.906000,param_2, qreg_0[1])
						main_circ.u(param_2,-0.471000,param_3, qreg_0[1])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(param_1, qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.rx(param_1, qreg_2[0])
				with else_1:
					main_circ.append(subcirc4,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_2[1]])
	with case_4(1):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_2[0])
		main_circ.u(param_3,param_2,param_3, qreg_2[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.u(param_2,0.327000,0.124000, qreg_2[1])
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.y(qreg_2[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_2[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_1, qreg_2[0])
main_circ.u(param_0,param_3,-0.707000, qreg_0[1])
main_circ.append(subcirc4,[qreg_0[1],qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.append(subcirc4,[qreg_2[1],qreg_0[0],qreg_0[1],qreg_2[0]])
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.id(qreg_0[1])
	with else_3:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.id(qreg_2[1])
			main_circ.id(qreg_2[1])
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_2[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.id(qreg_2[1])
			with case_2(1):
				main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.792000, param_1: -0.049000, param_2: -0.642000, param_3: -0.422000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1297")
