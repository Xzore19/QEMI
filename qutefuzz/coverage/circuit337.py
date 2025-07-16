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
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.z(qreg_3[0])
subcirc0.z(qreg_0[0])
subcirc0.s(qreg_1[0])
subcirc0.y(qreg_2[0])
subcirc0.h(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_3[0])
subcirc1.z(qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1.y(qreg_0[0])
subcirc1.s(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.h(qreg_0[1])
subcirc2.y(qreg_3[0])
subcirc2.y(qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2.h(qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[0])
subcirc3.h(qreg_3[0])
subcirc3.s(qreg_0[1])
subcirc3.h(qreg_3[0])
subcirc3.z(qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.y(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc3,[qreg_0[0],0,2,3])
		with case_1(1):
			main_circ.append(subcirc0,[1,qreg_1[0],0,qreg_0[0],3,2])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_1[0])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc2,[0,qreg_1[0],1,2])
	with else_1:
		main_circ.s(0)
		main_circ.y(qreg_0[0])
		main_circ.z(0)
		main_circ.append(subcirc2,[0,1,3,qreg_0[0]])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(2)
		main_circ.append(subcirc0,[2,qreg_0[0],qreg_1[0],1,0,3])
	with else_1:
		main_circ.h(qreg_0[0])
		main_circ.h(3)
		main_circ.z(0)
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.h(2)
				main_circ.h(2)
				main_circ.z(0)
				main_circ.append(subcirc3,[qreg_1[0],0,1,2])
			with case_1(1):
				main_circ.append(subcirc0,[qreg_0[0],2,1,qreg_1[0],0,3])
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(1)
		main_circ.measure(qreg_1[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.id(3)
		main_circ.barrier(0)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "337", "OptimizeAnnotated")
