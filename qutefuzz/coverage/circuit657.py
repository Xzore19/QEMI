from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(0)
	main_circ.cx(0,qreg_0[0])
	main_circ.u(param_0,0,param_2, qreg_0[0])
	main_circ.z(qreg_0[2])
	main_circ.cx(qreg_0[0],qreg_3[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(0,qreg_0[1])
	main_circ.h(qreg_0[0])
with else_1:
	main_circ.u(param_0,param_1,-0.760000, qreg_3[0])
	main_circ.z(0)
	main_circ.h(0)
	main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(0,param_3,param_1, qreg_3[0])
	main_circ.cx(qreg_0[1],qreg_0[0])
	main_circ.h(qreg_3[0])
	main_circ.cx(qreg_3[0],qreg_0[2])
with else_1:
	main_circ.u(param_1,0,-0.652000, qreg_0[2])
	main_circ.z(qreg_3[0])
	main_circ.h(qreg_0[2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(qreg_0[1],qreg_3[0])
	main_circ.u(0,param_1,param_1, qreg_0[2])
with else_1:
	main_circ.h(qreg_0[2])
	main_circ.z(qreg_0[1])
	main_circ.h(qreg_3[0])
	main_circ.z(qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0,0,-0.757000, qreg_0[1])
	main_circ.u(param_0,0,-0.022000, qreg_0[1])
	main_circ.h(qreg_0[2])
	main_circ.u(param_0,0,-0.532000, qreg_0[0])
with else_1:
	main_circ.z(qreg_0[1])
	main_circ.z(qreg_0[2])
	main_circ.u(param_3,0,-0.283000, 0)
	main_circ.h(qreg_0[0])
	main_circ.u(param_2,param_1,-0.703000, qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(qreg_0[1])
	main_circ.u(param_3,param_3,-0.872000, qreg_0[2])
	main_circ.z(qreg_0[1])
	main_circ.h(qreg_0[1])
with else_1:
	main_circ.h(qreg_0[1])
	main_circ.h(qreg_0[1])
	main_circ.z(0)
	main_circ.cx(qreg_0[0],qreg_0[1])
	main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(qreg_0[2],qreg_3[0])
with else_1:
	main_circ.cx(qreg_0[1],qreg_0[0])
	main_circ.cx(qreg_0[1],0)
	main_circ.cx(qreg_0[0],qreg_3[0])
	main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[0],qreg_0[2])
		main_circ.cx(qreg_3[0],qreg_0[0])
		main_circ.cx(qreg_0[2],qreg_0[1])
		main_circ.cx(qreg_0[1],qreg_3[0])
	with case_1(1):
		main_circ.u(0,0,param_1, 0)
		main_circ.cx(qreg_0[1],qreg_0[2])
		main_circ.z(0)
		main_circ.h(0)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_0[0])
		main_circ.barrier(qreg_0[1])
	with case_1(1):
		main_circ.id(qreg_3[0])
bindings = {param_0: -0.106000, param_1: -0.097000, param_2: 0.403000, param_3: -0.460000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "657")
