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
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.x(qreg_2[0])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.s(qreg_1[1])
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.h(qreg_0[0])
subcirc2.s(qreg_0[3])
subcirc2.s(qreg_0[2])
subcirc2.s(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.ry(0.791000, qreg_0[1])
subcirc3.s(qreg_0[2])
subcirc3.s(qreg_0[0])

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

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(2)
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_3:
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.append(subcirc3,[1,3,2,0])
			with case_2(1):
				main_circ.measure(1, creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.id(0)
					with case_1(1):
						main_circ.s(3)
						main_circ.x(2)
						main_circ.barrier(3)
				main_circ.barrier(0)
	with else_3:
		main_circ.append(subcirc3,[3,2,1,0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.append(subcirc3,[3,1,0,2])
with else_4:
	main_circ.x(0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_3:
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.append(subcirc3,[2,1,0,3])
		with else_2:
			main_circ.h(0)
			main_circ.ry(param_0, 1)
			main_circ.x(3)
	with else_3:
		main_circ.measure(0, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.id(1)
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc1,[3,1,0,2])
					with case_1(1):
						main_circ.s(1)
						main_circ.x(2)
						main_circ.h(3)
						main_circ.s(0)
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.append(subcirc3,[1,3,0,2])
					with case_1(1):
						main_circ.x(2)
						main_circ.h(1)
						main_circ.append(subcirc1,[2,1,3,0])
bindings = {param_0: -0.727000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "453", "CXCancellation")
