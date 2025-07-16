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
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.u(0,0,param_4, qreg_0[0])
main_circ.u(param_3,0,-0.986000, qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(3)
	main_circ.ry(param_2, 2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(param_4,0,param_1, 2)
with else_1:
	main_circ.u(pi/2,param_4,param_0, qreg_1[0])
	main_circ.ry(param_0, 2)
	main_circ.u(param_1,0,-0.852000, 0)
main_circ.u(param_4,param_2,param_2, qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(2)
		main_circ.u(param_2,param_3,-0.912000, 3)
		main_circ.u(param_3,param_4,param_0, 2)
		main_circ.ry(-0.412000, qreg_1[0])
	with case_1(1):
		main_circ.y(qreg_0[0])
		main_circ.u(pi/2,-0.592000,0.572000, 0)
		main_circ.u(0,param_1,0.113000, qreg_1[0])
		main_circ.u(param_2,-0.741000,param_2, 3)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_2,0,param_0, qreg_1[0])
		main_circ.u(0,param_1,param_3, 1)
		main_circ.u(param_3,param_0,param_4, 3)
		main_circ.u(param_4,-0.377000,0.294000, qreg_1[0])
	with case_1(1):
		main_circ.ry(param_4, qreg_0[0])
		main_circ.u(0,0,param_1, 1)
		main_circ.y(0)
		main_circ.u(param_1,param_2,param_3, qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(1)
	main_circ.y(0)
with else_1:
	main_circ.ry(param_3, 3)
	main_circ.ry(-0.505000, qreg_1[0])
	main_circ.u(0,0,param_2, 0)
	main_circ.ry(param_3, 1)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0,0,param_4, 1)
		main_circ.u(pi/2,param_4,0.104000, 3)
		main_circ.u(param_0,0.237000,param_0, 2)
		main_circ.ry(-0.536000, qreg_0[0])
	with case_1(1):
		main_circ.u(pi/2,0.013000,-0.360000, 0)
		main_circ.y(qreg_1[0])
		main_circ.ry(-0.621000, 3)
		main_circ.ry(param_4, 3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,0,-0.830000, qreg_0[0])
		main_circ.y(qreg_1[0])
		main_circ.u(pi/2,param_2,-0.026000, 0)
		main_circ.u(0,0,param_3, qreg_0[0])
	with case_1(1):
		main_circ.u(param_4,param_3,param_4, 3)
		main_circ.u(pi/2,param_0,param_4, 1)
		main_circ.y(1)
		main_circ.u(0,0,0.565000, qreg_1[0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.ry(param_4, qreg_0[0])
	main_circ.u(param_2,param_0,0.924000, 0)
	main_circ.ry(0.583000, 1)
	main_circ.u(param_4,0,param_1, qreg_1[0])
	main_circ.u(0,0,param_4, 1)
with else_1:
	main_circ.u(0,param_3,-0.183000, 0)
	main_circ.ry(param_4, 3)
	main_circ.u(pi/2,0.383000,param_3, 0)
	main_circ.y(0)
bindings = {param_0: -0.804000, param_1: -0.929000, param_2: -0.962000, param_3: 0.109000, param_4: 0.738000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "726", "NormalizeRXAngle")
