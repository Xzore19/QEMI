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
subcirc0.z(qreg_0[2])
subcirc0.u(0.762000,0.245000,-0.811000, qreg_0[3])
subcirc0.u(0,0,-0.669000, qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(-0.799000,param_2,-0.474000, qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(param_0,param_2,-0.066000, qreg_2[0])
				with else_1:
					main_circ.u(0,param_1,-0.311000, qreg_2[0])
					main_circ.z(qreg_2[0])
					main_circ.u(param_1,0,0.352000, qreg_2[0])
					main_circ.barrier(qreg_0[1])
		with case_3(1):
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_2,0.298000,-0.766000, qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.z(qreg_3[0])
					main_circ.u(0,param_1,0.668000, qreg_2[0])
					main_circ.barrier(qreg_3[0])
			main_circ.z(qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.id(qreg_3[0])
	with else_3:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.u(0,0,param_0, qreg_0[1])
					main_circ.y(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.u(param_1,0.998000,param_0, qreg_0[1])
					main_circ.z(qreg_0[1])
					main_circ.y(qreg_0[1])
					main_circ.id(qreg_2[0])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.u(0.518000,-0.631000,0.408000, qreg_2[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.u(param_0,0,param_2, qreg_3[0])
						main_circ.u(-0.530000,-0.645000,param_2, qreg_0[1])
						main_circ.y(qreg_3[0])
						main_circ.z(qreg_0[0])
					with case_1(1):
						main_circ.z(qreg_0[0])
						main_circ.z(qreg_2[0])
						main_circ.u(param_0,0,-0.152000, qreg_0[0])
						main_circ.y(qreg_0[1])
with else_4:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.id(qreg_3[0])
	with else_3:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(qreg_2[0])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(param_2,0,param_2, qreg_3[0])
				main_circ.y(qreg_3[0])
				main_circ.u(-0.644000,param_1,param_2, qreg_2[0])
				main_circ.y(qreg_3[0])
			with else_1:
				main_circ.y(qreg_0[1])
				main_circ.id(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.u(0.125000,-0.764000,param_2, qreg_0[0])
			with else_1:
				main_circ.z(qreg_0[0])
				main_circ.u(0,0,0.547000, qreg_3[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.y(qreg_0[0])
				main_circ.u(param_1,param_1,param_2, qreg_0[1])
				main_circ.id(qreg_3[0])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.y(qreg_0[1])
			main_circ.u(0,param_0,param_2, qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(0.852000,0.668000,-0.307000, qreg_0[0])
					main_circ.z(qreg_2[0])
					main_circ.y(qreg_0[1])
					main_circ.u(param_1,param_1,param_1, qreg_0[1])
				with case_1(1):
					main_circ.u(0.181000,param_0,param_0, qreg_0[1])
					main_circ.z(qreg_0[0])
					main_circ.id(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.u(param_1,param_0,param_2, qreg_3[0])
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.z(qreg_2[0])
					main_circ.id(qreg_0[0])
			main_circ.u(0.239000,0.751000,-0.083000, qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.y(qreg_3[0])
				main_circ.u(0,param_0,param_1, qreg_2[0])
				main_circ.z(qreg_0[1])
				main_circ.y(qreg_3[0])
				main_circ.z(qreg_3[0])
			with else_1:
				main_circ.y(qreg_3[0])
				main_circ.z(qreg_0[1])
with else_4:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.z(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_0[1])
				with case_2(1):
					main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[0])
				with else_1:
					main_circ.id(qreg_3[0])
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.id(qreg_2[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_3[0])
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.id(qreg_3[0])
			with else_2:
				main_circ.barrier(qreg_2[0])
			main_circ.id(qreg_2[0])
		with case_3(1):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.id(qreg_2[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_3[0])
				main_circ.barrier(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_3[0])
				with else_1:
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_3[0])
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.id(qreg_0[1])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.id(qreg_0[1])
			main_circ.barrier(qreg_0[0])
		with case_3(1):
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_0[1])
			with else_2:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.id(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[1])
					main_circ.id(qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[1])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_2[0])
				with case_2(1):
					main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.id(qreg_2[0])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[1])
					with else_1:
						main_circ.id(qreg_2[0])
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[0])
						with case_1(1):
							main_circ.id(qreg_3[0])
					main_circ.id(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.barrier(qreg_3[0])
			main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.id(qreg_0[1])
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.id(qreg_0[1])
			with case_2(1):
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.id(qreg_0[1])
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.id(qreg_0[0])
		with else_2:
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_2[0])
			main_circ.barrier(qreg_3[0])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.barrier(qreg_3[0])
			with case_2(1):
				main_circ.barrier(qreg_0[0])
		main_circ.id(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_3[0])
		main_circ.id(qreg_0[1])
	with else_3:
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.id(qreg_3[0])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_2[0])
				with case_1(1):
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_2[0])
			with else_1:
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_2[0])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[0])
			with else_1:
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_2[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_2[0])
				with case_1(1):
					main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_3[0])
			main_circ.id(qreg_2[0])
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_3[0])
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_2[0])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_3[0])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_3[0])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_3[0])
		with else_2:
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_3[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_3[0])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.barrier(qreg_3[0])
			with else_1:
				main_circ.barrier(qreg_2[0])
			main_circ.id(qreg_0[0])
		main_circ.id(qreg_2[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.barrier(qreg_0[1])
		with case_3(1):
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.barrier(qreg_0[1])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.id(qreg_0[0])
					with else_1:
						main_circ.id(qreg_3[0])
					main_circ.barrier(qreg_2[0])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.barrier(qreg_2[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_2[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[1])
					main_circ.id(qreg_3[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_3[0])
						with case_1(1):
							main_circ.id(qreg_2[0])
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.id(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_2[0])
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.id(qreg_2[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.id(qreg_2[0])
			with else_2:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_3[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_2[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_2[0])
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.id(qreg_2[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.id(qreg_0[0])
					main_circ.barrier(qreg_0[1])
			main_circ.id(qreg_3[0])
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.id(qreg_0[1])
				with case_2(1):
					main_circ.measure(qreg_2[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.barrier(qreg_3[0])
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.barrier(qreg_0[1])
				main_circ.id(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_2[0])
				main_circ.id(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_3[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.barrier(qreg_2[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_0[0])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_2[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_3[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_2[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[0])
				with else_1:
					main_circ.id(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_3[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_3[0])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.barrier(qreg_0[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_2[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[0])
				with else_1:
					main_circ.id(qreg_2[0])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.barrier(qreg_0[1])
				with else_1:
					main_circ.barrier(qreg_0[0])
				main_circ.id(qreg_0[0])
			main_circ.barrier(qreg_2[0])
		with case_3(1):
			main_circ.barrier(qreg_0[0])
	main_circ.barrier(qreg_3[0])
bindings = {param_0: 0.249000, param_1: -0.231000, param_2: -0.919000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "604", "CommutativeCancellation")
