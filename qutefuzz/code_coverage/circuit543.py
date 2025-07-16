from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(1)
			main_circ.cx(qreg_1[2],qreg_1[0])
			main_circ.y(0)
			main_circ.y(qreg_0[0])
		with case_1(1):
			main_circ.y(qreg_1[1])
			main_circ.rx(-0.450000, 0)
			main_circ.u(param_1,0.386000,param_2, qreg_1[0])
			main_circ.cx(qreg_1[2],qreg_1[0])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(qreg_1[1],0)
	main_circ.measure(qreg_1[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.y(1)
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_1[1],0)
			main_circ.y(0)
			main_circ.rx(0.436000, qreg_1[1])
			main_circ.u(param_0,-0.162000,-0.489000, qreg_1[0])
		with case_1(1):
			main_circ.cx(0,qreg_1[2])
			main_circ.y(qreg_1[0])
			main_circ.cx(qreg_1[0],1)
			main_circ.cx(0,qreg_1[1])
main_circ.measure(qreg_1[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(qreg_0[0])
			main_circ.u(param_0,-0.714000,-0.882000, qreg_1[2])
			main_circ.rx(0.430000, qreg_0[0])
			main_circ.u(param_1,-0.733000,-0.829000, qreg_1[2])
		with case_1(1):
			main_circ.y(qreg_0[0])
			main_circ.y(qreg_1[0])
			main_circ.y(0)
			main_circ.u(pi/2,-0.825000,-0.586000, qreg_0[0])
main_circ.cx(qreg_1[2],qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.y(1)
			main_circ.cx(qreg_1[1],qreg_1[0])
		with else_1:
			main_circ.u(param_2,0.242000,param_1, qreg_1[0])
			main_circ.u(param_2,param_2,param_1, 1)
	with case_2(1):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.y(qreg_1[2])
			main_circ.u(param_0,0.651000,-0.108000, 0)
			main_circ.y(qreg_1[2])
			main_circ.u(param_1,param_0,0.779000, 0)
			main_circ.u(pi/2,-0.835000,-0.540000, qreg_1[2])
		with else_1:
			main_circ.y(qreg_1[1])
main_circ.rx(param_1, 1)
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(0,qreg_0[0])
			main_circ.cx(qreg_1[0],qreg_0[0])
			main_circ.cx(qreg_1[0],qreg_1[2])
			main_circ.cx(qreg_0[0],0)
		with case_1(1):
			main_circ.cx(0,qreg_0[0])
			main_circ.cx(0,qreg_1[2])
			main_circ.cx(qreg_1[0],qreg_1[2])
			main_circ.rx(param_0, 1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_2,0.138000,param_2, qreg_1[2])
				main_circ.u(pi/2,0.092000,param_1, qreg_1[0])
				main_circ.y(qreg_1[0])
				main_circ.rx(param_0, qreg_0[0])
			with case_1(1):
				main_circ.u(pi/2,param_1,param_0, qreg_0[0])
				main_circ.y(qreg_1[0])
				main_circ.cx(1,qreg_0[0])
				main_circ.y(1)
	with case_2(1):
		main_circ.barrier(1)
bindings = {param_0: -0.244000, param_1: -0.694000, param_2: -0.850000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "543", "CollectMultiQBlocks")
