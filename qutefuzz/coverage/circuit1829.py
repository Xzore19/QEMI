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
subcirc0.y(qreg_0[2])
subcirc0.rz(-0.799000, qreg_0[2])
subcirc0.x(qreg_0[2])
subcirc0.x(qreg_3[0])
subcirc0.cz(qreg_3[0],qreg_0[0])
subcirc0.rz(0.032000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.cz(qreg_3[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_2[0])
subcirc1.x(qreg_2[0])
subcirc1.y(qreg_2[0])
subcirc1.rz(0.338000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.y(qreg_0[1])
subcirc2.cz(qreg_2[1],qreg_0[1])
subcirc2.rz(-0.981000, qreg_0[1])
subcirc2.rz(0.495000, qreg_2[1])
subcirc2.y(qreg_2[1])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_3[0],0])
	with case_1(1):
		main_circ.append(subcirc2,[qreg_1[0],qreg_2[0],qreg_3[0],0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(-0.754000, qreg_3[0])
		main_circ.rz(param_0, qreg_1[0])
		main_circ.append(subcirc2,[0,qreg_2[0],qreg_0[0],qreg_1[0]])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_1[0],0,qreg_0[0],qreg_3[0]])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_3[0],0])
	with case_1(1):
		main_circ.cz(qreg_0[0],qreg_2[0])
		main_circ.y(0)
		main_circ.rz(param_0, qreg_3[0])
		main_circ.append(subcirc1,[qreg_3[0],qreg_2[0],qreg_0[0],qreg_1[0]])
main_circ.y(qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cz(0,qreg_3[0])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.id(qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_1, 0)
		main_circ.barrier(0)
	with case_1(1):
		main_circ.cz(qreg_3[0],qreg_1[0])
		main_circ.barrier(qreg_2[0])
bindings = {param_0: 0.279000, param_1: 0.347000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1829")
