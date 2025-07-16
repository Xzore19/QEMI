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
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.x(qreg_2[0])
subcirc0.x(qreg_1[0])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_2[0])
subcirc0.cx(qreg_0[0],qreg_2[0])
subcirc0.ry(0.432000, qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

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
param_5 = Parameter("param_5")

main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.x(3)
			main_circ.x(2)
			main_circ.ry(0.751000, 1)
		with else_1:
			main_circ.id(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.cx(0,3)
			main_circ.id(0)
	with case_2(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(1)
		main_circ.cx(2,0)
		main_circ.ry(param_4, 2)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.x(3)
			main_circ.id(0)
		main_circ.cy(2,0)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.ry(-0.259000, 2)
			main_circ.x(0)
			main_circ.cx(2,1)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.x(0)
			main_circ.x(3)
	with case_2(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cx(0,3)
				main_circ.cx(1,2)
				main_circ.id(3)
			with case_1(1):
				main_circ.cx(2,3)
				main_circ.x(0)
				main_circ.cx(2,1)
				main_circ.x(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.x(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(0.977000, 2)
			main_circ.x(1)
			main_circ.ry(-0.837000, 3)
			main_circ.ry(param_1, 1)
		with case_1(1):
			main_circ.cy(2,1)
			main_circ.x(1)
			main_circ.ry(param_2, 2)
			main_circ.ry(0.571000, 0)
with else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.x(2)
		main_circ.id(2)
	with else_1:
		main_circ.x(0)
		main_circ.cx(3,1)
		main_circ.cx(3,1)
		main_circ.id(2)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(1)
		with else_1:
			main_circ.cy(0,3)
			main_circ.cy(0,2)
			main_circ.ry(-0.764000, 2)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(0,3)
	with case_2(1):
		main_circ.cx(0,2)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.ry(param_2, 1)
			main_circ.ry(param_0, 1)
			main_circ.cx(2,0)
			main_circ.cx(2,1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.cy(0,3)
with else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.x(0)
			main_circ.cx(3,2)
			main_circ.x(0)
			main_circ.x(1)
		with case_1(1):
			main_circ.barrier(0)
main_circ.ry(param_5, 3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.ry(param_1, 3)
			main_circ.ry(param_2, 0)
			main_circ.cx(1,2)
			main_circ.cx(1,3)
		with case_1(1):
			main_circ.id(3)
	main_circ.barrier(0)
bindings = {param_0: 0.671000, param_1: -0.311000, param_2: -0.483000, param_4: 0.069000, param_5: -0.787000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1704")
