from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
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

main_circ.ry(param_1, qreg_1[1])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(-0.125000, qreg_0[0])
	main_circ.z(qreg_1[1])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(0.740000,param_1,-0.249000, qreg_1[1])
	main_circ.z(qreg_1[0])
	main_circ.z(qreg_1[1])
	main_circ.z(qreg_0[0])
	main_circ.ry(param_2, qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.h(qreg_1[0])
		main_circ.ry(0.588000, qreg_1[0])
		main_circ.ry(param_1, qreg_3[0])
		main_circ.ry(-0.754000, qreg_3[0])
	with case_1(1):
		main_circ.ry(0.077000, qreg_0[0])
		main_circ.z(qreg_0[0])
		main_circ.z(qreg_1[1])
		main_circ.ry(param_3, qreg_1[1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_3[0])
		main_circ.u(0.333000,param_2,-0.861000, qreg_0[0])
		main_circ.ry(param_1, qreg_1[1])
		main_circ.u(0.023000,-0.344000,0.420000, qreg_1[1])
	with case_1(1):
		main_circ.u(param_2,0.813000,-0.513000, qreg_1[0])
		main_circ.ry(0.336000, qreg_1[1])
		main_circ.u(-0.738000,-0.729000,param_2, qreg_1[0])
		main_circ.z(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(param_2, qreg_1[0])
	main_circ.h(qreg_1[0])
	main_circ.z(qreg_1[0])
with else_1:
	main_circ.h(qreg_3[0])
main_circ.h(qreg_3[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(-0.071000,param_3,-0.835000, qreg_1[0])
		main_circ.u(0.289000,param_2,param_0, qreg_1[0])
		main_circ.u(param_0,-0.955000,-0.531000, qreg_0[0])
		main_circ.u(-0.815000,0.533000,0.036000, qreg_1[0])
	with case_1(1):
		main_circ.h(qreg_1[0])
		main_circ.u(-0.776000,-0.273000,-0.842000, qreg_3[0])
		main_circ.h(qreg_1[0])
		main_circ.z(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.180000, qreg_1[0])
	main_circ.u(param_1,param_3,param_1, qreg_1[0])
	main_circ.ry(param_1, qreg_0[0])
	main_circ.z(qreg_0[0])
with else_1:
	main_circ.z(qreg_1[1])
bindings = {param_0: -0.941000, param_1: 0.031000, param_2: 0.957000, param_3: -0.342000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "174", "ElidePermutations")
