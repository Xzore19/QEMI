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
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.ry(-0.627000, qreg_0[3])
subcirc0.s(qreg_0[2])
subcirc0.s(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.cx(qreg_0[0],qreg_2[1])
subcirc1.cz(qreg_2[1],qreg_2[0])
subcirc1.cz(qreg_2[1],qreg_0[0])
subcirc1.ry(0.862000, qreg_2[0])
subcirc1.cz(qreg_2[1],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_0[2])
subcirc2.cx(qreg_0[1],qreg_3[0])
subcirc2.s(qreg_0[1])
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_3[0])
subcirc3.cx(qreg_0[0],qreg_0[1])
subcirc3.cz(qreg_0[2],qreg_0[1])
subcirc3.s(qreg_0[1])
subcirc3.s(qreg_0[0])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.s(qreg_0[0])
		main_circ.append(subcirc1,[qreg_0[0],qreg_2[1],qreg_0[1],qreg_2[0]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[1],qreg_0[0])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_0[1],qreg_2[1],qreg_0[0],qreg_2[0]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(qreg_2[1],qreg_0[0])
	main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_2[1],qreg_2[0]])
with else_1:
	main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_2[1],qreg_2[0]])
main_circ.ry(param_0, qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_2[1]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(qreg_2[0])
	main_circ.id(qreg_0[1])
main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_2[1],qreg_0[0])
		main_circ.s(qreg_0[1])
		main_circ.barrier(qreg_2[1])
	with case_1(1):
		main_circ.id(qreg_0[1])
main_circ.measure(qreg_2[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_2[0],qreg_0[0])
		main_circ.ry(param_0, qreg_0[0])
		main_circ.cz(qreg_2[1],qreg_0[0])
		main_circ.id(qreg_0[1])
	with case_1(1):
		main_circ.id(qreg_2[0])
bindings = {param_0: 0.640000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1345")
