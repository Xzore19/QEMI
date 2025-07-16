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
subcirc0.u(pi/2,0.583000,0.996000, qreg_0[1])
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.u(pi/2,-0.746000,0.981000, qreg_0[2])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_2[0],qreg_0[1])
subcirc1.y(qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.cz(qreg_0[1],qreg_3[0])
subcirc1.u(pi/2,0.705000,0.849000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[3])
subcirc2.u(pi/2,0.199000,0.104000, qreg_0[3])
subcirc2.cz(qreg_0[0],qreg_0[2])
subcirc2.u(pi/2,0.160000,0.953000, qreg_0[3])
subcirc2.cz(qreg_0[2],qreg_0[3])
subcirc2.u(pi/2,-0.574000,-0.198000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(pi/2,-0.229000,0.694000, qreg_1[0])
subcirc3.h(qreg_2[1])
subcirc3.h(qreg_2[0])
subcirc3.h(qreg_2[0])
subcirc3.y(qreg_0[0])
subcirc3.cz(qreg_1[0],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.h(qreg_0[2])
with else_1:
	main_circ.y(qreg_3[0])
	main_circ.h(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,param_1,param_3, qreg_0[2])
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.y(qreg_3[0])
		main_circ.id(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_0[2]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_3[0]])
with else_1:
	main_circ.id(qreg_0[1])
main_circ.h(qreg_3[0])
main_circ.cz(qreg_3[0],qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[2])
	with case_1(1):
		main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.h(qreg_0[2])
		main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_1,param_3,param_0, qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_3,0.779000,-0.611000, qreg_0[2])
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.u(param_0,param_3,0.551000, qreg_0[2])
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(qreg_0[1])
	main_circ.u(pi/2,param_0,param_0, qreg_3[0])
	main_circ.y(qreg_0[0])
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_0[0],qreg_0[2])
	main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(qreg_0[1],qreg_0[0])
with else_1:
	main_circ.cz(qreg_3[0],qreg_0[0])
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,param_0,param_0, qreg_0[2])
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(qreg_0[0],qreg_0[2])
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_3[0])
	with case_1(1):
		main_circ.h(qreg_0[2])
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(qreg_0[2])
with else_1:
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_3,-0.876000,param_1, qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_3[0])
	with case_1(1):
		main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,0.788000,0.472000, qreg_0[0])
	main_circ.h(qreg_3[0])
with else_1:
	main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.h(qreg_3[0])
bindings = {param_0: 0.841000, param_1: -0.588000, param_3: 0.249000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1723", "OptimizeAnnotated")
