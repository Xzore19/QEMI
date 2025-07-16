from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
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

main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(param_0, qreg_1[0])
	main_circ.h(qreg_1[2])
	main_circ.h(qreg_1[2])
	main_circ.h(qreg_1[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(param_1, qreg_1[0])
	main_circ.h(qreg_1[0])
with else_1:
	main_circ.ry(0.030000, qreg_1[2])
	main_circ.h(qreg_1[2])
	main_circ.cy(qreg_1[2],qreg_1[0])
	main_circ.cy(qreg_1[0],qreg_0[0])
	main_circ.h(qreg_1[1])
main_circ.ry(param_2, qreg_1[0])
main_circ.cy(qreg_1[1],qreg_0[0])
main_circ.ry(-0.565000, qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_0[0])
	main_circ.ry(param_0, qreg_1[2])
	main_circ.cy(qreg_1[2],qreg_1[0])
main_circ.measure(qreg_1[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(param_1, qreg_1[2])
	main_circ.ry(param_2, qreg_1[0])
	main_circ.cy(qreg_0[0],qreg_1[1])
	main_circ.h(qreg_1[1])
with else_1:
	main_circ.ry(-0.086000, qreg_1[2])
	main_circ.u(0,param_2,0.142000, qreg_1[1])
	main_circ.u(param_1,0,0.982000, qreg_1[1])
	main_circ.h(qreg_1[2])
main_circ.h(qreg_1[2])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.h(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_1[0],qreg_0[0])
		main_circ.u(0,0,-0.881000, qreg_1[0])
		main_circ.h(qreg_1[1])
		main_circ.cy(qreg_1[0],qreg_1[2])
	with case_1(1):
		main_circ.u(param_2,0,param_1, qreg_0[0])
		main_circ.h(qreg_1[2])
		main_circ.ry(0.506000, qreg_0[0])
		main_circ.ry(0.401000, qreg_1[2])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.h(qreg_1[0])
with else_1:
	main_circ.u(param_2,param_1,0.514000, qreg_1[2])
	main_circ.u(0,param_0,-0.348000, qreg_0[0])
	main_circ.h(qreg_1[1])
	main_circ.h(qreg_1[2])
	main_circ.ry(param_0, qreg_1[1])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.h(qreg_0[0])
		main_circ.cy(qreg_1[0],qreg_0[0])
		main_circ.cy(qreg_1[1],qreg_1[0])
		main_circ.cy(qreg_1[2],qreg_0[0])
	with case_1(1):
		main_circ.cy(qreg_1[2],qreg_1[0])
		main_circ.cy(qreg_1[2],qreg_1[1])
		main_circ.cy(qreg_1[1],qreg_0[0])
		main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(qreg_1[2],qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cy(qreg_1[0],qreg_0[0])
	main_circ.cy(qreg_1[2],qreg_1[0])
	main_circ.u(param_1,0,param_0, qreg_0[0])
	main_circ.cy(qreg_0[0],qreg_1[0])
with else_1:
	main_circ.u(0,param_0,param_2, qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0,param_1,param_1, qreg_0[0])
		main_circ.ry(param_2, qreg_1[0])
		main_circ.h(qreg_1[1])
		main_circ.cy(qreg_0[0],qreg_1[1])
	with case_1(1):
		main_circ.barrier(qreg_1[2])
bindings = {param_0: -0.423000, param_1: -0.404000, param_2: 0.000000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "868")
