from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0.cx(qreg_2[0],qreg_2[1])
subcirc0.cx(qreg_2[1],qreg_0[1])
subcirc0.cx(qreg_2[1],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_3[0])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.u(pi/2,0.556000,-0.430000, qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cy(qreg_1[0],qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_1[2])
subcirc2.u(0,0,-0.769000, qreg_1[1])
subcirc2.cx(qreg_1[2],qreg_0[0])

main_circ = QuantumCircuit(2)
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
param_3 = Parameter("param_3")

main_circ.u(param_2,param_3,0.900000, qreg_0[1])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_3:
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],0,qreg_3[0],qreg_0[1]])
			with case_2(1):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(pi/2,-0.274000,-0.830000, qreg_0[2])
					main_circ.cx(qreg_0[0],qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,param_2,param_1, qreg_3[0])
						main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
					with case_1(1):
						main_circ.append(subcirc2,[1,qreg_0[0],0,qreg_0[2]])
	with else_3:
		main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],1,qreg_0[2],qreg_3[0]])
with else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.append(subcirc0,[1,0,qreg_0[1],qreg_0[0],qreg_0[2]])
				with case_1(1):
					main_circ.cx(qreg_0[2],qreg_0[0])
					main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0],1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0,param_2,0.344000, 1)
		main_circ.append(subcirc2,[0,qreg_0[0],1,qreg_0[1]])
with else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.u(pi/2,0.966000,-0.522000, qreg_3[0])
	with else_3:
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(qreg_0[2],1)
					main_circ.cx(qreg_3[0],qreg_0[1])
					main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_3[0],0,1])
				with case_1(1):
					main_circ.append(subcirc2,[qreg_3[0],qreg_0[1],qreg_0[0],1])
		with else_2:
			main_circ.append(subcirc2,[qreg_0[1],1,qreg_0[0],qreg_3[0]])
			main_circ.u(pi/2,param_0,param_2, qreg_0[2])
bindings = {param_0: 0.526000, param_1: -0.161000, param_2: 0.340000, param_3: -0.111000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1769")
