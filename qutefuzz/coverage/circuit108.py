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
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.ry(0.103000, qreg_0[0])
subcirc0.u(0,0,0.867000, qreg_2[0])
subcirc0.u(0,0,0.134000, qreg_2[0])
subcirc0.ry(-0.588000, qreg_2[1])
subcirc0.u(0,0,-0.243000, qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.u(0,0,0.706000, qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.u(0,0,-0.309000, qreg_0[1])
subcirc1.y(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.027000, qreg_0[0])
subcirc2.u(0,0,-0.293000, qreg_0[2])
subcirc2.y(qreg_0[1])
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.ry(-0.115000, qreg_0[0])
subcirc2.y(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cx(qreg_2[0],qreg_0[0])
subcirc3.cx(qreg_0[1],qreg_0[0])
subcirc3.u(0,0,0.502000, qreg_0[0])
subcirc3.u(0,0,-0.313000, qreg_0[1])
subcirc3.y(qreg_0[0])
subcirc3.y(qreg_2[0])

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

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc3,[qreg_3[0],0,qreg_0[2],qreg_0[1]])
	with else_1:
		main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(0,qreg_3[0])
		main_circ.cx(qreg_3[0],qreg_0[2])
	with else_1:
		main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_3[0],0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],0,qreg_0[0]])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.u(param_3,0,-0.498000, qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_3[0],0])
		with case_1(1):
			main_circ.append(subcirc3,[0,qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.cx(0,qreg_3[0])
				main_circ.append(subcirc1,[0,qreg_3[0],qreg_0[0],qreg_0[2]])
			with case_1(1):
				main_circ.cx(qreg_0[2],qreg_3[0])
				main_circ.y(qreg_0[1])
				main_circ.barrier(qreg_3[0])
	with case_2(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.barrier(qreg_0[1])
		main_circ.id(qreg_3[0])
bindings = {param_3: 0.924000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "108", "ConsolidateBlocks")
