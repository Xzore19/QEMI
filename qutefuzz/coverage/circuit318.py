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
subcirc0.u(pi/2,-0.313000,-0.090000, qreg_2[0])
subcirc0.ry(0.660000, qreg_0[1])
subcirc0.ry(-0.016000, qreg_0[1])
subcirc0.cx(qreg_2[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.778000, qreg_0[1])
subcirc1.ry(0.600000, qreg_0[2])
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.u(pi/2,0.945000,0.205000, qreg_3[0])

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
param_4 = Parameter("param_4")

main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.u(pi/2,-0.809000,param_4, 3)
					main_circ.cx(0,1)
					main_circ.cx(0,3)
					main_circ.append(subcirc1,[3,0,2,1])
				with case_1(1):
					main_circ.append(subcirc1,[3,1,2,0])
	with case_3(1):
		main_circ.append(subcirc1,[1,0,2,3])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.id(1)
		with else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc1,[3,1,0,2])
			with else_1:
				main_circ.rz(0.838000, 2)
				main_circ.barrier(3)
	with case_3(1):
		main_circ.rz(0.675000, 1)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cx(1,0)
				main_circ.rz(param_0, 1)
			with else_1:
				main_circ.cx(1,2)
				main_circ.ry(param_1, 1)
				main_circ.append(subcirc1,[0,3,2,1])
		with else_2:
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cx(3,1)
					main_circ.cx(1,3)
					main_circ.cx(3,2)
					main_circ.ry(0.918000, 0)
				with case_1(1):
					main_circ.id(2)
			main_circ.append(subcirc1,[2,1,0,3])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cx(3,1)
				main_circ.rz(param_2, 3)
				main_circ.u(param_2,param_4,param_0, 2)
				main_circ.id(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(3)
				with case_1(1):
					main_circ.id(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(1)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.id(3)
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.id(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.id(2)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(2)
			main_circ.barrier(0)
bindings = {param_0: -0.419000, param_1: -0.397000, param_2: -0.649000, param_4: 0.699000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "318", "RemoveResetInZeroState")
