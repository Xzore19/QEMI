from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.h(qreg_1[0])
subcirc0.y(qreg_1[1])
subcirc0.h(qreg_1[1])
subcirc0.u(pi/2,0.056000,-0.057000, qreg_1[0])
subcirc0.u(pi/2,-0.931000,0.677000, qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.155000,-0.104000, qreg_0[2])
subcirc1.u(pi/2,0.585000,0.214000, qreg_3[0])
subcirc1.y(qreg_0[0])
subcirc1.h(qreg_0[1])
subcirc1.h(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.h(qreg_0[0])
subcirc2.h(qreg_1[1])
subcirc2.u(pi/2,-0.680000,0.867000, qreg_1[1])
subcirc2.u(0,0,0.522000, qreg_1[2])
subcirc2.y(qreg_1[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.301000,0.447000, qreg_2[0])
subcirc3.h(qreg_0[0])
subcirc3.y(qreg_0[0])
subcirc3.y(qreg_0[1])
subcirc3.u(0,0,0.285000, qreg_3[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc2,[0,1,qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
		with else_1:
			main_circ.id(qreg_0[3])
	with case_2(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],qreg_0[2],0])
main_circ.append(subcirc3,[0,qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.u(pi/2,param_0,param_4, qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc2,[qreg_0[3],1,qreg_0[0],qreg_0[2],qreg_0[1],0])
		with case_1(1):
			main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],1,qreg_0[2]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.y(1)
		main_circ.u(0,0,0.954000, 1)
		main_circ.barrier(qreg_0[2])
	with else_1:
		main_circ.u(param_1,-0.042000,param_1, qreg_0[2])
		main_circ.u(pi/2,-0.146000,param_2, 0)
		main_circ.u(param_1,param_2,param_3, 1)
		main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0,param_0,0.386000, qreg_0[1])
			main_circ.append(subcirc0,[1,0,qreg_0[2],qreg_0[1]])
		with case_1(1):
			main_circ.append(subcirc3,[1,qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc3,[qreg_0[0],1,qreg_0[3],0])
		with else_1:
			main_circ.barrier(qreg_0[3])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(param_3,0.273000,-0.039000, qreg_0[0])
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_0[1])
bindings = {param_0: -0.004000, param_1: -0.916000, param_2: -0.622000, param_3: -0.328000, param_4: 0.089000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1600", "Optimize1qGatesSimpleCommutation")
