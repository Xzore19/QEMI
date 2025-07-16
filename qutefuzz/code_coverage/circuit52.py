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
subcirc0.z(qreg_0[3])
subcirc0.z(qreg_0[1])
subcirc0.rx(-0.609000, qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.z(qreg_0[3])
subcirc0.cz(qreg_0[0],qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.z(qreg_0[3])
subcirc1.u(0.442000,0.737000,0.867000, qreg_0[2])
subcirc1.z(qreg_0[0])
subcirc1.cz(qreg_0[1],qreg_0[3])
subcirc1.cz(qreg_0[2],qreg_0[1])
subcirc1.u(0.854000,-0.010000,0.347000, qreg_0[3])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_2[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.z(qreg_0[0])
						main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_2[0],qreg_2[1]])
					with case_1(1):
						main_circ.rx(param_1, qreg_2[1])
						main_circ.u(-0.686000,-0.875000,0.763000, 0)
						main_circ.u(0.048000,param_3,param_3, qreg_2[0])
						main_circ.z(qreg_1[0])
			with else_2:
				main_circ.measure(qreg_1[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_1[0])
				with else_1:
					main_circ.append(subcirc0,[qreg_2[0],0,qreg_2[1],qreg_0[0]])
		with case_3(1):
			main_circ.cz(qreg_2[1],qreg_1[0])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.z(qreg_0[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(param_1,-0.733000,param_2, qreg_0[0])
							main_circ.z(qreg_0[0])
							main_circ.u(-0.177000,0.506000,param_3, 0)
							main_circ.z(qreg_0[0])
						with case_1(1):
							main_circ.rx(0.736000, qreg_0[0])
							main_circ.cz(qreg_2[1],qreg_1[0])
							main_circ.cz(qreg_2[0],qreg_0[0])
							main_circ.id(qreg_2[1])
				with case_2(1):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.u(param_0,param_2,param_3, qreg_2[1])
						main_circ.rx(-0.187000, qreg_0[0])
						main_circ.rx(-0.398000, 0)
						main_circ.cz(qreg_0[0],qreg_2[0])
						main_circ.rx(param_3, qreg_2[0])
with else_4:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cz(qreg_2[1],qreg_0[0])
				main_circ.cz(0,qreg_2[0])
				main_circ.cz(qreg_2[0],qreg_0[0])
				main_circ.cz(qreg_1[0],qreg_2[0])
				main_circ.cz(qreg_1[0],qreg_0[0])
			with else_1:
				main_circ.z(qreg_2[0])
				main_circ.barrier(qreg_2[1])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],qreg_1[0],qreg_2[0]])
	with else_3:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.cz(qreg_1[0],qreg_0[0])
				main_circ.measure(qreg_2[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.measure(qreg_1[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_1[0])
				main_circ.id(qreg_2[1])
			with case_2(1):
				main_circ.measure(qreg_2[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_2[0])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.id(qreg_1[0])
bindings = {param_0: 0.316000, param_1: 0.763000, param_2: 0.585000, param_3: 0.198000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "52", "Optimize1qGatesDecomposition")
