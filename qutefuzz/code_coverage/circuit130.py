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
subcirc0.x(qreg_3[0])
subcirc0.rz(-0.124000, qreg_3[0])
subcirc0.u(0,0,-0.310000, qreg_3[0])
subcirc0.u(0,0,0.689000, qreg_3[0])
subcirc0.z(qreg_3[0])
subcirc0.rz(-0.834000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.x(qreg_0[1])
subcirc1.u(0,0,-0.616000, qreg_0[1])
subcirc1.x(qreg_3[0])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,-0.780000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

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

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.id(1)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.z(0)
			main_circ.u(0,param_1,param_3, 0)
			main_circ.rz(0.971000, 1)
			main_circ.z(0)
		with case_1(1):
			main_circ.barrier(0)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.x(2)
			main_circ.x(2)
			main_circ.u(0,param_3,param_2, 3)
			main_circ.x(3)
			main_circ.rz(-0.047000, 2)
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.rz(-0.433000, 1)
			main_circ.x(3)
			main_circ.x(2)
		with else_1:
			main_circ.z(2)
			main_circ.z(2)
			main_circ.barrier(2)
main_circ.u(param_2,param_3,-0.105000, 2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.z(3)
			main_circ.barrier(1)
	main_circ.rz(param_0, 2)
	main_circ.barrier(3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.z(0)
			main_circ.rz(0.934000, 0)
			main_circ.x(1)
			main_circ.id(1)
		with case_1(1):
			main_circ.u(param_2,param_3,param_3, 2)
			main_circ.rz(-0.426000, 2)
			main_circ.z(0)
			main_circ.rz(-0.033000, 3)
main_circ.z(3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.x(2)
			main_circ.u(param_2,0,param_3, 3)
			main_circ.rz(param_3, 2)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rz(0.887000, 0)
			main_circ.x(1)
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(3)
	with case_2(1):
		main_circ.id(3)
main_circ.x(2)
main_circ.u(param_0,0,0.854000, 2)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.z(2)
			main_circ.z(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.x(1)
			main_circ.rz(-0.064000, 2)
			main_circ.u(0,param_1,-0.816000, 2)
			main_circ.x(1)
			main_circ.x(0)
		with else_1:
			main_circ.u(param_2,0,-0.773000, 1)
			main_circ.x(0)
			main_circ.x(3)
			main_circ.z(3)
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.z(2)
		main_circ.u(param_3,0,0.932000, 1)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(0,0,0.455000, 1)
			main_circ.x(0)
			main_circ.rz(0.150000, 3)
			main_circ.id(1)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.rz(-0.042000, 1)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.rz(0.891000, 0)
		with else_1:
			main_circ.z(0)
			main_circ.barrier(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.id(1)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(0)
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(3)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.id(2)
		main_circ.barrier(2)
	with case_2(1):
		main_circ.id(3)
bindings = {param_0: -0.460000, param_1: 0.305000, param_2: 0.355000, param_3: -0.711000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "130", "ResetAfterMeasureSimplification")
