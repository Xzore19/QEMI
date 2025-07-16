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
subcirc0.u(0.062000,-0.637000,0.387000, qreg_0[2])
subcirc0.u(0,0,-0.251000, qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0.x(qreg_0[3])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0.917000,-0.999000,0.560000, qreg_0[1])
subcirc1.u(0,0,0.314000, qreg_0[1])
subcirc1.x(qreg_2[0])
subcirc1.rx(-0.195000, qreg_0[0])
subcirc1.u(0.009000,0.715000,0.442000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.555000, qreg_3[0])
subcirc2.x(qreg_3[0])
subcirc2.u(0,0,-0.846000, qreg_0[0])
subcirc2.u(-0.342000,0.617000,-0.016000, qreg_0[1])
subcirc2.u(-0.126000,-0.379000,-0.880000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0.773000,-0.623000,-0.455000, qreg_0[0])
subcirc3.rx(-0.886000, qreg_0[2])
subcirc3.u(0,0,-0.234000, qreg_0[1])
subcirc3.rx(-0.839000, qreg_0[0])
subcirc3.rx(-0.002000, qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.x(qreg_0[3])
subcirc4.rx(0.051000, qreg_0[0])
subcirc4.x(qreg_0[0])
subcirc4.u(0,0,0.744000, qreg_0[0])
subcirc4.u(0,0,0.725000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(1)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.x(1)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.append(subcirc1,[1,qreg_0[0],0,2])
			with else_1:
				main_circ.u(0,param_4,param_3, 1)
				main_circ.append(subcirc3,[0,1,2,3])
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc4,[2,qreg_0[0],0,3])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.rx(0.979000, qreg_0[0])
					main_circ.append(subcirc1,[1,0,3,qreg_0[0]])
				with else_1:
					main_circ.rx(0.032000, qreg_0[0])
					main_circ.x(qreg_0[0])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(3)
					with case_1(1):
						main_circ.rx(-0.060000, 3)
						main_circ.rx(param_3, 2)
						main_circ.id(2)
				main_circ.u(param_0,0,0.771000, qreg_0[0])
				main_circ.append(subcirc1,[1,3,2,qreg_0[0]])
main_circ.u(param_5,param_0,param_2, 1)
main_circ.u(0.953000,param_5,0.010000, 1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(-0.942000,param_3,param_1, 3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.append(subcirc4,[3,0,2,qreg_0[0]])
		with else_1:
			main_circ.id(0)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc3,[0,qreg_0[0],2,3])
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.append(subcirc1,[2,3,1,0])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.x(3)
			main_circ.rx(-0.669000, 2)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.u(0,0,-0.667000, qreg_0[0])
			main_circ.barrier(3)
bindings = {param_0: -0.027000, param_1: -0.878000, param_2: 0.993000, param_3: 0.736000, param_4: -0.461000, param_5: 0.375000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1254")
