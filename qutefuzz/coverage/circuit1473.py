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
subcirc0.s(qreg_3[0])
subcirc0.s(qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.rx(0.986000, qreg_3[0])
subcirc0.s(qreg_0[1])
subcirc0.cy(qreg_3[0],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,0.876000,-0.743000, qreg_2[0])
subcirc1.s(qreg_0[1])
subcirc1.u(pi/2,-0.281000,0.606000, qreg_0[0])
subcirc1.rx(-0.912000, qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1.s(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(0.884000, qreg_0[1])
subcirc2.u(pi/2,-0.938000,0.841000, qreg_3[0])
subcirc2.s(qreg_2[0])
subcirc2.s(qreg_3[0])
subcirc2.cy(qreg_0[0],qreg_2[0])
subcirc2.u(pi/2,0.086000,0.877000, qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[3],qreg_0[1])
subcirc3.u(pi/2,-0.675000,0.479000, qreg_0[2])
subcirc3.cy(qreg_0[0],qreg_0[2])
subcirc3.u(pi/2,-0.037000,-0.614000, qreg_0[1])
subcirc3.cy(qreg_0[2],qreg_0[3])
subcirc3.cy(qreg_0[0],qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.rx(param_1, 3)
main_circ.append(subcirc3,[3,1,2,qreg_0[0]])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.s(1)
			main_circ.append(subcirc2,[3,qreg_0[0],1,2])
	with else_2:
		main_circ.measure(2, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.append(subcirc3,[0,3,1,qreg_0[0]])
		with else_1:
			main_circ.u(pi/2,-0.408000,param_1, 2)
			main_circ.s(qreg_0[0])
with else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc3,[0,2,1,qreg_0[0]])
				with case_1(1):
					main_circ.cy(2,1)
					main_circ.append(subcirc2,[qreg_0[0],1,2,3])
		with case_2(1):
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(pi/2,-0.273000,param_2, 0)
				main_circ.rx(-0.710000, 3)
				main_circ.append(subcirc1,[qreg_0[0],3,2,0])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.u(pi/2,param_2,0.873000, 1)
			main_circ.id(qreg_0[0])
		main_circ.u(param_0,0.738000,0.536000, qreg_0[0])
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cy(2,1)
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(1)
			main_circ.barrier(1)
		with case_2(1):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.id(1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(3)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(1)
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(2)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.id(3)
	main_circ.barrier(qreg_0[0])
with else_3:
	main_circ.id(0)
bindings = {param_0: -0.359000, param_1: 0.910000, param_2: 0.968000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1473", "RemoveFinalReset")
