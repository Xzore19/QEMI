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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.y(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_1, 0)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cx(2,0)
	main_circ.cx(1,3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(2)
	main_circ.rz(param_3, qreg_0[0])
	main_circ.cx(qreg_0[0],2)
	main_circ.cx(0,1)
	main_circ.cx(3,2)
with else_1:
	main_circ.u(param_3,-0.098000,0.320000, 1)
main_circ.rz(-0.888000, 2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(qreg_0[0],3)
	main_circ.u(param_3,0.094000,-0.786000, 1)
	main_circ.rz(-0.020000, 0)
	main_circ.y(1)
	main_circ.rz(param_4, 2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(1)
		main_circ.rz(-0.917000, 2)
		main_circ.cx(3,2)
		main_circ.rz(-0.057000, 0)
	with case_1(1):
		main_circ.y(2)
		main_circ.cx(qreg_0[0],3)
		main_circ.cx(3,2)
		main_circ.cx(1,0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(0,1)
with else_1:
	main_circ.y(qreg_0[0])
	main_circ.cx(2,3)
	main_circ.u(param_1,0.657000,param_2, 0)
	main_circ.rz(param_4, 2)
main_circ.cx(0,qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_3,-0.956000,0.207000, 2)
	main_circ.y(2)
	main_circ.u(param_0,param_2,-0.842000, 1)
	main_circ.y(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(3,0)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rz(0.506000, 3)
		main_circ.y(2)
		main_circ.cx(0,2)
		main_circ.y(1)
	with case_1(1):
		main_circ.u(pi/2,-0.733000,-0.375000, 0)
		main_circ.rz(0.916000, 1)
		main_circ.u(pi/2,param_4,param_3, 2)
		main_circ.y(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(2,3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(0.643000, 2)
	main_circ.rz(param_1, 3)
	main_circ.y(1)
with else_1:
	main_circ.y(1)
	main_circ.y(2)
	main_circ.y(1)
	main_circ.u(param_0,param_3,param_0, qreg_0[0])
main_circ.u(param_3,-0.404000,0.178000, 2)
bindings = {param_0: 0.897000, param_1: 0.759000, param_2: -0.684000, param_3: 0.791000, param_4: 0.764000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "470")
