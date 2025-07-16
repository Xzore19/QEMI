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
subcirc0.rx(0.693000, qreg_0[0])
subcirc0.s(qreg_1[1])
subcirc0.u(pi/2,-0.903000,0.729000, qreg_1[0])
subcirc0.cx(qreg_0[0],qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.u(pi/2,param_1,param_2, qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_1[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rx(-0.802000, qreg_3[0])
			main_circ.u(param_1,-0.899000,param_0, qreg_1[1])
			main_circ.cx(qreg_1[1],qreg_3[0])
			main_circ.u(pi/2,param_0,param_1, qreg_0[0])
			main_circ.u(param_1,param_1,-0.564000, qreg_1[1])
		with else_1:
			main_circ.s(qreg_0[0])
			main_circ.s(qreg_0[0])
			main_circ.s(qreg_1[0])
			main_circ.cx(qreg_0[0],qreg_1[1])
with else_3:
	main_circ.u(pi/2,param_1,-0.950000, qreg_1[0])
main_circ.rx(param_4, qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.s(qreg_1[1])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.cx(qreg_3[0],qreg_1[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_2,param_4,-0.900000, qreg_3[0])
					main_circ.u(pi/2,-0.955000,param_0, qreg_1[0])
					main_circ.cx(qreg_0[0],qreg_1[0])
					main_circ.cx(qreg_3[0],qreg_1[0])
				with case_1(1):
					main_circ.cx(qreg_3[0],qreg_0[0])
					main_circ.rx(-0.002000, qreg_1[1])
					main_circ.id(qreg_1[1])
		with case_2(1):
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rx(-0.552000, qreg_1[1])
				main_circ.cx(qreg_3[0],qreg_1[0])
				main_circ.s(qreg_0[0])
				main_circ.barrier(qreg_1[1])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.s(qreg_0[0])
				main_circ.cx(qreg_1[0],qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_1[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_1[0])
			with else_1:
				main_circ.barrier(qreg_1[0])
			main_circ.s(qreg_1[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.rx(param_2, qreg_1[1])
					main_circ.rx(0.155000, qreg_1[1])
					main_circ.u(param_3,param_0,0.629000, qreg_0[0])
					main_circ.id(qreg_1[1])
				with else_1:
					main_circ.rx(-0.440000, qreg_1[1])
			with case_2(1):
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.s(qreg_3[0])
						main_circ.cx(qreg_0[0],qreg_1[1])
						main_circ.cx(qreg_3[0],qreg_1[0])
						main_circ.cx(qreg_0[0],qreg_1[1])
					with case_1(1):
						main_circ.cx(qreg_1[1],qreg_3[0])
						main_circ.rx(0.703000, qreg_0[0])
						main_circ.barrier(qreg_3[0])
	with case_3(1):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.rx(param_4, qreg_1[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_1[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.rx(param_1, qreg_1[0])
					main_circ.cx(qreg_3[0],qreg_1[0])
					main_circ.rx(param_1, qreg_3[0])
			with case_2(1):
				main_circ.u(pi/2,param_2,-0.002000, qreg_0[0])
				main_circ.u(pi/2,0.155000,param_1, qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(qreg_1[1])
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_1[1])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.barrier(qreg_1[1])
bindings = {param_0: 0.670000, param_1: -0.774000, param_2: -0.549000, param_3: -0.285000, param_4: -0.787000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1368")
