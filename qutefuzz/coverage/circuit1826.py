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
subcirc0.u(pi/2,0.574000,-0.804000, qreg_3[0])
subcirc0.ry(-0.831000, qreg_0[1])
subcirc0.h(qreg_3[0])
subcirc0.ry(-0.121000, qreg_3[0])
subcirc0.ry(-0.300000, qreg_0[2])
subcirc0.ry(-0.062000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.022000,0.307000, qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_3[0])
subcirc1.y(qreg_0[1])
subcirc1.h(qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(pi/2,-0.236000,param_0, qreg_0[0])
			main_circ.h(qreg_1[0])
		with else_1:
			main_circ.y(qreg_1[2])
			main_circ.h(qreg_1[2])
			main_circ.y(qreg_1[2])
			main_circ.h(qreg_1[1])
	with case_2(1):
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,-0.625000,param_1, qreg_1[0])
			main_circ.append(subcirc1,[0,qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.u(pi/2,-0.053000,-0.413000, qreg_0[0])
			main_circ.append(subcirc1,[qreg_0[0],qreg_1[0],0,qreg_1[2]])
	with case_2(1):
		main_circ.y(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.h(0)
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.y(qreg_1[0])
			main_circ.u(pi/2,-0.459000,-0.332000, qreg_1[0])
			main_circ.barrier(qreg_1[2])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_1[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[qreg_1[1],qreg_0[0],0,qreg_1[2]])
		with case_1(1):
			main_circ.append(subcirc1,[qreg_1[1],0,qreg_0[0],qreg_1[2]])
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.y(qreg_1[2])
	with else_1:
		main_circ.h(0)
		main_circ.append(subcirc1,[qreg_0[0],qreg_1[2],0,qreg_1[0]])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_1[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.append(subcirc1,[qreg_1[0],qreg_1[2],qreg_1[1],qreg_0[0]])
	with else_1:
		main_circ.barrier(qreg_1[0])
with else_2:
	main_circ.measure(qreg_1[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(param_0,-0.733000,-0.986000, 0)
		main_circ.barrier(qreg_1[1])
	with else_1:
		main_circ.u(pi/2,param_0,param_0, qreg_1[2])
		main_circ.y(qreg_1[0])
	main_circ.y(qreg_1[2])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(qreg_1[1])
		main_circ.barrier(qreg_1[1])
	with else_1:
		main_circ.h(qreg_1[0])
		main_circ.barrier(qreg_0[0])
	main_circ.h(0)
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(0.441000, qreg_0[0])
			main_circ.h(qreg_1[2])
			main_circ.id(0)
		with case_1(1):
			main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.001000, param_1: -0.082000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1826", "CommutationAnalysis")
