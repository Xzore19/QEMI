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
subcirc0.rx(0.813000, qreg_0[2])
subcirc0.rx(0.567000, qreg_0[3])
subcirc0.y(qreg_0[3])
subcirc0.u(0,0,0.527000, qreg_0[0])
subcirc0.y(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.617000, qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.u(0.022000,0.358000,0.461000, qreg_0[1])
subcirc1.u(0.212000,0.561000,0.912000, qreg_2[0])
subcirc1.u(0.836000,-0.714000,-0.840000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.535000,0.752000,0.982000, qreg_0[1])
subcirc2.y(qreg_3[0])
subcirc2.rx(0.197000, qreg_0[1])
subcirc2.rx(-0.762000, qreg_0[1])
subcirc2.u(0,0,0.658000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(-0.625000, qreg_1[0])
subcirc3.u(-0.979000,-0.445000,-0.230000, qreg_1[1])
subcirc3.u(0,0,0.293000, qreg_0[0])
subcirc3.y(qreg_1[1])
subcirc3.y(qreg_1[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.y(qreg_0[3])
subcirc4.u(-0.085000,0.602000,0.528000, qreg_0[0])
subcirc4.y(qreg_0[0])
subcirc4.u(0.117000,-0.019000,0.773000, qreg_0[2])
subcirc4.y(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_0,0,0.693000, qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(param_0,0,param_0, qreg_0[0])
		main_circ.rx(param_1, qreg_0[0])
		main_circ.rx(0.417000, 2)
		main_circ.id(0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_0,0,-0.252000, 2)
			main_circ.id(1)
		with case_1(1):
			main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],2,1])
with else_2:
	main_circ.append(subcirc2,[3,qreg_0[1],1,0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(param_1,param_1,-0.699000, 2)
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.append(subcirc1,[qreg_0[1],0,1,2,qreg_0[0]])
with else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.y(3)
			main_circ.u(0,0,param_0, 3)
			main_circ.u(param_0,param_1,param_1, qreg_0[1])
			main_circ.y(qreg_0[0])
		with case_1(1):
			main_circ.barrier(2)
	main_circ.append(subcirc0,[3,0,2,qreg_0[0]])
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rx(-0.342000, 2)
			main_circ.rx(param_0, qreg_0[0])
			main_circ.u(param_0,param_0,-0.453000, 0)
			main_circ.u(param_1,param_1,-0.193000, qreg_0[1])
		with else_1:
			main_circ.id(2)
	with case_2(1):
		main_circ.y(qreg_0[0])
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(-0.287000,param_1,param_1, 0)
			main_circ.append(subcirc1,[qreg_0[1],3,0,1,2])
		with else_1:
			main_circ.u(0,0,0.013000, qreg_0[0])
			main_circ.u(param_0,param_1,0.751000, 1)
			main_circ.append(subcirc0,[qreg_0[0],0,3,2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc4,[0,3,qreg_0[0],2])
		with case_1(1):
			main_circ.y(3)
			main_circ.barrier(3)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.id(2)
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.rx(param_0, 2)
		main_circ.barrier(3)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(2)
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(3)
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.id(1)
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(2)
	main_circ.y(qreg_0[1])
with else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(0,0,-0.331000, 1)
	with else_1:
		main_circ.barrier(2)
bindings = {param_0: -0.288000, param_1: -0.575000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "669")
