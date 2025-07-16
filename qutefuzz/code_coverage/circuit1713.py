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
subcirc0.z(qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.rz(-0.257000, qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.rz(param_3, qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_1[1],qreg_3[0]])
with else_3:
	main_circ.append(subcirc0,[qreg_0[0],qreg_1[1],qreg_3[0],qreg_1[0]])
main_circ.cy(qreg_3[0],qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_3[0])
	main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cy(qreg_0[0],qreg_3[0])
				main_circ.z(qreg_0[0])
				main_circ.y(qreg_3[0])
				main_circ.cy(qreg_3[0],qreg_0[0])
			with case_1(1):
				main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_3[0],qreg_1[1]])
	with else_2:
		main_circ.rz(0.255000, qreg_1[1])
		main_circ.y(qreg_1[1])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rz(param_1, qreg_3[0])
					main_circ.z(qreg_1[1])
					main_circ.y(qreg_1[1])
					main_circ.y(qreg_1[0])
				with case_1(1):
					main_circ.cy(qreg_1[1],qreg_1[0])
					main_circ.z(qreg_1[0])
					main_circ.y(qreg_0[0])
					main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],qreg_3[0],qreg_1[1]])
		with case_2(1):
			main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],qreg_0[0],qreg_3[0]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.z(qreg_0[0])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.rz(-0.854000, qreg_1[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(qreg_0[0],qreg_1[1])
				main_circ.cy(qreg_1[0],qreg_0[0])
				main_circ.y(qreg_3[0])
				main_circ.y(qreg_1[0])
			with else_1:
				main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_0[0],qreg_1[0]])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.z(qreg_0[0])
				main_circ.y(qreg_1[0])
			with else_1:
				main_circ.y(qreg_3[0])
				main_circ.cy(qreg_3[0],qreg_1[0])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_1[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rz(0.742000, qreg_1[0])
					main_circ.rz(param_4, qreg_1[0])
					main_circ.cy(qreg_3[0],qreg_1[1])
					main_circ.cy(qreg_0[0],qreg_3[0])
				with case_1(1):
					main_circ.z(qreg_1[1])
					main_circ.cy(qreg_0[0],qreg_3[0])
					main_circ.barrier(qreg_3[0])
bindings = {param_1: 0.949000, param_3: -0.868000, param_4: 0.353000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1713")
