from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(-0.003000,0.614000,-0.874000, qreg_1[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.035000, qreg_0[0])
	main_circ.cz(qreg_1[0],qreg_1[2])
	main_circ.x(qreg_0[0])
	main_circ.u(param_0,0.254000,-0.655000, 0)
	main_circ.cz(0,qreg_1[2])
with else_1:
	main_circ.u(param_0,param_0,param_0, 0)
	main_circ.u(param_0,param_0,param_0, qreg_1[1])
	main_circ.x(qreg_1[2])
	main_circ.ry(-0.376000, qreg_1[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_0, qreg_1[2])
		main_circ.ry(param_0, 0)
		main_circ.ry(0.969000, qreg_1[2])
		main_circ.ry(0.760000, qreg_0[0])
	with case_1(1):
		main_circ.cz(qreg_1[1],qreg_1[0])
		main_circ.cz(qreg_1[1],qreg_1[2])
		main_circ.x(0)
		main_circ.u(param_0,0.075000,0.894000, qreg_1[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(param_0, qreg_1[0])
	main_circ.u(-0.479000,param_0,0.523000, qreg_0[0])
with else_1:
	main_circ.x(qreg_1[2])
	main_circ.ry(param_0, qreg_1[0])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_0,0.001000,0.039000, qreg_1[2])
with else_1:
	main_circ.ry(-0.823000, qreg_1[0])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(0,qreg_1[0])
	main_circ.ry(-0.884000, qreg_0[0])
with else_1:
	main_circ.x(qreg_1[2])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[0],0)
		main_circ.u(param_0,param_0,-0.555000, qreg_0[0])
		main_circ.u(param_0,-0.505000,param_0, qreg_1[2])
		main_circ.ry(-0.526000, 0)
	with case_1(1):
		main_circ.ry(-0.366000, qreg_1[2])
		main_circ.x(qreg_0[0])
		main_circ.x(0)
		main_circ.u(-0.002000,param_0,param_0, qreg_1[1])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(qreg_1[0],qreg_0[0])
	main_circ.x(qreg_1[0])
main_circ.u(param_0,0.292000,param_0, qreg_1[2])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(0)
	main_circ.cz(qreg_1[0],qreg_0[0])
	main_circ.cz(0,qreg_1[2])
	main_circ.cz(qreg_1[1],qreg_0[0])
	main_circ.cz(qreg_0[0],qreg_1[1])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(qreg_0[0],qreg_1[0])
	main_circ.cz(qreg_1[1],qreg_1[2])
	main_circ.cz(qreg_1[2],qreg_1[0])
	main_circ.cz(0,qreg_1[2])
with else_1:
	main_circ.cz(0,qreg_0[0])
	main_circ.u(-0.588000,param_0,-0.513000, qreg_1[2])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(-0.348000, qreg_1[2])
	main_circ.u(param_0,param_0,0.104000, 0)
main_circ.measure(qreg_1[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0.678000,param_0,0.010000, 0)
		main_circ.u(param_0,param_0,param_0, qreg_0[0])
		main_circ.ry(0.226000, qreg_0[0])
		main_circ.u(param_0,0.060000,0.128000, qreg_1[1])
	with case_1(1):
		main_circ.u(0.793000,param_0,0.473000, qreg_1[2])
		main_circ.id(0)
bindings = {param_0: -0.604000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1903")
