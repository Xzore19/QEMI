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
subcirc0.s(qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.s(qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_3[0])
subcirc0.u(-0.654000,0.367000,-0.166000, qreg_0[1])
subcirc0.z(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.818000,0.961000,-0.941000, qreg_0[1])
subcirc1.s(qreg_3[0])
subcirc1.z(qreg_3[0])
subcirc1.u(0.175000,0.712000,-0.859000, qreg_0[2])
subcirc1.cx(qreg_0[0],qreg_0[2])
subcirc1.s(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.659000,-0.072000,0.561000, qreg_0[0])
subcirc2.z(qreg_2[0])
subcirc2.cx(qreg_3[0],qreg_0[1])
subcirc2.u(-0.552000,0.744000,-0.733000, qreg_0[0])
subcirc2.z(qreg_0[1])
subcirc2.s(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_0[0],qreg_2[0])
subcirc3.z(qreg_3[0])
subcirc3.s(qreg_3[0])
subcirc3.s(qreg_0[0])
subcirc3.u(-0.348000,0.058000,-0.630000, qreg_3[0])
subcirc3.cx(qreg_1[0],qreg_3[0])
subcirc3 = subcirc3.to_gate().control(2)

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

main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.u(0.785000,-0.825000,0.178000, qreg_0[1])
		main_circ.z(qreg_0[2])
		main_circ.s(qreg_0[0])
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(qreg_0[3])
	main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
with else_1:
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(qreg_0[3])
with else_1:
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
	with case_1(1):
		main_circ.u(param_1,-0.039000,0.651000, qreg_0[2])
		main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(qreg_0[1],qreg_0[0])
with else_1:
	main_circ.cx(qreg_0[1],qreg_0[0])
	main_circ.cx(qreg_0[3],qreg_0[0])
	main_circ.cx(qreg_0[1],qreg_0[2])
	main_circ.cx(qreg_0[2],qreg_0[3])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(qreg_0[0],qreg_0[3])
	main_circ.cx(qreg_0[0],qreg_0[1])
	main_circ.cx(qreg_0[0],qreg_0[2])
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.s(qreg_0[0])
	main_circ.u(0.935000,0.279000,param_2, qreg_0[0])
	main_circ.barrier(qreg_0[3])
bindings = {param_1: -0.506000, param_2: 0.197000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1103")
