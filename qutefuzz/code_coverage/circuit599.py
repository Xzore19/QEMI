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
subcirc0.rz(0.151000, qreg_2[1])
subcirc0.rz(0.679000, qreg_1[0])
subcirc0.rz(0.330000, qreg_2[1])
subcirc0.rz(0.478000, qreg_1[0])
subcirc0.s(qreg_0[0])
subcirc0.rz(-0.295000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.rz(param_0, qreg_0[2])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[2], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[3])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.z(qreg_0[0])
					main_circ.z(0)
					main_circ.rz(-0.320000, qreg_0[0])
					main_circ.barrier(0)
				with else_1:
					main_circ.cx(0,qreg_0[1])
			with case_2(1):
				main_circ.rz(param_2, qreg_0[0])
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(qreg_0[3])
					main_circ.rz(-0.679000, qreg_0[0])
				main_circ.rz(-0.291000, 0)
	with else_3:
		main_circ.measure(qreg_0[3], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cx(qreg_0[1],qreg_0[3])
				main_circ.rz(-0.726000, 0)
				main_circ.id(qreg_0[3])
			with else_1:
				main_circ.rz(param_1, qreg_0[0])
				main_circ.cx(qreg_0[2],qreg_0[3])
				main_circ.cx(0,qreg_0[2])
				main_circ.z(qreg_0[0])
				main_circ.cx(qreg_0[0],qreg_0[3])
with else_4:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[3], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.z(qreg_0[3])
						main_circ.z(qreg_0[1])
						main_circ.cx(qreg_0[0],qreg_0[3])
						main_circ.z(qreg_0[0])
					with case_1(1):
						main_circ.s(0)
						main_circ.cx(0,qreg_0[3])
						main_circ.s(qreg_0[1])
						main_circ.s(qreg_0[3])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.z(qreg_0[3])
					main_circ.cx(qreg_0[1],qreg_0[0])
				main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[2], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rz(0.735000, qreg_0[0])
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.s(qreg_0[0])
				main_circ.z(qreg_0[2])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[2], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cx(qreg_0[1],qreg_0[2])
					main_circ.cx(qreg_0[0],qreg_0[1])
					main_circ.cx(0,qreg_0[0])
					main_circ.cx(qreg_0[3],qreg_0[1])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(qreg_0[2])
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.z(qreg_0[1])
					main_circ.rz(param_0, 0)
					main_circ.z(qreg_0[2])
					main_circ.rz(0.193000, qreg_0[0])
				with else_1:
					main_circ.s(qreg_0[3])
					main_circ.cx(0,qreg_0[3])
					main_circ.rz(param_2, qreg_0[2])
					main_circ.id(qreg_0[1])
	with else_3:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.barrier(qreg_0[3])
		with else_2:
			main_circ.barrier(qreg_0[3])
		main_circ.id(0)
bindings = {param_0: 0.638000, param_1: 0.082000, param_2: 0.469000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "599", "CXCancellation")
