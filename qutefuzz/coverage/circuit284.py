from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.ry(-0.778000, qreg_2[1])
subcirc0.ry(-0.715000, qreg_0[0])
subcirc0.u(0,0,0.633000, qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.ry(-0.609000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.x(qreg_2[1])
subcirc1.s(qreg_0[0])
subcirc1.x(qreg_0[1])
subcirc1.x(qreg_2[1])
subcirc1.u(0,0,0.072000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,-0.657000, qreg_0[0])
subcirc2.ry(-0.859000, qreg_0[0])
subcirc2.x(qreg_0[2])
subcirc2.x(qreg_0[2])
subcirc2.u(0,0,-0.861000, qreg_0[1])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_0,0,param_0, qreg_0[0])
		main_circ.s(qreg_2[0])
		main_circ.ry(param_0, qreg_2[0])
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(param_0,0,param_0, qreg_2[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_0,0,param_0, qreg_0[0])
				main_circ.barrier(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(qreg_2[0])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[qreg_2[0],0,qreg_1[0],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.s(qreg_2[1])
		main_circ.ry(param_0, 0)
	with else_3:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_1[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.append(subcirc2,[qreg_2[1],qreg_2[0],qreg_1[0],qreg_0[0]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_2[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.s(qreg_2[0])
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,0,param_0, qreg_2[1])
					main_circ.append(subcirc0,[qreg_2[0],qreg_0[0],qreg_2[1],qreg_1[0]])
				with case_1(1):
					main_circ.u(param_0,0,0.907000, qreg_2[0])
					main_circ.ry(0.512000, qreg_2[1])
					main_circ.id(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_2[1], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(0,param_0,-0.627000, qreg_2[1])
	with else_3:
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(qreg_2[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.ry(param_0, qreg_1[0])
					main_circ.ry(param_0, 0)
					main_circ.append(subcirc0,[0,qreg_1[0],qreg_2[1],qreg_2[0]])
				with case_1(1):
					main_circ.append(subcirc0,[qreg_2[0],0,qreg_2[1],qreg_0[0]])
with else_4:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.x(qreg_0[0])
						main_circ.ry(param_0, qreg_0[0])
						main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_2[1],qreg_1[0]])
					with case_1(1):
						main_circ.ry(-0.639000, qreg_1[0])
						main_circ.u(param_0,0,param_0, qreg_2[1])
						main_circ.append(subcirc2,[qreg_0[0],qreg_1[0],0,qreg_2[1]])
			with case_2(1):
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.ry(param_0, 0)
						main_circ.u(param_0,0,0.935000, qreg_2[0])
						main_circ.s(qreg_2[0])
						main_circ.id(qreg_2[1])
					with case_1(1):
						main_circ.id(qreg_1[0])
				main_circ.id(0)
bindings = {param_0: -0.295000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "284", "Optimize1qGatesDecomposition")
