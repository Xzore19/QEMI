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
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,0.743000,param_0, 3)
	main_circ.cy(1,qreg_0[1])
	main_circ.y(1)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(2)
with else_1:
	main_circ.cy(0,3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,-0.619000,param_0, qreg_0[0])
	main_circ.y(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(0,3)
	main_circ.y(2)
	main_circ.y(0)
	main_circ.cy(0,qreg_0[0])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(0.552000,param_0,-0.858000, 0)
	main_circ.u(0.071000,0.856000,-0.748000, qreg_0[1])
	main_circ.s(qreg_0[0])
	main_circ.y(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,param_0,param_0, 0)
	main_circ.s(3)
	main_circ.u(-0.041000,param_0,-0.778000, 2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,-0.149000,0.841000, qreg_0[0])
	main_circ.u(param_0,-0.972000,param_0, 0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(0)
with else_1:
	main_circ.cy(qreg_0[1],3)
	main_circ.u(param_0,param_0,param_0, qreg_0[0])
	main_circ.cy(3,qreg_0[0])
	main_circ.u(-0.950000,param_0,param_0, 2)
	main_circ.u(-0.327000,param_0,param_0, 0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(0.361000,-0.845000,param_0, qreg_0[0])
	main_circ.u(param_0,param_0,-0.802000, 1)
with else_1:
	main_circ.u(0.614000,param_0,-0.038000, 2)
	main_circ.y(2)
	main_circ.s(0)
	main_circ.y(qreg_0[1])
	main_circ.u(param_0,param_0,param_0, 1)
main_circ.y(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(2,0)
with else_1:
	main_circ.u(param_0,-0.129000,0.666000, 0)
	main_circ.y(2)
	main_circ.s(1)
	main_circ.cy(1,3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(1,2)
	main_circ.cy(qreg_0[1],0)
	main_circ.cy(2,1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(qreg_0[0],qreg_0[1])
	main_circ.cy(1,qreg_0[1])
	main_circ.cy(qreg_0[1],0)
	main_circ.cy(qreg_0[1],3)
main_circ.u(param_0,param_0,-0.572000, 1)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(qreg_0[0],0)
	main_circ.s(2)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(1)
		main_circ.s(2)
		main_circ.cy(0,2)
		main_circ.cy(3,qreg_0[1])
	with case_1(1):
		main_circ.id(1)
bindings = {param_0: 0.736000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "455", "InverseCancellation")
