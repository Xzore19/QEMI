from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.783000,0.852000, qreg_3[0])
subcirc0.u(pi/2,0.599000,0.032000, qreg_0[0])
subcirc0.u(pi/2,-0.698000,-0.105000, qreg_0[1])
subcirc0.u(0,0,0.650000, qreg_3[0])
subcirc0.u(0,0,-0.302000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_2[0],qreg_3[0])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.s(qreg_3[0])
subcirc1.s(qreg_0[0])
subcirc1.u(0,0,0.947000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.808000, qreg_2[0])
subcirc2.cy(qreg_0[0],qreg_0[1])
subcirc2.cy(qreg_3[0],qreg_0[0])
subcirc2.u(0,0,-0.563000, qreg_2[0])
subcirc2.u(pi/2,-0.250000,-0.304000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

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

main_circ.cy(qreg_2[0],qreg_0[1])
main_circ.u(param_0,param_0,0.875000, qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_4:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.id(qreg_0[1])
		with case_3(1):
			main_circ.u(pi/2,0.052000,0.652000, qreg_2[0])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.id(qreg_0[1])
						with case_1(1):
							main_circ.u(param_0,param_0,0.639000, qreg_0[0])
							main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.barrier(qreg_0[1])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.id(qreg_0[0])
					main_circ.measure(qreg_0[1], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.barrier(qreg_0[0])
					main_circ.u(param_0,0,param_0, qreg_0[1])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.u(param_0,param_0,param_0, qreg_0[0])
							main_circ.u(param_0,param_0,0.725000, qreg_0[0])
							main_circ.cy(qreg_0[0],qreg_0[1])
							main_circ.cy(qreg_0[1],qreg_2[0])
						with case_1(1):
							main_circ.cy(qreg_3[0],qreg_0[0])
							main_circ.u(param_0,0.255000,param_0, qreg_0[0])
							main_circ.u(param_0,0,0.292000, qreg_2[0])
							main_circ.id(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.u(param_0,0,param_0, qreg_0[1])
							main_circ.u(0,param_0,0.579000, qreg_0[1])
							main_circ.barrier(qreg_0[1])
						with case_1(1):
							main_circ.cy(qreg_0[1],qreg_3[0])
							main_circ.u(param_0,0,0.263000, qreg_2[0])
							main_circ.barrier(qreg_0[1])
with else_4:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(pi/2,0.768000,param_0, qreg_0[1])
						main_circ.u(param_0,param_0,param_0, qreg_3[0])
						main_circ.u(0,param_0,param_0, qreg_3[0])
						main_circ.s(qreg_0[1])
					with case_1(1):
						main_circ.id(qreg_0[1])
			with else_2:
				main_circ.measure(qreg_0[1], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.s(qreg_3[0])
					main_circ.s(qreg_2[0])
					main_circ.id(qreg_0[0])
				with else_1:
					main_circ.cy(qreg_3[0],qreg_0[0])
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.id(qreg_2[0])
				with else_1:
					main_circ.u(param_0,param_0,param_0, qreg_0[1])
					main_circ.barrier(qreg_3[0])
		with case_3(1):
			main_circ.measure(qreg_0[1], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_2:
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(qreg_2[0])
					with case_1(1):
						main_circ.u(param_0,0,-0.589000, qreg_3[0])
						main_circ.cy(qreg_0[1],qreg_2[0])
						main_circ.barrier(qreg_0[1])
				main_circ.barrier(qreg_3[0])
			with else_2:
				main_circ.measure(qreg_0[0], creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.barrier(qreg_2[0])
					with case_1(1):
						main_circ.id(qreg_0[1])
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.u(0,0,param_0, qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.barrier(qreg_0[0])
					main_circ.s(qreg_0[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.u(pi/2,-0.785000,-0.238000, qreg_3[0])
						main_circ.id(qreg_2[0])
					with else_1:
						main_circ.id(qreg_0[0])
					main_circ.cy(qreg_3[0],qreg_2[0])
					main_circ.measure(qreg_0[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_3[0])
					with else_1:
						main_circ.u(0,0,param_0, qreg_3[0])
						main_circ.barrier(qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.switch(creg_0[1]) as case_1:
						with case_1(0):
							main_circ.id(qreg_2[0])
						with case_1(1):
							main_circ.s(qreg_0[0])
							main_circ.barrier(qreg_2[0])
					main_circ.measure(qreg_0[1], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.barrier(qreg_0[0])
					with else_1:
						main_circ.barrier(qreg_3[0])
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.cy(qreg_3[0],qreg_2[0])
						main_circ.s(qreg_2[0])
						main_circ.s(qreg_2[0])
						main_circ.u(param_0,param_0,param_0, qreg_0[1])
main_circ.u(param_0,-0.798000,0.044000, qreg_2[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_2[0])
						with case_1(1):
							main_circ.u(pi/2,param_0,-0.943000, qreg_0[1])
							main_circ.cy(qreg_0[1],qreg_3[0])
							main_circ.cy(qreg_3[0],qreg_0[1])
							main_circ.cy(qreg_2[0],qreg_0[0])
				with case_2(1):
					main_circ.measure(qreg_3[0], creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.cy(qreg_2[0],qreg_3[0])
						main_circ.cy(qreg_0[0],qreg_0[1])
						main_circ.cy(qreg_0[0],qreg_2[0])
					with else_1:
						main_circ.s(qreg_0[1])
						main_circ.s(qreg_0[1])
						main_circ.barrier(qreg_0[0])
	with case_4(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_3:
			with case_3(0):
				main_circ.barrier(qreg_0[1])
			with case_3(1):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.id(qreg_0[1])
					with case_2(1):
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.id(qreg_0[1])
						main_circ.measure(qreg_0[0], creg_0[1])
						with main_circ.if_test((creg_0[1],0)):
							main_circ.barrier(qreg_0[1])
						main_circ.measure(qreg_0[1], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.u(0,param_0,param_0, qreg_2[0])
							main_circ.s(qreg_0[0])
							main_circ.barrier(qreg_0[1])
						main_circ.measure(qreg_0[1], creg_0[1])
						with main_circ.switch(creg_0[1]) as case_1:
							with case_1(0):
								main_circ.cy(qreg_2[0],qreg_0[1])
								main_circ.s(qreg_3[0])
								main_circ.s(qreg_3[0])
								main_circ.barrier(qreg_2[0])
							with case_1(1):
								main_circ.id(qreg_0[0])
main_circ.u(0,param_0,param_0, qreg_3[0])
main_circ.cy(qreg_0[1],qreg_3[0])
bindings = {param_0: -0.993000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "136", "OptimizeAnnotated")
