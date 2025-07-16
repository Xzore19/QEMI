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
subcirc0.u(0,0,0.726000, qreg_0[1])
subcirc0.u(0,0,-0.143000, qreg_2[0])
subcirc0.rx(-0.897000, qreg_0[0])
subcirc0.u(pi/2,0.246000,0.516000, qreg_2[0])
subcirc0.u(0,0,-0.554000, qreg_0[0])
subcirc0.rx(0.443000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.652000,-0.884000, qreg_3[0])
subcirc1.u(0,0,-0.836000, qreg_0[2])
subcirc1.rx(0.966000, qreg_0[1])
subcirc1.u(pi/2,-0.554000,0.888000, qreg_3[0])
subcirc1.u(0,0,-0.130000, qreg_3[0])
subcirc1.u(0,0,-0.022000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.h(qreg_0[3])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.rx(param_5, qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.h(qreg_0[0])
					main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],0,1,qreg_0[0],qreg_0[2]])
				with case_1(1):
					main_circ.u(0,0,0.660000, qreg_0[0])
					main_circ.h(1)
					main_circ.u(0,param_1,param_5, qreg_0[3])
					main_circ.u(param_2,param_2,0.950000, 1)
		with case_2(1):
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(0,param_2,0.348000, 0)
					main_circ.barrier(1)
				with case_1(1):
					main_circ.h(qreg_0[2])
					main_circ.rx(-0.193000, qreg_0[1])
					main_circ.rx(-0.290000, qreg_0[2])
					main_circ.h(qreg_0[0])
with else_3:
	main_circ.rx(-0.861000, qreg_0[1])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_0[2],1,qreg_0[3],0])
			with case_1(1):
				main_circ.id(qreg_0[0])
	with else_2:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_3, qreg_0[3])
			main_circ.u(param_6,0,param_4, qreg_0[3])
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(qreg_0[0])
				main_circ.append(subcirc0,[qreg_0[2],0,1,qreg_0[0],qreg_0[3],qreg_0[1]])
			with case_1(1):
				main_circ.id(qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.h(qreg_0[3])
					main_circ.u(param_2,0.777000,param_1, qreg_0[3])
					main_circ.rx(0.966000, qreg_0[3])
					main_circ.id(qreg_0[3])
				with case_1(1):
					main_circ.h(0)
					main_circ.u(param_5,param_5,param_2, 1)
					main_circ.u(param_0,param_5,param_0, qreg_0[0])
					main_circ.append(subcirc0,[qreg_0[1],1,qreg_0[0],qreg_0[2],0,qreg_0[3]])
	with case_3(1):
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[2], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[3])
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.id(qreg_0[1])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(0)
				with else_1:
					main_circ.barrier(1)
				main_circ.id(qreg_0[2])
		main_circ.id(qreg_0[2])
bindings = {param_0: 0.030000, param_1: -0.418000, param_2: 0.951000, param_3: -0.893000, param_4: 0.053000, param_5: -0.733000, param_6: -0.978000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "562")
