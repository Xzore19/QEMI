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
subcirc0.h(qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_3[0])
subcirc0.ry(-0.924000, qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.h(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,-0.627000,-0.424000, qreg_0[0])
subcirc1.h(qreg_0[0])
subcirc1.u(pi/2,-0.489000,-0.928000, qreg_2[0])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.228000, qreg_3[0])
subcirc2.h(qreg_0[0])
subcirc2.u(pi/2,0.197000,-0.361000, qreg_0[2])
subcirc2.cx(qreg_0[1],qreg_0[2])
subcirc2.cx(qreg_3[0],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

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

main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(0)
	with case_1(1):
		main_circ.h(3)
		main_circ.h(1)
		main_circ.cx(2,0)
		main_circ.cx(1,2)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,-0.434000,param_0, 0)
main_circ.cx(2,3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cx(1,2)
		main_circ.ry(-0.095000, 0)
		main_circ.id(3)
	with case_1(1):
		main_circ.id(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(param_3, 2)
	main_circ.h(2)
with else_1:
	main_circ.cx(3,2)
	main_circ.id(1)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(3)
	with case_1(1):
		main_circ.ry(param_0, 3)
		main_circ.cx(1,2)
		main_circ.barrier(3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,-0.618000,0.674000, 2)
	main_circ.cx(2,1)
	main_circ.u(pi/2,param_3,param_2, 3)
	main_circ.barrier(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(-0.515000, 3)
	main_circ.h(1)
	main_circ.u(pi/2,param_4,param_3, 3)
	main_circ.id(1)
main_circ.cx(0,1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,param_5,-0.750000, 1)
	main_circ.cx(2,1)
	main_circ.ry(0.272000, 3)
	main_circ.id(0)
with else_1:
	main_circ.id(0)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(pi/2,param_5,param_4, 2)
	main_circ.barrier(3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.id(0)
main_circ.u(param_2,0.178000,param_4, 3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(1)
	with case_1(1):
		main_circ.id(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(1)
	main_circ.ry(param_5, 1)
with else_1:
	main_circ.barrier(0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(pi/2,-0.800000,param_3, 3)
	main_circ.ry(param_1, 1)
	main_circ.cx(0,3)
	main_circ.ry(param_4, 1)
	main_circ.h(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(0,3)
	main_circ.u(pi/2,param_5,-0.544000, 2)
	main_circ.barrier(3)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.h(2)
	main_circ.barrier(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(param_4, 1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(2,3)
	main_circ.cx(0,1)
	main_circ.cx(0,2)
with else_1:
	main_circ.cx(2,0)
	main_circ.id(1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(3)
main_circ.cx(2,1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(pi/2,-0.784000,param_0, 0)
with else_1:
	main_circ.id(0)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(param_0, 2)
	main_circ.ry(0.769000, 3)
	main_circ.id(3)
with else_1:
	main_circ.ry(param_5, 0)
	main_circ.cx(3,2)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(-0.162000, 3)
	main_circ.h(3)
	main_circ.barrier(0)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_2, 0)
		main_circ.cx(3,2)
		main_circ.barrier(3)
	with case_1(1):
		main_circ.h(2)
		main_circ.id(3)
bindings = {param_0: 0.866000, param_1: 0.710000, param_2: -0.346000, param_3: -0.989000, param_4: -0.309000, param_5: -0.559000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1119", "RemoveFinalReset")
