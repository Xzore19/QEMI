from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cy(qreg_0[0],qreg_2[0])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.u(-0.258000,0.970000,-0.211000, qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0.u(0.861000,0.614000,-0.689000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_2[0],0)
		main_circ.z(qreg_0[0])
		main_circ.u(0.215000,param_0,0.928000, qreg_0[1])
		main_circ.cy(qreg_2[1],0)
	with case_1(1):
		main_circ.rz(param_5, qreg_0[1])
		main_circ.u(param_2,param_2,param_3, qreg_0[0])
		main_circ.id(qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(0,qreg_2[0])
		main_circ.u(param_1,-0.458000,param_5, qreg_0[0])
		main_circ.rz(param_0, qreg_2[0])
		main_circ.cy(qreg_0[0],qreg_0[1])
	with case_1(1):
		main_circ.cy(0,qreg_2[1])
		main_circ.u(param_0,param_0,param_4, qreg_2[0])
		main_circ.z(qreg_0[0])
		main_circ.id(0)
main_circ.rz(param_0, qreg_2[1])
main_circ.cy(qreg_2[1],qreg_0[0])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.cy(qreg_2[1],qreg_2[0])
	main_circ.u(0.456000,param_5,param_2, qreg_2[0])
	main_circ.u(param_3,param_1,-0.226000, qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(0)
with else_1:
	main_circ.u(-0.207000,0.130000,-0.774000, 0)
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(-0.973000,param_2,param_2, qreg_2[1])
	main_circ.cy(qreg_0[1],0)
	main_circ.rz(-0.233000, qreg_0[0])
main_circ.rz(0.952000, 0)
main_circ.rz(-0.180000, qreg_0[1])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(-0.930000,param_1,param_4, qreg_2[0])
		main_circ.cy(qreg_0[0],qreg_2[0])
		main_circ.cy(qreg_2[1],qreg_2[0])
		main_circ.rz(0.826000, qreg_0[1])
	with case_1(1):
		main_circ.cy(qreg_0[0],qreg_2[1])
		main_circ.id(qreg_2[0])
main_circ.rz(param_3, qreg_0[0])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_0[0],qreg_2[1])
		main_circ.rz(param_3, qreg_0[0])
		main_circ.z(qreg_2[1])
		main_circ.cy(qreg_2[0],qreg_0[1])
	with case_1(1):
		main_circ.id(qreg_2[1])
main_circ.cy(qreg_2[1],qreg_0[1])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rz(-0.691000, qreg_2[1])
	main_circ.u(0.643000,param_3,-0.968000, qreg_2[0])
	main_circ.u(param_3,param_1,0.726000, qreg_0[1])
	main_circ.u(-0.334000,param_5,param_4, qreg_0[0])
main_circ.cy(qreg_0[1],0)
main_circ.z(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_2,param_2,-0.718000, qreg_2[0])
with else_1:
	main_circ.cy(qreg_2[1],0)
	main_circ.cy(qreg_2[1],qreg_0[1])
	main_circ.cy(0,qreg_0[1])
	main_circ.z(qreg_0[1])
	main_circ.id(qreg_2[0])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.z(qreg_2[1])
		main_circ.barrier(qreg_2[0])
	with case_1(1):
		main_circ.cy(0,qreg_2[0])
		main_circ.rz(param_1, 0)
		main_circ.cy(qreg_2[1],qreg_2[0])
		main_circ.barrier(qreg_2[1])
main_circ.cy(qreg_2[0],0)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(qreg_2[0])
with else_1:
	main_circ.id(qreg_2[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.z(qreg_2[0])
	main_circ.cy(qreg_2[1],qreg_0[0])
	main_circ.z(qreg_2[1])
	main_circ.z(qreg_2[0])
with else_1:
	main_circ.cy(0,qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(-0.741000,param_1,param_2, qreg_2[1])
with else_1:
	main_circ.cy(0,qreg_2[1])
	main_circ.u(param_2,param_1,0.992000, qreg_0[0])
	main_circ.cy(qreg_2[1],0)
bindings = {param_0: -0.203000, param_1: -0.802000, param_2: 0.946000, param_3: 0.670000, param_4: 0.113000, param_5: -0.942000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1830", "CommutativeInverseCancellation")
