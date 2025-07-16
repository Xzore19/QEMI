from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_2[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rx(-0.526000, qreg_2[1])
			main_circ.x(qreg_0[0])
			main_circ.y(qreg_2[1])
			main_circ.cy(qreg_0[0],0)
			main_circ.rx(-0.671000, qreg_2[0])
	with else_2:
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.x(qreg_1[0])
				main_circ.cy(qreg_2[1],1)
				main_circ.x(1)
				main_circ.rx(0.244000, qreg_2[0])
			with case_1(1):
				main_circ.cy(qreg_2[0],1)
				main_circ.x(qreg_2[0])
				main_circ.rx(param_2, 0)
				main_circ.x(qreg_1[0])
with else_3:
	main_circ.measure(qreg_2[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.rx(-0.081000, qreg_2[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.x(1)
				main_circ.y(qreg_1[0])
				main_circ.rx(param_4, 1)
				main_circ.x(qreg_0[0])
				main_circ.y(qreg_0[0])
			with else_1:
				main_circ.cy(qreg_2[0],qreg_2[1])
				main_circ.cy(1,qreg_1[0])
				main_circ.rx(-0.622000, 1)
		with case_2(1):
			main_circ.cy(qreg_2[0],1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rx(param_4, qreg_1[0])
					main_circ.rx(param_6, qreg_0[0])
					main_circ.cy(qreg_0[0],qreg_1[0])
					main_circ.rx(param_3, qreg_0[0])
				with case_1(1):
					main_circ.x(0)
					main_circ.rx(param_1, 0)
					main_circ.y(qreg_1[0])
					main_circ.rx(param_1, qreg_2[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.rx(-0.963000, 1)
				main_circ.x(qreg_2[1])
				main_circ.cy(qreg_0[0],qreg_2[1])
				main_circ.x(1)
			with case_1(1):
				main_circ.cy(qreg_2[1],0)
				main_circ.y(1)
				main_circ.rx(0.144000, qreg_0[0])
				main_circ.rx(param_1, qreg_2[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.x(qreg_1[0])
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.cy(qreg_2[0],qreg_2[1])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(0,1)
				main_circ.cy(0,qreg_2[1])
				main_circ.cy(qreg_0[0],qreg_1[0])
				main_circ.cy(0,qreg_2[1])
			with case_1(1):
				main_circ.cy(qreg_2[1],qreg_1[0])
				main_circ.cy(1,qreg_2[0])
				main_circ.cy(qreg_1[0],0)
				main_circ.x(qreg_0[0])
	with else_2:
		main_circ.cy(qreg_0[0],qreg_2[0])
		main_circ.cy(qreg_2[0],0)
with else_3:
	main_circ.measure(qreg_2[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.rx(param_1, qreg_2[0])
			main_circ.y(qreg_2[1])
			main_circ.x(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.y(0)
				main_circ.rx(param_6, 0)
				main_circ.cy(qreg_2[0],1)
		with case_2(1):
			main_circ.barrier(qreg_2[1])
bindings = {param_1: -0.012000, param_2: 0.167000, param_3: -0.348000, param_4: -0.851000, param_6: 0.096000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1177", "HoareOptimizer")
