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
subcirc0.z(qreg_0[3])
subcirc0.z(qreg_0[1])
subcirc0.rz(-0.595000, qreg_0[1])
subcirc0.rz(0.184000, qreg_0[1])
subcirc0.rz(0.017000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.z(qreg_0[2])
subcirc1.ry(0.066000, qreg_0[0])
subcirc1.ry(0.439000, qreg_0[2])
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.cz(qreg_2[0],qreg_0[1])
subcirc2.rz(-0.154000, qreg_3[0])
subcirc2.z(qreg_0[0])
subcirc2.rz(-0.156000, qreg_2[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_2[1],qreg_0[0],0])
		with case_1(1):
			main_circ.rz(-0.586000, qreg_0[0])
			main_circ.id(0)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc2,[qreg_2[1],qreg_0[0],qreg_2[0],qreg_0[1]])
		with else_1:
			main_circ.barrier(0)
	with case_2(1):
		main_circ.append(subcirc0,[qreg_2[0],qreg_2[1],0,qreg_0[0],qreg_0[1]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cz(qreg_0[0],qreg_0[1])
		main_circ.append(subcirc2,[0,qreg_2[1],qreg_0[0],qreg_2[0]])
	with else_1:
		main_circ.cz(qreg_0[1],0)
		main_circ.z(qreg_2[1])
		main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],0,qreg_0[1]])
with else_2:
	main_circ.cz(qreg_2[1],qreg_0[0])
main_circ.z(qreg_2[1])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.cz(qreg_2[0],qreg_0[1])
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cz(qreg_0[0],qreg_2[0])
		main_circ.append(subcirc2,[qreg_2[1],0,qreg_0[0],qreg_0[1]])
with else_2:
	main_circ.append(subcirc2,[qreg_2[1],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.cz(qreg_2[0],qreg_0[0])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.cz(qreg_2[0],qreg_2[1])
			main_circ.cz(qreg_2[0],0)
			main_circ.cz(qreg_0[0],qreg_2[1])
			main_circ.cz(qreg_0[0],0)
			main_circ.cz(qreg_2[0],qreg_0[1])
		with else_1:
			main_circ.cz(qreg_2[0],qreg_2[1])
			main_circ.ry(0.529000, qreg_0[0])
			main_circ.rz(0.086000, 0)
			main_circ.rz(-0.301000, qreg_0[0])
			main_circ.barrier(qreg_0[1])
	with case_2(1):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.ry(-0.417000, 0)
			main_circ.z(qreg_2[0])
			main_circ.ry(param_0, qreg_2[1])
			main_circ.id(0)
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(0)
		main_circ.barrier(qreg_2[0])
bindings = {param_0: 0.324000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1501", "CollectMultiQBlocks")
