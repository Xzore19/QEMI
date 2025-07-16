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
subcirc0.rx(-0.074000, qreg_3[0])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.u(0.754000,-0.929000,0.743000, qreg_0[2])
subcirc0.y(qreg_0[1])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0.y(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(-0.170000,0.611000,-0.499000, qreg_0[1])
subcirc1.u(-0.796000,-0.595000,0.965000, qreg_0[2])
subcirc1.cy(qreg_0[3],qreg_0[2])
subcirc1.rx(0.198000, qreg_0[2])
subcirc1.u(0.069000,-0.206000,0.912000, qreg_0[0])
subcirc1.y(qreg_0[3])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.374000,0.401000,0.538000, qreg_3[0])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.y(qreg_0[2])
subcirc2.u(0.038000,0.175000,-0.701000, qreg_3[0])
subcirc2.y(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rx(0.340000, 0)
				main_circ.barrier(qreg_0[3])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[0],qreg_0[2],qreg_0[3]])
		with else_2:
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1],0])
			with else_1:
				main_circ.cy(qreg_0[2],qreg_0[3])
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc1,[qreg_0[3],qreg_0[0],0,qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
			with else_1:
				main_circ.y(qreg_0[3])
				main_circ.cy(qreg_0[0],qreg_0[1])
		with else_2:
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
			with else_1:
				main_circ.u(param_0,param_3,param_0, qreg_0[0])
				main_circ.rx(0.526000, 0)
	with case_3(1):
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.y(qreg_0[3])
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(param_1,-0.455000,param_2, qreg_0[3])
						main_circ.y(qreg_0[2])
						main_circ.u(0.856000,0.312000,param_1, qreg_0[2])
						main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[2],qreg_0[0]])
					with case_1(1):
						main_circ.cy(qreg_0[0],qreg_0[1])
						main_circ.cy(qreg_0[3],qreg_0[1])
						main_circ.cy(qreg_0[2],0)
						main_circ.cy(qreg_0[0],qreg_0[2])
			with case_2(1):
				main_circ.cy(qreg_0[1],qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.cy(qreg_0[0],0)
						main_circ.cy(qreg_0[0],0)
						main_circ.y(qreg_0[2])
						main_circ.y(0)
					with case_1(1):
						main_circ.u(param_0,param_1,param_2, qreg_0[3])
						main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.barrier(qreg_0[3])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rx(param_3, qreg_0[1])
				main_circ.u(0.259000,0.034000,param_1, qreg_0[3])
			with else_1:
				main_circ.barrier(qreg_0[1])
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[2])
			main_circ.id(qreg_0[3])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(qreg_0[2])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[3], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[3])
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[2])
			main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[2])
			with else_1:
				main_circ.id(qreg_0[3])
			main_circ.id(qreg_0[1])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(0)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[3])
				with else_1:
					main_circ.id(qreg_0[3])
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[2])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_0[3])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[2])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_0[3])
		main_circ.barrier(0)
bindings = {param_0: -0.039000, param_1: -0.454000, param_2: -0.278000, param_3: 0.005000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "586", "Optimize1qGates")
