from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_3:
			with case_3(0):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.measure(1, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.cx(0,qreg_0[0])
						main_circ.ry(-0.381000, 0)
						main_circ.cx(qreg_0[0],2)
						main_circ.ry(0.799000, 3)
					with else_1:
						main_circ.cy(3,qreg_0[0])
						main_circ.ry(param_3, 1)
						main_circ.cx(3,qreg_0[0])
						main_circ.s(3)
						main_circ.cx(qreg_0[0],0)
			with case_3(1):
				main_circ.s(1)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.ry(param_4, qreg_1[0])
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.s(qreg_0[0])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(3, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.s(0)
							main_circ.cy(0,qreg_0[0])
							main_circ.s(qreg_0[0])
							main_circ.ry(-0.322000, 1)
						with case_1(1):
							main_circ.ry(param_3, 1)
							main_circ.s(qreg_1[0])
							main_circ.s(qreg_0[0])
							main_circ.s(2)
				with else_2:
					main_circ.measure(1, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.cy(1,2)
						main_circ.ry(param_0, qreg_1[0])
						main_circ.cx(3,2)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.ry(0.873000, qreg_0[0])
						main_circ.s(2)
						main_circ.ry(0.217000, 2)
						main_circ.cy(qreg_0[0],1)
						main_circ.cy(qreg_1[0],3)
					with else_1:
						main_circ.s(2)
	with case_4(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cy(qreg_1[0],3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cy(2,1)
				with else_1:
					main_circ.s(2)
					main_circ.s(qreg_1[0])
		with else_3:
			main_circ.measure(qreg_1[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.s(1)
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.s(3)
					main_circ.measure(3, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.cy(qreg_1[0],3)
						main_circ.ry(0.517000, qreg_1[0])
				with case_2(1):
					main_circ.measure(0, creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.ry(param_3, 3)
						main_circ.ry(param_2, 3)
					main_circ.measure(qreg_1[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.cy(2,3)
						main_circ.cy(1,qreg_1[0])
						main_circ.cx(qreg_0[0],2)
						main_circ.s(qreg_0[0])
						main_circ.s(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.cx(3,2)
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.s(1)
					main_circ.s(3)
					main_circ.ry(0.059000, 1)
					main_circ.s(0)
				with case_1(1):
					main_circ.cx(qreg_1[0],1)
					main_circ.cy(qreg_1[0],qreg_0[0])
					main_circ.cx(2,qreg_1[0])
					main_circ.ry(param_1, qreg_0[0])
with else_4:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cx(0,1)
				main_circ.ry(0.554000, 1)
			with else_1:
				main_circ.cy(1,2)
				main_circ.id(2)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.id(0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(qreg_1[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(2)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_1[0])
			with else_1:
				main_circ.id(3)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(0)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(1)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_1[0])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_1[0])
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.id(qreg_1[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.barrier(2)
			main_circ.barrier(2)
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(qreg_1[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_1[0])
				with case_1(1):
					main_circ.barrier(qreg_1[0])
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(1)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.id(3)
			main_circ.id(0)
	main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.421000, param_1: -0.480000, param_2: -0.943000, param_3: -0.803000, param_4: -0.589000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1044", "Collect2qBlocks")
