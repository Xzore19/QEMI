from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0,0,-0.590000, qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.u(0,0,-0.399000, qreg_0[1])
subcirc0.u(0,0,-0.849000, qreg_3[0])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0,param_0,0.629000, qreg_0[0])
	main_circ.id(qreg_2[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(qreg_0[0])
	main_circ.cy(qreg_2[1],qreg_2[0])
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.y(qreg_2[1])
main_circ.cx(qreg_2[0],qreg_0[1])
main_circ.cy(qreg_2[1],qreg_0[1])
main_circ.y(qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[1],qreg_0[0])
		main_circ.u(0,0,param_0, qreg_0[0])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.cy(qreg_0[1],qreg_2[1])
		main_circ.cx(qreg_0[1],qreg_0[0])
		main_circ.id(qreg_0[1])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_2[1],qreg_2[0])
		main_circ.y(qreg_2[0])
		main_circ.u(param_2,0,param_1, qreg_0[0])
		main_circ.cy(qreg_2[0],qreg_2[1])
	with case_1(1):
		main_circ.y(qreg_2[1])
		main_circ.cx(qreg_2[0],qreg_0[1])
		main_circ.cx(qreg_2[1],qreg_0[0])
		main_circ.cy(qreg_2[0],qreg_2[1])
main_circ.cx(qreg_2[1],qreg_0[1])
main_circ.cy(qreg_2[1],qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_0[0],qreg_0[1])
		main_circ.barrier(qreg_2[0])
	with case_1(1):
		main_circ.y(qreg_2[0])
		main_circ.cx(qreg_0[1],qreg_2[0])
		main_circ.u(0,0,0.990000, qreg_0[1])
		main_circ.u(0,0,param_0, qreg_2[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(qreg_2[0])
		main_circ.cy(qreg_2[1],qreg_0[0])
		main_circ.y(qreg_2[1])
		main_circ.u(param_0,param_2,param_2, qreg_0[0])
	with case_1(1):
		main_circ.y(qreg_0[0])
		main_circ.cy(qreg_2[0],qreg_2[1])
		main_circ.cx(qreg_2[1],qreg_0[1])
		main_circ.u(param_1,param_1,-0.007000, qreg_2[1])
main_circ.u(param_0,0,-0.034000, qreg_0[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[1])
	with case_1(1):
		main_circ.u(0,0,param_2, qreg_0[0])
		main_circ.y(qreg_0[1])
		main_circ.cx(qreg_0[1],qreg_2[0])
		main_circ.u(0,0,param_2, qreg_0[0])
main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_2[1],qreg_0[0])
		main_circ.cx(qreg_2[0],qreg_0[0])
		main_circ.y(qreg_0[1])
		main_circ.id(qreg_0[1])
	with case_1(1):
		main_circ.cy(qreg_0[0],qreg_2[1])
		main_circ.id(qreg_2[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,param_1,-0.768000, qreg_0[0])
	main_circ.u(0,param_0,param_0, qreg_2[1])
with else_1:
	main_circ.barrier(qreg_2[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cx(qreg_0[1],qreg_2[0])
	main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.y(qreg_0[1])
with else_1:
	main_circ.u(param_1,0,-0.888000, qreg_2[1])
	main_circ.cy(qreg_2[1],qreg_0[0])
	main_circ.y(qreg_0[1])
	main_circ.barrier(qreg_2[1])
bindings = {param_0: -0.842000, param_1: -0.013000, param_2: 0.814000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "546", "CollectLinearFunctions")
