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
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rx(0.116000, qreg_3[0])
subcirc0.cy(qreg_1[0],qreg_0[0])
subcirc0.rx(-0.302000, qreg_2[0])
subcirc0.rx(-0.600000, qreg_2[0])
subcirc0.z(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.z(qreg_0[1])
subcirc1.rz(0.143000, qreg_0[0])
subcirc1.z(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(-0.580000, qreg_0[1])
subcirc2.rx(-0.264000, qreg_0[2])
subcirc2.z(qreg_0[0])
subcirc2.rz(-0.048000, qreg_0[0])
subcirc2.rx(0.968000, qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.z(qreg_0[1])
				main_circ.rz(0.978000, qreg_0[2])
				main_circ.cy(qreg_0[2],qreg_3[0])
				main_circ.cy(qreg_0[0],qreg_0[1])
			with case_1(1):
				main_circ.rz(-0.574000, qreg_0[2])
				main_circ.cy(qreg_0[2],qreg_0[1])
				main_circ.rz(param_0, qreg_0[1])
				main_circ.rz(0.145000, qreg_0[1])
with else_3:
	main_circ.rz(0.339000, qreg_0[2])
	main_circ.append(subcirc2,[qreg_3[0],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.append(subcirc1,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
	with else_2:
		main_circ.rx(param_0, qreg_3[0])
with else_3:
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
		with else_1:
			main_circ.rz(param_0, qreg_0[2])
			main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cy(qreg_0[0],qreg_0[1])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cy(qreg_0[0],qreg_3[0])
		main_circ.rz(param_0, qreg_0[1])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[2])
					with case_1(1):
						main_circ.z(qreg_0[1])
						main_circ.rz(0.182000, qreg_0[0])
						main_circ.rz(-0.296000, qreg_0[2])
						main_circ.rz(-0.185000, qreg_0[2])
			with case_2(1):
				main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cy(qreg_0[0],qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cy(qreg_0[1],qreg_0[0])
					main_circ.cy(qreg_0[0],qreg_0[2])
					main_circ.cy(qreg_0[1],qreg_3[0])
					main_circ.cy(qreg_0[2],qreg_3[0])
					main_circ.cy(qreg_0[0],qreg_0[1])
				with else_1:
					main_circ.cy(qreg_3[0],qreg_0[2])
					main_circ.cy(qreg_0[0],qreg_0[1])
					main_circ.cy(qreg_0[1],qreg_0[2])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cy(qreg_0[1],qreg_3[0])
					main_circ.rx(param_0, qreg_0[2])
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.z(qreg_0[2])
						main_circ.z(qreg_0[2])
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_3[0])
bindings = {param_0: 0.391000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "813", "Collect1qRuns")
