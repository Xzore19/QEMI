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
subcirc0.cz(qreg_2[1],qreg_0[0])
subcirc0.s(qreg_2[1])
subcirc0.ry(-0.558000, qreg_2[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_1[0])
subcirc1.cx(qreg_1[0],qreg_2[0])
subcirc1.s(qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_1[0])
subcirc1.cz(qreg_3[0],qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.ry(0.285000, 1)
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cz(3,2)
			main_circ.s(3)
			main_circ.append(subcirc1,[0,1,3,2])
		with case_1(1):
			main_circ.append(subcirc1,[3,0,2,1])
with else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(1)
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.s(0)
			main_circ.s(3)
			main_circ.id(0)
		with case_1(1):
			main_circ.id(0)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.ry(param_3, 0)
		main_circ.cx(2,1)
	with else_1:
		main_circ.cx(1,3)
		main_circ.ry(param_2, 3)
		main_circ.cz(0,2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.s(2)
		main_circ.s(2)
		main_circ.append(subcirc1,[1,0,2,3])
	with else_1:
		main_circ.id(1)
with else_2:
	main_circ.ry(param_2, 3)
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.s(0)
		main_circ.cx(1,3)
		main_circ.append(subcirc1,[3,2,1,0])
main_circ.s(0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.id(3)
	with case_2(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.append(subcirc1,[1,0,3,2])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cx(2,1)
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(param_1, 2)
			main_circ.cx(1,3)
			main_circ.s(3)
			main_circ.s(1)
		with case_1(1):
			main_circ.cz(3,1)
			main_circ.ry(param_2, 2)
			main_circ.cz(3,0)
			main_circ.cz(3,0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.ry(-0.465000, 0)
		main_circ.ry(param_1, 2)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(1)
	with else_1:
		main_circ.s(1)
		main_circ.s(2)
		main_circ.barrier(1)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(3)
		with case_1(1):
			main_circ.id(3)
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.id(2)
		with case_1(1):
			main_circ.barrier(2)
	main_circ.barrier(1)
bindings = {param_1: -0.698000, param_2: 0.807000, param_3: 0.264000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "181", "Collect1qRuns")
