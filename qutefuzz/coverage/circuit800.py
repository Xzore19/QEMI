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
subcirc0.z(qreg_2[1])
subcirc0.cy(qreg_2[1],qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.rx(-0.706000, qreg_2[1])
subcirc0.u(pi/2,-0.717000,0.594000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[1],qreg_3[0])
subcirc1.u(pi/2,-0.324000,0.387000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.u(pi/2,-0.565000,0.752000, qreg_0[1])
subcirc1.cy(qreg_0[0],qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(pi/2,0.413000,-0.267000, qreg_0[0])
subcirc2.cy(qreg_0[3],qreg_0[2])
subcirc2.rx(-0.612000, qreg_0[2])
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.z(1)
main_circ.append(subcirc1,[3,0,1,2])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.id(0)
	with case_2(1):
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cy(1,0)
				main_circ.id(3)
			with case_1(1):
				main_circ.cy(2,1)
				main_circ.cy(1,2)
				main_circ.barrier(2)
		main_circ.z(3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cy(2,3)
			main_circ.u(pi/2,0.690000,-0.439000, 3)
			main_circ.z(1)
			main_circ.append(subcirc0,[1,3,2,0])
	with case_2(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(pi/2,0.178000,param_3, 0)
			main_circ.rx(0.909000, 0)
			main_circ.barrier(1)
		with else_1:
			main_circ.id(0)
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(param_3,param_0,-0.598000, 2)
				main_circ.u(pi/2,0.822000,-0.667000, 1)
				main_circ.u(pi/2,param_2,param_0, 2)
				main_circ.u(pi/2,param_3,param_3, 0)
			with case_1(1):
				main_circ.z(0)
				main_circ.cy(2,0)
				main_circ.u(param_3,-0.434000,-0.627000, 0)
				main_circ.append(subcirc1,[2,0,1,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(3,1)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cy(2,1)
			main_circ.rx(-0.080000, 0)
			main_circ.rx(-0.574000, 1)
			main_circ.barrier(3)
		with case_1(1):
			main_circ.z(2)
			main_circ.z(2)
			main_circ.rx(param_2, 0)
			main_circ.barrier(2)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(1)
			main_circ.id(0)
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(2)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(3)
		main_circ.barrier(0)
	with case_2(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.id(0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.id(0)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(2)
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(2)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.id(2)
		main_circ.barrier(0)
bindings = {param_0: 0.562000, param_2: -0.180000, param_3: -0.257000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "800")
