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
subcirc0.z(qreg_0[1])
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.cx(qreg_0[3],qreg_0[1])
subcirc0.u(0,0,-0.750000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.505000, qreg_2[1])
subcirc1.cx(qreg_0[1],qreg_2[1])
subcirc1.cz(qreg_2[1],qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc0,[1,0,2,3])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cx(0,qreg_0[0])
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[qreg_0[0],2,0,3,1])
		with case_1(1):
			main_circ.z(3)
			main_circ.cx(3,2)
			main_circ.u(0,param_3,param_0, qreg_0[0])
			main_circ.cx(0,2)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cz(1,2)
		main_circ.u(0,param_1,0.301000, 1)
		main_circ.cz(qreg_0[1],2)
		main_circ.u(0,0,param_0, 3)
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc0,[0,3,qreg_0[0],qreg_0[1]])
		with case_1(1):
			main_circ.u(param_4,0,-0.745000, 2)
			main_circ.cz(3,qreg_0[1])
			main_circ.u(0,param_1,-0.806000, 1)
			main_circ.cz(qreg_0[0],0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.cx(qreg_0[0],0)
with else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0,param_1,0.395000, 1)
			main_circ.append(subcirc1,[1,qreg_0[0],2,qreg_0[1],3])
		with case_1(1):
			main_circ.z(3)
			main_circ.cz(3,qreg_0[1])
			main_circ.cx(qreg_0[0],1)
			main_circ.z(3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],1,0,2])
			main_circ.z(qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(1,qreg_0[0])
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(0,2)
			main_circ.u(param_1,param_4,param_3, 0)
			main_circ.cx(qreg_0[1],3)
			main_circ.cz(1,qreg_0[0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.z(qreg_0[0])
		main_circ.cz(qreg_0[1],3)
		main_circ.cz(3,0)
		main_circ.z(qreg_0[0])
	with else_1:
		main_circ.z(qreg_0[0])
		main_circ.cx(3,qreg_0[0])
		main_circ.u(0,0,0.743000, 1)
		main_circ.cz(qreg_0[0],3)
		main_circ.cx(qreg_0[0],1)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.z(1)
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cx(3,0)
			main_circ.barrier(3)
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(2)
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(2)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.id(1)
		main_circ.barrier(qreg_0[1])
	with case_2(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.barrier(qreg_0[1])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.barrier(qreg_0[1])
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[1])
		with else_1:
			main_circ.id(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.barrier(1)
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.id(2)
bindings = {param_0: -0.646000, param_1: -0.364000, param_3: 0.967000, param_4: 0.887000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1810", "Collect2qBlocks")
