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
subcirc0.rz(-0.707000, qreg_2[0])
subcirc0.rz(0.133000, qreg_0[0])
subcirc0.x(qreg_2[0])
subcirc0.rz(-0.452000, qreg_0[1])
subcirc0.u(pi/2,0.257000,-0.296000, qreg_3[0])
subcirc0.x(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.x(3)
					main_circ.barrier(3)
			main_circ.rz(-0.910000, 0)
			main_circ.id(3)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.x(1)
					main_circ.u(param_1,param_2,param_0, 2)
					main_circ.z(0)
					main_circ.u(param_0,-0.269000,-0.993000, 1)
				with case_1(1):
					main_circ.z(2)
					main_circ.barrier(3)
	with case_3(1):
		main_circ.barrier(0)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rz(0.600000, 3)
			main_circ.x(2)
			main_circ.rz(-0.643000, 0)
	with else_2:
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.x(0)
				main_circ.z(2)
				main_circ.u(param_2,-0.071000,param_0, 3)
				main_circ.z(0)
			with case_1(1):
				main_circ.x(3)
				main_circ.u(param_2,0.282000,-0.150000, 3)
				main_circ.id(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.x(2)
			main_circ.z(0)
			main_circ.x(0)
		with else_1:
			main_circ.id(0)
		main_circ.x(0)
	with else_2:
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_0,param_2,-0.973000, 3)
				main_circ.u(pi/2,param_0,param_1, 1)
				main_circ.id(0)
			with case_1(1):
				main_circ.x(2)
				main_circ.u(pi/2,param_1,-0.646000, 1)
				main_circ.id(2)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rz(-0.501000, 1)
			main_circ.rz(param_1, 2)
			main_circ.barrier(1)
with else_3:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.x(0)
			main_circ.u(param_0,param_0,param_1, 0)
		with else_1:
			main_circ.u(pi/2,param_2,param_0, 2)
			main_circ.id(0)
	with else_2:
		main_circ.u(pi/2,-0.401000,-0.339000, 3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.z(3)
				main_circ.z(0)
				main_circ.z(1)
				main_circ.x(2)
			with case_1(1):
				main_circ.u(pi/2,0.556000,param_0, 0)
				main_circ.u(pi/2,0.231000,-0.743000, 3)
				main_circ.u(param_0,param_0,param_0, 3)
				main_circ.rz(0.434000, 1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(pi/2,param_0,0.670000, 3)
			main_circ.z(3)
			main_circ.z(2)
			main_circ.id(1)
		with else_1:
			main_circ.barrier(2)
with else_3:
	main_circ.z(1)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.z(2)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rz(param_0, 2)
					main_circ.id(0)
				with case_1(1):
					main_circ.u(param_2,param_0,-0.216000, 3)
					main_circ.z(3)
					main_circ.z(0)
					main_circ.z(0)
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(pi/2,-0.397000,param_1, 2)
					main_circ.x(3)
					main_circ.barrier(2)
				with case_1(1):
					main_circ.x(3)
					main_circ.u(pi/2,-0.772000,0.576000, 2)
					main_circ.rz(-0.305000, 3)
					main_circ.rz(param_1, 1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(param_0, 3)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.x(2)
				main_circ.id(3)
			with case_1(1):
				main_circ.id(2)
with else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(3)
		main_circ.id(3)
	main_circ.id(0)
bindings = {param_0: 0.558000, param_1: -0.552000, param_2: 0.278000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1696", "Optimize1qGatesSimpleCommutation")
