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

main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(qreg_0[0],qreg_3[0])
with else_1:
	main_circ.u(param_1,-0.241000,param_1, qreg_0[1])
	main_circ.s(qreg_3[0])
	main_circ.cz(qreg_2[0],qreg_0[1])
	main_circ.s(qreg_2[0])
	main_circ.u(0.775000,-0.059000,param_0, qreg_0[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.z(qreg_0[1])
	main_circ.z(qreg_0[0])
	main_circ.cz(qreg_3[0],qreg_0[0])
with else_1:
	main_circ.u(param_0,0.147000,param_0, qreg_3[0])
	main_circ.s(qreg_3[0])
	main_circ.z(qreg_2[0])
	main_circ.z(qreg_2[0])
	main_circ.z(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(-0.315000,-0.296000,param_0, qreg_0[0])
		main_circ.u(param_2,-0.844000,0.142000, qreg_0[1])
		main_circ.s(qreg_3[0])
		main_circ.s(qreg_3[0])
	with case_1(1):
		main_circ.z(qreg_0[0])
		main_circ.z(qreg_0[1])
		main_circ.cz(qreg_3[0],qreg_0[0])
		main_circ.u(param_2,0.569000,0.434000, qreg_0[1])
main_circ.s(qreg_3[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(qreg_3[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(0.300000,-0.980000,param_0, qreg_2[0])
	main_circ.u(param_0,param_2,param_2, qreg_0[1])
	main_circ.z(qreg_0[0])
	main_circ.s(qreg_0[0])
with else_1:
	main_circ.cz(qreg_0[1],qreg_3[0])
	main_circ.cz(qreg_3[0],qreg_0[0])
	main_circ.cz(qreg_0[0],qreg_2[0])
	main_circ.cz(qreg_0[0],qreg_2[0])
	main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(qreg_0[0],qreg_3[0])
	main_circ.cz(qreg_0[0],qreg_2[0])
	main_circ.cz(qreg_0[1],qreg_2[0])
with else_1:
	main_circ.u(-0.691000,param_0,param_1, qreg_3[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(qreg_0[0],qreg_0[1])
	main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_0[1])
	main_circ.barrier(qreg_3[0])
with else_1:
	main_circ.barrier(qreg_2[0])
bindings = {param_0: -0.446000, param_1: 0.895000, param_2: 0.235000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1387")
