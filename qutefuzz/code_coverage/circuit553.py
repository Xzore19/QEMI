from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(-0.073000, qreg_1[0])
subcirc0.s(qreg_2[0])
subcirc0.rx(0.877000, qreg_0[0])
subcirc0.ry(-0.560000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.967000, qreg_0[2])
subcirc1.ry(0.895000, qreg_0[2])
subcirc1.s(qreg_0[1])
subcirc1.rx(0.437000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.ry(0.259000, qreg_2[1])
subcirc2.s(qreg_0[0])
subcirc2.rz(-0.480000, qreg_2[0])
subcirc2.s(qreg_2[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.rx(-0.175000, qreg_1[0])
subcirc3.rx(0.279000, qreg_1[0])
subcirc3.rz(-0.217000, qreg_1[2])
subcirc3.s(qreg_1[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc2,[qreg_3[0],qreg_2[0],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_2[0]])
	with case_2(1):
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.ry(0.029000, qreg_3[0])
			main_circ.rx(param_0, qreg_3[0])
		with else_1:
			main_circ.rx(param_3, qreg_3[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rx(0.038000, qreg_2[0])
				main_circ.append(subcirc2,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_3[0]])
			with case_1(1):
				main_circ.barrier(qreg_0[1])
main_circ.rx(param_0, qreg_2[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_2[0])
main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc2,[qreg_2[0],qreg_3[0],qreg_0[0],qreg_0[1]])
			with case_1(1):
				main_circ.ry(param_1, qreg_3[0])
				main_circ.rz(-0.968000, qreg_3[0])
				main_circ.append(subcirc2,[qreg_2[0],qreg_3[0],qreg_0[0],qreg_0[1]])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.append(subcirc2,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.ry(param_3, qreg_0[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rz(-0.578000, qreg_2[0])
		main_circ.rx(param_4, qreg_2[0])
		main_circ.barrier(qreg_3[0])
	with else_1:
		main_circ.rz(0.497000, qreg_3[0])
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_2, qreg_2[0])
			main_circ.rx(-0.366000, qreg_0[1])
			main_circ.barrier(qreg_0[1])
		with case_1(1):
			main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_3[0],qreg_0[1]])
with else_2:
	main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_3[0]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_3[0]])
bindings = {param_0: 0.651000, param_1: 0.685000, param_2: 0.513000, param_3: 0.854000, param_4: -0.648000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "553", "InverseCancellation")
