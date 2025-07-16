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
subcirc0.y(qreg_0[1])
subcirc0.rx(0.255000, qreg_3[0])
subcirc0.z(qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.rx(-0.895000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rx(0.817000, qreg_0[2])
subcirc1.y(qreg_0[2])
subcirc1.rx(-0.268000, qreg_3[0])
subcirc1.z(qreg_3[0])
subcirc1.y(qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.rx(param_1, qreg_3[0])
				main_circ.rx(0.655000, qreg_3[0])
				main_circ.z(qreg_0[0])
				main_circ.id(qreg_0[0])
	with else_3:
		main_circ.u(param_1,0.644000,-0.783000, qreg_3[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.z(qreg_0[1])
				main_circ.u(param_2,param_2,0.800000, qreg_0[0])
				main_circ.barrier(qreg_0[2])
			with else_1:
				main_circ.u(-0.621000,0.701000,-0.271000, 0)
				main_circ.z(qreg_0[1])
				main_circ.id(qreg_0[2])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.y(qreg_3[0])
				main_circ.y(qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.y(qreg_3[0])
						main_circ.z(qreg_0[0])
						main_circ.y(qreg_0[1])
						main_circ.z(qreg_0[0])
					with case_1(1):
						main_circ.y(qreg_0[1])
						main_circ.rx(param_0, qreg_0[1])
						main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.rx(param_1, 0)
					main_circ.rx(param_1, qreg_0[2])
				with else_1:
					main_circ.append(subcirc1,[0,qreg_3[0],qreg_0[0],qreg_0[1]])
	with case_4(1):
		main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],0])
main_circ.rx(param_1, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(-0.805000,param_0,param_2, qreg_0[1])
							main_circ.u(-0.703000,param_1,0.589000, qreg_0[0])
							main_circ.z(0)
							main_circ.y(qreg_0[2])
						with case_1(1):
							main_circ.rx(0.351000, qreg_3[0])
							main_circ.rx(param_2, qreg_3[0])
							main_circ.barrier(qreg_0[1])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[2], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(0)
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[2])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[2], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.id(qreg_0[2])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.barrier(qreg_0[1])
			with else_2:
				main_circ.barrier(0)
			main_circ.id(0)
bindings = {param_0: -0.108000, param_1: -0.091000, param_2: -0.665000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "760", "ResetAfterMeasureSimplification")
