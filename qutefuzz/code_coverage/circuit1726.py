from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.h(qreg_1[1])
subcirc0.rz(-0.400000, qreg_1[1])
subcirc0.x(qreg_1[1])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.u(pi/2,param_2,param_0, 0)
		main_circ.x(2)
		main_circ.id(1)
	with else_1:
		main_circ.h(2)
		main_circ.u(param_1,-0.633000,0.218000, 0)
with else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rz(param_1, 2)
		main_circ.id(2)
	with else_1:
		main_circ.u(pi/2,-0.673000,-0.322000, 3)
		main_circ.rz(param_2, 1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.h(0)
		main_circ.u(param_0,param_2,-0.706000, 0)
		main_circ.u(pi/2,param_2,param_1, 3)
		main_circ.u(pi/2,param_2,param_1, 3)
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rz(-0.163000, 0)
		main_circ.x(3)
		main_circ.rz(0.047000, 1)
with else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.rz(-0.027000, 0)
		main_circ.h(0)
		main_circ.h(3)
		main_circ.rz(param_0, 3)
		main_circ.u(pi/2,param_2,param_1, 0)
	with else_1:
		main_circ.id(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.h(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_2,-0.090000,0.072000, 2)
			main_circ.h(2)
			main_circ.barrier(3)
		with case_1(1):
			main_circ.x(3)
			main_circ.id(2)
with else_2:
	main_circ.barrier(3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.h(3)
				main_circ.barrier(1)
			with case_1(1):
				main_circ.x(3)
				main_circ.id(2)
		main_circ.x(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,-0.694000,-0.614000, 1)
				main_circ.rz(0.892000, 1)
				main_circ.rz(0.853000, 2)
				main_circ.rz(0.975000, 3)
			with case_1(1):
				main_circ.x(1)
				main_circ.rz(0.722000, 0)
				main_circ.rz(param_0, 0)
				main_circ.barrier(1)
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.x(3)
		main_circ.u(param_2,param_0,0.807000, 1)
		main_circ.x(2)
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.rz(param_2, 1)
				main_circ.h(3)
				main_circ.rz(param_2, 1)
				main_circ.x(0)
			with case_1(1):
				main_circ.h(3)
				main_circ.rz(param_2, 1)
				main_circ.rz(param_2, 3)
				main_circ.x(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.x(2)
		main_circ.u(param_0,-0.108000,-0.665000, 3)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(3)
		with case_1(1):
			main_circ.h(1)
			main_circ.u(param_1,-0.802000,0.875000, 2)
			main_circ.u(pi/2,0.277000,param_0, 3)
			main_circ.x(2)
with else_2:
	main_circ.h(0)
	main_circ.rz(-0.450000, 3)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.x(0)
				main_circ.rz(param_2, 1)
				main_circ.h(0)
				main_circ.barrier(3)
			with case_1(1):
				main_circ.x(2)
				main_circ.barrier(1)
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(3)
		main_circ.id(3)
bindings = {param_0: -0.259000, param_1: -0.982000, param_2: -0.013000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1726")
