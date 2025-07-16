from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.h(0)
main_circ.u(-0.577000,param_0,param_0, 0)
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_0,param_0,-0.116000, qreg_1[0])
			main_circ.u(param_0,0.708000,0.046000, qreg_1[0])
			main_circ.u(param_0,-0.836000,0.605000, qreg_1[0])
			main_circ.u(param_0,0.905000,param_0, qreg_1[1])
main_circ.h(0)
main_circ.h(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(qreg_1[2])
				main_circ.h(qreg_0[0])
				main_circ.cx(qreg_1[2],qreg_1[0])
				main_circ.cx(0,qreg_1[2])
			with case_1(1):
				main_circ.rx(param_0, qreg_0[0])
				main_circ.rx(param_0, qreg_0[0])
				main_circ.u(-0.178000,param_0,0.433000, qreg_0[0])
				main_circ.u(param_0,param_0,param_0, qreg_1[1])
with else_3:
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cx(qreg_0[0],qreg_1[1])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(param_0,param_0,param_0, qreg_1[1])
			main_circ.cx(qreg_1[0],qreg_1[1])
			main_circ.u(-0.619000,param_0,param_0, qreg_0[0])
			main_circ.cx(qreg_1[0],qreg_0[0])
			main_circ.rx(param_0, 0)
		with else_1:
			main_circ.h(qreg_1[1])
			main_circ.cx(qreg_0[0],qreg_1[1])
			main_circ.h(qreg_0[0])
			main_circ.h(qreg_1[1])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(-0.782000,param_0,0.003000, qreg_1[2])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.rx(param_0, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(qreg_1[0],qreg_1[2])
			main_circ.cx(qreg_0[0],0)
			main_circ.cx(0,qreg_1[0])
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_0[0],qreg_1[0])
				main_circ.cx(qreg_1[1],0)
				main_circ.rx(param_0, qreg_1[0])
				main_circ.rx(-0.047000, 0)
			with case_1(1):
				main_circ.h(qreg_1[2])
				main_circ.u(param_0,0.585000,param_0, qreg_1[2])
				main_circ.rx(param_0, qreg_1[0])
				main_circ.rx(-0.857000, qreg_1[0])
	with else_2:
		main_circ.measure(qreg_1[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(param_0,param_0,-0.574000, qreg_1[0])
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[1])
			with case_1(1):
				main_circ.barrier(qreg_1[2])
		main_circ.barrier(qreg_1[0])
bindings = {param_0: -0.827000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1542")
