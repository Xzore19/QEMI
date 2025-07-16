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
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.cx(qreg_0[0],qreg_2[1])
subcirc0.z(qreg_0[1])
subcirc0.cx(qreg_2[1],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.149000,0.302000, qreg_1[0])
subcirc1.cx(qreg_3[0],qreg_2[0])
subcirc1.z(qreg_1[0])
subcirc1.u(pi/2,-0.110000,0.812000, qreg_0[0])
subcirc1.z(qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cz(qreg_1[2],qreg_1[0])
subcirc2.z(qreg_1[2])
subcirc2.cx(qreg_1[0],qreg_0[0])
subcirc2.z(qreg_1[1])
subcirc2.u(pi/2,-0.546000,-0.416000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

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

main_circ.u(pi/2,param_1,-0.408000, 0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cx(2,0)
		main_circ.append(subcirc1,[2,1,0,3])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.append(subcirc1,[2,1,3,0])
with else_2:
	main_circ.append(subcirc0,[0,1,2,3])
main_circ.u(pi/2,-0.723000,param_1, 3)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc0,[3,2,1,0])
	with else_1:
		main_circ.u(pi/2,-1.000000,param_0, 3)
		main_circ.u(pi/2,0.921000,param_2, 0)
		main_circ.u(pi/2,0.350000,param_1, 3)
		main_circ.cz(2,1)
with else_2:
	main_circ.append(subcirc0,[0,3,2,1])
main_circ.u(pi/2,param_1,param_1, 0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(3)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(2,0)
		main_circ.append(subcirc0,[2,1,0,3])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(0,3)
		main_circ.append(subcirc1,[3,1,0,2])
with else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.u(pi/2,0.133000,param_1, 3)
	with else_1:
		main_circ.cx(0,2)
		main_circ.u(param_0,0.188000,param_2, 1)
		main_circ.append(subcirc1,[3,0,1,2])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(0)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(0,1)
			main_circ.cz(0,1)
			main_circ.z(3)
			main_circ.barrier(3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(2)
		with else_1:
			main_circ.barrier(2)
		main_circ.id(1)
	with case_2(1):
		main_circ.barrier(2)
bindings = {param_0: -0.656000, param_1: -0.825000, param_2: 0.510000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "335")
