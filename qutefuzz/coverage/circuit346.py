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
subcirc0.u(-0.446000,-0.886000,0.829000, qreg_0[1])
subcirc0.u(0.652000,0.843000,-0.476000, qreg_0[1])
subcirc0.z(qreg_2[0])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[2])
subcirc1.z(qreg_0[0])
subcirc1.u(-0.620000,0.561000,0.961000, qreg_0[2])
subcirc1.u(0,0,-0.402000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.925000,0.616000,0.416000, qreg_3[0])
subcirc2.u(0,0,-0.865000, qreg_0[1])
subcirc2.u(0.623000,0.385000,0.029000, qreg_0[0])
subcirc2.u(0.785000,-0.793000,0.575000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_4:
	with case_4(0):
		main_circ.z(qreg_0[0])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_3:
			with case_3(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_2:
					with case_2(0):
						main_circ.measure(qreg_3[0], creg_0[0])
						with main_circ.if_test((creg_0[0],0)):
							main_circ.z(qreg_1[0])
							main_circ.z(qreg_1[1])
							main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_3[0]])
					with case_2(1):
						main_circ.id(qreg_1[0])
			with case_3(1):
				main_circ.measure(qreg_3[0], creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_2:
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.z(qreg_0[0])
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.u(0.527000,param_0,param_0, qreg_0[0])
							main_circ.u(-0.406000,param_0,param_0, qreg_3[0])
							main_circ.u(0,param_0,0.819000, qreg_3[0])
							main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_3[0],qreg_1[0]])
				with else_2:
					main_circ.measure(qreg_3[0], creg_0[0])
					with main_circ.switch(creg_0[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.z(qreg_0[0])
							main_circ.z(qreg_1[0])
							main_circ.s(qreg_3[0])
							main_circ.s(qreg_1[0])
	with case_4(1):
		main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_4:
	with case_4(0):
		main_circ.z(qreg_0[0])
		main_circ.measure(qreg_1[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_1[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.u(param_0,0,0.692000, qreg_0[0])
						main_circ.s(qreg_0[0])
						main_circ.u(0.327000,param_0,-0.102000, qreg_1[1])
						main_circ.u(param_0,param_0,-0.048000, qreg_1[0])
				with case_2(1):
					main_circ.u(param_0,0,param_0, qreg_1[0])
					main_circ.measure(qreg_3[0], creg_1[0])
					with main_circ.if_test((creg_1[0],0)) as else_1:
						main_circ.id(qreg_3[0])
					with else_1:
						main_circ.id(qreg_1[1])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.s(qreg_3[0])
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_0[0])
					with main_circ.if_test((creg_0[0],0)):
						main_circ.z(qreg_1[1])
						main_circ.u(param_0,param_0,param_0, qreg_3[0])
						main_circ.z(qreg_1[1])
						main_circ.barrier(qreg_1[0])
	with case_4(1):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_3:
			main_circ.measure(qreg_1[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_2:
				with case_2(0):
					main_circ.u(param_0,0,param_0, qreg_3[0])
					main_circ.measure(qreg_1[1], creg_1[0])
					with main_circ.if_test((creg_1[0],0)):
						main_circ.barrier(qreg_1[0])
					main_circ.measure(qreg_0[0], creg_1[0])
					with main_circ.switch(creg_1[0]) as case_1:
						with case_1(0):
							main_circ.barrier(qreg_0[0])
						with case_1(1):
							main_circ.s(qreg_3[0])
							main_circ.z(qreg_3[0])
							main_circ.barrier(qreg_0[0])
					main_circ.s(qreg_1[1])
				with case_2(1):
					main_circ.append(subcirc0,[qreg_1[1],qreg_3[0],qreg_1[0],qreg_0[0]])
		with else_3:
			main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_0[0])
	main_circ.z(qreg_1[1])
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.s(qreg_1[1])
					main_circ.z(qreg_1[1])
					main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_3[0],qreg_1[1]])
				with case_1(1):
					main_circ.z(qreg_0[0])
					main_circ.id(qreg_1[1])
bindings = {param_0: 0.905000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "346")
