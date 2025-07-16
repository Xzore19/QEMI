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
subcirc0.ry(-0.825000, qreg_0[0])
subcirc0.rx(-0.917000, qreg_0[2])
subcirc0.rx(-0.134000, qreg_0[0])
subcirc0.rx(0.463000, qreg_0[3])

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
param_3 = Parameter("param_3")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_3, qreg_0[3])
		main_circ.s(qreg_0[3])
		main_circ.ry(-0.867000, qreg_0[0])
		main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
	with case_1(1):
		main_circ.ry(-0.031000, qreg_0[1])
		main_circ.cy(qreg_0[1],qreg_0[2])
		main_circ.cy(qreg_0[0],qreg_0[2])
		main_circ.rx(0.628000, qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.797000, qreg_0[2])
		main_circ.s(qreg_0[1])
		main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
	with case_1(1):
		main_circ.cy(qreg_0[1],qreg_0[3])
		main_circ.ry(param_1, qreg_0[0])
		main_circ.ry(param_3, qreg_0[0])
		main_circ.s(qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_0[3]])
with else_1:
	main_circ.rx(param_2, qreg_0[3])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
with else_1:
	main_circ.rx(param_2, qreg_0[0])
	main_circ.ry(param_3, qreg_0[0])
main_circ.cy(qreg_0[3],qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
	with case_1(1):
		main_circ.ry(param_2, qreg_0[0])
		main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.cy(qreg_0[0],qreg_0[3])
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_0[0],qreg_0[3])
		main_circ.cy(qreg_0[1],qreg_0[0])
		main_circ.cy(qreg_0[1],qreg_0[0])
		main_circ.cy(qreg_0[0],qreg_0[2])
	with case_1(1):
		main_circ.cy(qreg_0[2],qreg_0[3])
		main_circ.cy(qreg_0[0],qreg_0[3])
		main_circ.cy(qreg_0[0],qreg_0[3])
		main_circ.cy(qreg_0[3],qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cy(qreg_0[1],qreg_0[0])
	main_circ.cy(qreg_0[1],qreg_0[0])
	main_circ.rx(param_0, qreg_0[1])
	main_circ.barrier(qreg_0[2])
with else_1:
	main_circ.rx(0.613000, qreg_0[1])
	main_circ.barrier(qreg_0[1])
bindings = {param_0: -0.205000, param_1: -0.654000, param_2: -0.680000, param_3: 0.143000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1359", "RemoveResetInZeroState")
