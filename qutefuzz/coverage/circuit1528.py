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
subcirc0.y(qreg_0[0])
subcirc0.u(0.633000,-0.151000,-0.791000, qreg_0[0])
subcirc0.u(0.271000,-0.016000,0.626000, qreg_1[0])
subcirc0.rz(-0.250000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.402000, qreg_3[0])
subcirc1.u(0.202000,0.809000,0.013000, qreg_3[0])
subcirc1.u(-0.838000,-0.876000,-0.499000, qreg_3[0])
subcirc1.rz(0.827000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

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

main_circ.y(0)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.rz(param_2, qreg_0[0])
		main_circ.append(subcirc0,[qreg_0[0],0,2,3,1])
	with case_2(1):
		main_circ.u(param_1,0,param_1, qreg_0[0])
		main_circ.id(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_2,param_2,-0.622000, 1)
		main_circ.rz(0.573000, 3)
		main_circ.u(param_0,-0.591000,-0.376000, qreg_0[0])
		main_circ.append(subcirc0,[0,3,qreg_0[0],2,1])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc0,[3,2,1,qreg_0[0],0])
	with else_1:
		main_circ.rz(-0.995000, 1)
		main_circ.rz(param_1, 3)
		main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.rz(0.683000, 1)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.y(qreg_0[0])
	main_circ.barrier(1)
main_circ.u(0.534000,param_2,-0.584000, 2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(param_2,0.348000,0.988000, 3)
with else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_1,0,0.086000, qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.rz(param_0, 2)
	main_circ.id(1)
with else_2:
	main_circ.append(subcirc0,[qreg_0[0],0,3,2,1])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.append(subcirc0,[2,0,3,qreg_0[0],1])
		with else_1:
			main_circ.u(param_1,0,param_1, qreg_0[0])
	with case_2(1):
		main_circ.append(subcirc0,[2,1,3,0,qreg_0[0]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(0.148000,0.595000,0.814000, 3)
			main_circ.y(qreg_0[0])
			main_circ.append(subcirc0,[qreg_0[0],0,2,1,3])
		with case_1(1):
			main_circ.u(0,param_0,param_0, qreg_0[0])
			main_circ.y(1)
			main_circ.barrier(2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0,param_0,-0.464000, 2)
		main_circ.u(param_1,0,-0.739000, 3)
		main_circ.u(0,0,param_0, 1)
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0,0,param_0, 3)
		main_circ.id(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0.126000,param_1,0.982000, 3)
			main_circ.u(param_1,param_0,0.863000, qreg_0[0])
			main_circ.u(-0.690000,-0.012000,0.327000, qreg_0[0])
			main_circ.barrier(2)
		with case_1(1):
			main_circ.y(1)
			main_circ.barrier(1)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_2,0,param_0, qreg_0[0])
				main_circ.u(param_1,0,param_1, 3)
				main_circ.id(3)
			with case_1(1):
				main_circ.id(0)
		main_circ.id(2)
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.id(1)
		main_circ.id(2)
bindings = {param_0: 0.238000, param_1: -0.014000, param_2: 0.451000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1528", "ResetAfterMeasureSimplification")
