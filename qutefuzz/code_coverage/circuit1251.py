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
subcirc0.x(qreg_0[0])
subcirc0.h(qreg_0[1])
subcirc0.rx(-0.656000, qreg_3[0])
subcirc0.rz(-0.232000, qreg_0[1])
subcirc0.rz(0.589000, qreg_0[1])
subcirc0.x(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.x(3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(1)
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.x(3)
			main_circ.rz(-0.813000, 2)
			main_circ.rz(param_2, 3)
			main_circ.id(1)
		with case_1(1):
			main_circ.barrier(2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rz(0.562000, 3)
			main_circ.rx(param_1, 1)
			main_circ.id(2)
		with case_1(1):
			main_circ.rz(param_3, 3)
			main_circ.rz(-0.017000, 2)
			main_circ.x(1)
			main_circ.rx(param_0, 3)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(param_3, 2)
		main_circ.h(0)
		main_circ.rz(0.707000, 0)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.rx(-0.130000, 3)
	with else_1:
		main_circ.h(2)
		main_circ.rx(param_0, 2)
		main_circ.id(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rz(-0.716000, 2)
			main_circ.rx(param_0, 1)
			main_circ.rz(0.997000, 3)
			main_circ.rz(param_1, 3)
		with case_1(1):
			main_circ.x(3)
			main_circ.rx(param_0, 3)
			main_circ.h(0)
			main_circ.rx(param_1, 1)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(1)
				main_circ.barrier(1)
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.x(2)
			main_circ.rx(param_1, 0)
			main_circ.h(0)
			main_circ.x(0)
			main_circ.rz(param_1, 2)
	with case_2(1):
		main_circ.rz(param_0, 0)
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.rx(param_3, 0)
				main_circ.x(3)
				main_circ.x(1)
				main_circ.barrier(1)
main_circ.h(3)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.x(3)
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.h(3)
		main_circ.id(2)
	with else_1:
		main_circ.id(2)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.x(1)
	with else_1:
		main_circ.barrier(2)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(1)
		with case_1(1):
			main_circ.id(3)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rx(-0.220000, 3)
		main_circ.rx(0.645000, 0)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.x(1)
			main_circ.rz(param_2, 2)
			main_circ.barrier(1)
		with case_1(1):
			main_circ.rx(param_2, 2)
			main_circ.h(0)
			main_circ.rz(-0.841000, 1)
			main_circ.barrier(1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.h(0)
			main_circ.x(0)
			main_circ.barrier(0)
		with else_1:
			main_circ.id(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.barrier(1)
	with case_2(1):
		main_circ.id(0)
bindings = {param_0: 0.047000, param_1: -0.310000, param_2: 0.059000, param_3: 0.192000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1251", "CommutativeCancellation")
