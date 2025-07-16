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
subcirc0.cx(qreg_0[1],qreg_0[3])
subcirc0.u(0.938000,0.164000,-0.139000, qreg_0[3])
subcirc0.u(-0.865000,0.415000,0.413000, qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_0[1])

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

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cx(3,1)
		main_circ.u(-0.588000,param_0,0.635000, 1)
		main_circ.cx(1,2)
		main_circ.z(0)
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.z(0)
			main_circ.u(0.210000,param_0,param_0, 2)
			main_circ.z(3)
			main_circ.u(param_3,param_3,param_2, 1)
		with case_1(1):
			main_circ.cx(1,0)
			main_circ.u(param_2,param_2,-0.551000, 2)
			main_circ.z(1)
			main_circ.u(param_3,-0.658000,0.868000, 0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cx(3,2)
		main_circ.append(subcirc0,[0,1,2,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.z(3)
		main_circ.z(3)
		main_circ.u(-0.989000,0.477000,param_2, 3)
		main_circ.z(0)
	with else_1:
		main_circ.append(subcirc0,[0,3,1,2])
main_circ.u(-0.671000,param_3,-0.542000, 1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.u(0.324000,param_0,0.270000, 0)
	with else_1:
		main_circ.z(3)
		main_circ.u(param_1,0.705000,param_3, 2)
		main_circ.append(subcirc0,[0,2,3,1])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(param_3,0.985000,param_2, 2)
			main_circ.z(0)
			main_circ.cx(1,3)
			main_circ.u(0.033000,param_3,-0.603000, 0)
		with case_1(1):
			main_circ.cx(0,2)
			main_circ.cx(1,0)
			main_circ.u(0.126000,-0.495000,param_1, 0)
			main_circ.cx(1,3)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(3,0)
		main_circ.cx(2,0)
	with else_1:
		main_circ.cx(2,1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(-0.608000,0.768000,param_1, 3)
with else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(1,2)
			main_circ.z(3)
			main_circ.z(3)
			main_circ.u(param_1,param_1,-0.984000, 2)
		with case_1(1):
			main_circ.z(3)
			main_circ.u(param_0,param_0,param_2, 0)
			main_circ.append(subcirc0,[2,0,3,1])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(0,3)
				main_circ.u(0,param_0,param_1, 2)
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(3)
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.id(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.id(1)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.barrier(0)
		main_circ.barrier(1)
	with case_2(1):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(2)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(0)
		main_circ.id(0)
bindings = {param_0: 0.453000, param_1: 0.733000, param_2: -0.930000, param_3: -0.469000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1246", "ConsolidateBlocks")
