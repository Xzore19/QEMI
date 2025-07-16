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
subcirc0.u(pi/2,0.600000,-0.800000, qreg_2[1])
subcirc0.u(pi/2,-0.604000,-0.827000, qreg_2[0])
subcirc0.u(pi/2,0.895000,-0.995000, qreg_0[1])
subcirc0.u(pi/2,0.627000,0.918000, qreg_2[0])
subcirc0.cy(qreg_0[1],qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.cy(qreg_2[1],qreg_2[0])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_2[0])
subcirc1.cz(qreg_0[1],qreg_2[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cy(qreg_2[0],qreg_2[1])
subcirc2.cy(qreg_2[1],qreg_2[0])
subcirc2.y(qreg_0[1])
subcirc2.u(pi/2,0.919000,0.308000, qreg_0[1])
subcirc2.cy(qreg_0[0],qreg_2[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cy(qreg_3[0],qreg_0[2])
subcirc3.u(pi/2,0.456000,0.488000, qreg_0[1])
subcirc3.u(pi/2,-0.651000,0.614000, qreg_3[0])
subcirc3.cy(qreg_0[0],qreg_3[0])
subcirc3.cy(qreg_0[2],qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(pi/2,-0.045000,0.936000, qreg_0[1])
subcirc4.y(qreg_0[3])
subcirc4.y(qreg_0[1])
subcirc4.u(pi/2,0.582000,0.598000, qreg_0[0])
subcirc4.cy(qreg_0[3],qreg_0[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(0)
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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc1,[qreg_1[0],qreg_2[0],qreg_3[0],qreg_0[0]])
			with else_1:
				main_circ.u(param_1,-0.240000,0.721000, qreg_1[0])
		with else_2:
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.append(subcirc1,[qreg_2[0],qreg_0[0],qreg_3[0],qreg_1[0]])
	with case_3(1):
		main_circ.u(param_3,-0.561000,param_3, qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cy(qreg_0[0],qreg_3[0])
				main_circ.cz(qreg_0[0],qreg_3[0])
				main_circ.u(pi/2,param_5,0.940000, qreg_2[0])
				main_circ.barrier(qreg_3[0])
			with else_1:
				main_circ.id(qreg_1[0])
			main_circ.measure(qreg_1[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.id(qreg_3[0])
			main_circ.append(subcirc1,[qreg_3[0],qreg_2[0],qreg_1[0],qreg_0[0]])
		with else_2:
			main_circ.cz(qreg_0[0],qreg_1[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(qreg_1[0])
			main_circ.measure(qreg_3[0], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_2[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_4,-0.803000,0.234000, qreg_0[0])
					main_circ.barrier(qreg_0[0])
				with case_1(1):
					main_circ.id(qreg_0[0])
			main_circ.measure(qreg_3[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(qreg_1[0],qreg_0[0])
				main_circ.id(qreg_1[0])
			with else_1:
				main_circ.barrier(qreg_2[0])
			main_circ.measure(qreg_1[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],qreg_2[0],qreg_3[0]])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cz(qreg_3[0],qreg_0[0])
		main_circ.id(qreg_0[0])
	main_circ.id(qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.u(param_6,param_1,0.499000, qreg_3[0])
			main_circ.y(qreg_2[0])
			main_circ.cy(qreg_1[0],qreg_3[0])
			main_circ.append(subcirc1,[qreg_2[0],qreg_1[0],qreg_0[0],qreg_3[0]])
		with else_1:
			main_circ.barrier(qreg_1[0])
	with else_2:
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.id(qreg_0[0])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.u(param_3,param_1,0.514000, qreg_1[0])
			main_circ.measure(qreg_2[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(pi/2,-0.817000,0.027000, qreg_0[0])
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.y(qreg_3[0])
				main_circ.y(qreg_0[0])
				main_circ.id(qreg_0[0])
		with case_2(1):
			main_circ.y(qreg_1[0])
			main_circ.id(qreg_2[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.barrier(qreg_1[0])
with else_3:
	main_circ.barrier(qreg_3[0])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],qreg_2[0],qreg_3[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(param_1,param_1,param_3, qreg_1[0])
			main_circ.id(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cz(qreg_0[0],qreg_1[0])
			main_circ.u(pi/2,param_2,0.454000, qreg_0[0])
			main_circ.barrier(qreg_3[0])
		with else_1:
			main_circ.cz(qreg_0[0],qreg_2[0])
			main_circ.u(pi/2,-0.402000,-0.742000, qreg_0[0])
			main_circ.id(qreg_0[0])
	with else_2:
		main_circ.id(qreg_3[0])
with else_3:
	main_circ.y(qreg_3[0])
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_1[0])
			with else_1:
				main_circ.id(qreg_0[0])
			main_circ.id(qreg_2[0])
		with case_2(1):
			main_circ.id(qreg_3[0])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.id(qreg_2[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.barrier(qreg_2[0])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_2[0])
			with case_1(1):
				main_circ.id(qreg_0[0])
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_3[0])
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.barrier(qreg_1[0])
	with else_2:
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_2[0])
		main_circ.id(qreg_2[0])
	main_circ.barrier(qreg_2[0])
bindings = {param_1: -0.339000, param_2: 0.406000, param_3: -0.839000, param_4: 0.077000, param_5: 0.440000, param_6: 0.396000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1822")
