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
subcirc0.cy(qreg_3[0],qreg_1[0])
subcirc0.h(qreg_3[0])
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0.h(qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_3[0])
subcirc0.cy(qreg_1[1],qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[2],qreg_0[0])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.cy(qreg_0[2],qreg_3[0])
subcirc1.h(qreg_0[2])
subcirc1.cz(qreg_3[0],qreg_0[2])
subcirc1.cz(qreg_0[1],qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cz(qreg_0[0],qreg_2[1])
subcirc2.cy(qreg_2[1],qreg_2[0])
subcirc2.u(0,0,-0.747000, qreg_2[1])
subcirc2.u(0,0,0.972000, qreg_0[1])
subcirc2.cz(qreg_2[1],qreg_0[1])
subcirc2.cz(qreg_2[0],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.h(3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(param_2,0,0.010000, 1)
			main_circ.append(subcirc1,[0,qreg_0[0],1,2])
with else_3:
	main_circ.h(2)
main_circ.cy(1,qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cz(qreg_0[0],2)
					main_circ.u(param_7,0,-0.943000, 1)
					main_circ.barrier(2)
				with case_1(1):
					main_circ.append(subcirc0,[2,qreg_0[0],3,1])
	with case_3(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.append(subcirc1,[1,3,2,qreg_0[0]])
				with else_1:
					main_circ.h(3)
					main_circ.cz(1,2)
					main_circ.h(qreg_0[0])
					main_circ.u(param_6,param_7,param_6, 0)
					main_circ.append(subcirc1,[3,1,2,qreg_0[0]])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.cz(2,0)
					main_circ.id(2)
				main_circ.measure(2, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.append(subcirc1,[0,2,qreg_0[0],1])
					with case_1(1):
						main_circ.cy(1,0)
						main_circ.cz(qreg_0[0],2)
						main_circ.h(0)
						main_circ.u(param_2,0,param_3, 2)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.barrier(3)
	with else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.h(1)
			main_circ.append(subcirc0,[0,qreg_0[0],1,2])
		with else_1:
			main_circ.id(qreg_0[0])
with else_3:
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.barrier(3)
		with case_2(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(0,0,0.476000, 1)
				main_circ.id(2)
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cz(0,2)
			with else_1:
				main_circ.cz(3,qreg_0[0])
				main_circ.cz(3,2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.cz(qreg_0[0],3)
			main_circ.id(2)
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(2)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(3)
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.barrier(2)
		main_circ.barrier(3)
	with else_2:
		main_circ.measure(0, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(3)
			with case_1(1):
				main_circ.barrier(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(1)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.id(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.id(0)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.id(2)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(1)
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(3)
			with case_1(1):
				main_circ.barrier(1)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(1)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.barrier(3)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.id(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(1)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.id(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(3)
		with else_1:
			main_circ.id(2)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.id(0)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(2)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(3)
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[0])
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.barrier(1)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.id(0)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(0)
		main_circ.barrier(0)
	main_circ.id(2)
with else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.barrier(0)
	with else_2:
		main_circ.id(1)
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.id(1)
			main_circ.id(2)
		with case_2(1):
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.id(2)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(2, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.id(1)
			main_circ.barrier(2)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.barrier(3)
	with else_2:
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.id(3)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_0[0])
		main_circ.id(2)
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(3)
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.id(2)
	main_circ.id(2)
bindings = {param_2: -0.955000, param_3: 0.916000, param_6: 0.022000, param_7: 0.456000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "643", "CollectLinearFunctions")
