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
subcirc0.rx(0.401000, qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.rx(-0.667000, qreg_3[0])
subcirc0.rx(-0.603000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(-0.754000, qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_0[0])
subcirc1.rx(0.410000, qreg_0[1])

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.y(3)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.y(2)
				main_circ.append(subcirc1,[1,qreg_0[0],2,3])
			with case_1(1):
				main_circ.z(1)
				main_circ.z(1)
				main_circ.rx(-0.600000, 1)
				main_circ.y(3)
	with case_2(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(0,0,-0.897000, 2)
			main_circ.append(subcirc1,[0,3,2,1])
		with else_1:
			main_circ.z(0)
			main_circ.rx(param_3, 3)
			main_circ.y(1)
			main_circ.y(qreg_0[0])
			main_circ.append(subcirc0,[3,0,qreg_0[0],2])
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[1,2,qreg_0[0],0])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.z(3)
		main_circ.append(subcirc1,[2,0,1,qreg_0[0]])
with else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_1,param_2,-0.675000, 0)
		main_circ.u(0,param_4,-0.007000, 2)
		main_circ.rx(param_1, 1)
		main_circ.z(3)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc1,[2,1,qreg_0[0],3])
main_circ.append(subcirc1,[1,2,0,qreg_0[0]])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc1,[2,3,1,0])
	with else_1:
		main_circ.id(2)
bindings = {param_1: 0.656000, param_2: 0.088000, param_3: 0.361000, param_4: 0.148000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "192")
