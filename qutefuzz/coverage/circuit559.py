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
subcirc0.rx(0.953000, qreg_0[2])
subcirc0.rx(0.887000, qreg_0[0])
subcirc0.rx(-0.810000, qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.cy(qreg_1[0],2)
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.z(0)
				main_circ.z(qreg_0[0])
				main_circ.ry(param_3, 2)
				main_circ.cy(1,qreg_0[0])
				main_circ.z(1)
		with case_2(1):
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.z(0)
					main_circ.rx(-0.411000, 3)
					main_circ.rx(0.237000, 3)
					main_circ.cy(qreg_1[0],2)
				with case_1(1):
					main_circ.rx(0.602000, qreg_1[0])
					main_circ.barrier(0)
with else_3:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.z(1)
			main_circ.cy(3,0)
			main_circ.z(1)
			main_circ.ry(param_4, qreg_1[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.barrier(1)
with else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(3)
			main_circ.ry(-0.061000, qreg_1[0])
			main_circ.ry(0.194000, 3)
			main_circ.rx(-0.598000, 1)
			main_circ.id(qreg_1[0])
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cy(3,qreg_1[0])
			main_circ.z(1)
			main_circ.z(1)
			main_circ.rx(param_3, 2)
	with else_2:
		main_circ.barrier(qreg_1[0])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(0)
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cy(1,2)
			main_circ.ry(param_5, 3)
			main_circ.rx(param_3, qreg_1[0])
			main_circ.barrier(1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(0,qreg_0[0])
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cy(qreg_1[0],3)
			main_circ.id(1)
		with else_1:
			main_circ.rx(0.431000, qreg_0[0])
			main_circ.ry(param_1, 1)
			main_circ.ry(param_0, 1)
			main_circ.ry(-0.960000, qreg_0[0])
			main_circ.cy(qreg_1[0],3)
	with else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.z(1)
			main_circ.ry(param_2, 2)
		with else_1:
			main_circ.cy(qreg_0[0],0)
			main_circ.cy(qreg_1[0],3)
			main_circ.cy(2,1)
			main_circ.cy(3,2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(qreg_0[0],0)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cy(qreg_1[0],2)
				main_circ.cy(qreg_1[0],0)
				main_circ.rx(param_5, 3)
				main_circ.z(1)
			with case_1(1):
				main_circ.z(3)
				main_circ.ry(-0.908000, qreg_1[0])
				main_circ.z(qreg_1[0])
				main_circ.cy(qreg_0[0],qreg_1[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.z(1)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.z(qreg_1[0])
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.ry(-0.009000, qreg_0[0])
				main_circ.ry(0.676000, 0)
				main_circ.id(3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.id(qreg_1[0])
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(2)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(1)
			with case_1(1):
				main_circ.id(qreg_1[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(3)
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.id(1)
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.barrier(2)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.barrier(0)
	with else_2:
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(0)
		main_circ.id(qreg_1[0])
bindings = {param_0: -0.689000, param_1: -0.420000, param_2: 0.725000, param_3: -0.798000, param_4: 0.775000, param_5: -0.637000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "559")
