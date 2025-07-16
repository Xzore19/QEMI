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
subcirc0.u(pi/2,-0.190000,0.488000, qreg_3[0])
subcirc0.u(pi/2,-0.090000,-0.027000, qreg_0[0])
subcirc0.u(0,0,-0.106000, qreg_0[0])
subcirc0.z(qreg_1[0])
subcirc0.u(pi/2,-0.189000,0.468000, qreg_1[0])
subcirc0.u(pi/2,-0.206000,0.893000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,-0.741000, qreg_0[1])
subcirc1.u(0,0,-0.616000, qreg_0[1])
subcirc1.u(pi/2,-0.084000,0.147000, qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_2[0])
subcirc1.u(pi/2,-0.901000,-0.260000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_3[0])
subcirc2.y(qreg_0[1])
subcirc2.u(pi/2,-0.905000,-0.940000, qreg_0[0])
subcirc2.z(qreg_0[1])
subcirc2.y(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(pi/2,0.715000,-0.098000, qreg_0[0])
subcirc3.z(qreg_2[0])
subcirc3.y(qreg_2[0])
subcirc3.u(0,0,-0.903000, qreg_0[0])
subcirc3.u(0,0,-0.439000, qreg_0[0])
subcirc3.u(0,0,0.105000, qreg_2[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.u(param_0,param_0,0.001000, 1)
				with else_1:
					main_circ.z(0)
					main_circ.u(pi/2,param_0,param_0, 1)
					main_circ.u(param_0,0,param_0, 1)
					main_circ.z(0)
			with case_2(1):
				main_circ.y(3)
				main_circ.measure(2, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc0,[1,2,3,0])
					with case_1(1):
						main_circ.barrier(2)
	with case_3(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.append(subcirc3,[2,3,0,1])
		with else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc2,[1,0,2,3])
			with else_1:
				main_circ.append(subcirc0,[1,2,3,0])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.append(subcirc2,[2,0,1,3])
	with case_3(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc0,[1,2,3,0])
			with else_1:
				main_circ.barrier(0)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(2)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.u(pi/2,-0.208000,param_0, 1)
			main_circ.y(1)
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.u(pi/2,param_0,param_0, 1)
					main_circ.z(0)
					main_circ.barrier(0)
		with case_2(1):
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.id(3)
			with else_1:
				main_circ.id(3)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(3)
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(3)
			main_circ.id(1)
	main_circ.barrier(1)
bindings = {param_0: 0.059000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1975")
