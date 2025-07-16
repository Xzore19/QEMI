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
subcirc0.ry(0.697000, qreg_0[0])
subcirc0.u(pi/2,-0.214000,-0.493000, qreg_3[0])
subcirc0.ry(-0.443000, qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[2])
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_2[0])
subcirc1.cx(qreg_3[0],qreg_2[0])
subcirc1.x(qreg_2[0])
subcirc1.ry(0.244000, qreg_2[0])
subcirc1.ry(-0.593000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(pi/2,0.569000,-0.176000, qreg_1[0])
subcirc2.cx(qreg_0[0],qreg_1[0])
subcirc2.u(pi/2,-0.157000,-0.983000, qreg_1[0])
subcirc2.cx(qreg_1[2],qreg_1[0])
subcirc2.ry(0.923000, qreg_0[0])
subcirc2.u(pi/2,0.207000,-0.236000, qreg_1[2])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.ry(-0.009000, qreg_3[0])
subcirc3.ry(-0.001000, qreg_0[2])
subcirc3.cx(qreg_3[0],qreg_0[0])
subcirc3.u(pi/2,-0.060000,-0.221000, qreg_3[0])
subcirc3.ry(0.072000, qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cx(qreg_1[1],qreg_1[0])
subcirc4.ry(-0.115000, qreg_1[1])
subcirc4.u(pi/2,0.978000,-0.052000, qreg_1[1])
subcirc4.x(qreg_0[0])
subcirc4.ry(0.287000, qreg_1[0])
subcirc4.u(pi/2,0.859000,-0.698000, qreg_1[1])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[0,3,qreg_0[0],1])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc3,[2,0,qreg_0[0],3])
			with case_1(1):
				main_circ.ry(-0.093000, 0)
				main_circ.u(param_4,0.334000,0.738000, 3)
				main_circ.append(subcirc1,[2,1,0,3])
with else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc4,[2,0,qreg_0[0],1,3])
			with else_1:
				main_circ.cx(1,2)
				main_circ.append(subcirc2,[1,3,qreg_0[0],2,0])
		with case_2(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc2,[1,0,qreg_0[0],2,3])
			with else_1:
				main_circ.cx(0,1)
				main_circ.cx(1,qreg_0[0])
				main_circ.append(subcirc3,[3,qreg_0[0],2,1])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.barrier(3)
with else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.cx(0,3)
				main_circ.x(0)
				main_circ.barrier(2)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.u(param_4,param_1,0.854000, 0)
					main_circ.ry(-0.744000, 3)
					main_circ.id(2)
		with case_2(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(0)
			main_circ.barrier(1)
bindings = {param_1: 0.260000, param_4: 0.255000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "827", "InverseCancellation")
