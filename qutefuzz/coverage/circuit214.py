from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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

main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(0.997000, qreg_3[0])
	main_circ.s(qreg_3[0])
	main_circ.rz(param_1, qreg_3[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(qreg_1[0],1)
	main_circ.cz(qreg_1[1],qreg_1[0])
with else_1:
	main_circ.cy(qreg_3[0],qreg_1[0])
main_circ.cz(qreg_3[0],qreg_1[1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_0[0],1)
		main_circ.s(0)
		main_circ.cy(qreg_1[0],qreg_0[0])
		main_circ.s(qreg_3[0])
	with case_1(1):
		main_circ.s(0)
		main_circ.rz(0.409000, qreg_0[0])
		main_circ.s(qreg_1[1])
		main_circ.cz(0,qreg_1[1])
main_circ.cz(0,1)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(1,qreg_1[1])
	main_circ.s(qreg_1[1])
	main_circ.cz(qreg_1[0],qreg_3[0])
with else_1:
	main_circ.cz(1,qreg_1[0])
	main_circ.cy(1,qreg_0[0])
	main_circ.cz(1,0)
	main_circ.cy(1,qreg_0[0])
	main_circ.s(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(0.286000, qreg_1[0])
	main_circ.cy(0,1)
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_0, 1)
		main_circ.s(1)
		main_circ.s(qreg_1[0])
		main_circ.rz(param_1, qreg_0[0])
	with case_1(1):
		main_circ.s(qreg_1[1])
		main_circ.rz(-0.748000, 1)
		main_circ.rz(-0.262000, 0)
		main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.cz(qreg_1[0],1)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(0,qreg_0[0])
	main_circ.s(qreg_0[0])
	main_circ.cz(qreg_1[1],0)
with else_1:
	main_circ.rz(-0.973000, 1)
	main_circ.cy(qreg_3[0],1)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(0)
		main_circ.cz(qreg_3[0],qreg_1[0])
		main_circ.s(0)
		main_circ.cz(0,qreg_1[0])
	with case_1(1):
		main_circ.rz(param_1, 1)
		main_circ.cy(qreg_3[0],qreg_0[0])
		main_circ.cz(qreg_3[0],1)
		main_circ.cz(qreg_3[0],0)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(1,qreg_1[1])
	main_circ.s(qreg_1[0])
	main_circ.rz(-0.196000, qreg_1[0])
	main_circ.s(1)
with else_1:
	main_circ.cy(qreg_0[0],1)
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cy(1,0)
with else_1:
	main_circ.rz(-0.699000, 1)
	main_circ.cz(qreg_1[1],qreg_0[0])
	main_circ.cy(1,qreg_1[0])
	main_circ.s(qreg_0[0])
main_circ.cz(0,qreg_3[0])
bindings = {param_0: 0.506000, param_1: -0.671000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "214", "TemplateOptimization")
