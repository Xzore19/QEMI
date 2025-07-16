from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,0.106000,-0.376000, qreg_0[0])
subcirc0.cx(qreg_1[0],qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.cx(qreg_1[0],qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[2])
subcirc1.s(qreg_0[1])
subcirc1.rz(0.768000, qreg_3[0])
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,-0.082000,0.158000, qreg_0[0])
subcirc2.u(pi/2,-0.138000,0.554000, qreg_0[0])
subcirc2.cx(qreg_0[3],qreg_0[1])
subcirc2.rz(0.267000, qreg_0[2])
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.u(pi/2,0.544000,0.219000, qreg_0[3])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,0.355000,-0.805000, qreg_0[0])
subcirc3.u(pi/2,-0.264000,-0.103000, qreg_0[2])
subcirc3.s(qreg_0[3])
subcirc3.rz(0.660000, qreg_0[1])
subcirc3.u(pi/2,0.347000,0.978000, qreg_0[1])
subcirc3.u(pi/2,-0.549000,0.390000, qreg_0[3])
subcirc3 = subcirc3.to_gate().control(3)

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

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.append(subcirc0,[3,0,qreg_0[1],1])
				with else_1:
					main_circ.u(pi/2,-0.618000,0.429000, 0)
					main_circ.append(subcirc2,[0,1,qreg_0[0],qreg_0[1]])
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(0)
				main_circ.cx(1,qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.s(qreg_0[0])
					main_circ.s(2)
					main_circ.id(2)
				main_circ.u(param_1,param_1,param_2, qreg_0[0])
	with else_3:
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.s(2)
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],3,1])
			with else_1:
				main_circ.append(subcirc0,[qreg_0[1],0,2,1])
main_circ.append(subcirc2,[3,2,qreg_0[0],qreg_0[1]])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.rz(-0.942000, 1)
					main_circ.append(subcirc1,[3,qreg_0[0],0,qreg_0[1]])
			with case_2(1):
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc2,[0,1,qreg_0[1],qreg_0[0]])
					with case_1(1):
						main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],3,1])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,param_1,param_2, 2)
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.u(pi/2,-0.925000,0.675000, 0)
						main_circ.cx(2,1)
						main_circ.barrier(3)
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.barrier(1)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(2)
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.barrier(2)
		main_circ.barrier(3)
	with else_3:
		main_circ.id(qreg_0[0])
bindings = {param_1: -0.064000, param_2: -0.555000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "732")
