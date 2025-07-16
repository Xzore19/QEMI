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
subcirc0.h(qreg_0[2])
subcirc0.h(qreg_3[0])
subcirc0.rx(-0.734000, qreg_3[0])
subcirc0.rz(0.421000, qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.rx(-0.517000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.rz(0.925000, qreg_1[2])
subcirc1.rx(0.219000, qreg_1[0])
subcirc1.h(qreg_1[1])
subcirc1.rx(-0.997000, qreg_1[2])
subcirc1.cz(qreg_1[0],qreg_1[1])
subcirc1.cz(qreg_1[1],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cz(qreg_1[1],qreg_1[2])
subcirc2.rx(0.041000, qreg_1[1])
subcirc2.h(qreg_1[1])
subcirc2.rz(-0.020000, qreg_1[0])
subcirc2.cz(qreg_1[2],qreg_1[0])
subcirc2.cz(qreg_1[2],qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(0.400000, qreg_0[1])
subcirc3.rz(-0.677000, qreg_0[0])
subcirc3.h(qreg_0[2])
subcirc3.rx(0.405000, qreg_0[2])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

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
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rx(0.942000, qreg_0[0])
		main_circ.h(qreg_0[3])
		main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[3],qreg_0[2]])
	with case_1(1):
		main_circ.rz(param_6, qreg_0[2])
		main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_0[3])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1]])
	with case_1(1):
		main_circ.rx(-0.792000, qreg_0[3])
		main_circ.cz(qreg_0[3],qreg_0[2])
		main_circ.rz(param_4, qreg_0[3])
		main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rx(-0.346000, qreg_0[2])
	main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rz(param_5, qreg_0[1])
		main_circ.rx(0.233000, qreg_0[1])
		main_circ.cz(qreg_0[0],qreg_0[1])
		main_circ.cz(qreg_0[0],qreg_0[2])
	with case_1(1):
		main_circ.cz(qreg_0[3],qreg_0[1])
		main_circ.cz(qreg_0[1],qreg_0[3])
		main_circ.cz(qreg_0[0],qreg_0[2])
		main_circ.cz(qreg_0[3],qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[2],qreg_0[1])
		main_circ.cz(qreg_0[0],qreg_0[2])
		main_circ.cz(qreg_0[1],qreg_0[3])
		main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
	with case_1(1):
		main_circ.id(qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_0[2])
main_circ.rx(-0.142000, qreg_0[1])
bindings = {param_4: 0.092000, param_5: -0.742000, param_6: -0.600000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1043", "Collect1qRuns")
