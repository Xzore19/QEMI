from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.z(qreg_0[2])
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_0[0],1)
			main_circ.u(0,param_0,-0.064000, qreg_0[0])
			main_circ.cy(qreg_0[0],qreg_0[1])
			main_circ.z(qreg_0[0])
		with case_1(1):
			main_circ.cy(qreg_0[2],qreg_0[1])
			main_circ.ry(-0.442000, qreg_0[0])
			main_circ.u(param_0,0,param_0, qreg_0[0])
			main_circ.ry(-0.402000, qreg_0[1])
main_circ.cy(qreg_0[0],1)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.ry(-0.037000, qreg_0[0])
			main_circ.ry(param_0, qreg_0[3])
			main_circ.z(qreg_0[3])
			main_circ.u(param_0,0,0.246000, qreg_0[3])
		with case_1(1):
			main_circ.u(0,0,0.488000, 0)
			main_circ.ry(param_0, qreg_0[3])
			main_circ.cy(qreg_0[2],0)
			main_circ.cy(qreg_0[0],1)
with else_2:
	main_circ.ry(param_0, qreg_0[0])
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.z(qreg_0[2])
			main_circ.cy(0,qreg_0[2])
			main_circ.u(param_0,0,param_0, qreg_0[1])
			main_circ.ry(param_0, 0)
		with case_1(1):
			main_circ.ry(-0.948000, 1)
			main_circ.ry(param_0, 1)
			main_circ.z(qreg_0[0])
			main_circ.z(qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.ry(-0.184000, qreg_0[3])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.z(qreg_0[0])
			main_circ.u(0,param_0,-0.617000, qreg_0[2])
			main_circ.cy(qreg_0[3],qreg_0[2])
			main_circ.z(qreg_0[1])
		with else_1:
			main_circ.u(param_0,param_0,0.591000, 0)
			main_circ.cy(qreg_0[1],qreg_0[2])
			main_circ.cy(qreg_0[0],1)
			main_circ.cy(1,qreg_0[0])
			main_circ.cy(1,0)
	with case_2(1):
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.cy(qreg_0[2],0)
			main_circ.cy(qreg_0[3],qreg_0[1])
		with else_1:
			main_circ.ry(param_0, 0)
		main_circ.z(1)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(param_0,0,0.030000, 0)
			main_circ.z(0)
			main_circ.z(qreg_0[2])
			main_circ.z(qreg_0[2])
		with case_1(1):
			main_circ.u(param_0,0,0.429000, 0)
			main_circ.ry(param_0, 1)
			main_circ.id(qreg_0[0])
bindings = {param_0: 0.475000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "538", "Optimize1qGatesDecomposition")
