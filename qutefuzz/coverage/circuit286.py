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
subcirc0.rx(0.486000, qreg_2[1])
subcirc0.u(0,0,-0.877000, qreg_0[1])
subcirc0.u(pi/2,-0.366000,-0.355000, qreg_2[0])
subcirc0.u(pi/2,0.017000,0.020000, qreg_0[1])
subcirc0.rx(0.783000, qreg_0[0])
subcirc0.u(pi/2,0.052000,0.689000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,0.511000, qreg_0[3])
subcirc1.rx(-0.229000, qreg_0[3])
subcirc1.x(qreg_0[2])
subcirc1.rx(-0.496000, qreg_0[2])
subcirc1.rx(-0.566000, qreg_0[3])
subcirc1.u(0,0,-0.762000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_2,0,param_2, 2)
			main_circ.u(param_2,0,0.459000, qreg_1[0])
			main_circ.u(pi/2,0.455000,param_1, 1)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[3,qreg_1[0],2,0,1,qreg_0[0]])
			with case_1(1):
				main_circ.u(pi/2,param_1,param_1, 0)
				main_circ.u(param_2,param_0,-0.856000, qreg_0[0])
				main_circ.rx(param_1, 2)
				main_circ.rx(-0.987000, 1)
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0,param_0,param_1, qreg_0[0])
			main_circ.append(subcirc1,[0,3,1,qreg_1[0],2])
main_circ.append(subcirc1,[2,qreg_0[0],1,3,0])
main_circ.u(param_0,param_2,0.427000, qreg_1[0])
main_circ.rx(-0.493000, qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[qreg_1[0],1,0,3,2])
		with case_1(1):
			main_circ.u(param_1,0.621000,param_0, 2)
			main_circ.append(subcirc1,[3,qreg_0[0],2,1,qreg_1[0]])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(pi/2,param_0,-0.404000, 2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.x(2)
			main_circ.u(pi/2,-0.770000,param_1, 0)
			main_circ.barrier(3)
		with case_1(1):
			main_circ.u(0,param_1,param_0, 2)
			main_circ.id(3)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_2,param_0,param_0, 3)
		main_circ.u(0,0,-0.410000, 1)
		main_circ.u(pi/2,param_0,param_2, qreg_1[0])
		main_circ.u(param_2,0.415000,-0.459000, 3)
		main_circ.id(qreg_1[0])
with else_2:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_1[0])
		with case_1(1):
			main_circ.id(2)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(2)
	main_circ.barrier(0)
bindings = {param_0: -0.499000, param_1: 0.321000, param_2: -0.647000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "286")
