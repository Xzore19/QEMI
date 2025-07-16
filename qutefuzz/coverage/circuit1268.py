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
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(param_0,param_0,param_0, qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cx(qreg_1[0],qreg_3[0])
		main_circ.cz(qreg_3[0],0)
		main_circ.cx(qreg_2[0],qreg_1[0])
		main_circ.cx(1,qreg_0[0])
	with else_1:
		main_circ.ry(0.580000, qreg_3[0])
		main_circ.ry(param_0, qreg_0[0])
		main_circ.u(param_0,param_0,param_0, qreg_0[0])
with else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(qreg_2[0],0)
		main_circ.ry(param_0, 1)
		main_circ.cx(1,0)
		main_circ.cx(qreg_1[0],1)
	with else_1:
		main_circ.cz(qreg_0[0],qreg_2[0])
		main_circ.cx(qreg_0[0],0)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(1,qreg_2[0])
		main_circ.ry(-0.119000, 1)
		main_circ.u(pi/2,-0.104000,0.000000, qreg_1[0])
		main_circ.cz(0,qreg_0[0])
		main_circ.ry(0.602000, qreg_0[0])
	with else_1:
		main_circ.cx(qreg_1[0],qreg_0[0])
		main_circ.u(pi/2,param_0,-0.035000, qreg_1[0])
		main_circ.cx(qreg_1[0],qreg_3[0])
		main_circ.u(pi/2,-0.970000,-0.062000, qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cx(qreg_1[0],0)
		main_circ.u(param_0,param_0,-0.669000, 0)
		main_circ.cz(qreg_3[0],0)
		main_circ.u(param_0,0.139000,0.895000, qreg_3[0])
	with else_1:
		main_circ.cz(qreg_3[0],qreg_2[0])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.ry(0.037000, qreg_1[0])
			main_circ.ry(0.405000, qreg_3[0])
			main_circ.u(pi/2,param_0,param_0, qreg_3[0])
			main_circ.ry(param_0, 1)
		with case_1(1):
			main_circ.u(pi/2,0.106000,-0.510000, 0)
			main_circ.cx(qreg_0[0],qreg_1[0])
			main_circ.ry(param_0, 1)
			main_circ.ry(-0.181000, 1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.cz(1,0)
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.ry(-0.731000, qreg_3[0])
				main_circ.cz(qreg_2[0],0)
				main_circ.ry(param_0, 0)
				main_circ.cx(qreg_2[0],1)
			with case_1(1):
				main_circ.cz(qreg_3[0],qreg_1[0])
				main_circ.ry(-0.482000, qreg_2[0])
				main_circ.barrier(qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_2[0])
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.barrier(qreg_3[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.barrier(qreg_1[0])
		main_circ.id(qreg_1[0])
bindings = {param_0: -0.999000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1268")
