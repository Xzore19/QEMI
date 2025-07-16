from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_0[1],qreg_2[0])
subcirc0.u(0,0,0.252000, qreg_0[0])
subcirc0.cy(qreg_3[0],qreg_2[0])
subcirc0.u(0,0,0.818000, qreg_0[1])
subcirc0.cx(qreg_2[0],qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_3[0],qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.y(qreg_3[0])
subcirc1.y(qreg_1[1])
subcirc1.y(qreg_3[0])
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
subcirc2.cy(qreg_0[1],qreg_0[0])
subcirc2.y(qreg_3[0])
subcirc2.cx(qreg_2[0],qreg_0[0])
subcirc2.y(qreg_2[0])
subcirc2.cy(qreg_0[0],qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_3[0],1)
			main_circ.u(0,param_1,-0.755000, qreg_1[1])
			main_circ.cy(qreg_0[0],0)
			main_circ.id(qreg_1[0])
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.id(qreg_0[0])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.cy(qreg_1[0],qreg_1[1])
		with else_1:
			main_circ.cx(1,qreg_3[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[0,1,qreg_1[0],qreg_3[0]])
			with case_1(1):
				main_circ.append(subcirc2,[qreg_0[0],1,0,qreg_1[0],qreg_1[1]])
	with case_2(1):
		main_circ.y(qreg_1[1])
		main_circ.cy(qreg_3[0],1)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc2,[qreg_1[1],qreg_0[0],qreg_1[0],1,qreg_3[0]])
		with else_1:
			main_circ.id(0)
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(qreg_1[0],qreg_0[0])
			main_circ.append(subcirc0,[1,qreg_1[0],qreg_1[1],qreg_3[0]])
	with case_2(1):
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.append(subcirc0,[1,qreg_1[0],qreg_3[0],qreg_0[0]])
main_circ.cy(0,qreg_3[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cx(qreg_0[0],qreg_3[0])
		main_circ.y(1)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.y(qreg_3[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0,param_4,0.238000, qreg_1[1])
			main_circ.y(qreg_3[0])
			main_circ.u(param_3,param_0,param_0, qreg_1[1])
			main_circ.cy(0,qreg_1[1])
		with case_1(1):
			main_circ.u(param_3,0,param_4, qreg_3[0])
			main_circ.y(0)
			main_circ.id(qreg_3[0])
main_circ.cy(0,qreg_1[1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(0,param_2,param_2, 0)
		main_circ.cx(0,qreg_1[1])
		main_circ.y(qreg_0[0])
		main_circ.cy(qreg_3[0],qreg_1[0])
	with else_1:
		main_circ.id(qreg_0[0])
main_circ.u(param_4,param_3,-0.154000, 1)
bindings = {param_0: -0.559000, param_1: -0.754000, param_2: 0.926000, param_3: -0.226000, param_4: 0.090000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1808")
