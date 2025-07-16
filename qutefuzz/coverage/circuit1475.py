from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
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

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(qreg_0[0])
	main_circ.y(1)
	main_circ.z(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rx(param_2, qreg_0[2])
	main_circ.rx(-0.894000, qreg_0[1])
	main_circ.z(qreg_0[3])
	main_circ.rx(param_2, qreg_0[1])
	main_circ.z(qreg_0[3])
with else_1:
	main_circ.y(qreg_0[0])
	main_circ.z(0)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rx(-0.695000, qreg_0[2])
	main_circ.z(qreg_0[1])
	main_circ.y(1)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(0.500000, 1)
	main_circ.rx(-0.618000, qreg_0[0])
	main_circ.z(0)
	main_circ.rz(param_3, qreg_0[0])
with else_1:
	main_circ.y(qreg_0[3])
	main_circ.z(qreg_0[0])
	main_circ.rx(-0.650000, qreg_0[1])
	main_circ.rz(-0.535000, qreg_0[0])
	main_circ.y(qreg_0[2])
main_circ.y(qreg_0[2])
main_circ.rx(-0.889000, qreg_0[1])
main_circ.y(1)
main_circ.rx(param_1, qreg_0[3])
main_circ.z(qreg_0[2])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(-0.551000, qreg_0[3])
	main_circ.rx(param_2, qreg_0[1])
	main_circ.y(0)
	main_circ.rz(param_2, qreg_0[0])
	main_circ.z(qreg_0[0])
main_circ.rz(param_1, 1)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_0, qreg_0[0])
		main_circ.z(qreg_0[2])
		main_circ.rz(-0.918000, qreg_0[1])
		main_circ.y(qreg_0[0])
	with case_1(1):
		main_circ.rz(-0.685000, qreg_0[2])
		main_circ.y(qreg_0[3])
		main_circ.y(qreg_0[3])
		main_circ.rx(param_1, qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(1)
	main_circ.rx(param_0, qreg_0[3])
	main_circ.rx(-0.449000, qreg_0[2])
	main_circ.y(1)
	main_circ.rz(0.371000, qreg_0[3])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(0)
		main_circ.barrier(1)
	with case_1(1):
		main_circ.id(qreg_0[0])
bindings = {param_0: -0.858000, param_1: 0.476000, param_2: -0.205000, param_3: 0.591000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1475", "HoareOptimizer")
