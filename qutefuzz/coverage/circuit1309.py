from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.x(qreg_0[1])
		main_circ.u(0,0,param_0, qreg_0[0])
		main_circ.z(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0,0,-0.702000, qreg_0[0])
			main_circ.u(0,param_1,0.647000, qreg_0[0])
			main_circ.z(qreg_0[2])
			main_circ.u(pi/2,-0.660000,param_1, qreg_0[1])
		with case_1(1):
			main_circ.z(qreg_0[2])
			main_circ.z(qreg_0[2])
			main_circ.u(param_0,0,0.868000, qreg_0[0])
			main_circ.u(param_1,param_1,param_1, qreg_0[1])
main_circ.u(0,0,param_0, qreg_0[0])
main_circ.z(qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.z(qreg_0[1])
			main_circ.u(0,0,param_0, qreg_0[2])
			main_circ.u(0,0,-0.516000, qreg_0[2])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0,param_1,0.230000, qreg_0[0])
			main_circ.u(0,param_0,param_1, qreg_0[3])
			main_circ.u(0,0,-0.056000, qreg_0[2])
			main_circ.z(qreg_0[0])
			main_circ.u(pi/2,param_1,param_1, qreg_0[2])
		with else_1:
			main_circ.z(qreg_0[2])
			main_circ.u(param_1,0.585000,0.007000, qreg_0[1])
			main_circ.u(param_0,0.737000,-0.461000, qreg_0[2])
			main_circ.u(0,param_0,0.601000, qreg_0[2])
	with case_2(1):
		main_circ.x(qreg_0[2])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(qreg_0[3])
			main_circ.u(param_0,param_1,param_1, qreg_0[2])
			main_circ.u(param_1,-0.582000,-0.491000, qreg_0[1])
			main_circ.u(param_1,param_0,0.752000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.x(qreg_0[0])
		main_circ.z(qreg_0[0])
	with else_1:
		main_circ.u(param_0,param_1,param_1, qreg_0[2])
		main_circ.z(qreg_0[3])
		main_circ.x(qreg_0[1])
		main_circ.u(0,param_1,param_1, qreg_0[1])
		main_circ.u(param_1,param_0,-0.376000, qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(0,0,-0.234000, qreg_0[2])
			main_circ.u(param_0,0,param_0, qreg_0[0])
			main_circ.x(qreg_0[3])
			main_circ.x(qreg_0[3])
		with case_1(1):
			main_circ.z(qreg_0[3])
			main_circ.u(0,0,-0.118000, qreg_0[0])
			main_circ.z(qreg_0[0])
			main_circ.u(param_1,0.587000,param_1, qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.z(qreg_0[0])
		main_circ.u(param_1,param_1,-0.535000, qreg_0[3])
		main_circ.u(param_1,param_1,0.875000, qreg_0[1])
		main_circ.z(qreg_0[0])
		main_circ.u(param_1,param_0,param_1, qreg_0[1])
main_circ.u(param_1,param_1,-0.468000, qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_1,param_1,param_0, qreg_0[3])
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[3])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[1])
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[1])
	with else_1:
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_0[3])
	with else_1:
		main_circ.id(qreg_0[3])
	main_circ.id(qreg_0[2])
bindings = {param_0: 0.547000, param_1: 0.218000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1309", "RemoveDiagonalGatesBeforeMeasure")
