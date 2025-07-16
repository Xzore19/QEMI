from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
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
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,param_3,param_0, qreg_3[0])
		main_circ.u(pi/2,-0.170000,param_1, qreg_2[0])
		main_circ.rz(param_3, qreg_0[0])
		main_circ.y(qreg_1[0])
	with case_1(1):
		main_circ.rz(-0.896000, qreg_1[0])
		main_circ.rz(param_1, qreg_2[0])
		main_circ.rz(-0.364000, qreg_1[0])
		main_circ.rz(0.232000, 0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_3, qreg_1[0])
		main_circ.y(0)
		main_circ.rz(0.625000, 0)
		main_circ.y(qreg_2[0])
	with case_1(1):
		main_circ.u(param_2,param_0,param_2, qreg_3[0])
		main_circ.rz(param_3, qreg_2[0])
		main_circ.u(pi/2,0.490000,0.778000, 0)
		main_circ.y(qreg_0[0])
main_circ.s(qreg_3[0])
main_circ.u(param_1,param_1,param_0, qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[0])
		main_circ.s(qreg_3[0])
		main_circ.rz(0.210000, qreg_0[0])
		main_circ.rz(param_0, 0)
	with case_1(1):
		main_circ.u(pi/2,-0.769000,0.240000, qreg_0[0])
		main_circ.s(qreg_0[0])
		main_circ.y(qreg_3[0])
		main_circ.y(qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_1, qreg_3[0])
		main_circ.y(qreg_3[0])
		main_circ.y(qreg_2[0])
		main_circ.u(param_0,param_3,param_3, qreg_3[0])
	with case_1(1):
		main_circ.rz(0.412000, qreg_3[0])
		main_circ.s(qreg_0[0])
		main_circ.rz(0.341000, 0)
		main_circ.u(param_2,-0.630000,param_3, 0)
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_1,param_2,0.176000, 0)
	main_circ.rz(0.499000, qreg_0[0])
	main_circ.y(qreg_3[0])
	main_circ.y(qreg_1[0])
	main_circ.s(qreg_3[0])
with else_1:
	main_circ.s(qreg_2[0])
	main_circ.u(pi/2,param_3,-0.286000, qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(qreg_1[0])
	main_circ.rz(param_2, 0)
with else_1:
	main_circ.u(param_1,0.231000,0.717000, 0)
	main_circ.rz(param_0, 0)
main_circ.s(qreg_1[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_2,-0.735000,param_3, qreg_1[0])
		main_circ.u(pi/2,param_2,-0.200000, qreg_1[0])
		main_circ.rz(-0.957000, qreg_1[0])
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.barrier(0)
bindings = {param_0: 0.465000, param_1: -0.841000, param_2: -0.316000, param_3: -0.122000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1753", "Optimize1qGatesSimpleCommutation")
