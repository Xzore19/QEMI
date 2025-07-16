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
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_3[0])
subcirc0.u(pi/2,0.819000,0.046000, qreg_0[1])
subcirc0.y(qreg_3[0])
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,-0.995000,-0.598000, qreg_2[0])
subcirc1.cx(qreg_2[1],qreg_2[0])
subcirc1.y(qreg_2[0])
subcirc1.u(0.441000,-0.181000,-0.600000, qreg_1[0])
subcirc1.y(qreg_2[1])
subcirc1.u(pi/2,0.065000,-0.461000, qreg_1[0])

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

main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.y(qreg_0[0])
				main_circ.y(qreg_0[3])
				main_circ.cx(qreg_0[1],qreg_0[2])
				main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
			with else_1:
				main_circ.u(param_3,param_4,param_1, qreg_0[3])
				main_circ.y(qreg_0[1])
				main_circ.u(-0.422000,-0.930000,0.757000, qreg_0[1])
				main_circ.y(qreg_0[0])
				main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
		with else_2:
			main_circ.u(param_5,-0.808000,param_0, qreg_0[2])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(param_0,param_4,0.161000, qreg_0[2])
				main_circ.y(qreg_0[3])
			with else_1:
				main_circ.u(param_3,param_6,param_6, qreg_0[0])
				main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.u(pi/2,-0.745000,-0.187000, qreg_0[1])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_0[3]])
		with else_1:
			main_circ.cx(qreg_0[3],qreg_0[0])
			main_circ.cx(qreg_0[1],qreg_0[2])
			main_circ.cx(qreg_0[0],qreg_0[3])
			main_circ.u(param_1,param_6,-0.139000, qreg_0[2])
	with else_2:
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cx(qreg_0[0],qreg_0[2])
		with else_1:
			main_circ.cx(qreg_0[1],qreg_0[2])
			main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
with else_3:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cx(qreg_0[0],qreg_0[1])
			main_circ.barrier(qreg_0[0])
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.u(param_1,0.733000,param_4, qreg_0[1])
					main_circ.u(param_6,-0.147000,0.521000, qreg_0[3])
					main_circ.y(qreg_0[3])
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.id(qreg_0[3])
			main_circ.barrier(qreg_0[0])
		with case_2(1):
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.823000, param_1: 0.546000, param_3: -0.119000, param_4: 0.564000, param_5: 0.158000, param_6: -0.628000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1722", "NormalizeRXAngle")
