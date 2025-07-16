from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.h(2)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.h(0)
		main_circ.rx(param_4, 0)
		main_circ.cy(qreg_0[0],2)
		main_circ.ry(-0.873000, qreg_0[0])
with else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cy(qreg_1[0],3)
		main_circ.rx(param_0, 3)
		main_circ.ry(-0.892000, 1)
		main_circ.h(qreg_0[0])
		main_circ.ry(-0.285000, 0)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.h(1)
		main_circ.rx(-0.845000, qreg_1[0])
	main_circ.ry(0.106000, 1)
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.h(3)
		main_circ.h(qreg_0[0])
		main_circ.rx(param_0, 1)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rx(param_2, qreg_1[0])
			main_circ.ry(0.094000, qreg_0[0])
		with else_1:
			main_circ.ry(param_4, qreg_1[0])
			main_circ.rx(-0.434000, 3)
			main_circ.ry(0.124000, qreg_0[0])
			main_circ.h(0)
	with case_2(1):
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.ry(-0.714000, 3)
				main_circ.ry(0.366000, qreg_1[0])
				main_circ.rx(param_2, 3)
				main_circ.h(0)
			with case_1(1):
				main_circ.h(2)
				main_circ.ry(param_3, qreg_0[0])
				main_circ.h(2)
				main_circ.cy(qreg_0[0],3)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.rx(0.314000, 3)
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.ry(param_2, 0)
			main_circ.h(2)
			main_circ.cy(qreg_0[0],qreg_1[0])
			main_circ.cy(2,1)
		with case_1(1):
			main_circ.cy(1,2)
			main_circ.cy(0,qreg_1[0])
			main_circ.cy(3,2)
			main_circ.cy(1,3)
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.cy(2,3)
		main_circ.cy(qreg_0[0],2)
		main_circ.cy(qreg_1[0],2)
		main_circ.cy(qreg_0[0],0)
		main_circ.cy(2,qreg_1[0])
	with else_1:
		main_circ.ry(-0.927000, qreg_1[0])
		main_circ.cy(2,qreg_0[0])
		main_circ.h(0)
bindings = {param_0: -0.217000, param_2: -0.890000, param_3: -0.860000, param_4: 0.616000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1315")
