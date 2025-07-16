from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.198000,0.072000, qreg_0[0])
subcirc0.z(qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.u(pi/2,0.073000,0.259000, qreg_0[0])
subcirc0.z(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.543000, qreg_0[3])
subcirc1.y(qreg_0[1])
subcirc1.rz(-0.802000, qreg_0[3])
subcirc1.z(qreg_0[3])
subcirc1.z(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(0.192000, qreg_0[3])
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_0[0])
subcirc2.y(qreg_0[0])
subcirc2.rz(0.466000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.y(qreg_0[1])
subcirc3.rz(-0.505000, qreg_2[1])
subcirc3.u(pi/2,-0.356000,0.582000, qreg_0[0])
subcirc3.z(qreg_2[1])
subcirc3.y(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(1)

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

main_circ.rz(param_0, 0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_2,-0.046000,0.344000, 3)
	main_circ.y(2)
	main_circ.z(0)
	main_circ.rz(0.867000, 2)
with else_1:
	main_circ.append(subcirc3,[0,3,qreg_0[0],qreg_1[0],2])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],3,1])
main_circ.append(subcirc1,[2,1,3,0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc0,[0,qreg_1[0],2,qreg_0[0]])
with else_1:
	main_circ.rz(param_2, qreg_0[0])
	main_circ.id(1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(0.968000, 2)
	main_circ.barrier(0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc3,[3,2,1,0,qreg_1[0]])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.z(qreg_0[0])
		main_circ.append(subcirc3,[3,1,qreg_0[0],0,qreg_1[0]])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_1[0],0,qreg_0[0],2])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(2)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(qreg_0[0])
	main_circ.append(subcirc1,[2,qreg_0[0],0,1])
with else_1:
	main_circ.rz(0.581000, 0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_1, 2)
	main_circ.id(2)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.id(1)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(1)
with else_1:
	main_circ.id(qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(1)
with else_1:
	main_circ.z(2)
	main_circ.barrier(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_1[0])
with else_1:
	main_circ.y(1)
	main_circ.id(0)
bindings = {param_0: -0.361000, param_1: -0.474000, param_2: -0.505000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "197", "InverseCancellation")
