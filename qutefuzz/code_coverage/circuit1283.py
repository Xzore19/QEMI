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
subcirc0.x(qreg_0[0])
subcirc0.u(0.817000,-0.810000,-0.889000, qreg_0[3])
subcirc0.y(qreg_0[3])
subcirc0.u(0,0,0.155000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.y(3)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(2)
				main_circ.u(0,param_0,param_0, 2)
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.y(0)
					main_circ.u(0,param_0,param_1, 2)
					main_circ.u(param_0,0,param_2, 1)
					main_circ.u(0.102000,-0.616000,-0.775000, 0)
				with else_1:
					main_circ.x(3)
					main_circ.x(0)
					main_circ.id(1)
			with case_2(1):
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(0,0,param_2, 1)
						main_circ.barrier(1)
					with case_1(1):
						main_circ.x(3)
						main_circ.x(2)
						main_circ.y(0)
						main_circ.u(0,param_1,param_2, 2)
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.barrier(3)
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.u(-0.029000,param_0,-0.661000, 1)
				main_circ.u(param_0,param_2,param_1, 3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.x(1)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.x(2)
						main_circ.x(0)
						main_circ.u(param_0,0,0.959000, 1)
						main_circ.x(0)
					with case_1(1):
						main_circ.id(3)
			with case_2(1):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.u(-0.854000,param_1,-0.264000, 1)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.x(3)
					main_circ.y(2)
				main_circ.id(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.x(0)
					main_circ.id(1)
				with case_1(1):
					main_circ.id(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0,param_1,param_0, 3)
				main_circ.u(param_1,0,param_1, 3)
				main_circ.x(3)
				main_circ.u(param_1,0.505000,-0.392000, 1)
			with else_1:
				main_circ.y(2)
				main_circ.u(0,param_1,-0.609000, 0)
				main_circ.u(0,param_2,param_2, 0)
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.x(2)
				main_circ.u(param_2,0,0.851000, 3)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.y(3)
			main_circ.y(2)
with else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.x(0)
			main_circ.y(3)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(-0.046000,param_0,param_0, 0)
					main_circ.y(0)
					main_circ.id(3)
				with case_1(1):
					main_circ.x(2)
					main_circ.id(3)
		with case_2(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(3)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.y(3)
					main_circ.x(1)
					main_circ.y(1)
					main_circ.u(0,0,-0.035000, 2)
				with case_1(1):
					main_circ.x(1)
					main_circ.id(1)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.id(2)
	with case_3(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.x(2)
			main_circ.x(1)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.y(3)
				main_circ.u(0,0,param_1, 1)
				main_circ.y(2)
				main_circ.id(2)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.x(3)
with else_3:
	main_circ.id(2)
main_circ.u(param_0,param_0,param_2, 0)
bindings = {param_0: -0.627000, param_1: -0.781000, param_2: -0.413000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1283")
