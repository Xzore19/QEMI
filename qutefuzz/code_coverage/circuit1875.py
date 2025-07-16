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
subcirc0.rx(0.952000, qreg_0[1])
subcirc0.rx(-0.824000, qreg_0[2])
subcirc0.rz(-0.164000, qreg_0[0])
subcirc0.u(pi/2,0.457000,-0.703000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_2[0])
			with case_1(1):
				main_circ.u(pi/2,param_0,-0.346000, qreg_1[0])
				main_circ.rx(-0.659000, 0)
				main_circ.rz(-0.855000, qreg_2[0])
				main_circ.x(qreg_3[0])
	with else_2:
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.x(qreg_3[0])
			main_circ.u(param_3,param_0,param_0, qreg_2[0])
			main_circ.barrier(qreg_0[0])
with else_3:
	main_circ.rz(param_3, qreg_1[0])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.rz(-0.299000, qreg_2[0])
				main_circ.rx(param_3, 0)
				main_circ.u(pi/2,param_2,-0.975000, qreg_1[0])
				main_circ.rx(0.149000, qreg_3[0])
			with case_1(1):
				main_circ.u(pi/2,param_3,-0.019000, qreg_2[0])
				main_circ.rz(param_2, qreg_0[0])
				main_circ.rz(-0.446000, qreg_1[0])
				main_circ.x(0)
main_circ.x(qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rz(param_3, qreg_0[0])
				main_circ.id(qreg_3[0])
			with else_1:
				main_circ.rx(param_1, qreg_2[0])
				main_circ.rz(-0.650000, 0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rx(param_3, 0)
				main_circ.x(qreg_2[0])
				main_circ.id(qreg_3[0])
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.rx(-0.684000, qreg_2[0])
					main_circ.rz(param_3, qreg_2[0])
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.u(param_1,param_1,0.461000, 0)
					main_circ.u(pi/2,-0.690000,0.388000, qreg_0[0])
					main_circ.rz(0.578000, 0)
					main_circ.rz(param_2, qreg_1[0])
			with case_2(1):
				main_circ.barrier(qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.x(qreg_3[0])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,param_0,param_2, 0)
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.u(param_2,0.806000,param_3, qreg_3[0])
				main_circ.u(pi/2,param_3,param_0, qreg_3[0])
				main_circ.barrier(qreg_1[0])
			with case_1(1):
				main_circ.barrier(qreg_2[0])
	with else_2:
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(pi/2,0.849000,0.134000, qreg_0[0])
			main_circ.barrier(qreg_2[0])
		with else_1:
			main_circ.u(pi/2,param_3,param_0, qreg_1[0])
			main_circ.barrier(qreg_2[0])
		main_circ.rx(param_0, 0)
		main_circ.u(pi/2,param_0,0.837000, 0)
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(pi/2,param_3,param_0, qreg_1[0])
			main_circ.id(0)
		with else_1:
			main_circ.rz(param_2, qreg_0[0])
			main_circ.rz(param_3, 0)
			main_circ.id(0)
with else_3:
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(qreg_3[0])
		with else_1:
			main_circ.u(pi/2,param_2,-0.714000, qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.x(0)
		with else_1:
			main_circ.x(qreg_3[0])
			main_circ.rx(-0.684000, qreg_0[0])
			main_circ.x(qreg_3[0])
			main_circ.u(param_0,0.771000,-0.549000, 0)
	with else_2:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_2[0])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.x(qreg_2[0])
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rx(-0.134000, qreg_1[0])
		with else_1:
			main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.x(0)
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(param_2,0.803000,-0.364000, qreg_2[0])
		with else_1:
			main_circ.id(0)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rx(0.533000, qreg_1[0])
			main_circ.rz(-0.853000, 0)
			main_circ.rx(-0.974000, qreg_1[0])
		with else_1:
			main_circ.x(qreg_1[0])
			main_circ.rx(-0.838000, qreg_2[0])
	with else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,param_0,-0.994000, qreg_2[0])
			main_circ.id(qreg_1[0])
with else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_0,param_1,0.813000, qreg_2[0])
					main_circ.x(qreg_3[0])
					main_circ.u(pi/2,param_2,param_0, qreg_0[0])
					main_circ.id(qreg_1[0])
				with case_1(1):
					main_circ.u(param_2,param_2,param_1, qreg_2[0])
					main_circ.x(qreg_3[0])
					main_circ.rz(param_3, qreg_1[0])
					main_circ.id(qreg_2[0])
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[0])
				with case_1(1):
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_3[0])
			main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.875000, param_1: 0.520000, param_2: -0.885000, param_3: 0.924000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1875", "CommutativeInverseCancellation")
