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
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rx(param_2, 0)
with else_1:
	main_circ.y(0)
	main_circ.rz(param_0, 3)
	main_circ.s(qreg_0[0])
	main_circ.s(qreg_0[0])
	main_circ.rx(param_1, 2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rz(param_2, 3)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rx(param_2, 3)
	main_circ.rz(0.410000, 0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(qreg_0[0])
	main_circ.s(0)
	main_circ.rx(param_2, 2)
with else_1:
	main_circ.rz(param_0, 2)
	main_circ.s(3)
	main_circ.rx(0.585000, 3)
	main_circ.y(qreg_0[0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(-0.391000, 3)
	main_circ.rx(0.295000, 3)
	main_circ.rz(param_1, 2)
	main_circ.rz(param_0, 1)
	main_circ.s(1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(-0.852000, 0)
		main_circ.rx(-0.169000, 0)
		main_circ.rz(param_0, qreg_0[0])
		main_circ.s(qreg_0[0])
	with case_1(1):
		main_circ.s(2)
		main_circ.y(2)
		main_circ.s(1)
		main_circ.y(1)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(param_1, 0)
	main_circ.rx(-0.618000, qreg_0[0])
with else_1:
	main_circ.rx(param_2, 1)
main_circ.y(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rx(0.287000, qreg_0[0])
	main_circ.y(1)
	main_circ.rz(0.797000, qreg_0[0])
	main_circ.rz(-0.482000, 0)
	main_circ.rz(param_2, 1)
with else_1:
	main_circ.rx(param_2, 0)
	main_circ.y(qreg_0[0])
bindings = {param_0: -0.327000, param_1: 0.212000, param_2: -0.182000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "583")
