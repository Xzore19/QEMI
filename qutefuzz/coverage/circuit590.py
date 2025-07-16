from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(0.932000, qreg_1[1])
subcirc0.z(qreg_0[0])
subcirc0.ry(-0.936000, qreg_3[0])
subcirc0.u(pi/2,-0.898000,0.736000, qreg_3[0])
subcirc0.z(qreg_1[0])
subcirc0.u(pi/2,-0.124000,-0.631000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_3[0])
subcirc1.u(pi/2,0.301000,0.089000, qreg_3[0])
subcirc1.u(pi/2,0.377000,-0.215000, qreg_0[0])
subcirc1.u(pi/2,0.990000,-0.683000, qreg_2[0])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_3[0])
subcirc2.h(qreg_0[1])
subcirc2.u(pi/2,-0.387000,0.413000, qreg_0[1])
subcirc2.z(qreg_0[2])
subcirc2.ry(-0.108000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(2)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.ry(param_0, 2)
		main_circ.append(subcirc2,[3,qreg_0[0],0,2])
	with case_2(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(2)
			main_circ.barrier(1)
		main_circ.u(pi/2,-0.583000,param_0, 3)
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.append(subcirc2,[3,2,0,qreg_0[0]])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(0.700000, qreg_0[0])
			main_circ.append(subcirc2,[0,3,2,1])
		with case_1(1):
			main_circ.z(qreg_0[0])
			main_circ.append(subcirc1,[1,0,2,3])
main_circ.ry(0.593000, 3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc1,[1,2,0,qreg_0[0]])
			with case_1(1):
				main_circ.id(0)
	with case_2(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_0,-0.566000,0.456000, 2)
				main_circ.id(3)
			with case_1(1):
				main_circ.ry(0.009000, 2)
				main_circ.u(param_1,param_2,-0.792000, 1)
				main_circ.append(subcirc1,[0,1,2,qreg_0[0]])
main_circ.z(0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(param_2, 0)
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc1,[0,qreg_0[0],2,1])
	with else_1:
		main_circ.barrier(2)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.h(3)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(3)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.ry(param_0, qreg_0[0])
			main_circ.u(param_1,-0.760000,-0.018000, 1)
			main_circ.id(3)
		with else_1:
			main_circ.u(pi/2,param_1,0.036000, 1)
			main_circ.id(3)
	with case_2(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.id(3)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(3)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.id(0)
		main_circ.barrier(2)
bindings = {param_0: -0.198000, param_1: 0.859000, param_2: 0.224000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "590", "Optimize1qGatesDecomposition")
