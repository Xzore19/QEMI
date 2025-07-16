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
subcirc0.cy(qreg_0[0],qreg_3[0])
subcirc0.s(qreg_3[0])
subcirc0.s(qreg_2[0])
subcirc0.h(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1.h(qreg_2[0])
subcirc1.ry(-0.133000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_0[2])
subcirc2.cy(qreg_3[0],qreg_0[2])
subcirc2.h(qreg_0[1])
subcirc2.s(qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_0[2])
	main_circ.s(qreg_0[1])
	main_circ.cy(qreg_0[0],qreg_0[3])
	main_circ.s(qreg_0[2])
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_0[1])
	main_circ.cy(qreg_0[3],qreg_0[1])
	main_circ.cy(qreg_0[1],qreg_0[2])
with else_1:
	main_circ.h(qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.h(qreg_0[3])
	main_circ.cy(qreg_0[2],qreg_0[1])
	main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
with else_1:
	main_circ.ry(param_4, qreg_0[1])
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[1])
	with case_1(1):
		main_circ.cy(qreg_0[2],qreg_0[0])
		main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.h(qreg_0[0])
		main_circ.h(qreg_0[2])
		main_circ.s(qreg_0[1])
		main_circ.barrier(qreg_0[2])
	with case_1(1):
		main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(qreg_0[2])
with else_1:
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
	main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_0[2])
	main_circ.h(qreg_0[3])
	main_circ.h(qreg_0[3])
	main_circ.barrier(qreg_0[2])
with else_1:
	main_circ.ry(0.489000, qreg_0[1])
	main_circ.cy(qreg_0[2],qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(qreg_0[0],qreg_0[3])
	main_circ.barrier(qreg_0[3])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(qreg_0[2],qreg_0[0])
	main_circ.id(qreg_0[3])
with else_1:
	main_circ.h(qreg_0[0])
	main_circ.h(qreg_0[3])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.ry(param_4, qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_0[3]])
bindings = {param_4: -0.561000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "243")
