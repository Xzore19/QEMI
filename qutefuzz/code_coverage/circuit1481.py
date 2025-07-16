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
subcirc0.u(pi/2,0.770000,-0.569000, qreg_0[0])
subcirc0.u(pi/2,-0.233000,0.495000, qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.u(0,0,0.050000, qreg_0[0])
subcirc0.z(qreg_3[0])
subcirc0.u(pi/2,0.595000,0.713000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.z(qreg_1[1])
subcirc1.z(qreg_1[2])
subcirc1.z(qreg_1[2])
subcirc1.z(qreg_0[0])
subcirc1.u(pi/2,0.459000,-0.269000, qreg_1[2])
subcirc1.u(pi/2,0.791000,-0.173000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,-0.392000,-0.976000, qreg_0[1])
subcirc2.h(qreg_0[2])
subcirc2.u(pi/2,0.056000,0.928000, qreg_0[3])
subcirc2.z(qreg_0[1])
subcirc2.u(0,0,0.096000, qreg_0[1])
subcirc2.z(qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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
	main_circ.u(param_2,0,param_0, qreg_2[0])
	main_circ.append(subcirc1,[qreg_0[1],qreg_2[0],qreg_0[0],0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.append(subcirc0,[qreg_3[0],qreg_2[0],qreg_0[1],0,qreg_0[0]])
		with case_3(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.z(qreg_3[0])
					main_circ.u(param_1,param_0,param_2, qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(param_0,0,-0.187000, qreg_0[0])
						main_circ.h(qreg_2[0])
						main_circ.u(param_0,param_2,param_0, qreg_0[1])
						main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_3[0],0])
					with case_1(1):
						main_circ.append(subcirc2,[0,qreg_3[0],qreg_0[1],qreg_2[0]])
			with else_2:
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.append(subcirc0,[0,qreg_3[0],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],0,qreg_3[0],qreg_0[1]])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(param_1,0,param_2, qreg_2[0])
							main_circ.u(param_1,param_0,-0.997000, 0)
							main_circ.append(subcirc2,[qreg_2[0],0,qreg_0[0],qreg_0[1]])
						with case_1(1):
							main_circ.id(0)
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(0, creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.z(qreg_0[1])
							main_circ.u(pi/2,param_0,0.138000, 0)
							main_circ.z(0)
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(0)
						with case_1(1):
							main_circ.id(0)
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(0)
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(0)
					main_circ.id(qreg_0[0])
bindings = {param_0: -0.922000, param_1: -0.843000, param_2: -0.215000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1481")
