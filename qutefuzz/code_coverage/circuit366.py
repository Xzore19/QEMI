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
subcirc0.rx(0.587000, qreg_0[0])
subcirc0.ry(0.693000, qreg_0[2])
subcirc0.rx(0.430000, qreg_0[3])
subcirc0.rx(-0.175000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_3[0])
subcirc1.rx(0.385000, qreg_0[2])
subcirc1.s(qreg_0[0])
subcirc1.rx(0.514000, qreg_0[1])
subcirc1.rx(-0.579000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[2])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_0[0])
subcirc2.rx(-0.652000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
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

main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc2,[1,qreg_0[0],2,3])
	with case_2(1):
		main_circ.rx(-0.001000, 0)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc2,[3,0,1,qreg_0[0]])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rx(param_1, 0)
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.z(0)
		main_circ.ry(param_3, 0)
		main_circ.s(1)
	with else_1:
		main_circ.ry(param_5, 2)
		main_circ.rx(0.888000, 1)
		main_circ.barrier(qreg_0[0])
with else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.id(1)
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.ry(param_5, 3)
			main_circ.append(subcirc2,[0,qreg_0[0],3,2])
		with case_1(1):
			main_circ.rx(-0.809000, 0)
			main_circ.rx(-0.456000, 2)
			main_circ.append(subcirc2,[2,1,0,3])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.z(2)
		main_circ.append(subcirc0,[3,2,0,qreg_0[0],1])
	with else_1:
		main_circ.rx(param_0, 0)
		main_circ.s(qreg_0[0])
		main_circ.barrier(1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc2,[1,qreg_0[0],3,2])
	with else_1:
		main_circ.z(2)
		main_circ.id(3)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.ry(0.676000, qreg_0[0])
		main_circ.z(1)
		main_circ.s(0)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(param_0, 1)
			main_circ.ry(param_1, 0)
			main_circ.rx(param_3, 1)
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.barrier(3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.rx(-0.340000, qreg_0[0])
		main_circ.barrier(3)
	with else_1:
		main_circ.id(0)
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(3)
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.barrier(0)
bindings = {param_0: -0.722000, param_1: -0.693000, param_3: 0.341000, param_5: -0.198000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "366")
