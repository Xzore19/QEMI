from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.u(0,0,0.001000, qreg_1[0])
subcirc0.y(qreg_1[2])
subcirc0.u(0,0,0.477000, qreg_1[1])
subcirc0.y(qreg_1[0])
subcirc0.rz(0.496000, qreg_1[2])
subcirc0.rz(-0.779000, qreg_1[1])

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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.u(param_2,param_0,-0.151000, qreg_0[0])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.y(qreg_2[1])
			main_circ.y(qreg_2[0])
		with else_1:
			main_circ.u(0,param_0,param_5, qreg_0[0])
		main_circ.u(param_0,-0.904000,param_4, qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.y(qreg_2[0])
			main_circ.u(param_7,-0.885000,0.197000, qreg_2[0])
			main_circ.rz(param_2, qreg_2[1])
		with else_1:
			main_circ.rz(param_6, qreg_0[1])
			main_circ.rz(param_0, qreg_0[1])
			main_circ.rz(param_1, qreg_2[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(param_7,0,0.779000, qreg_2[1])
			main_circ.y(qreg_2[1])
			main_circ.y(qreg_0[0])
			main_circ.u(0,param_7,-0.802000, qreg_2[0])
		with case_1(1):
			main_circ.rz(-0.484000, qreg_0[0])
			main_circ.u(param_5,0.382000,param_5, qreg_2[1])
			main_circ.rz(param_0, qreg_2[1])
			main_circ.u(pi/2,0.711000,param_3, qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(pi/2,-0.132000,param_3, qreg_0[1])
		main_circ.u(pi/2,0.552000,0.089000, qreg_0[0])
		main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_2[1]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_2[1],qreg_0[1]])
		with case_1(1):
			main_circ.u(pi/2,param_2,0.715000, qreg_2[0])
			main_circ.u(0,0,param_2, qreg_2[1])
			main_circ.rz(param_6, qreg_2[0])
			main_circ.append(subcirc0,[qreg_2[1],qreg_0[1],qreg_2[0],qreg_0[0]])
with else_2:
	main_circ.append(subcirc0,[qreg_0[1],qreg_2[1],qreg_2[0],qreg_0[0]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.rz(0.160000, qreg_0[0])
		main_circ.rz(-0.323000, qreg_0[1])
		main_circ.id(qreg_0[1])
	with else_1:
		main_circ.id(qreg_2[0])
with else_2:
	main_circ.barrier(qreg_2[0])
bindings = {param_0: 0.735000, param_1: 0.183000, param_2: -0.576000, param_3: -0.167000, param_4: -0.501000, param_5: -0.534000, param_6: 0.810000, param_7: -0.753000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1518", "Optimize1qGatesSimpleCommutation")
