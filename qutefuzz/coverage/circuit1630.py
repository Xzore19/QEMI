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
subcirc0.x(qreg_0[0])
subcirc0.rx(-0.532000, qreg_0[2])
subcirc0.cx(qreg_0[3],qreg_0[1])
subcirc0.x(qreg_0[1])
subcirc0.rx(0.443000, qreg_0[2])
subcirc0.rx(0.002000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_1[2])
subcirc1.rx(0.242000, qreg_1[2])
subcirc1.rx(0.050000, qreg_0[0])
subcirc1.x(qreg_1[1])
subcirc1.rx(-0.070000, qreg_1[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[3])
subcirc2.x(qreg_0[2])
subcirc2.rx(-0.201000, qreg_0[0])
subcirc2.rx(0.863000, qreg_0[0])
subcirc2.rx(0.691000, qreg_0[3])
subcirc2.x(qreg_0[1])

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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc1,[0,2,3,1])
	with else_1:
		main_circ.rz(param_1, 0)
main_circ.rx(0.899000, 3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[3,0,1,qreg_1[0]])
		with case_1(1):
			main_circ.x(3)
			main_circ.append(subcirc2,[2,qreg_0[0],3,1])
with else_2:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc0,[0,2,3,qreg_1[0]])
	with else_1:
		main_circ.cx(qreg_1[0],3)
		main_circ.rx(0.835000, 2)
		main_circ.append(subcirc1,[1,qreg_0[0],3,2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc1,[3,2,1,0])
	with else_1:
		main_circ.rx(-0.564000, 0)
		main_circ.cx(1,2)
		main_circ.cx(qreg_1[0],1)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_0[0],qreg_1[0])
			main_circ.cx(qreg_0[0],1)
			main_circ.cx(2,0)
			main_circ.cx(2,qreg_0[0])
		with case_1(1):
			main_circ.cx(1,qreg_0[0])
			main_circ.cx(0,2)
			main_circ.cx(qreg_0[0],0)
			main_circ.cx(3,qreg_0[0])
main_circ.cx(qreg_1[0],1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cx(qreg_1[0],2)
		main_circ.cx(1,0)
		main_circ.cx(2,qreg_1[0])
	with else_1:
		main_circ.cx(qreg_0[0],1)
		main_circ.rz(0.495000, 2)
		main_circ.cx(qreg_1[0],qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.id(1)
	main_circ.barrier(2)
bindings = {param_1: 0.939000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1630")
