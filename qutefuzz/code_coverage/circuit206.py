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
subcirc0.u(0.254000,0.371000,-0.939000, qreg_3[0])
subcirc0.ry(0.153000, qreg_3[0])
subcirc0.s(qreg_0[1])
subcirc0.s(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.864000,0.960000,0.082000, qreg_0[1])
subcirc1.s(qreg_0[2])
subcirc1.s(qreg_0[3])
subcirc1.rx(-0.094000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_3[0])
subcirc2.ry(-0.968000, qreg_3[0])
subcirc2.u(-0.206000,0.100000,0.863000, qreg_3[0])
subcirc2.rx(0.764000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(0)
		main_circ.barrier(0)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.s(0)
		main_circ.u(0.848000,param_1,param_1, 1)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.ry(param_2, 0)
	main_circ.s(0)
with else_3:
	main_circ.ry(param_1, 1)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(3)
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.ry(param_1, 0)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.ry(-0.452000, 0)
				main_circ.s(3)
				main_circ.s(1)
				main_circ.rx(param_1, 3)
				main_circ.rx(param_1, 3)
	with case_3(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(0)
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(3)
					main_circ.s(2)
					main_circ.barrier(1)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.rx(0.523000, 0)
					main_circ.barrier(1)
				with else_1:
					main_circ.u(0.128000,param_0,param_0, 2)
					main_circ.id(2)
			with case_2(1):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.ry(-0.344000, 3)
					main_circ.u(param_1,0.175000,0.699000, 3)
				with else_1:
					main_circ.id(2)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.rx(-0.720000, 1)
						main_circ.barrier(3)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.ry(0.238000, 3)
				with else_1:
					main_circ.u(param_1,param_1,param_2, 1)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.id(3)
with else_3:
	main_circ.s(0)
	main_circ.u(param_0,-0.781000,-0.795000, 2)
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.rx(param_2, 3)
				main_circ.barrier(0)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.u(param_2,param_1,param_2, 3)
				main_circ.ry(param_0, 0)
				main_circ.id(2)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.rx(param_2, 3)
		with case_2(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.rx(0.705000, 2)
				main_circ.barrier(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.rx(-0.273000, 0)
					main_circ.barrier(0)
				with case_1(1):
					main_circ.u(0.321000,param_0,0.772000, 0)
					main_circ.ry(-0.078000, 2)
					main_circ.ry(0.718000, 3)
					main_circ.id(0)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.u(param_1,0.501000,-0.241000, 2)
			main_circ.u(0.497000,param_0,0.428000, 2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.ry(param_0, 0)
			main_circ.id(1)
		with else_1:
			main_circ.ry(0.314000, 3)
			main_circ.barrier(1)
		main_circ.u(param_0,-0.271000,-0.614000, 1)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.ry(0.918000, 2)
			main_circ.rx(param_0, 0)
			main_circ.ry(0.648000, 1)
			main_circ.u(param_2,0.089000,param_2, 1)
			main_circ.u(0.966000,-0.505000,-0.497000, 3)
with else_3:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rx(param_2, 3)
			main_circ.s(2)
			main_circ.id(3)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.s(2)
			main_circ.id(3)
		with else_1:
			main_circ.id(2)
main_circ.s(2)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.barrier(3)
		main_circ.id(1)
	with else_2:
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.rx(param_1, 3)
				main_circ.rx(-0.425000, 1)
				main_circ.u(0.101000,param_0,0.642000, 1)
				main_circ.barrier(1)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(-0.928000,0.114000,param_0, 2)
		with else_1:
			main_circ.id(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(1)
		main_circ.id(0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.barrier(1)
with else_3:
	main_circ.u(param_1,param_1,0.390000, 3)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(0)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rx(-0.353000, 0)
				main_circ.ry(param_1, 2)
				main_circ.barrier(0)
			with case_1(1):
				main_circ.ry(0.686000, 1)
				main_circ.id(0)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.ry(0.975000, 0)
			main_circ.u(param_1,param_0,-0.840000, 0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rx(param_2, 3)
				main_circ.id(2)
			with else_1:
				main_circ.barrier(3)
			main_circ.rx(param_1, 0)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(2)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.s(3)
				main_circ.barrier(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0.113000,param_2,-0.826000, 3)
				main_circ.id(0)
			with else_1:
				main_circ.rx(0.304000, 1)
				main_circ.barrier(0)
		with case_2(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.barrier(3)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.id(1)
			main_circ.barrier(2)
bindings = {param_0: 0.773000, param_1: -0.845000, param_2: 0.261000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "206", "RemoveDiagonalGatesBeforeMeasure")
