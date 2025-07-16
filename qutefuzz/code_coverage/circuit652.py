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
subcirc0.u(-0.416000,-0.265000,-0.766000, qreg_0[1])
subcirc0.rz(-0.925000, qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.431000,-0.954000,0.353000, qreg_0[3])
subcirc1.rz(0.730000, qreg_0[2])
subcirc1.z(qreg_0[3])
subcirc1.s(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.append(subcirc1,[2,0,qreg_0[0],qreg_0[1],1,3])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.s(3)
			main_circ.append(subcirc1,[3,1,2,qreg_0[1],qreg_0[0],0])
		with case_3(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(0, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.z(3)
						main_circ.u(param_1,-0.416000,-0.422000, 3)
						main_circ.rz(-0.947000, 3)
						main_circ.append(subcirc0,[0,1,2,qreg_0[1]])
					with else_1:
						main_circ.rz(0.092000, 0)
						main_circ.append(subcirc0,[qreg_0[1],1,3,qreg_0[0]])
				with case_2(1):
					main_circ.rz(0.168000, 2)
					main_circ.measure(1, creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.append(subcirc1,[0,2,qreg_0[0],1,qreg_0[1],3])
						with case_1(1):
							main_circ.u(0.037000,param_0,0.022000, 2)
							main_circ.append(subcirc1,[1,2,3,qreg_0[0],qreg_0[1],0])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_4:
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.append(subcirc0,[2,0,1,qreg_0[1]])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(0, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc0,[3,2,qreg_0[0],0])
					with case_1(1):
						main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],3,2,0,1])
			with else_2:
				main_circ.z(3)
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)) as else_1:
					main_circ.u(param_0,-0.730000,param_1, qreg_0[1])
					main_circ.s(qreg_0[0])
					main_circ.append(subcirc1,[3,qreg_0[1],1,qreg_0[0],2,0])
				with else_1:
					main_circ.append(subcirc1,[qreg_0[1],2,0,3,qreg_0[0],1])
with else_4:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_3:
		with case_3(0):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.s(1)
					main_circ.u(0.643000,param_0,param_2, qreg_0[0])
					main_circ.u(0.194000,0.713000,param_2, qreg_0[0])
				with else_1:
					main_circ.u(param_1,0.075000,param_0, qreg_0[1])
					main_circ.z(2)
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.barrier(3)
				main_circ.id(qreg_0[0])
		with case_3(1):
			main_circ.barrier(2)
bindings = {param_0: 0.936000, param_1: 0.644000, param_2: -0.476000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "652")
