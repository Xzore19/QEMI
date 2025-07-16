from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rx(-0.425000, 0)
	main_circ.cx(qreg_3[0],0)
	main_circ.rx(0.816000, qreg_0[1])
with else_1:
	main_circ.cx(qreg_0[1],qreg_0[2])
	main_circ.cz(0,qreg_0[2])
	main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.h(qreg_0[0])
		main_circ.rx(-0.660000, qreg_0[0])
		main_circ.rx(param_0, qreg_0[0])
		main_circ.rx(param_1, qreg_3[0])
	with case_1(1):
		main_circ.rx(param_0, qreg_0[2])
		main_circ.h(qreg_3[0])
		main_circ.cx(qreg_0[0],0)
		main_circ.cz(qreg_0[1],qreg_3[0])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rx(0.629000, qreg_3[0])
		main_circ.cz(qreg_0[2],qreg_3[0])
		main_circ.rx(-0.749000, qreg_0[1])
		main_circ.h(qreg_0[0])
	with case_1(1):
		main_circ.cz(0,qreg_3[0])
		main_circ.h(qreg_0[0])
		main_circ.h(qreg_0[2])
		main_circ.h(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[2],qreg_3[0])
		main_circ.h(qreg_3[0])
		main_circ.cx(qreg_0[1],0)
		main_circ.h(qreg_0[0])
	with case_1(1):
		main_circ.h(qreg_0[1])
		main_circ.h(qreg_0[1])
		main_circ.cz(qreg_3[0],qreg_0[0])
		main_circ.rx(param_1, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rx(0.471000, 0)
	main_circ.cz(qreg_0[2],qreg_0[0])
	main_circ.rx(param_0, qreg_0[1])
with else_1:
	main_circ.cx(qreg_0[1],qreg_0[2])
	main_circ.h(qreg_0[0])
	main_circ.rx(param_1, qreg_0[0])
main_circ.rx(0.275000, qreg_3[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(qreg_3[0])
	main_circ.cz(qreg_0[1],qreg_3[0])
	main_circ.cx(qreg_0[1],0)
	main_circ.cz(qreg_0[1],qreg_3[0])
	main_circ.cx(qreg_0[0],qreg_0[1])
with else_1:
	main_circ.rx(param_0, qreg_0[0])
	main_circ.id(0)
bindings = {param_0: 0.620000, param_1: 0.138000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "372", "ResetAfterMeasureSimplification")
