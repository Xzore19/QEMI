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
subcirc0.z(qreg_0[0])
subcirc0.s(qreg_3[0])
subcirc0.u(0,0,-0.835000, qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0.u(0,0,0.653000, qreg_0[0])
subcirc0.u(0,0,0.903000, qreg_0[0])

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

main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(0,param_1,0.215000, 3)
		main_circ.u(param_2,param_2,param_0, 3)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[3,1,qreg_0[0],2])
			with case_1(1):
				main_circ.s(3)
				main_circ.ry(param_1, 0)
				main_circ.u(0,0,0.121000, 1)
				main_circ.s(qreg_1[0])
	with case_2(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.s(2)
			main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],3,2])
		with else_1:
			main_circ.s(1)
			main_circ.z(2)
main_circ.ry(param_1, 0)
main_circ.z(qreg_1[0])
main_circ.s(3)
main_circ.ry(-0.704000, 3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.ry(0.682000, qreg_0[0])
			main_circ.u(0,param_1,0.718000, 3)
			main_circ.s(1)
			main_circ.z(1)
		with case_1(1):
			main_circ.append(subcirc0,[2,qreg_1[0],1,qreg_0[0]])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(0,0,param_2, 1)
		main_circ.s(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.z(3)
				main_circ.ry(-0.228000, 3)
				main_circ.u(param_0,param_0,param_1, qreg_1[0])
				main_circ.ry(param_0, qreg_0[0])
			with case_1(1):
				main_circ.s(0)
				main_circ.append(subcirc0,[2,qreg_1[0],1,0])
	with case_2(1):
		main_circ.z(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[qreg_0[0],2,1,qreg_1[0]])
			with case_1(1):
				main_circ.s(3)
				main_circ.barrier(3)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.s(qreg_1[0])
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.id(2)
with else_2:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.barrier(2)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(1)
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.barrier(2)
	main_circ.id(qreg_0[0])
bindings = {param_0: 0.676000, param_1: 0.905000, param_2: 0.287000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1154")
