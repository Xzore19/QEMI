from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rz(0.577000, qreg_2[0])
subcirc0.u(-0.260000,-0.946000,-0.658000, qreg_3[0])
subcirc0.u(0.340000,-0.878000,-0.435000, qreg_0[0])
subcirc0.u(0.572000,-0.195000,0.827000, qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.418000,-0.536000,0.255000, qreg_0[0])
subcirc1.z(qreg_3[0])
subcirc1.u(0.372000,0.483000,0.082000, qreg_0[1])
subcirc1.z(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.z(qreg_0[3])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_0[2])
subcirc2.z(qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rz(0.522000, qreg_0[0])
subcirc3.u(-0.411000,0.046000,0.304000, qreg_2[1])
subcirc3.u(pi/2,0.957000,-0.410000, qreg_2[1])
subcirc3.rz(-0.232000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

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

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(2)
			with else_1:
				main_circ.u(pi/2,param_4,param_1, 0)
				main_circ.rz(param_0, 0)
				main_circ.append(subcirc1,[2,0,3,1,qreg_0[0]])
main_circ.u(param_4,param_4,param_5, 1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.id(0)
				with case_2(1):
					main_circ.rz(-0.113000, 2)
					main_circ.append(subcirc1,[qreg_0[0],0,1,3,2])
		with case_3(1):
			main_circ.append(subcirc0,[qreg_0[0],3,0,2])
with else_4:
	main_circ.u(pi/2,param_2,param_2, 0)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.id(qreg_0[0])
	with else_3:
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.id(2)
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc2,[2,3,1,qreg_0[0]])
			with else_1:
				main_circ.append(subcirc2,[1,3,0,2])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.z(2)
with else_4:
	main_circ.z(1)
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc1,[1,3,qreg_0[0],2,0])
					with case_1(1):
						main_circ.u(param_0,0.490000,-0.317000, 1)
						main_circ.append(subcirc1,[qreg_0[0],3,2,0,1])
			with else_2:
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.u(0.456000,param_2,param_4, qreg_0[0])
						main_circ.append(subcirc2,[0,2,1,qreg_0[0]])
					with case_1(1):
						main_circ.rz(-0.443000, 3)
						main_circ.append(subcirc0,[3,1,0,qreg_0[0]])
		with case_3(1):
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.append(subcirc0,[qreg_0[0],0,1,3])
					main_circ.u(pi/2,-0.108000,param_2, 0)
main_circ.u(0.108000,0.776000,param_5, 1)
main_circ.u(param_4,param_4,-0.753000, 2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.z(0)
				main_circ.rz(param_5, 3)
				main_circ.append(subcirc2,[1,2,3,0])
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.id(qreg_0[0])
	with else_3:
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.id(0)
			with case_2(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(0)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.barrier(0)
		main_circ.barrier(2)
bindings = {param_0: 0.242000, param_1: 0.827000, param_2: 0.899000, param_4: -0.731000, param_5: -0.747000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1433", "ElidePermutations")
