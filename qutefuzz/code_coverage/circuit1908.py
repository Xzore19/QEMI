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
subcirc0.rx(-0.455000, qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.x(qreg_0[3])
subcirc0.x(qreg_0[0])
subcirc0.rx(0.919000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.cy(qreg_0[3],qreg_0[2])
subcirc1.h(qreg_0[3])
subcirc1.h(qreg_0[3])
subcirc1.x(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_0[2])
subcirc2.h(qreg_0[0])
subcirc2.h(qreg_0[1])
subcirc2.h(qreg_3[0])
subcirc2.rx(-0.455000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.h(qreg_2[0])
subcirc3.rx(-0.948000, qreg_2[0])
subcirc3.h(qreg_2[1])
subcirc3.x(qreg_2[1])
subcirc3.h(qreg_2[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.h(qreg_0[0])
subcirc4.x(qreg_3[0])
subcirc4.h(qreg_0[1])
subcirc4.cy(qreg_0[2],qreg_0[1])
subcirc4.cy(qreg_0[0],qreg_3[0])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.rx(0.664000, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_3:
		with case_3(0):
			main_circ.append(subcirc2,[0,qreg_0[0],1,2])
		with case_3(1):
			main_circ.id(1)
main_circ.rx(-0.784000, 2)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(0,2)
	main_circ.append(subcirc4,[1,qreg_0[0],3,0,2])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_4:
	with case_4(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_3:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.append(subcirc2,[qreg_0[0],2,1,3])
					with else_1:
						main_circ.append(subcirc2,[1,3,qreg_0[0],0])
				with case_2(1):
					main_circ.measure(2, creg_0[1])
					with main_circ.if_test((creg_0[1],0)):
						main_circ.h(3)
						main_circ.cy(2,3)
						main_circ.x(qreg_0[0])
						main_circ.append(subcirc2,[2,qreg_0[0],0,3])
		with else_3:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)):
					main_circ.cy(3,qreg_0[0])
					main_circ.cy(0,qreg_0[0])
					main_circ.h(0)
	with case_4(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(3)
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_2:
				with case_2(0):
					main_circ.measure(1, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.h(3)
						main_circ.x(0)
					with else_1:
						main_circ.id(3)
					main_circ.measure(3, creg_0[0])
					with main_circ.if_test((creg_0[0],0)) as else_1:
						main_circ.cy(3,1)
					with else_1:
						main_circ.x(qreg_0[0])
						main_circ.append(subcirc0,[0,2,1,3])
				with case_2(1):
					main_circ.measure(0, creg_0[1])
					with main_circ.if_test((creg_0[1],0)) as else_1:
						main_circ.cy(qreg_0[0],0)
						main_circ.cy(qreg_0[0],1)
						main_circ.cy(2,qreg_0[0])
						main_circ.cy(0,2)
					with else_1:
						main_circ.cy(qreg_0[0],0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.cy(1,3)
			main_circ.cy(2,1)
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.cy(1,2)
					main_circ.append(subcirc0,[1,qreg_0[0],3,0])
				with case_1(1):
					main_circ.rx(param_0, qreg_0[0])
					main_circ.id(1)
		with else_2:
			main_circ.cy(2,1)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.barrier(2)
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cy(2,0)
					main_circ.id(1)
				with case_1(1):
					main_circ.id(1)
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.id(0)
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.id(2)
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.id(qreg_0[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(0)
			main_circ.id(0)
with else_4:
	main_circ.id(qreg_0[0])
bindings = {param_0: -0.645000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1908")
