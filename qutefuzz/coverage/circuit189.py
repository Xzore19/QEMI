from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.x(qreg_3[0])
subcirc0.cy(qreg_1[0],qreg_0[0])
subcirc0.u(0,0,0.653000, qreg_1[0])
subcirc0.cy(qreg_1[0],qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.105000, qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cx(qreg_1[2],qreg_1[1])
subcirc2.x(qreg_0[0])
subcirc2.cy(qreg_0[0],qreg_1[2])
subcirc2.cy(qreg_0[0],qreg_1[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[3],qreg_0[1])
subcirc3.cx(qreg_0[0],qreg_0[3])
subcirc3.x(qreg_0[3])
subcirc3.u(0,0,-0.649000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],qreg_3[0],qreg_0[0]])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.cy(qreg_0[1],qreg_0[0])
			main_circ.barrier(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_3[0])
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_2[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[1],qreg_2[0])
					main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_3[0]])
				with case_1(1):
					main_circ.x(qreg_0[0])
					main_circ.u(param_2,0,param_3, qreg_2[0])
					main_circ.id(qreg_0[1])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.x(qreg_0[1])
					main_circ.cy(qreg_2[0],qreg_0[1])
					main_circ.barrier(qreg_3[0])
				with case_1(1):
					main_circ.cx(qreg_0[0],qreg_0[1])
					main_circ.cx(qreg_3[0],qreg_2[0])
					main_circ.id(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cy(qreg_2[0],qreg_3[0])
				main_circ.u(0,0,param_4, qreg_3[0])
				main_circ.x(qreg_2[0])
				main_circ.u(param_2,0,-0.196000, qreg_0[0])
			with else_1:
				main_circ.x(qreg_0[1])
	with case_3(1):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(0,param_3,-0.854000, qreg_0[1])
				main_circ.u(0,param_1,-0.330000, qreg_0[0])
			with else_1:
				main_circ.u(0,param_0,0.023000, qreg_0[0])
		main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_2[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.cy(qreg_0[1],qreg_3[0])
						main_circ.cy(qreg_2[0],qreg_3[0])
						main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_2[0]])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.id(qreg_0[0])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,0,-0.378000, qreg_0[1])
					main_circ.cy(qreg_3[0],qreg_0[1])
					main_circ.u(param_1,param_1,param_0, qreg_2[0])
					main_circ.x(qreg_2[0])
				with case_1(1):
					main_circ.barrier(qreg_2[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.id(qreg_0[0])
	with case_3(1):
		main_circ.barrier(qreg_0[1])
main_circ.cy(qreg_3[0],qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_2[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_2,param_0,param_2, qreg_0[0])
				main_circ.x(qreg_0[0])
				main_circ.x(qreg_2[0])
				main_circ.u(param_1,0,param_0, qreg_2[0])
			with case_1(1):
				main_circ.barrier(qreg_3[0])
	with else_2:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cx(qreg_0[0],qreg_3[0])
			main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],qreg_3[0],qreg_0[0]])
		with else_1:
			main_circ.id(qreg_0[1])
with else_3:
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(0,0,param_4, qreg_2[0])
				main_circ.append(subcirc2,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_2[0]])
			with else_1:
				main_circ.cy(qreg_0[1],qreg_0[0])
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.cy(qreg_3[0],qreg_0[1])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_3[0])
			main_circ.u(param_3,param_4,0.423000, qreg_0[1])
			main_circ.measure(qreg_2[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,param_3,param_4, qreg_3[0])
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_2[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[0])
				with case_1(1):
					main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.barrier(qreg_0[1])
bindings = {param_0: -0.577000, param_1: 0.433000, param_2: 0.427000, param_3: 0.016000, param_4: 0.045000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "189")
