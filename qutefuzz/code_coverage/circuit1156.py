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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.ry(-0.407000, qreg_0[2])
subcirc0.z(qreg_0[3])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.ry(-0.858000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(0.424000, qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.cx(qreg_0[0],qreg_0[1])
subcirc1.rx(-0.230000, qreg_0[2])
subcirc1.ry(0.447000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.180000, qreg_0[2])
subcirc2.ry(-0.749000, qreg_3[0])
subcirc2.z(qreg_0[1])
subcirc2.ry(-0.378000, qreg_0[2])
subcirc2.rx(-0.308000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

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
param_4 = Parameter("param_4")

main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.append(subcirc1,[qreg_1[0],0,2,3])
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.ry(0.833000, 0)
		main_circ.barrier(3)
	with else_1:
		main_circ.z(3)
		main_circ.cx(3,0)
		main_circ.append(subcirc2,[0,3,2,qreg_0[0],1,qreg_1[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.z(0)
			main_circ.ry(param_3, 0)
			main_circ.append(subcirc2,[2,qreg_1[0],3,1,0,qreg_0[0]])
		with case_1(1):
			main_circ.append(subcirc2,[qreg_0[0],3,1,qreg_1[0],0,2])
with else_2:
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[3,2,1,qreg_0[0]])
		with case_1(1):
			main_circ.ry(0.659000, 1)
			main_circ.append(subcirc2,[3,1,2,qreg_0[0],0,qreg_1[0]])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cx(2,qreg_0[0])
			main_circ.cx(3,qreg_1[0])
			main_circ.cx(3,qreg_1[0])
			main_circ.cx(1,qreg_0[0])
		with case_1(1):
			main_circ.cx(3,1)
			main_circ.cx(0,qreg_0[0])
			main_circ.cx(3,qreg_1[0])
			main_circ.cx(3,qreg_1[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rx(-0.089000, 1)
		main_circ.z(1)
	with else_1:
		main_circ.id(qreg_1[0])
	main_circ.barrier(qreg_1[0])
with else_2:
	main_circ.measure(qreg_1[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.id(0)
		with case_1(1):
			main_circ.id(1)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(1)
	with else_1:
		main_circ.barrier(qreg_1[0])
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(3)
	with else_1:
		main_circ.barrier(qreg_0[0])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.barrier(1)
	main_circ.id(qreg_1[0])
bindings = {param_3: -0.624000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1156")
