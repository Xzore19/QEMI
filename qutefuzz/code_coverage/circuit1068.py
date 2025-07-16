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
subcirc0.cy(qreg_0[3],qreg_0[0])
subcirc0.u(0,0,-0.974000, qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.cy(qreg_0[3],qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

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

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(-0.590000,param_0,param_0, 3)
			main_circ.u(0.536000,param_1,param_0, qreg_0[0])
			main_circ.cy(3,qreg_0[0])
			main_circ.u(param_0,param_1,param_0, 2)
		with else_1:
			main_circ.u(-0.294000,0.255000,param_1, 2)
			main_circ.u(0,0,param_1, 2)
			main_circ.cy(3,qreg_0[0])
			main_circ.u(0.267000,-0.594000,-0.900000, qreg_0[0])
	with case_2(1):
		main_circ.h(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(2)
				main_circ.cy(3,1)
				main_circ.append(subcirc0,[3,qreg_0[0],2,1,0])
			with case_1(1):
				main_circ.h(0)
				main_circ.cy(3,1)
				main_circ.cy(qreg_0[0],2)
				main_circ.u(0,param_1,-0.822000, 3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.u(0,param_1,0.414000, 2)
	main_circ.h(1)
with else_2:
	main_circ.append(subcirc0,[qreg_0[0],2,0,1,3])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.h(1)
			main_circ.h(1)
			main_circ.h(0)
			main_circ.h(0)
		with case_1(1):
			main_circ.append(subcirc0,[1,qreg_0[0],3,2,0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(0,3)
		main_circ.u(param_1,param_1,param_1, 0)
		main_circ.u(0,0,param_1, 3)
		main_circ.append(subcirc0,[2,0,3,qreg_0[0],1])
	with else_1:
		main_circ.u(0,param_0,param_1, 1)
		main_circ.id(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(0)
			main_circ.id(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(param_0,param_1,0.453000, 3)
			main_circ.u(param_1,param_0,param_1, 2)
			main_circ.barrier(0)
		with else_1:
			main_circ.cy(3,0)
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(3)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.barrier(2)
		main_circ.barrier(3)
bindings = {param_0: 0.843000, param_1: -0.157000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1068")
