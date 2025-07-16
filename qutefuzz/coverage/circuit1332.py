from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.y(qreg_0[0])
subcirc0.u(-0.348000,-0.338000,0.865000, qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.u(pi/2,-0.726000,-0.010000, qreg_2[0])
subcirc0.u(-0.774000,0.620000,-0.828000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(-0.702000,0.469000,0.787000, 1)
		main_circ.u(-0.065000,0.244000,param_2, qreg_0[3])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,0.943000,param_2, qreg_0[0])
				main_circ.barrier(qreg_0[3])
			with case_1(1):
				main_circ.u(pi/2,-0.338000,param_2, qreg_0[1])
				main_circ.id(qreg_0[2])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.u(param_2,-0.151000,param_1, qreg_0[0])
				main_circ.u(param_2,param_1,0.168000, 1)
				main_circ.u(pi/2,param_1,0.664000, qreg_0[0])
				main_circ.u(param_2,param_0,param_0, qreg_0[2])
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.y(qreg_0[1])
				main_circ.u(param_0,-0.399000,param_2, qreg_0[1])
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[3])
	with else_2:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.z(qreg_0[0])
				main_circ.y(0)
				main_circ.y(qreg_0[3])
				main_circ.u(param_2,-0.306000,-0.658000, 1)
			with case_1(1):
				main_circ.z(qreg_0[1])
				main_circ.y(qreg_0[2])
				main_circ.u(pi/2,0.390000,0.954000, qreg_0[3])
				main_circ.u(param_2,param_1,-0.995000, 1)
with else_3:
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(param_1,-0.650000,param_1, qreg_0[3])
				main_circ.barrier(1)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.z(qreg_0[3])
				main_circ.y(qreg_0[1])
				main_circ.y(qreg_0[3])
			with else_1:
				main_circ.u(0.027000,param_2,param_0, 0)
				main_circ.barrier(qreg_0[1])
		with case_2(1):
			main_circ.measure(qreg_0[3], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.z(qreg_0[2])
				main_circ.z(qreg_0[1])
				main_circ.u(param_1,param_0,param_1, qreg_0[0])
				main_circ.id(1)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.z(qreg_0[0])
					main_circ.z(qreg_0[2])
					main_circ.u(pi/2,param_1,0.402000, qreg_0[1])
					main_circ.y(qreg_0[1])
				with case_1(1):
					main_circ.barrier(1)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.z(qreg_0[2])
				main_circ.y(1)
				main_circ.y(qreg_0[1])
				main_circ.u(pi/2,0.787000,param_2, 1)
				main_circ.u(pi/2,param_2,-0.246000, 0)
			with else_1:
				main_circ.id(qreg_0[0])
		with else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(pi/2,param_1,-0.172000, 1)
				main_circ.u(param_0,param_0,param_1, qreg_0[1])
				main_circ.y(0)
				main_circ.y(qreg_0[3])
				main_circ.y(qreg_0[0])
			with else_1:
				main_circ.z(qreg_0[2])
				main_circ.u(0.083000,param_2,param_2, qreg_0[1])
				main_circ.barrier(qreg_0[3])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.y(qreg_0[0])
						main_circ.u(param_2,param_1,param_2, qreg_0[2])
						main_circ.u(param_0,param_2,0.264000, 0)
						main_circ.u(param_0,param_1,param_1, qreg_0[2])
					with case_1(1):
						main_circ.u(param_0,-0.198000,param_0, qreg_0[0])
						main_circ.u(-0.445000,param_2,-0.513000, qreg_0[3])
						main_circ.z(1)
						main_circ.id(0)
			with case_2(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.u(-0.413000,-0.781000,-0.246000, qreg_0[2])
						main_circ.u(param_1,-0.156000,-0.811000, qreg_0[1])
						main_circ.id(0)
					with case_1(1):
						main_circ.u(-0.139000,0.958000,param_0, 1)
						main_circ.id(0)
				main_circ.y(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_0[2])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[1])
			with case_1(1):
				main_circ.barrier(qreg_0[3])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[3])
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[1])
			with case_1(1):
				main_circ.barrier(qreg_0[2])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.id(qreg_0[3])
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.id(qreg_0[2])
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[2])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[3])
		with else_1:
			main_circ.id(qreg_0[2])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[3])
		main_circ.id(qreg_0[3])
	with else_2:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[3])
			with case_1(1):
				main_circ.barrier(1)
		main_circ.barrier(qreg_0[2])
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.id(1)
		with case_2(1):
			main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.barrier(0)
	with else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.barrier(1)
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[3])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[3])
		with else_1:
			main_circ.id(0)
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.id(qreg_0[2])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[3])
		with else_1:
			main_circ.id(1)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[1])
		main_circ.id(qreg_0[3])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.id(0)
		with case_2(1):
			main_circ.id(qreg_0[2])
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(0)
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[3])
			with case_1(1):
				main_circ.id(qreg_0[3])
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[3])
			with case_1(1):
				main_circ.barrier(qreg_0[3])
		main_circ.id(qreg_0[2])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[2])
			with case_1(1):
				main_circ.id(1)
		main_circ.id(0)
	main_circ.id(qreg_0[0])
bindings = {param_0: 0.512000, param_1: -0.563000, param_2: 0.927000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1332")
