from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(2)
	main_circ.u(param_2,-0.697000,param_1, qreg_0[0])
with else_1:
	main_circ.u(0,0,0.180000, 3)
	main_circ.y(2)
	main_circ.u(param_0,param_1,0.824000, qreg_0[0])
	main_circ.u(pi/2,param_1,-0.210000, 2)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,0.305000,-0.739000, qreg_0[1])
		main_circ.y(3)
		main_circ.y(3)
		main_circ.y(2)
	with case_1(1):
		main_circ.u(0,0,0.027000, 1)
		main_circ.y(qreg_0[0])
		main_circ.y(0)
		main_circ.rz(param_2, 1)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0,0,0.614000, 0)
with else_1:
	main_circ.y(2)
	main_circ.u(param_1,param_2,param_2, 0)
	main_circ.u(param_1,param_2,param_2, qreg_0[0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(param_0,param_0,param_0, qreg_0[0])
with else_1:
	main_circ.y(qreg_0[1])
	main_circ.u(param_1,-0.851000,param_0, 1)
	main_circ.u(param_0,param_0,-0.670000, 0)
	main_circ.y(0)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(pi/2,-0.793000,-0.929000, 2)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.y(3)
		main_circ.u(0,param_2,param_2, qreg_0[0])
		main_circ.rz(-0.355000, 2)
		main_circ.u(pi/2,param_2,param_2, qreg_0[0])
	with case_1(1):
		main_circ.rz(param_2, qreg_0[1])
		main_circ.rz(param_2, 0)
		main_circ.rz(-0.652000, 0)
		main_circ.u(pi/2,-0.546000,param_2, 2)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.y(2)
		main_circ.u(0,param_0,-0.491000, 1)
		main_circ.u(0,0,param_2, qreg_0[1])
		main_circ.u(0,param_0,param_0, 1)
	with case_1(1):
		main_circ.y(3)
		main_circ.rz(param_0, 1)
		main_circ.u(param_0,0.964000,-0.013000, 3)
		main_circ.y(2)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.y(1)
		main_circ.rz(param_2, qreg_0[1])
		main_circ.y(3)
		main_circ.u(param_1,param_2,-0.177000, qreg_0[1])
	with case_1(1):
		main_circ.u(0,param_0,param_2, qreg_0[0])
		main_circ.rz(param_2, qreg_0[0])
		main_circ.rz(-0.587000, 1)
		main_circ.rz(param_0, qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(-0.371000, 2)
	main_circ.u(pi/2,-0.978000,0.382000, 2)
	main_circ.u(param_0,param_0,0.658000, qreg_0[0])
with else_1:
	main_circ.u(param_0,param_2,param_0, qreg_0[0])
	main_circ.u(pi/2,0.906000,-0.780000, 0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(2)
with else_1:
	main_circ.u(pi/2,param_0,0.952000, 0)
	main_circ.u(param_1,param_2,0.072000, qreg_0[0])
	main_circ.y(1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(2)
	main_circ.barrier(3)
bindings = {param_0: 0.194000, param_1: -0.205000, param_2: -0.548000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "566")
