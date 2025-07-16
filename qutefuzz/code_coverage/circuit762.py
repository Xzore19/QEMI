from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(param_1, qreg_1[0])
	main_circ.ry(param_0, qreg_1[0])
	main_circ.u(param_2,0.782000,-0.932000, qreg_1[1])
	main_circ.u(param_0,-0.093000,-0.355000, qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_0,-0.906000,param_1, qreg_1[1])
main_circ.measure(qreg_1[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(0,qreg_1[0])
	main_circ.x(0)
	main_circ.ry(0.279000, qreg_0[0])
	main_circ.u(-0.482000,-0.196000,0.397000, qreg_1[0])
	main_circ.x(qreg_1[0])
with else_1:
	main_circ.ry(0.099000, qreg_1[0])
	main_circ.ry(-0.981000, 1)
	main_circ.u(param_1,param_2,0.415000, qreg_1[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.ry(param_0, qreg_1[1])
	main_circ.u(-0.653000,param_2,0.180000, qreg_1[1])
	main_circ.ry(param_1, 1)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_0[0],qreg_1[0])
	main_circ.u(0.696000,0.173000,param_2, 1)
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_1[2],qreg_0[0])
	main_circ.cz(1,qreg_1[0])
	main_circ.x(qreg_1[1])
	main_circ.u(0.741000,-0.216000,param_0, 1)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_2,param_1,0.865000, qreg_1[1])
		main_circ.ry(-0.117000, qreg_1[0])
		main_circ.u(param_1,-0.387000,-0.424000, qreg_1[2])
		main_circ.x(qreg_1[1])
	with case_1(1):
		main_circ.ry(0.952000, qreg_1[2])
		main_circ.x(qreg_0[0])
		main_circ.cz(qreg_1[2],0)
		main_circ.cz(0,1)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(0,qreg_0[0])
with else_1:
	main_circ.u(-0.974000,0.430000,-0.309000, qreg_1[2])
	main_circ.ry(param_1, qreg_1[1])
	main_circ.x(qreg_1[1])
	main_circ.cz(0,qreg_0[0])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(qreg_1[0])
	main_circ.x(0)
with else_1:
	main_circ.x(qreg_0[0])
	main_circ.u(param_1,param_0,0.717000, qreg_1[0])
	main_circ.x(qreg_1[2])
	main_circ.cz(qreg_1[0],qreg_1[1])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(1,qreg_0[0])
	main_circ.cz(qreg_1[2],qreg_0[0])
	main_circ.cz(1,qreg_1[2])
	main_circ.cz(qreg_1[1],qreg_1[0])
main_circ.cz(qreg_1[0],qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(qreg_1[0],1)
	main_circ.cz(qreg_1[2],qreg_1[1])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(qreg_0[0],1)
	main_circ.cz(qreg_0[0],qreg_1[1])
	main_circ.u(param_2,-0.944000,param_2, 0)
	main_circ.u(-0.056000,0.046000,param_2, qreg_1[1])
	main_circ.u(param_2,param_1,-0.083000, qreg_1[1])
with else_1:
	main_circ.u(param_0,0.455000,-0.971000, 1)
	main_circ.ry(param_2, 0)
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(param_0,0.364000,param_2, qreg_1[1])
	main_circ.cz(qreg_1[0],qreg_1[2])
	main_circ.id(qreg_1[1])
with else_1:
	main_circ.id(1)
bindings = {param_0: 0.629000, param_1: 0.266000, param_2: -0.141000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "762", "ElidePermutations")
