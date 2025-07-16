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
subcirc0.z(qreg_0[2])
subcirc0.ry(-0.230000, qreg_0[2])
subcirc0.s(qreg_0[2])
subcirc0.ry(-0.797000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.s(qreg_1[1])
subcirc1.ry(-0.360000, qreg_1[0])
subcirc1.s(qreg_1[2])
subcirc1.z(qreg_1[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_2[0])
subcirc2.s(qreg_0[1])
subcirc2.z(qreg_0[0])
subcirc2.s(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[0])
subcirc3.s(qreg_0[0])
subcirc3.s(qreg_0[2])
subcirc3.s(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(-0.574000, 2)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc0,[3,0,1,2])
with else_1:
	main_circ.append(subcirc0,[3,0,1,2])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.ry(param_1, 2)
	main_circ.ry(-0.175000, 1)
	main_circ.u(0,0,-0.998000, 2)
	main_circ.s(2)
with else_1:
	main_circ.u(param_0,0,param_0, 0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.945000, 1)
	main_circ.append(subcirc0,[3,1,0,2])
with else_1:
	main_circ.append(subcirc3,[2,0,3,1])
main_circ.u(param_1,param_0,0.922000, 0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc3,[2,1,3,0])
with else_1:
	main_circ.u(param_0,param_0,param_0, 3)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[2,0,1,3])
	with case_1(1):
		main_circ.barrier(3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(0)
with else_1:
	main_circ.s(1)
	main_circ.id(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[1,0,3,2])
with else_1:
	main_circ.id(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(1)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.ry(param_1, 0)
main_circ.s(0)
main_circ.append(subcirc0,[1,3,2,0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.s(3)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(2)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(3)
		main_circ.z(1)
		main_circ.append(subcirc0,[0,2,3,1])
	with case_1(1):
		main_circ.append(subcirc3,[1,3,2,0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(1)
with else_1:
	main_circ.barrier(3)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.s(2)
	main_circ.barrier(3)
bindings = {param_0: -0.164000, param_1: 0.873000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1567")
