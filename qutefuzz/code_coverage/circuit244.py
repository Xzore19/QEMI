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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,0,0.237000, qreg_0[0])
	main_circ.u(0,param_0,-0.904000, qreg_1[0])
	main_circ.u(pi/2,param_0,param_2, 1)
	main_circ.x(1)
with else_1:
	main_circ.x(qreg_3[0])
	main_circ.x(qreg_2[0])
	main_circ.u(0,0,param_0, qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.h(qreg_2[0])
		main_circ.x(1)
		main_circ.h(qreg_0[0])
		main_circ.u(pi/2,0.929000,param_1, qreg_0[0])
	with case_1(1):
		main_circ.h(qreg_0[0])
		main_circ.h(0)
		main_circ.h(0)
		main_circ.h(1)
main_circ.x(qreg_1[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,param_0,-0.428000, qreg_1[0])
		main_circ.u(param_2,param_1,0.948000, qreg_0[0])
		main_circ.u(param_0,0.142000,0.526000, qreg_2[0])
		main_circ.u(0,param_1,param_1, qreg_3[0])
	with case_1(1):
		main_circ.u(pi/2,0.899000,param_0, qreg_2[0])
		main_circ.h(qreg_2[0])
		main_circ.h(0)
		main_circ.u(param_1,0,0.126000, qreg_3[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(1)
		main_circ.x(1)
		main_circ.u(param_2,0.357000,0.568000, 1)
		main_circ.x(1)
	with case_1(1):
		main_circ.h(qreg_2[0])
		main_circ.x(qreg_2[0])
		main_circ.x(qreg_2[0])
		main_circ.u(pi/2,0.617000,param_0, qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.x(qreg_1[0])
	main_circ.h(1)
	main_circ.x(qreg_1[0])
with else_1:
	main_circ.x(1)
	main_circ.h(qreg_1[0])
	main_circ.u(0,param_1,-0.684000, qreg_2[0])
	main_circ.h(qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,0.170000,-0.204000, qreg_1[0])
	main_circ.u(param_2,0,param_1, 1)
	main_circ.u(pi/2,param_2,param_1, qreg_2[0])
	main_circ.h(0)
main_circ.x(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,param_1,param_2, qreg_1[0])
with else_1:
	main_circ.x(qreg_2[0])
	main_circ.u(0,param_2,0.466000, qreg_3[0])
bindings = {param_0: -0.904000, param_1: 0.940000, param_2: 0.216000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "244")
