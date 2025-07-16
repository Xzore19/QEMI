from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.s(qreg_0[1])
subcirc0.u(-0.315000,0.406000,0.102000, qreg_0[1])
subcirc0.u(pi/2,0.583000,0.572000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.s(qreg_0[2])
subcirc1.u(pi/2,0.957000,0.053000, qreg_0[0])
subcirc1.s(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(pi/2,0.008000,0.463000, qreg_1[0])
subcirc2.u(-0.031000,0.052000,-0.785000, qreg_0[0])
subcirc2.u(0.882000,0.596000,0.806000, qreg_0[0])
subcirc2.s(qreg_1[0])
subcirc2.s(qreg_0[0])

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

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(1,0)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.s(1)
			main_circ.append(subcirc2,[0,1,qreg_0[0],2])
		with case_1(1):
			main_circ.u(pi/2,-0.192000,param_0, 3)
			main_circ.s(0)
			main_circ.cz(2,3)
			main_circ.u(param_0,param_0,0.327000, 1)
with else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.barrier(3)
	with else_1:
		main_circ.append(subcirc1,[2,0,qreg_0[0],3])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.s(0)
		main_circ.u(param_0,0.739000,-0.773000, qreg_0[0])
		main_circ.u(param_0,param_0,0.393000, qreg_0[0])
		main_circ.append(subcirc2,[3,qreg_0[0],1,0])
	with else_1:
		main_circ.s(3)
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(3,0)
		main_circ.u(param_0,0.067000,param_0, 3)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc2,[qreg_0[0],1,3,2])
	with else_1:
		main_circ.cz(1,2)
		main_circ.cz(1,3)
		main_circ.cz(3,2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(2,qreg_0[0])
		main_circ.cz(qreg_0[0],1)
		main_circ.cz(2,0)
		main_circ.cz(qreg_0[0],0)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cz(qreg_0[0],3)
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cz(0,1)
			main_circ.s(2)
			main_circ.u(param_0,param_0,0.191000, 3)
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.cz(1,2)
			main_circ.id(0)
bindings = {param_0: -0.985000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1906")
