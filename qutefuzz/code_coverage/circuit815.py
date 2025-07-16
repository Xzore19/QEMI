from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.z(qreg_2[1])
subcirc0.cx(qreg_2[1],qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_1[0])
subcirc0.cx(qreg_0[0],qreg_2[1])
subcirc0.z(qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.220000,0.222000,-0.355000, qreg_0[2])
subcirc1.u(0.134000,-0.262000,0.101000, qreg_0[2])
subcirc1.u(-0.145000,-0.935000,0.020000, qreg_0[1])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.u(-0.313000,0.812000,0.079000, qreg_0[2])
subcirc1.cy(qreg_3[0],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_1[0])
subcirc2.cy(qreg_3[0],qreg_0[0])
subcirc2.u(0.522000,0.666000,-0.710000, qreg_3[0])
subcirc2.u(0.839000,0.163000,0.967000, qreg_1[0])
subcirc2.z(qreg_1[0])
subcirc2.z(qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[1],qreg_0[2])
subcirc3.z(qreg_0[2])
subcirc3.u(0.307000,-0.406000,-0.128000, qreg_0[2])
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.cy(qreg_0[0],qreg_0[3])
subcirc3.u(-0.407000,-0.563000,0.599000, qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.z(qreg_2[1])
subcirc4.cy(qreg_2[1],qreg_2[0])
subcirc4.u(-0.427000,0.134000,-0.896000, qreg_2[1])
subcirc4.z(qreg_2[0])
subcirc4.cx(qreg_2[0],qreg_2[1])
subcirc4.cx(qreg_0[1],qreg_0[0])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],0,qreg_0[0]])
	with else_2:
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
			with case_1(1):
				main_circ.cx(qreg_0[2],qreg_0[1])
				main_circ.cx(qreg_0[2],qreg_0[1])
				main_circ.append(subcirc3,[qreg_3[0],qreg_0[2],qreg_0[1],0])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc3,[0,qreg_3[0],qreg_0[0],qreg_0[1]])
			with else_1:
				main_circ.cy(qreg_3[0],qreg_0[0])
				main_circ.append(subcirc3,[qreg_0[0],0,qreg_0[1],qreg_0[2]])
	with case_3(1):
		main_circ.cy(qreg_3[0],qreg_0[2])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.z(qreg_0[1])
				main_circ.measure(qreg_0[1], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc0,[0,qreg_3[0],qreg_0[1],qreg_0[0]])
					with case_1(1):
						main_circ.id(qreg_0[0])
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_3[0]])
				with else_1:
					main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[2])
		main_circ.z(qreg_0[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[2])
				with case_1(1):
					main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(0)
				with case_1(1):
					main_circ.barrier(qreg_3[0])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_3[0])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_0[1])
			with else_1:
				main_circ.barrier(qreg_0[0])
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[2])
		main_circ.barrier(0)
	with case_3(1):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_3[0])
			main_circ.measure(qreg_3[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[2])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_0[2])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[1])
				with case_1(1):
					main_circ.id(qreg_0[1])
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_3[0])
			with else_1:
				main_circ.barrier(qreg_3[0])
			main_circ.barrier(qreg_3[0])
		main_circ.barrier(0)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "815")
