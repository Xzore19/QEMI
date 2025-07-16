from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rx(0.944000, qreg_0[0])
		main_circ.rx(param_3, qreg_2[0])
		main_circ.h(qreg_3[0])
		main_circ.rz(0.015000, qreg_0[1])
		main_circ.rx(param_3, qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cz(qreg_0[1],qreg_3[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(param_3, qreg_3[0])
		main_circ.cz(qreg_0[0],qreg_2[0])
		main_circ.h(qreg_2[0])
		main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cz(qreg_0[0],qreg_3[0])
		main_circ.rx(param_4, qreg_0[1])
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_0, qreg_2[0])
			main_circ.h(qreg_0[1])
			main_circ.h(qreg_0[0])
			main_circ.rx(0.141000, qreg_0[1])
		with case_1(1):
			main_circ.cz(qreg_0[1],qreg_3[0])
			main_circ.rz(param_2, qreg_0[1])
			main_circ.cz(qreg_0[1],qreg_3[0])
			main_circ.rx(0.377000, qreg_0[0])
with else_2:
	main_circ.rx(param_2, qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(qreg_2[0])
		main_circ.h(qreg_0[1])
	with else_1:
		main_circ.rx(param_2, qreg_0[1])
		main_circ.rz(-0.638000, qreg_3[0])
with else_2:
	main_circ.cz(qreg_0[1],qreg_2[0])
	main_circ.rz(0.459000, qreg_0[1])
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.cz(qreg_2[0],qreg_3[0])
			main_circ.rx(param_1, qreg_3[0])
			main_circ.rz(-0.810000, qreg_0[1])
			main_circ.cz(qreg_2[0],qreg_3[0])
		with case_1(1):
			main_circ.cz(qreg_3[0],qreg_0[1])
			main_circ.cz(qreg_2[0],qreg_0[0])
			main_circ.cz(qreg_0[1],qreg_2[0])
			main_circ.rx(param_3, qreg_3[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cz(qreg_3[0],qreg_0[1])
				main_circ.rz(-0.913000, qreg_0[1])
				main_circ.rz(-0.189000, qreg_3[0])
				main_circ.cz(qreg_0[0],qreg_3[0])
			with case_1(1):
				main_circ.rx(param_1, qreg_3[0])
				main_circ.h(qreg_3[0])
				main_circ.rz(param_2, qreg_0[1])
				main_circ.rz(param_0, qreg_2[0])
	with case_2(1):
		main_circ.measure(qreg_3[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.id(qreg_0[1])
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_3[0])
		with else_1:
			main_circ.id(qreg_0[0])
		main_circ.measure(qreg_2[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_0[1])
bindings = {param_0: -0.570000, param_1: 0.300000, param_2: 0.925000, param_3: -0.404000, param_4: -0.660000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1324")
