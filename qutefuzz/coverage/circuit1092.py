from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.cx(qreg_0[2],qreg_0[0])
						main_circ.u(0.251000,param_0,param_2, qreg_0[1])
						main_circ.cx(qreg_0[1],qreg_0[0])
						main_circ.cx(qreg_0[1],qreg_0[0])
					with case_1(1):
						main_circ.cx(qreg_0[2],qreg_0[1])
						main_circ.cx(qreg_0[2],qreg_0[1])
						main_circ.u(0.138000,-0.678000,param_2, qreg_3[0])
						main_circ.rz(param_2, 1)
			with case_2(1):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.u(param_1,0.717000,param_3, 0)
					main_circ.rz(param_1, 0)
					main_circ.u(param_2,0.630000,0.341000, qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.rz(0.841000, 0)
					main_circ.rx(param_1, qreg_3[0])
					main_circ.rx(-0.583000, qreg_0[0])
					main_circ.cx(qreg_3[0],1)
				with else_1:
					main_circ.cx(0,qreg_0[2])
					main_circ.rz(param_3, 1)
					main_circ.cx(0,qreg_0[2])
					main_circ.rz(param_2, qreg_0[1])
with else_4:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rx(param_4, qreg_3[0])
					main_circ.u(0.012000,-0.896000,-0.677000, 1)
					main_circ.cx(qreg_0[0],qreg_3[0])
					main_circ.u(param_4,-0.563000,0.515000, qreg_0[2])
				with case_1(1):
					main_circ.rx(param_0, 1)
					main_circ.rx(-0.461000, qreg_3[0])
					main_circ.u(param_4,0.267000,param_1, 1)
					main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0.478000,param_0,param_3, qreg_0[2])
				main_circ.rx(param_4, qreg_0[0])
				main_circ.rz(0.316000, qreg_0[2])
			with else_1:
				main_circ.u(-0.764000,0.318000,-0.296000, qreg_0[2])
				main_circ.rx(0.885000, qreg_0[0])
				main_circ.cx(qreg_3[0],qreg_0[0])
				main_circ.cx(qreg_0[0],qreg_0[2])
		with else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rx(0.949000, 0)
				main_circ.cx(qreg_0[2],qreg_3[0])
			with else_1:
				main_circ.u(param_0,0.065000,param_4, 0)
				main_circ.cx(qreg_3[0],qreg_0[2])
				main_circ.cx(qreg_0[0],qreg_0[2])
				main_circ.rz(0.225000, qreg_0[1])
				main_circ.u(-0.284000,param_3,param_0, qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(-0.120000, qreg_3[0])
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rz(0.507000, qreg_0[2])
				main_circ.u(-0.858000,0.407000,param_0, 0)
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rx(-0.990000, 0)
					main_circ.u(param_3,-0.864000,param_3, 0)
					main_circ.rz(param_1, qreg_3[0])
					main_circ.rz(param_0, qreg_0[1])
		with case_3(1):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.rx(0.526000, qreg_3[0])
				main_circ.cx(0,qreg_0[1])
			with else_2:
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.u(-0.190000,0.309000,param_2, qreg_0[2])
					main_circ.u(-0.276000,0.807000,-0.026000, 0)
					main_circ.id(qreg_0[2])
				with else_1:
					main_circ.id(qreg_3[0])
bindings = {param_0: -0.160000, param_1: -0.754000, param_2: -0.801000, param_3: 0.123000, param_4: 0.274000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1092", "Optimize1qGates")
