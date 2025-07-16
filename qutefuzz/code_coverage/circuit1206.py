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
subcirc0.u(pi/2,0.290000,-0.888000, qreg_0[0])
subcirc0.u(pi/2,-0.594000,0.113000, qreg_0[2])
subcirc0.u(pi/2,0.520000,-0.259000, qreg_0[2])
subcirc0.u(pi/2,-0.760000,-0.110000, qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.347000,0.459000, qreg_1[0])
subcirc1.u(pi/2,0.055000,0.827000, qreg_3[0])
subcirc1.z(qreg_1[1])
subcirc1.u(0,0,0.570000, qreg_3[0])
subcirc1.u(0,0,-0.747000, qreg_1[0])
subcirc1 = subcirc1.to_gate().control(3)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.barrier(qreg_0[0])
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(param_3,param_4,-0.406000, 3)
				main_circ.z(3)
				main_circ.z(1)
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.s(3)
with else_3:
	main_circ.id(2)
main_circ.s(0)
main_circ.s(1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.s(3)
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.u(0,param_0,param_2, 2)
					main_circ.barrier(3)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(pi/2,param_2,-0.438000, 0)
					main_circ.id(1)
				with case_1(1):
					main_circ.s(3)
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.s(1)
			with else_1:
				main_circ.id(2)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.s(1)
				main_circ.u(0,0,param_0, 3)
				main_circ.s(0)
	with case_3(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.s(qreg_0[0])
				main_circ.s(qreg_0[0])
				main_circ.s(3)
				main_circ.u(pi/2,0.484000,param_3, 0)
				main_circ.barrier(2)
			with else_1:
				main_circ.u(0,0,param_4, 1)
				main_circ.id(2)
		with else_2:
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.u(param_1,param_1,param_3, 3)
				main_circ.u(param_2,0,param_2, qreg_0[0])
				main_circ.u(0,0,-0.630000, 2)
				main_circ.id(0)
main_circ.u(param_1,param_3,-0.137000, 1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(0)
			with else_1:
				main_circ.u(param_1,param_2,-0.420000, 2)
				main_circ.z(3)
				main_circ.barrier(1)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.s(1)
					main_circ.id(1)
				with case_1(1):
					main_circ.s(3)
					main_circ.s(0)
					main_circ.id(2)
		with case_2(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.s(2)
					main_circ.z(1)
					main_circ.u(param_1,param_4,-0.748000, 3)
					main_circ.s(qreg_0[0])
				with case_1(1):
					main_circ.u(param_4,0,0.164000, 2)
					main_circ.u(param_0,-0.729000,-0.497000, 2)
					main_circ.u(param_2,param_0,-0.558000, 2)
					main_circ.s(3)
main_circ.s(3)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.z(0)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(0)
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.z(qreg_0[0])
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(0)
				with else_1:
					main_circ.id(1)
				main_circ.id(3)
			with case_2(1):
				main_circ.measure(2, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(3)
					with case_1(1):
						main_circ.s(qreg_0[0])
						main_circ.z(0)
						main_circ.z(qreg_0[0])
						main_circ.barrier(0)
				main_circ.measure(3, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.z(2)
						main_circ.z(1)
						main_circ.u(param_0,param_4,param_3, 3)
						main_circ.s(0)
					with case_1(1):
						main_circ.barrier(0)
	with case_3(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(param_4,param_3,0.704000, 0)
					main_circ.u(param_3,0,-0.103000, 3)
					main_circ.z(qreg_0[0])
					main_circ.barrier(3)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(param_3,0,param_3, qreg_0[0])
					main_circ.barrier(1)
				with else_1:
					main_circ.u(param_3,param_1,param_2, 3)
			with case_2(1):
				main_circ.measure(0, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.z(1)
					main_circ.u(pi/2,-0.912000,-0.401000, 2)
					main_circ.id(0)
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(pi/2,-0.888000,param_2, 3)
					main_circ.s(qreg_0[0])
				with else_1:
					main_circ.z(1)
					main_circ.u(pi/2,param_3,param_1, 3)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.z(2)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.s(1)
				main_circ.z(2)
				main_circ.barrier(2)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(0)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(1)
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(3)
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(3, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.barrier(3)
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.barrier(3)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(1)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(2)
			with else_1:
				main_circ.id(0)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(0)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(3)
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(0)
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.id(3)
			main_circ.measure(3, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(3)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(1)
			main_circ.barrier(2)
		with case_2(1):
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(3)
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(1)
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.barrier(0)
bindings = {param_0: -0.041000, param_1: 0.272000, param_2: 0.906000, param_3: -0.556000, param_4: 0.923000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1206")
