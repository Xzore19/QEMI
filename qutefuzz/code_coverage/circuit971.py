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
subcirc0.y(qreg_1[0])
subcirc0.ry(-0.596000, qreg_3[0])
subcirc0.y(qreg_3[0])
subcirc0.u(pi/2,0.900000,-0.878000, qreg_0[0])
subcirc0.s(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.s(2)
					main_circ.ry(param_3, qreg_0[0])
					main_circ.ry(param_2, 3)
					main_circ.ry(0.083000, qreg_0[0])
				with case_1(1):
					main_circ.s(2)
					main_circ.y(qreg_0[0])
					main_circ.s(1)
					main_circ.append(subcirc0,[qreg_1[0],3,1,2,qreg_0[0],0])
		with else_2:
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.y(0)
				main_circ.s(1)
				main_circ.y(qreg_0[0])
				main_circ.u(param_0,param_0,-0.150000, 0)
				main_circ.y(1)
			with else_1:
				main_circ.ry(-0.931000, 0)
				main_circ.s(3)
				main_circ.u(param_0,param_3,0.786000, 2)
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(param_2,-0.653000,-0.692000, 3)
				main_circ.ry(0.966000, 1)
			with else_1:
				main_circ.s(3)
				main_circ.append(subcirc0,[2,1,3,qreg_1[0],qreg_0[0],0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc0,[1,qreg_0[0],2,qreg_1[0],3,0])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.y(0)
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.ry(-0.900000, qreg_1[0])
					main_circ.s(qreg_1[0])
					main_circ.append(subcirc0,[0,1,3,qreg_0[0],2,qreg_1[0]])
				with case_1(1):
					main_circ.u(param_0,0.860000,0.525000, 3)
					main_circ.append(subcirc0,[1,2,qreg_0[0],3,0,qreg_1[0]])
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.s(2)
			with else_1:
				main_circ.ry(0.091000, 3)
				main_circ.s(2)
			main_circ.append(subcirc0,[qreg_1[0],0,2,3,qreg_0[0],1])
with else_3:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_1,param_1,param_0, 2)
				main_circ.s(qreg_0[0])
				main_circ.y(qreg_0[0])
				main_circ.ry(0.847000, qreg_1[0])
		with case_2(1):
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_1[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_1[0])
			with else_1:
				main_circ.id(qreg_1[0])
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(3)
				with case_1(1):
					main_circ.id(qreg_1[0])
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_1[0])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.id(2)
bindings = {param_0: 0.517000, param_1: 0.090000, param_2: 0.316000, param_3: -0.636000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "971")
