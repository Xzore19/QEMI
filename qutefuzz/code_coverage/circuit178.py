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
subcirc0.x(qreg_3[0])
subcirc0.y(qreg_0[0])
subcirc0.x(qreg_0[2])
subcirc0.x(qreg_0[2])
subcirc0.y(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_2[1])
subcirc1.x(qreg_2[0])
subcirc1.x(qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.rx(-0.403000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(2)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rx(param_4, qreg_3[0])
		main_circ.u(-0.930000,param_2,param_1, qreg_3[0])
		main_circ.rx(param_1, 1)
		main_circ.y(1)
		main_circ.y(1)
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.y(1)
			main_circ.x(qreg_0[2])
			main_circ.u(0.427000,0.793000,param_4, qreg_0[2])
			main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],0,qreg_3[0],qreg_0[1],1])
		with case_1(1):
			main_circ.x(0)
			main_circ.append(subcirc0,[1,qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1],0])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.y(qreg_3[0])
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.id(qreg_0[2])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.x(qreg_0[1])
			main_circ.u(0.742000,0.353000,param_0, qreg_0[2])
			main_circ.y(qreg_0[0])
			main_circ.y(qreg_3[0])
		with case_1(1):
			main_circ.y(qreg_0[2])
			main_circ.rx(0.229000, qreg_3[0])
			main_circ.append(subcirc0,[0,qreg_0[2],1,qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.x(qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0.338000,-0.972000,param_4, qreg_3[0])
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],qreg_0[2],0,qreg_0[1],1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rx(0.662000, qreg_0[2])
		main_circ.x(0)
		main_circ.y(qreg_0[1])
	with else_1:
		main_circ.u(-0.346000,0.290000,0.228000, 0)
		main_circ.y(qreg_0[1])
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_4,param_0,param_3, qreg_3[0])
			main_circ.y(qreg_0[1])
			main_circ.y(qreg_0[2])
			main_circ.rx(param_0, 1)
		with case_1(1):
			main_circ.x(1)
			main_circ.barrier(qreg_0[0])
main_circ.u(0.295000,param_0,param_3, qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.y(qreg_0[0])
	with else_1:
		main_circ.x(0)
		main_circ.u(0.163000,param_0,0.498000, 0)
		main_circ.u(param_4,param_4,param_2, qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[0])
	main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.barrier(1)
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(0)
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.id(0)
	main_circ.barrier(0)
bindings = {param_0: 0.990000, param_1: -0.372000, param_2: -0.204000, param_3: 0.365000, param_4: -0.817000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "178")
