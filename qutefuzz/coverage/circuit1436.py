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
subcirc0.z(qreg_3[0])
subcirc0.u(0,0,0.118000, qreg_0[1])
subcirc0.u(0,0,0.985000, qreg_0[1])
subcirc0.rx(0.786000, qreg_0[0])
subcirc0.u(0,0,-0.492000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rz(0.028000, qreg_2[1])
subcirc1.u(0,0,-0.316000, qreg_0[0])
subcirc1.z(qreg_2[0])
subcirc1.rx(-0.299000, qreg_2[1])
subcirc1.rx(0.445000, qreg_2[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc0,[qreg_0[0],2,qreg_1[0],0,1,3])
	with else_3:
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.rx(0.749000, 1)
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(0,0,0.735000, qreg_1[0])
						main_circ.rz(param_3, qreg_1[0])
						main_circ.u(0,param_0,0.985000, 2)
						main_circ.rz(-0.547000, qreg_1[0])
					with case_1(1):
						main_circ.rx(-0.696000, 2)
						main_circ.append(subcirc1,[0,3,1,qreg_0[0]])
			with case_2(1):
				main_circ.measure(3, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],2,1,3,0])
					with case_1(1):
						main_circ.u(param_1,param_1,0.510000, 0)
						main_circ.append(subcirc0,[0,3,1,2,qreg_1[0],qreg_0[0]])
with else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.z(1)
			main_circ.measure(qreg_1[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],1,3,0,2])
				with case_2(1):
					main_circ.append(subcirc0,[3,2,0,qreg_0[0],qreg_1[0],1])
		with case_3(1):
			main_circ.measure(2, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.rz(0.184000, 3)
						main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],0,1])
				with case_2(1):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.append(subcirc0,[2,0,qreg_1[0],3,1,qreg_0[0]])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.u(0,0,-0.371000, 1)
					with else_1:
						main_circ.rz(-0.277000, 1)
						main_circ.append(subcirc1,[0,3,1,qreg_1[0]])
				with case_2(1):
					main_circ.rx(-0.796000, 1)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(1)
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.rz(-0.800000, 2)
							main_circ.u(0,0,0.505000, qreg_0[0])
							main_circ.id(qreg_1[0])
						with case_1(1):
							main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(2)
						with case_1(1):
							main_circ.barrier(1)
					main_circ.barrier(1)
	with case_4(1):
		main_circ.id(qreg_1[0])
bindings = {param_0: 0.989000, param_1: -0.826000, param_3: -0.822000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1436")
