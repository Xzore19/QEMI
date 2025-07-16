from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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
param_1 = Parameter("param_1")

main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.z(2)
	main_circ.ry(param_0, 0)
	main_circ.s(3)
	main_circ.z(3)
with else_1:
	main_circ.cz(3,0)
	main_circ.s(2)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(0)
	main_circ.s(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[0])
		main_circ.ry(param_1, 3)
		main_circ.ry(0.672000, qreg_0[0])
		main_circ.z(2)
	with case_1(1):
		main_circ.z(1)
		main_circ.ry(-0.855000, 3)
		main_circ.cz(0,1)
		main_circ.ry(param_1, qreg_0[0])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(1)
	main_circ.ry(-0.807000, 0)
	main_circ.s(1)
	main_circ.ry(0.265000, 2)
main_circ.ry(-0.106000, 3)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(3)
		main_circ.ry(-0.447000, 0)
		main_circ.ry(-0.979000, qreg_0[0])
		main_circ.cz(1,qreg_0[0])
	with case_1(1):
		main_circ.ry(param_0, 3)
		main_circ.z(2)
		main_circ.cz(0,2)
		main_circ.ry(0.316000, 1)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(-0.273000, 2)
		main_circ.s(1)
		main_circ.z(1)
		main_circ.ry(-0.747000, 0)
	with case_1(1):
		main_circ.ry(param_1, qreg_0[0])
		main_circ.ry(0.833000, 3)
		main_circ.ry(param_0, 2)
		main_circ.ry(-0.071000, 0)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(0,qreg_0[0])
	main_circ.ry(0.956000, 0)
	main_circ.ry(param_1, qreg_0[0])
main_circ.ry(0.999000, 2)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[0])
		main_circ.cz(3,1)
		main_circ.cz(0,1)
		main_circ.cz(0,3)
	with case_1(1):
		main_circ.cz(2,qreg_0[0])
		main_circ.cz(0,3)
		main_circ.cz(2,3)
		main_circ.cz(qreg_0[0],2)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(0,3)
	main_circ.cz(0,qreg_0[0])
	main_circ.cz(2,0)
	main_circ.cz(2,3)
	main_circ.cz(3,2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(0,3)
		main_circ.ry(0.830000, 3)
		main_circ.s(3)
		main_circ.z(2)
	with case_1(1):
		main_circ.cz(2,0)
		main_circ.ry(param_0, 3)
		main_circ.barrier(3)
bindings = {param_0: 0.456000, param_1: -0.785000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "312", "Optimize1qGatesSimpleCommutation")
