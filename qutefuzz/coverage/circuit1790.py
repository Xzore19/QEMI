from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
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
param_3 = Parameter("param_3")

main_circ.rz(param_3, 3)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(2,qreg_1[0])
	main_circ.rz(0.071000, 2)
	main_circ.cy(1,2)
	main_circ.u(0.439000,-0.162000,-0.141000, 2)
	main_circ.u(0.438000,param_2,param_1, 3)
main_circ.rz(param_2, 0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cy(3,qreg_0[0])
	main_circ.x(0)
	main_circ.rz(0.086000, 0)
with else_1:
	main_circ.rz(-0.687000, 2)
	main_circ.u(param_0,param_1,-0.251000, 0)
	main_circ.u(param_3,0.740000,param_1, 1)
	main_circ.rz(-0.041000, qreg_0[0])
	main_circ.rz(0.923000, 1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_2,param_0,param_3, 2)
		main_circ.x(qreg_0[0])
		main_circ.rz(-0.489000, 2)
		main_circ.cy(0,qreg_0[0])
	with case_1(1):
		main_circ.rz(-0.290000, 3)
		main_circ.x(3)
		main_circ.x(1)
		main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.170000,param_1,param_2, qreg_0[0])
	main_circ.cy(qreg_1[0],2)
	main_circ.rz(param_1, 2)
main_circ.cy(qreg_0[0],1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_2,param_2,param_1, 2)
	main_circ.cy(3,2)
with else_1:
	main_circ.cy(qreg_0[0],0)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(0)
		main_circ.u(param_2,0.587000,param_3, 1)
		main_circ.rz(param_3, 3)
		main_circ.u(-0.175000,param_0,-0.729000, 1)
	with case_1(1):
		main_circ.rz(-0.166000, 2)
		main_circ.x(qreg_0[0])
		main_circ.rz(-0.137000, 1)
		main_circ.u(param_3,param_3,-0.790000, 0)
main_circ.cy(1,qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(0,1)
	main_circ.cy(qreg_0[0],qreg_1[0])
	main_circ.cy(qreg_1[0],1)
	main_circ.cy(1,qreg_1[0])
	main_circ.cy(1,0)
with else_1:
	main_circ.x(1)
	main_circ.rz(param_3, 2)
main_circ.u(param_1,-0.118000,param_2, 2)
main_circ.cy(0,1)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.x(qreg_0[0])
		main_circ.u(0.665000,param_1,-0.123000, 2)
		main_circ.rz(param_0, 3)
		main_circ.rz(param_2, 0)
	with case_1(1):
		main_circ.rz(0.626000, qreg_0[0])
		main_circ.barrier(1)
bindings = {param_0: 0.580000, param_1: 0.944000, param_2: -0.254000, param_3: -0.642000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1790", "CommutativeInverseCancellation")
