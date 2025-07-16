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
subcirc0.rx(-0.832000, qreg_0[0])
subcirc0.rx(-0.663000, qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_0[2])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.h(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

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

main_circ.rx(param_3, 2)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.h(qreg_0[0])
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cz(qreg_0[0],2)
		main_circ.u(pi/2,param_2,-0.019000, 3)
		main_circ.h(2)
		main_circ.id(3)
	with else_1:
		main_circ.h(1)
with else_2:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cz(qreg_0[0],1)
		main_circ.rx(0.914000, 2)
		main_circ.rx(param_0, 1)
		main_circ.barrier(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.barrier(0)
	with case_2(1):
		main_circ.h(0)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[0])
		with else_1:
			main_circ.h(3)
			main_circ.u(param_0,0.853000,param_0, 3)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_3,-0.692000,param_3, 0)
			main_circ.u(param_3,param_0,-0.131000, 1)
			main_circ.id(3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.u(pi/2,param_1,param_3, 2)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(3)
		main_circ.u(pi/2,-0.521000,-0.239000, 3)
		main_circ.h(2)
	with else_1:
		main_circ.cz(qreg_0[0],0)
with else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(2)
	with else_1:
		main_circ.rx(-0.723000, qreg_0[0])
		main_circ.h(3)
		main_circ.id(qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.rx(-0.298000, 0)
			main_circ.h(1)
		main_circ.cz(3,qreg_0[0])
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(2)
		with else_1:
			main_circ.u(pi/2,0.141000,0.041000, qreg_0[0])
			main_circ.cz(3,2)
			main_circ.rx(param_0, 1)
			main_circ.cz(1,0)
			main_circ.cz(0,1)
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_0, 0)
			main_circ.rx(param_0, 3)
			main_circ.cz(1,qreg_0[0])
			main_circ.h(1)
			main_circ.cz(qreg_0[0],2)
main_circ.cz(qreg_0[0],2)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cz(1,3)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.cz(3,1)
			main_circ.cz(3,0)
			main_circ.cz(0,3)
			main_circ.h(0)
			main_circ.u(param_0,0.253000,-0.499000, 3)
		with else_1:
			main_circ.u(pi/2,param_3,0.001000, 2)
			main_circ.barrier(1)
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(3)
			with case_1(1):
				main_circ.h(2)
				main_circ.barrier(2)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cz(1,0)
			main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,param_0,param_2, qreg_0[0])
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.h(2)
				main_circ.rx(param_0, 0)
				main_circ.u(param_0,0.221000,param_3, 2)
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.barrier(1)
bindings = {param_0: -0.693000, param_1: 0.424000, param_2: -0.037000, param_3: 0.636000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "853", "OptimizeAnnotated")
