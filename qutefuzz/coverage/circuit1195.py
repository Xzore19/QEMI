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
subcirc0.cy(qreg_0[2],qreg_3[0])
subcirc0.u(-0.369000,-0.593000,-0.825000, qreg_3[0])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.cy(qreg_0[2],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_3[0],qreg_1[0])
subcirc1.cy(qreg_3[0],qreg_1[0])
subcirc1.u(pi/2,-0.458000,-0.515000, qreg_1[1])
subcirc1.cz(qreg_1[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_3[0],qreg_0[1])
subcirc2.u(0.184000,0.055000,0.057000, qreg_3[0])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.u(pi/2,-0.602000,-0.442000, qreg_3[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[qreg_2[0],0,qreg_0[1],qreg_2[1],qreg_0[0]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(param_4,param_0,param_4, qreg_2[0])
			main_circ.cy(qreg_0[0],qreg_0[1])
		with else_1:
			main_circ.u(pi/2,param_2,0.512000, qreg_2[1])
			main_circ.u(-0.688000,param_2,param_0, qreg_2[0])
			main_circ.cy(qreg_0[1],0)
	with case_2(1):
		main_circ.measure(qreg_2[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc1,[0,qreg_0[1],qreg_2[1],qreg_2[0],qreg_0[0]])
			with case_1(1):
				main_circ.cz(qreg_0[0],qreg_2[0])
				main_circ.cy(qreg_0[1],qreg_0[0])
				main_circ.cy(qreg_2[0],qreg_0[0])
				main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cy(0,qreg_0[0])
			main_circ.u(param_3,param_2,param_0, 0)
			main_circ.u(param_0,-0.290000,-0.850000, qreg_2[0])
			main_circ.u(0.110000,-0.576000,param_3, qreg_2[0])
		with case_1(1):
			main_circ.cy(0,qreg_0[0])
			main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(qreg_0[0],0)
		main_circ.append(subcirc1,[0,qreg_2[0],qreg_0[0],qreg_2[1],qreg_0[1]])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(pi/2,param_2,param_1, qreg_2[0])
			main_circ.append(subcirc2,[qreg_2[1],0,qreg_0[0],qreg_2[0]])
		with case_1(1):
			main_circ.append(subcirc1,[qreg_2[0],qreg_2[1],0,qreg_0[0],qreg_0[1]])
with else_2:
	main_circ.cz(qreg_0[0],qreg_0[1])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.cy(qreg_2[0],qreg_0[0])
			main_circ.u(0.874000,param_4,param_1, qreg_0[1])
			main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.append(subcirc2,[qreg_2[1],qreg_0[1],0,qreg_2[0]])
	with case_2(1):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,param_0,param_4, qreg_2[0])
			main_circ.cz(qreg_2[1],qreg_2[0])
			main_circ.cy(qreg_2[1],qreg_0[1])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_2,param_2,0.708000, 0)
				main_circ.append(subcirc1,[qreg_0[1],0,qreg_2[1],qreg_2[0],qreg_0[0]])
			with case_1(1):
				main_circ.cz(qreg_0[1],0)
				main_circ.u(param_3,0.369000,param_3, qreg_2[1])
				main_circ.barrier(qreg_2[0])
bindings = {param_0: -0.277000, param_1: 0.435000, param_2: 0.952000, param_3: 0.208000, param_4: -0.328000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1195", "CollectMultiQBlocks")
