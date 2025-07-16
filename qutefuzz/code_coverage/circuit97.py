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
subcirc0.rx(0.048000, qreg_0[2])
subcirc0.h(qreg_3[0])
subcirc0.rx(-0.546000, qreg_0[2])
subcirc0.h(qreg_0[2])
subcirc0.y(qreg_0[0])
subcirc0.u(-0.345000,0.868000,0.320000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.929000, qreg_3[0])
subcirc1.u(-0.118000,-0.394000,-0.601000, qreg_3[0])
subcirc1.rx(-0.671000, qreg_3[0])
subcirc1.u(-0.486000,0.068000,-0.319000, qreg_0[1])
subcirc1.u(-0.040000,-0.451000,-0.370000, qreg_0[0])
subcirc1.u(0.128000,-0.488000,0.170000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.h(qreg_0[1])
subcirc2.rx(0.132000, qreg_0[1])
subcirc2.u(0.829000,-0.489000,-0.969000, qreg_2[0])
subcirc2.u(0.698000,0.183000,-0.044000, qreg_0[1])
subcirc2.y(qreg_2[0])
subcirc2.rx(0.481000, qreg_3[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
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

main_circ.u(param_1,param_0,0.795000, qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.append(subcirc0,[qreg_2[1],qreg_2[0],qreg_0[1],qreg_0[0]])
	with else_2:
		main_circ.u(-0.275000,0.691000,param_0, qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc2,[qreg_0[0],qreg_2[1],qreg_2[0],qreg_0[1]])
with else_3:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc0,[qreg_2[1],qreg_0[1],qreg_2[0],qreg_0[0]])
		with else_1:
			main_circ.h(qreg_2[0])
			main_circ.h(qreg_2[1])
			main_circ.append(subcirc2,[qreg_2[0],qreg_0[1],qreg_2[1],qreg_0[0]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.h(qreg_2[0])
				main_circ.h(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.h(qreg_0[0])
					main_circ.y(qreg_2[0])
				with else_1:
					main_circ.id(qreg_0[1])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.y(qreg_2[1])
					main_circ.rx(0.514000, qreg_0[0])
				with else_1:
					main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
		with else_2:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[0])
				with case_1(1):
					main_circ.id(qreg_2[1])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.h(qreg_0[1])
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.barrier(qreg_2[1])
bindings = {param_0: -0.603000, param_1: -0.874000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "97", "Optimize1qGates")
