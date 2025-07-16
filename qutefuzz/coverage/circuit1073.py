from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.ry(param_6, 0)
			main_circ.rz(param_7, qreg_3[0])
			main_circ.cy(0,qreg_0[2])
			main_circ.rz(0.430000, 0)
		with else_1:
			main_circ.cy(qreg_3[0],qreg_0[1])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rz(param_0, qreg_0[0])
			main_circ.ry(0.106000, qreg_0[1])
			main_circ.cy(qreg_0[0],qreg_0[2])
			main_circ.rx(param_7, qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.ry(param_6, 1)
		main_circ.rx(-0.887000, qreg_3[0])
	with else_1:
		main_circ.rx(param_4, 1)
		main_circ.ry(param_0, qreg_3[0])
		main_circ.rx(-0.411000, qreg_0[0])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rx(param_7, qreg_0[1])
		main_circ.rx(0.136000, 0)
		main_circ.ry(param_7, qreg_0[2])
		main_circ.rx(-0.617000, qreg_0[2])
		main_circ.cy(1,qreg_0[2])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.rz(0.332000, qreg_0[1])
		main_circ.ry(0.032000, qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.rz(-0.962000, 1)
		main_circ.rz(param_1, qreg_0[1])
		main_circ.rz(param_3, qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.ry(-0.048000, qreg_0[2])
			main_circ.rx(param_2, qreg_3[0])
			main_circ.cy(qreg_0[2],0)
			main_circ.cy(qreg_3[0],qreg_0[0])
		with case_1(1):
			main_circ.rz(param_2, qreg_0[1])
			main_circ.rx(-0.486000, 0)
			main_circ.ry(0.659000, 0)
			main_circ.cy(qreg_0[2],0)
with else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(qreg_3[0],qreg_0[0])
	with else_1:
		main_circ.cy(1,qreg_0[0])
		main_circ.cy(qreg_0[0],qreg_0[1])
		main_circ.cy(qreg_0[0],0)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(0,qreg_0[2])
		main_circ.rx(0.562000, 0)
	with else_1:
		main_circ.cy(qreg_0[0],qreg_3[0])
		main_circ.rx(-0.770000, qreg_0[0])
		main_circ.ry(-0.993000, qreg_0[1])
		main_circ.cy(0,qreg_0[0])
		main_circ.cy(0,1)
bindings = {param_0: 0.959000, param_1: -0.261000, param_2: 0.055000, param_3: -0.955000, param_4: -0.895000, param_6: 0.877000, param_7: -0.566000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1073")
