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
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_0[0],qreg_0[2])
				main_circ.rz(param_1, qreg_0[2])
				main_circ.y(qreg_0[1])
				main_circ.rz(0.518000, 1)
			with case_1(1):
				main_circ.cz(1,qreg_0[1])
				main_circ.y(1)
				main_circ.cz(0,qreg_0[1])
				main_circ.u(param_1,-0.167000,0.268000, qreg_0[2])
	with case_2(1):
		main_circ.u(pi/2,-0.152000,param_2, 0)
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_0[0],0)
				main_circ.cz(0,qreg_0[0])
				main_circ.u(param_1,-0.759000,param_2, qreg_0[1])
				main_circ.y(1)
			with case_1(1):
				main_circ.y(qreg_0[0])
				main_circ.rz(param_1, qreg_0[2])
				main_circ.rz(0.348000, qreg_0[0])
				main_circ.rz(param_2, qreg_3[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.y(qreg_0[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rz(param_0, 1)
	with else_1:
		main_circ.rz(param_1, qreg_3[0])
main_circ.u(pi/2,param_2,param_2, 1)
main_circ.rz(-0.595000, qreg_0[1])
main_circ.rz(param_2, qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.y(qreg_3[0])
		main_circ.y(qreg_0[0])
		main_circ.y(qreg_0[2])
	with else_1:
		main_circ.y(qreg_0[2])
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cz(qreg_0[0],qreg_3[0])
			main_circ.u(param_2,param_0,-0.476000, qreg_0[2])
			main_circ.u(param_1,0.960000,param_1, qreg_0[2])
			main_circ.u(pi/2,param_0,param_2, qreg_0[1])
		with case_1(1):
			main_circ.y(qreg_0[1])
			main_circ.rz(0.810000, 0)
			main_circ.y(1)
			main_circ.rz(param_0, qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.cz(qreg_0[2],qreg_3[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(qreg_0[2],qreg_0[1])
		main_circ.cz(1,qreg_0[0])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.y(qreg_3[0])
			main_circ.cz(0,qreg_0[2])
			main_circ.cz(qreg_3[0],0)
			main_circ.cz(qreg_3[0],qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cz(qreg_0[0],0)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_0[2],1)
				main_circ.cz(0,1)
				main_circ.cz(qreg_0[0],qreg_0[1])
				main_circ.rz(param_0, qreg_0[0])
			with case_1(1):
				main_circ.u(pi/2,0.305000,-0.899000, qreg_3[0])
				main_circ.cz(qreg_3[0],0)
				main_circ.cz(0,qreg_0[0])
				main_circ.u(param_1,0.051000,param_1, 0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rz(param_1, 0)
			main_circ.cz(qreg_3[0],0)
			main_circ.cz(0,qreg_0[1])
			main_circ.cz(qreg_0[2],qreg_0[1])
		with case_1(1):
			main_circ.u(param_0,0.147000,-0.791000, qreg_0[1])
			main_circ.barrier(qreg_3[0])
with else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.barrier(qreg_0[1])
	main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.171000, param_1: -0.830000, param_2: -0.069000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "636", "Optimize1qGatesDecomposition")
