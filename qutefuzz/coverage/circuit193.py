from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.s(qreg_2[0])
subcirc0.rz(0.819000, qreg_2[1])
subcirc0.y(qreg_1[0])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[3])
subcirc1.cy(qreg_0[2],qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.rz(-0.836000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[1])
subcirc2.y(qreg_0[3])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.y(qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.s(1)
main_circ.cy(2,0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cy(1,3)
	main_circ.s(3)
	main_circ.id(1)
with else_1:
	main_circ.rz(-0.873000, 2)
	main_circ.s(3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cy(1,2)
with else_1:
	main_circ.s(3)
	main_circ.cy(2,1)
	main_circ.id(1)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(0.853000, 0)
		main_circ.s(2)
		main_circ.id(0)
	with case_1(1):
		main_circ.cy(0,1)
		main_circ.rz(-0.734000, 0)
		main_circ.barrier(1)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(2)
	with case_1(1):
		main_circ.id(2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(1,3)
	main_circ.barrier(1)
main_circ.s(0)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(2)
with else_1:
	main_circ.y(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(1)
	main_circ.barrier(0)
with else_1:
	main_circ.id(0)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.y(3)
		main_circ.rz(param_5, 3)
		main_circ.y(1)
		main_circ.barrier(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_1, 0)
	main_circ.barrier(3)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(2)
	main_circ.rz(0.532000, 2)
	main_circ.s(0)
	main_circ.s(0)
	main_circ.cy(1,0)
with else_1:
	main_circ.s(2)
	main_circ.rz(-0.343000, 0)
	main_circ.barrier(1)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(0)
main_circ.s(1)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(2,0)
		main_circ.rz(-0.175000, 1)
		main_circ.cy(1,0)
		main_circ.cy(2,3)
	with case_1(1):
		main_circ.cy(1,3)
		main_circ.cy(3,2)
		main_circ.id(0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(3)
	main_circ.id(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(3)
with else_1:
	main_circ.barrier(3)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(1)
	with case_1(1):
		main_circ.id(3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(2)
	main_circ.id(2)
with else_1:
	main_circ.id(0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(2)
	with case_1(1):
		main_circ.s(1)
		main_circ.barrier(0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(3)
		main_circ.id(2)
	with case_1(1):
		main_circ.rz(-0.168000, 2)
		main_circ.y(1)
		main_circ.barrier(3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(3)
	main_circ.s(0)
	main_circ.id(1)
bindings = {param_1: 0.103000, param_5: 0.569000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "193", "CXCancellation")
