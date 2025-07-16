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
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(0,0,0.705000, qreg_2[0])
subcirc0.u(0,0,-0.609000, qreg_2[1])
subcirc0.rx(0.294000, qreg_1[0])
subcirc0.s(qreg_2[1])
subcirc0.s(qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

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

main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.rx(0.649000, 0)
			main_circ.s(2)
			main_circ.rz(param_2, 2)
			main_circ.s(qreg_0[0])
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.s(qreg_0[0])
		main_circ.rz(0.146000, 0)
		main_circ.id(qreg_0[0])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.rx(-0.985000, 0)
with else_2:
	main_circ.u(0,param_1,param_2, qreg_1[0])
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rz(param_0, 1)
		main_circ.rz(param_0, qreg_1[0])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rx(0.212000, 2)
			main_circ.u(param_2,0,param_2, 0)
			main_circ.s(0)
			main_circ.u(param_2,param_2,param_2, qreg_0[0])
		with case_1(1):
			main_circ.id(1)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_2, qreg_1[0])
			main_circ.rz(-0.608000, qreg_0[0])
			main_circ.rx(param_0, 0)
			main_circ.s(1)
		with case_1(1):
			main_circ.s(0)
			main_circ.rz(0.718000, 1)
			main_circ.s(qreg_1[0])
			main_circ.rz(param_3, 3)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.s(2)
		main_circ.rz(0.496000, qreg_0[0])
		main_circ.rz(0.174000, 3)
		main_circ.id(qreg_0[0])
main_circ.rz(-0.577000, qreg_1[0])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.u(0,0,param_0, 1)
				main_circ.rx(param_3, 3)
				main_circ.s(0)
				main_circ.rz(param_3, 3)
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rz(param_3, 2)
			main_circ.rx(param_2, 1)
		main_circ.rx(param_2, 0)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_3,0,-0.065000, 0)
				main_circ.rx(param_0, 2)
				main_circ.barrier(3)
			with case_1(1):
				main_circ.s(qreg_1[0])
				main_circ.u(param_2,0,param_3, 3)
				main_circ.rx(0.443000, qreg_1[0])
				main_circ.rz(param_2, qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(0,param_2,0.636000, qreg_1[0])
		main_circ.rz(0.701000, qreg_0[0])
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_1, 3)
			main_circ.rz(param_0, qreg_1[0])
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(-0.747000, qreg_1[0])
			main_circ.rz(param_0, 1)
			main_circ.s(2)
			main_circ.u(param_2,param_1,param_1, 2)
			main_circ.u(param_2,0,-0.580000, qreg_0[0])
main_circ.u(0,0,param_0, qreg_1[0])
main_circ.s(qreg_1[0])
bindings = {param_0: 0.334000, param_1: 0.021000, param_2: -0.475000, param_3: -0.184000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1016")
