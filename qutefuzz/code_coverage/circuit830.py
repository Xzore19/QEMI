from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.u(-0.058000,-0.761000,-0.525000, qreg_0[1])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_0,param_0,-0.761000, qreg_3[0])
		main_circ.z(qreg_0[0])
		main_circ.u(pi/2,param_1,param_1, qreg_3[0])
		main_circ.u(param_0,param_2,param_0, qreg_2[0])
with else_2:
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.z(qreg_0[0])
		main_circ.u(param_1,-0.285000,param_2, qreg_3[0])
		main_circ.z(qreg_2[0])
		main_circ.u(pi/2,0.288000,param_0, qreg_0[1])
	with else_1:
		main_circ.z(qreg_0[0])
		main_circ.u(pi/2,0.856000,-0.629000, qreg_0[1])
		main_circ.u(param_0,0.267000,0.080000, qreg_3[0])
		main_circ.u(param_1,param_1,-0.277000, qreg_3[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(qreg_0[0])
		main_circ.z(qreg_0[1])
		main_circ.h(qreg_3[0])
		main_circ.u(param_0,-0.012000,-0.020000, qreg_0[1])
	with else_1:
		main_circ.u(pi/2,param_1,param_1, qreg_0[0])
		main_circ.u(param_1,param_2,param_0, qreg_2[0])
		main_circ.u(pi/2,param_2,-0.639000, qreg_0[1])
		main_circ.u(pi/2,param_1,0.685000, qreg_0[0])
		main_circ.z(qreg_0[1])
with else_2:
	main_circ.h(qreg_0[1])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.z(qreg_0[1])
			main_circ.u(-0.704000,param_0,-0.937000, qreg_3[0])
			main_circ.z(qreg_0[1])
			main_circ.u(-0.813000,param_2,0.201000, qreg_2[0])
		with case_1(1):
			main_circ.u(param_0,param_0,-0.187000, qreg_0[1])
			main_circ.h(qreg_0[1])
			main_circ.u(-0.639000,-0.783000,param_0, qreg_3[0])
			main_circ.u(param_1,param_0,-0.082000, qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(qreg_3[0])
				main_circ.h(qreg_3[0])
				main_circ.u(0.252000,param_2,param_0, qreg_0[0])
				main_circ.u(0.154000,param_0,0.163000, qreg_2[0])
			with case_1(1):
				main_circ.u(param_1,-0.637000,param_1, qreg_0[1])
				main_circ.h(qreg_0[1])
				main_circ.u(param_0,param_1,param_2, qreg_0[0])
				main_circ.u(param_2,0.568000,param_0, qreg_3[0])
	with case_2(1):
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.h(qreg_0[1])
				main_circ.u(0.108000,0.675000,param_2, qreg_0[0])
				main_circ.z(qreg_0[0])
				main_circ.h(qreg_2[0])
			with case_1(1):
				main_circ.h(qreg_0[1])
				main_circ.h(qreg_0[0])
				main_circ.z(qreg_2[0])
				main_circ.barrier(qreg_3[0])
bindings = {param_0: 0.518000, param_1: 0.776000, param_2: -0.877000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "830", "CommutativeCancellation")
