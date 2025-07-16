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
subcirc0.cx(qreg_0[0],qreg_3[0])
subcirc0.rx(0.811000, qreg_0[1])
subcirc0.rx(0.631000, qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_3[0])
subcirc0.cx(qreg_0[2],qreg_3[0])
subcirc0.rx(0.343000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_1[2])
subcirc1.rx(0.567000, qreg_0[0])
subcirc1.ry(-0.381000, qreg_0[0])
subcirc1.rx(-0.485000, qreg_1[2])
subcirc1.rx(-0.361000, qreg_1[1])
subcirc1.ry(-0.822000, qreg_1[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.rx(param_1, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.ry(param_0, qreg_0[3])
			main_circ.rx(param_3, qreg_0[3])
			main_circ.cx(qreg_0[1],qreg_0[2])
			main_circ.ry(-0.401000, 0)
			main_circ.ry(0.032000, qreg_0[0])
		with else_1:
			main_circ.ry(param_3, 0)
			main_circ.rx(param_0, 0)
			main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[3],0,qreg_0[2]])
	with else_2:
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.z(qreg_0[2])
		with else_1:
			main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[3],0,qreg_0[1]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.ry(-0.885000, qreg_0[3])
		main_circ.rx(0.955000, qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[qreg_0[3],0,qreg_0[2],qreg_0[1],qreg_0[0]])
			with case_1(1):
				main_circ.rx(param_1, qreg_0[1])
				main_circ.cx(qreg_0[3],qreg_0[2])
				main_circ.rx(-0.150000, qreg_0[3])
				main_circ.cx(0,qreg_0[0])
	with else_2:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.ry(param_3, qreg_0[1])
			main_circ.rx(-0.775000, 0)
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],0,qreg_0[3]])
		with else_1:
			main_circ.cx(qreg_0[1],qreg_0[0])
			main_circ.cx(0,qreg_0[2])
			main_circ.cx(0,qreg_0[3])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(qreg_0[0],0)
				main_circ.append(subcirc1,[qreg_0[0],qreg_0[3],qreg_0[2],qreg_0[1]])
			with else_1:
				main_circ.cx(qreg_0[3],qreg_0[1])
		with case_2(1):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.cx(qreg_0[2],qreg_0[3])
				main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.ry(param_0, qreg_0[0])
				main_circ.id(0)
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.ry(-0.821000, qreg_0[3])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.z(qreg_0[0])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(qreg_0[0],qreg_0[3])
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[3])
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.barrier(qreg_0[2])
			with case_2(1):
				main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(0)
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(0)
			main_circ.id(0)
		with else_2:
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[2])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_0[3])
		main_circ.id(qreg_0[2])
bindings = {param_0: -0.903000, param_1: -0.580000, param_3: -0.685000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1982", "TemplateOptimization")
