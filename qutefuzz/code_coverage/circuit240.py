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
subcirc0.rz(-0.047000, qreg_2[0])
subcirc0.u(0.078000,-0.459000,-0.787000, qreg_2[1])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.cy(qreg_2[1],qreg_2[0])
subcirc0.rz(0.213000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.cy(qreg_0[2],qreg_0[0])
subcirc1.u(-0.378000,0.979000,0.527000, qreg_0[3])
subcirc1.rz(0.551000, qreg_0[3])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_1[1],qreg_0[0])
subcirc2.u(-0.048000,0.535000,0.543000, qreg_1[0])
subcirc2.u(0.458000,0.819000,0.356000, qreg_3[0])
subcirc2.cy(qreg_1[1],qreg_1[0])
subcirc2.rz(0.038000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(-0.592000,param_1,param_0, 2)
		main_circ.append(subcirc0,[1,0,3,2])
	with else_1:
		main_circ.rx(param_1, 2)
with else_2:
	main_circ.cy(0,3)
	main_circ.u(0.732000,0.937000,-0.084000, 1)
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(0)
	main_circ.barrier(2)
main_circ.append(subcirc0,[3,0,1,2])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(-0.353000,-0.992000,0.248000, 3)
				main_circ.rz(0.034000, 3)
				main_circ.rx(param_0, 3)
				main_circ.append(subcirc0,[0,3,2,1])
			with case_1(1):
				main_circ.append(subcirc0,[3,2,1,0])
	with case_2(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rz(param_0, 0)
			main_circ.rz(param_1, 0)
			main_circ.barrier(3)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.rz(0.180000, 3)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[2,3,1,0])
			with case_1(1):
				main_circ.rx(param_2, 0)
				main_circ.rz(param_2, 0)
				main_circ.u(param_1,0.465000,0.744000, 1)
				main_circ.rx(-0.711000, 2)
main_circ.rz(0.243000, 2)
main_circ.rx(-0.740000, 1)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.cy(0,2)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cy(1,2)
				main_circ.cy(2,1)
				main_circ.cy(1,0)
				main_circ.cy(2,0)
			with case_1(1):
				main_circ.cy(2,1)
				main_circ.cy(2,0)
				main_circ.u(param_1,param_2,param_1, 3)
				main_circ.u(param_2,param_1,param_2, 2)
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(2,0)
			main_circ.append(subcirc0,[2,0,1,3])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(-0.736000,param_1,-0.713000, 1)
			main_circ.cy(1,0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.id(1)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(0)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(3)
		with else_1:
			main_circ.id(2)
		main_circ.barrier(1)
	with case_2(1):
		main_circ.barrier(3)
bindings = {param_0: -0.353000, param_1: -0.281000, param_2: -0.827000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "240")
