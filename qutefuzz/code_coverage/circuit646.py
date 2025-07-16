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
subcirc0.x(qreg_1[1])
subcirc0.ry(0.659000, qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0.ry(0.647000, qreg_1[1])
subcirc0.u(pi/2,-0.142000,0.471000, qreg_0[0])
subcirc0.x(qreg_1[0])
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

main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.y(qreg_1[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_1[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.x(qreg_0[0])
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.y(qreg_0[0])
				main_circ.y(qreg_1[0])
				main_circ.y(qreg_0[0])
	with else_3:
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[1], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.ry(param_0, qreg_1[1])
						main_circ.x(qreg_1[0])
						main_circ.x(qreg_3[0])
						main_circ.u(param_0,param_0,param_0, qreg_1[1])
					with case_1(1):
						main_circ.u(param_0,0.211000,-0.232000, qreg_1[1])
						main_circ.u(param_0,0.175000,0.824000, qreg_1[1])
						main_circ.u(pi/2,0.706000,-0.181000, qreg_0[0])
						main_circ.barrier(qreg_1[0])
			with case_2(1):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(param_0,0.826000,param_0, qreg_1[0])
						main_circ.id(qreg_1[1])
					with case_1(1):
						main_circ.y(qreg_1[1])
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[0])
					with case_1(1):
						main_circ.y(qreg_3[0])
						main_circ.ry(-0.128000, qreg_3[0])
						main_circ.ry(0.307000, qreg_1[1])
						main_circ.u(pi/2,0.978000,param_0, qreg_1[0])
with else_4:
	main_circ.id(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.y(qreg_3[0])
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.ry(0.215000, qreg_3[0])
						main_circ.x(qreg_3[0])
						main_circ.ry(param_0, qreg_3[0])
						main_circ.id(qreg_1[0])
			with case_2(1):
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.ry(param_0, qreg_0[0])
					main_circ.ry(param_0, qreg_3[0])
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.x(qreg_1[1])
					main_circ.u(param_0,param_0,-0.687000, qreg_0[0])
					main_circ.barrier(qreg_1[1])
				with else_1:
					main_circ.barrier(qreg_3[0])
	with else_3:
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_3[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.ry(0.877000, qreg_0[0])
					main_circ.u(pi/2,0.063000,0.927000, qreg_3[0])
					main_circ.x(qreg_1[1])
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.x(qreg_0[0])
					main_circ.x(qreg_3[0])
					main_circ.x(qreg_1[0])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.ry(-0.641000, qreg_0[0])
					main_circ.x(qreg_1[0])
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.u(pi/2,-0.621000,-0.049000, qreg_0[0])
					main_circ.ry(-0.305000, qreg_3[0])
					main_circ.x(qreg_1[1])
with else_4:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.barrier(qreg_0[0])
	with else_3:
		main_circ.u(param_0,param_0,0.694000, qreg_1[0])
		main_circ.x(qreg_0[0])
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_1[1])
				with else_1:
					main_circ.x(qreg_1[1])
					main_circ.y(qreg_1[1])
					main_circ.x(qreg_1[1])
				main_circ.u(param_0,param_0,-0.147000, qreg_1[0])
			with case_2(1):
				main_circ.measure(qreg_1[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_1[1])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_1[1])
				with else_1:
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_3[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.id(qreg_1[0])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_1[0])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(qreg_1[1])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.barrier(qreg_3[0])
bindings = {param_0: -0.639000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "646", "ConsolidateBlocks")
