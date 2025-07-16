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
subcirc0.rz(-0.879000, qreg_0[0])
subcirc0.rz(0.553000, qreg_3[0])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.rz(0.887000, qreg_0[1])
subcirc0.rz(-0.471000, qreg_0[2])
subcirc0.rz(0.703000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.192000, qreg_0[1])
subcirc1.u(pi/2,-0.486000,0.351000, qreg_2[0])
subcirc1.s(qreg_3[0])
subcirc1.u(pi/2,-0.783000,0.658000, qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1.cy(qreg_0[1],qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.s(0)
				main_circ.u(pi/2,param_0,-0.845000, 1)
				main_circ.rz(param_3, 0)
				main_circ.u(pi/2,param_3,0.104000, 0)
			with case_1(1):
				main_circ.s(2)
				main_circ.u(pi/2,-0.912000,-0.368000, 3)
				main_circ.append(subcirc1,[1,0,qreg_0[0],3,2])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.append(subcirc0,[qreg_0[1],0,qreg_0[0],1,3,2])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc1,[qreg_0[1],1,2,qreg_0[0],0])
					with case_1(1):
						main_circ.append(subcirc1,[3,qreg_0[0],0,qreg_0[1],2])
	with case_3(1):
		main_circ.u(pi/2,param_1,param_3, 1)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.rz(-0.723000, 0)
					main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[0],3,2,0])
				with else_1:
					main_circ.cy(1,0)
			with case_2(1):
				main_circ.cy(0,3)
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.cy(3,2)
					main_circ.cy(0,3)
					main_circ.cy(1,3)
					main_circ.cy(qreg_0[1],0)
main_circ.cy(qreg_0[1],3)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.cy(qreg_0[0],1)
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.cy(1,2)
						main_circ.s(qreg_0[0])
						main_circ.cy(2,0)
						main_circ.id(1)
					with case_1(1):
						main_circ.barrier(qreg_0[0])
			with case_2(1):
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(0)
					with case_1(1):
						main_circ.barrier(2)
				main_circ.measure(0, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(1)
				with else_1:
					main_circ.id(1)
				main_circ.id(qreg_0[1])
	with case_3(1):
		main_circ.barrier(1)
bindings = {param_0: -0.168000, param_1: 0.276000, param_3: 0.289000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1843")
