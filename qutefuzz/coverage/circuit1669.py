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
subcirc0.u(pi/2,-0.357000,0.314000, qreg_0[1])
subcirc0.cy(qreg_2[0],qreg_0[1])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.cy(qreg_2[0],qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,0.021000,0.655000, qreg_2[1])
subcirc1.u(pi/2,-0.688000,0.370000, qreg_2[0])
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_2[0])
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
subcirc2.cx(qreg_0[0],qreg_2[0])
subcirc2.ry(-0.935000, qreg_2[0])
subcirc2.cx(qreg_1[0],qreg_3[0])
subcirc2.ry(-0.632000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(-0.462000, qreg_1[0])
subcirc3.cy(qreg_1[0],qreg_0[0])
subcirc3.cy(qreg_1[0],qreg_3[0])
subcirc3.cy(qreg_1[1],qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc2,[3,0,1,2])
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.append(subcirc3,[0,2,3,1])
			with else_2:
				main_circ.cy(0,3)
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,-0.508000,0.833000, 1)
						main_circ.append(subcirc2,[1,2,3,0])
					with case_1(1):
						main_circ.ry(param_1, 2)
						main_circ.barrier(1)
	with case_4(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(2,3)
			main_circ.u(param_1,param_2,-0.297000, 1)
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.append(subcirc2,[3,2,0,1])
					main_circ.append(subcirc2,[3,0,2,1])
			with else_2:
				main_circ.barrier(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cy(0,3)
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.append(subcirc0,[1,0,2,3])
				with case_1(1):
					main_circ.cy(2,0)
					main_circ.append(subcirc3,[2,1,0,3])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc2,[2,0,1,3])
with else_4:
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.ry(0.834000, 3)
							main_circ.append(subcirc0,[2,1,3,0])
						with case_1(1):
							main_circ.id(2)
				with case_2(1):
					main_circ.measure(2, creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(3)
					main_circ.barrier(2)
		with case_3(1):
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(2, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(0)
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(3)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(3)
				with else_1:
					main_circ.id(1)
				main_circ.barrier(0)
			with else_2:
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.barrier(3)
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(2)
				main_circ.id(0)
			main_circ.barrier(0)
bindings = {param_1: -0.139000, param_2: 0.234000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1669")
