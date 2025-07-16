from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.ry(param_0, 0)
main_circ.ry(param_0, 3)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.y(2)
			main_circ.s(0)
			main_circ.s(qreg_0[1])
			main_circ.y(1)
			main_circ.ry(0.890000, 0)
		with else_1:
			main_circ.s(qreg_0[1])
			main_circ.y(1)
			main_circ.u(param_0,param_0,param_0, qreg_0[1])
			main_circ.ry(param_0, qreg_0[1])
with else_3:
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.y(2)
				main_circ.ry(-0.354000, 3)
				main_circ.ry(param_0, qreg_0[0])
				main_circ.u(pi/2,param_0,param_0, 3)
			with case_1(1):
				main_circ.s(0)
				main_circ.ry(0.789000, 3)
				main_circ.y(qreg_0[0])
				main_circ.u(param_0,param_0,0.721000, 2)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.ry(param_0, qreg_0[1])
			main_circ.u(pi/2,0.535000,-0.239000, 1)
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.ry(0.895000, 2)
					main_circ.s(2)
					main_circ.s(3)
					main_circ.u(param_0,param_0,param_0, 1)
				with case_1(1):
					main_circ.ry(-0.027000, qreg_0[1])
					main_circ.y(0)
					main_circ.y(3)
					main_circ.ry(param_0, qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(pi/2,param_0,param_0, 0)
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.s(qreg_0[0])
				main_circ.y(0)
				main_circ.ry(0.755000, 2)
				main_circ.y(3)
			with else_1:
				main_circ.s(qreg_0[1])
				main_circ.u(pi/2,param_0,param_0, 0)
	with case_3(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.ry(param_0, qreg_0[0])
				main_circ.s(2)
				main_circ.ry(0.095000, 3)
				main_circ.ry(0.393000, 3)
				main_circ.s(0)
			with else_1:
				main_circ.y(0)
		with else_2:
			main_circ.ry(param_0, qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.ry(0.823000, qreg_0[0])
				main_circ.y(qreg_0[1])
				main_circ.s(1)
				main_circ.u(pi/2,0.295000,-0.288000, 2)
			with else_1:
				main_circ.s(2)
bindings = {param_0: -0.423000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1194", "Collect2qBlocks")
