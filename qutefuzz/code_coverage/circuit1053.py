from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.cy(qreg_0[2],qreg_0[3])
subcirc0.u(0,0,-0.479000, qreg_0[0])
subcirc0.ry(0.028000, qreg_0[0])
subcirc0.ry(-0.062000, qreg_0[1])
subcirc0.u(pi/2,-0.270000,-0.901000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_3,-0.342000,-0.535000, qreg_0[0])
	main_circ.cy(qreg_1[0],qreg_0[0])
	main_circ.u(0,0,-0.742000, qreg_1[1])
with else_1:
	main_circ.cy(qreg_1[1],qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_1,-0.742000,0.862000, qreg_1[1])
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(qreg_3[0],qreg_1[1])
	main_circ.id(qreg_3[0])
main_circ.u(param_0,0,-0.258000, qreg_1[1])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(qreg_1[1],qreg_3[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_1[0])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.093000, qreg_3[0])
		main_circ.u(param_1,-0.901000,-0.222000, qreg_1[0])
		main_circ.ry(-0.804000, qreg_1[0])
		main_circ.u(param_0,param_4,0.178000, qreg_3[0])
	with case_1(1):
		main_circ.ry(0.443000, qreg_0[0])
		main_circ.ry(0.637000, qreg_0[0])
		main_circ.u(pi/2,0.595000,param_1, qreg_1[0])
		main_circ.ry(-0.285000, qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.ry(param_3, qreg_1[0])
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0,0,param_3, qreg_1[0])
		main_circ.id(qreg_1[1])
	with case_1(1):
		main_circ.ry(param_4, qreg_1[1])
		main_circ.cy(qreg_1[1],qreg_0[0])
		main_circ.ry(param_1, qreg_3[0])
		main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_3[0])
main_circ.ry(param_1, qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.946000, qreg_1[1])
		main_circ.u(param_3,param_1,param_0, qreg_1[1])
		main_circ.u(0,0,param_4, qreg_1[0])
		main_circ.u(param_4,-0.923000,0.836000, qreg_0[0])
	with case_1(1):
		main_circ.ry(param_3, qreg_3[0])
		main_circ.ry(0.732000, qreg_1[0])
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(0.049000, qreg_3[0])
with else_1:
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(param_2, qreg_1[0])
	main_circ.u(0,param_2,0.073000, qreg_1[0])
	main_circ.cy(qreg_0[0],qreg_1[0])
	main_circ.id(qreg_1[0])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.u(param_1,-0.278000,param_1, qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_3[0])
main_circ.u(param_4,param_0,-0.460000, qreg_1[1])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_3, qreg_3[0])
		main_circ.ry(param_0, qreg_0[0])
		main_circ.cy(qreg_0[0],qreg_1[0])
		main_circ.cy(qreg_1[1],qreg_1[0])
	with case_1(1):
		main_circ.cy(qreg_1[0],qreg_1[1])
		main_circ.cy(qreg_0[0],qreg_1[0])
		main_circ.cy(qreg_0[0],qreg_1[0])
		main_circ.cy(qreg_1[1],qreg_0[0])
main_circ.cy(qreg_3[0],qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_0[0],qreg_1[1])
		main_circ.cy(qreg_0[0],qreg_1[0])
		main_circ.id(qreg_3[0])
	with case_1(1):
		main_circ.u(param_1,0,param_4, qreg_3[0])
		main_circ.u(param_3,param_4,param_2, qreg_3[0])
		main_circ.u(pi/2,0.257000,param_3, qreg_0[0])
		main_circ.u(pi/2,-0.243000,param_1, qreg_0[0])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_4,param_0,0.541000, qreg_0[0])
		main_circ.u(0,param_4,param_0, qreg_0[0])
		main_circ.u(0,param_2,param_1, qreg_0[0])
		main_circ.u(pi/2,param_0,param_4, qreg_3[0])
	with case_1(1):
		main_circ.u(pi/2,0.764000,0.819000, qreg_3[0])
		main_circ.id(qreg_0[0])
bindings = {param_0: 0.660000, param_1: -0.504000, param_2: 0.441000, param_3: 0.300000, param_4: 0.381000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1053")
