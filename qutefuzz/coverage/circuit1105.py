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
subcirc0.z(qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0.u(pi/2,-0.213000,-0.866000, qreg_0[1])
subcirc0.z(qreg_3[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cz(qreg_0[1],qreg_3[0])
			main_circ.append(subcirc0,[qreg_3[0],qreg_2[0],qreg_0[1],qreg_0[0]])
		with case_1(1):
			main_circ.s(qreg_2[0])
			main_circ.cz(qreg_3[0],qreg_2[0])
			main_circ.cz(qreg_2[0],qreg_0[1])
			main_circ.s(qreg_2[0])
with else_2:
	main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.z(qreg_2[0])
			main_circ.z(qreg_0[0])
			main_circ.z(qreg_0[0])
			main_circ.z(qreg_0[1])
		with case_1(1):
			main_circ.u(param_6,0.717000,param_4, qreg_2[0])
			main_circ.u(pi/2,-0.691000,param_2, qreg_0[1])
			main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_3[0],qreg_0[1]])
main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(qreg_2[0],qreg_0[1])
			main_circ.u(param_1,param_5,param_3, qreg_2[0])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_3[0],qreg_0[0]])
			with case_1(1):
				main_circ.u(param_1,param_6,0.324000, qreg_0[1])
				main_circ.z(qreg_3[0])
				main_circ.cz(qreg_0[1],qreg_0[0])
				main_circ.cz(qreg_3[0],qreg_2[0])
	with case_2(1):
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cz(qreg_0[0],qreg_0[1])
			main_circ.cz(qreg_0[1],qreg_3[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_0[1],qreg_2[0])
				main_circ.cz(qreg_3[0],qreg_0[1])
				main_circ.cz(qreg_0[1],qreg_3[0])
				main_circ.cz(qreg_2[0],qreg_0[0])
			with case_1(1):
				main_circ.u(param_4,param_0,-0.289000, qreg_2[0])
				main_circ.cz(qreg_0[0],qreg_0[1])
				main_circ.s(qreg_2[0])
				main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.s(qreg_3[0])
		main_circ.barrier(qreg_3[0])
	with else_1:
		main_circ.id(qreg_3[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[1])
	main_circ.id(qreg_2[0])
with else_2:
	main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.915000, param_1: -0.797000, param_2: 0.482000, param_3: -0.843000, param_4: 0.092000, param_5: 0.844000, param_6: 0.625000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1105")
