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
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.rz(-0.326000, qreg_0[1])
subcirc0.ry(0.411000, qreg_0[3])
subcirc0.u(pi/2,-0.369000,0.336000, qreg_0[1])
subcirc0.cx(qreg_0[2],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.190000, qreg_0[3])
subcirc1.rz(0.563000, qreg_0[3])
subcirc1.u(pi/2,0.732000,0.933000, qreg_0[2])
subcirc1.ry(0.384000, qreg_0[0])
subcirc1.ry(0.529000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.498000, qreg_1[0])
subcirc2.rz(-0.938000, qreg_3[0])
subcirc2.ry(-0.730000, qreg_1[0])
subcirc2.cx(qreg_0[0],qreg_1[0])
subcirc2.cx(qreg_1[0],qreg_2[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.671000, qreg_2[0])
subcirc3.u(pi/2,0.251000,0.081000, qreg_2[0])
subcirc3.ry(-0.834000, qreg_0[1])
subcirc3.u(pi/2,0.358000,-0.115000, qreg_0[0])
subcirc3.ry(0.375000, qreg_2[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_2,0.851000,param_2, 2)
			main_circ.append(subcirc0,[qreg_1[0],0,qreg_0[0],2])
		with case_1(1):
			main_circ.append(subcirc3,[2,0,3,1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.barrier(3)
	with else_1:
		main_circ.append(subcirc3,[1,qreg_1[0],qreg_0[0],2])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_1[0])
			with case_1(1):
				main_circ.append(subcirc3,[qreg_1[0],1,2,0])
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.ry(param_0, qreg_1[0])
			main_circ.id(0)
		with else_1:
			main_circ.append(subcirc3,[1,0,qreg_0[0],3])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc3,[qreg_0[0],0,qreg_1[0],3])
		with case_1(1):
			main_circ.cx(qreg_0[0],2)
			main_circ.cx(qreg_0[0],qreg_1[0])
			main_circ.cx(3,qreg_1[0])
			main_circ.cx(3,0)
with else_2:
	main_circ.cx(qreg_1[0],0)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(0,2)
			main_circ.cx(0,2)
			main_circ.cx(qreg_1[0],3)
			main_circ.cx(2,1)
		with case_1(1):
			main_circ.cx(qreg_0[0],0)
			main_circ.cx(qreg_0[0],qreg_1[0])
			main_circ.id(qreg_0[0])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.id(2)
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rz(0.070000, 1)
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(3)
			with case_1(1):
				main_circ.id(qreg_1[0])
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.id(qreg_1[0])
		main_circ.id(0)
bindings = {param_0: -0.428000, param_2: -0.521000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1066", "RemoveDiagonalGatesBeforeMeasure")
