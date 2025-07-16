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
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(qreg_0[1])
		main_circ.ry(param_0, qreg_0[3])
		main_circ.y(qreg_0[1])
		main_circ.u(param_3,0.585000,param_0, qreg_0[0])
	with case_1(1):
		main_circ.y(qreg_0[2])
		main_circ.cz(qreg_0[1],qreg_0[2])
		main_circ.u(param_3,param_0,0.099000, qreg_0[1])
		main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(qreg_0[0],qreg_0[2])
	main_circ.cz(qreg_0[0],qreg_0[3])
with else_1:
	main_circ.ry(0.138000, qreg_0[2])
	main_circ.u(pi/2,0.687000,param_3, qreg_0[3])
	main_circ.ry(-0.303000, qreg_0[2])
main_circ.u(pi/2,param_3,param_3, qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(qreg_0[3],qreg_0[0])
with else_1:
	main_circ.ry(-0.047000, qreg_0[2])
	main_circ.cz(qreg_0[2],qreg_0[1])
	main_circ.u(pi/2,-0.858000,-0.414000, qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(qreg_0[0])
	main_circ.u(param_3,param_3,param_1, qreg_0[0])
	main_circ.y(qreg_0[0])
	main_circ.ry(-0.079000, qreg_0[3])
	main_circ.u(param_3,param_2,0.428000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(qreg_0[0])
	main_circ.u(param_3,param_1,param_3, qreg_0[0])
	main_circ.y(qreg_0[0])
	main_circ.cz(qreg_0[3],qreg_0[1])
	main_circ.ry(-0.006000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(qreg_0[1],qreg_0[3])
	main_circ.ry(param_1, qreg_0[0])
	main_circ.u(pi/2,param_0,param_0, qreg_0[3])
	main_circ.u(param_0,-0.324000,0.467000, qreg_0[2])
	main_circ.ry(param_2, qreg_0[0])
with else_1:
	main_circ.y(qreg_0[1])
	main_circ.cz(qreg_0[0],qreg_0[3])
	main_circ.u(param_3,-0.973000,0.814000, qreg_0[2])
	main_circ.y(qreg_0[2])
	main_circ.u(pi/2,param_2,-0.075000, qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[0],qreg_0[3])
		main_circ.cz(qreg_0[3],qreg_0[1])
		main_circ.cz(qreg_0[0],qreg_0[1])
		main_circ.cz(qreg_0[3],qreg_0[1])
	with case_1(1):
		main_circ.cz(qreg_0[2],qreg_0[0])
		main_circ.cz(qreg_0[2],qreg_0[1])
		main_circ.cz(qreg_0[0],qreg_0[1])
		main_circ.ry(param_0, qreg_0[1])
main_circ.cz(qreg_0[2],qreg_0[3])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_0[2],qreg_0[0])
	main_circ.u(param_3,param_2,-0.068000, qreg_0[2])
	main_circ.cz(qreg_0[1],qreg_0[3])
	main_circ.u(pi/2,param_2,param_1, qreg_0[2])
	main_circ.y(qreg_0[3])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.ry(param_2, qreg_0[3])
		main_circ.ry(-0.566000, qreg_0[3])
		main_circ.barrier(qreg_0[3])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.887000, param_1: -0.309000, param_2: -0.689000, param_3: 0.971000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1615")
