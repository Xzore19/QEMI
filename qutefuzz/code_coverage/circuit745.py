from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.rz(-0.246000, qreg_0[0])
subcirc0.u(pi/2,0.069000,0.833000, qreg_1[2])
subcirc0.rz(-0.771000, qreg_1[1])
subcirc0.cz(qreg_0[0],qreg_1[0])
subcirc0.cz(qreg_0[0],qreg_1[2])
subcirc0.cz(qreg_1[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(-0.781000, qreg_0[1])
subcirc1.cz(qreg_0[3],qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1.u(pi/2,-0.482000,0.880000, qreg_0[3])
subcirc1.cz(qreg_0[1],qreg_0[3])
subcirc1.s(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_3[0])
subcirc2.cz(qreg_1[0],qreg_1[1])
subcirc2.s(qreg_1[0])
subcirc2.s(qreg_0[0])
subcirc2.rz(0.770000, qreg_1[1])
subcirc2.s(qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(0.037000, qreg_0[3])
subcirc3.u(pi/2,0.423000,-0.075000, qreg_0[1])
subcirc3.cz(qreg_0[0],qreg_0[3])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3.cz(qreg_0[3],qreg_0[1])
subcirc3.u(pi/2,0.031000,0.301000, qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_1[1],qreg_0[0])
subcirc4.s(qreg_1[1])
subcirc4.cz(qreg_0[0],qreg_1[1])
subcirc4.s(qreg_0[0])
subcirc4.rz(-0.111000, qreg_3[0])
subcirc4.u(pi/2,0.409000,0.420000, qreg_0[0])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_0[3],qreg_0[1]])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_0[3])
with else_1:
	main_circ.u(param_0,param_0,param_2, qreg_0[0])
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.u(pi/2,param_1,0.281000, qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[2])
		main_circ.u(param_2,param_2,param_1, qreg_0[1])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.cz(qreg_0[2],qreg_0[0])
		main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[2])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(qreg_0[2],qreg_0[0])
	main_circ.cz(qreg_0[1],qreg_0[2])
	main_circ.cz(qreg_0[1],qreg_0[2])
	main_circ.cz(qreg_0[0],qreg_0[2])
with else_1:
	main_circ.cz(qreg_0[2],qreg_0[0])
	main_circ.cz(qreg_0[1],qreg_0[3])
	main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_0[2])
with else_1:
	main_circ.cz(qreg_0[2],qreg_0[1])
	main_circ.cz(qreg_0[0],qreg_0[3])
	main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,-0.962000,param_0, qreg_0[3])
		main_circ.cz(qreg_0[3],qreg_0[0])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.barrier(qreg_0[2])
bindings = {param_0: 0.359000, param_1: 0.315000, param_2: 0.832000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "745")
