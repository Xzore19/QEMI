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
subcirc0.cx(qreg_3[0],qreg_0[1])
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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
param_7 = Parameter("param_7")

main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(qreg_3[0])
			main_circ.u(pi/2,-0.086000,-0.308000, qreg_3[0])
			main_circ.cx(qreg_3[0],qreg_1[0])
			main_circ.u(param_0,param_6,param_6, qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.z(qreg_1[0])
						main_circ.x(qreg_3[0])
						main_circ.x(qreg_3[0])
						main_circ.cx(qreg_1[0],qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.z(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(pi/2,param_5,-0.002000, qreg_1[1])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.cx(qreg_1[1],qreg_1[0])
						main_circ.cx(qreg_1[0],qreg_1[1])
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.u(pi/2,param_7,param_3, qreg_3[0])
						main_circ.cx(qreg_1[1],qreg_3[0])
						main_circ.x(qreg_1[1])
						main_circ.cx(qreg_1[0],qreg_0[0])
	with case_3(1):
		main_circ.z(qreg_3[0])
		main_circ.u(param_5,param_2,param_2, qreg_1[0])
		main_circ.z(qreg_3[0])
		main_circ.u(param_0,param_0,param_6, qreg_1[1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.x(qreg_1[1])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.x(qreg_1[0])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[1])
			with case_1(1):
				main_circ.z(qreg_0[0])
				main_circ.cx(qreg_1[0],qreg_3[0])
				main_circ.cx(qreg_3[0],qreg_1[0])
				main_circ.cx(qreg_3[0],qreg_1[0])
	with else_2:
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.cx(qreg_1[1],qreg_3[0])
			main_circ.z(qreg_3[0])
			main_circ.z(qreg_1[0])
with else_3:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_1[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.z(qreg_0[0])
				main_circ.cx(qreg_1[1],qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(qreg_0[0],qreg_1[0])
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.z(qreg_0[0])
				main_circ.cx(qreg_1[0],qreg_1[1])
				main_circ.x(qreg_1[1])
				main_circ.u(param_3,param_1,param_0, qreg_1[1])
				main_circ.x(qreg_3[0])
		with case_2(1):
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.z(qreg_3[0])
					main_circ.x(qreg_1[1])
					main_circ.cx(qreg_0[0],qreg_1[1])
					main_circ.u(pi/2,-0.116000,param_0, qreg_0[0])
				with case_1(1):
					main_circ.x(qreg_1[1])
					main_circ.barrier(qreg_1[1])
bindings = {param_0: 0.450000, param_1: -0.985000, param_2: 0.510000, param_3: -0.402000, param_5: -0.704000, param_6: -0.544000, param_7: 0.283000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1400", "CollectLinearFunctions")
