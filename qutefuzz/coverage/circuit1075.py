from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(param_0, qreg_0[0])
	main_circ.u(param_1,0.030000,0.324000, qreg_3[0])
	main_circ.x(qreg_3[0])
	main_circ.y(qreg_3[0])
	main_circ.x(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(0)
	main_circ.u(-0.100000,param_1,-0.898000, qreg_0[1])
	main_circ.x(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0.680000,-0.681000,-0.349000, qreg_0[1])
	main_circ.u(-0.849000,0.465000,-0.845000, qreg_0[1])
	main_circ.ry(0.971000, 0)
	main_circ.x(qreg_2[0])
	main_circ.x(qreg_0[1])
with else_1:
	main_circ.y(qreg_0[0])
	main_circ.ry(param_3, qreg_0[1])
	main_circ.x(qreg_0[0])
	main_circ.x(qreg_3[0])
main_circ.u(param_0,-0.076000,param_2, qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0.791000,-0.170000,param_3, qreg_0[0])
	main_circ.u(-0.227000,param_1,-0.425000, qreg_0[0])
	main_circ.ry(-0.234000, 0)
	main_circ.ry(param_0, 0)
	main_circ.x(0)
with else_1:
	main_circ.u(param_4,param_3,0.205000, qreg_2[0])
	main_circ.ry(-0.313000, qreg_0[0])
	main_circ.u(-0.420000,param_4,param_4, 0)
	main_circ.x(qreg_3[0])
	main_circ.ry(-0.423000, qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.841000, qreg_0[0])
	main_circ.ry(param_2, qreg_0[0])
	main_circ.ry(0.578000, qreg_3[0])
	main_circ.ry(param_0, qreg_2[0])
	main_circ.u(-0.478000,0.617000,param_4, qreg_0[0])
with else_1:
	main_circ.x(0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(qreg_0[1])
	main_circ.x(qreg_0[1])
	main_circ.y(qreg_3[0])
	main_circ.ry(param_3, qreg_0[1])
with else_1:
	main_circ.y(qreg_0[0])
	main_circ.y(qreg_0[1])
	main_circ.u(param_0,-0.514000,param_0, qreg_0[1])
	main_circ.ry(param_0, qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(-0.420000,-0.819000,-0.119000, qreg_3[0])
	main_circ.y(qreg_3[0])
	main_circ.x(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(-0.745000, 0)
	main_circ.x(0)
	main_circ.ry(0.473000, 0)
with else_1:
	main_circ.ry(param_1, qreg_2[0])
	main_circ.u(param_2,0.012000,param_4, qreg_0[0])
	main_circ.u(param_1,-0.951000,param_0, qreg_3[0])
	main_circ.ry(param_2, qreg_0[1])
	main_circ.x(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(qreg_3[0])
	main_circ.u(-0.204000,0.674000,0.900000, 0)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(param_1,-0.816000,param_3, 0)
		main_circ.x(qreg_3[0])
		main_circ.id(0)
	with case_1(1):
		main_circ.id(qreg_0[0])
bindings = {param_0: 0.706000, param_1: 0.580000, param_2: -0.716000, param_3: 0.495000, param_4: 0.103000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1075")
