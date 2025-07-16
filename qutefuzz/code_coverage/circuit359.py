from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,0.037000,param_0, 0)
				main_circ.rz(-0.148000, 3)
				main_circ.u(0,0,param_1, 0)
				main_circ.s(0)
			with case_1(1):
				main_circ.u(0,0,-0.406000, 2)
				main_circ.u(param_1,param_0,0.875000, qreg_1[0])
				main_circ.rz(param_1, 3)
				main_circ.u(pi/2,-0.866000,0.491000, 3)
	with else_2:
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rz(-0.771000, 0)
			main_circ.u(pi/2,-0.595000,param_1, 0)
			main_circ.u(param_1,param_1,param_0, qreg_0[0])
			main_circ.u(param_1,param_1,0.180000, qreg_1[0])
			main_circ.u(pi/2,0.574000,param_0, 3)
		with else_1:
			main_circ.u(param_1,0.982000,0.284000, 3)
			main_circ.rz(param_0, 2)
			main_circ.u(pi/2,-0.231000,param_0, 2)
			main_circ.s(0)
main_circ.u(param_0,0.616000,param_1, 3)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.s(3)
				main_circ.u(0,param_1,-0.468000, 0)
				main_circ.u(pi/2,param_0,0.289000, 0)
			with else_1:
				main_circ.s(2)
				main_circ.u(param_1,0,param_0, qreg_0[0])
				main_circ.u(pi/2,-0.961000,param_0, 0)
				main_circ.u(param_1,0,param_0, qreg_1[0])
				main_circ.s(1)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.s(qreg_0[0])
				main_circ.s(2)
				main_circ.rz(param_1, qreg_0[0])
				main_circ.u(0,0,param_0, 1)
				main_circ.u(0,0,param_0, qreg_1[0])
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(0,0,param_1, 0)
				main_circ.u(param_1,0.689000,param_0, qreg_1[0])
				main_circ.u(param_0,0,param_1, qreg_0[0])
				main_circ.u(param_0,-0.888000,param_0, 0)
				main_circ.u(param_0,0.375000,-0.213000, 0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_0,param_0,param_0, 1)
			main_circ.measure(0, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rz(0.544000, 1)
					main_circ.u(param_0,0,param_1, 2)
					main_circ.u(pi/2,param_0,param_1, 2)
					main_circ.u(param_0,0,param_0, 3)
				with case_1(1):
					main_circ.u(param_0,param_1,0.415000, 3)
					main_circ.u(param_0,param_0,-0.303000, 2)
					main_circ.s(2)
					main_circ.s(3)
	with case_3(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(1)
						main_circ.u(param_1,param_1,-0.919000, 3)
						main_circ.s(1)
						main_circ.u(0,0,0.748000, qreg_1[0])
					with case_1(1):
						main_circ.s(qreg_1[0])
						main_circ.u(pi/2,0.101000,-0.120000, 0)
						main_circ.u(param_1,param_0,0.887000, 1)
						main_circ.rz(param_0, 0)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(qreg_0[0])
						main_circ.u(param_1,0.866000,param_0, 0)
						main_circ.rz(param_1, qreg_1[0])
						main_circ.rz(param_1, qreg_0[0])
					with case_1(1):
						main_circ.u(param_1,param_0,param_1, qreg_1[0])
						main_circ.id(3)
bindings = {param_0: 0.587000, param_1: 0.646000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "359", "CommutativeInverseCancellation")
