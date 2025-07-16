from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(pi/2,0.052000,0.884000, qreg_0[1])
subcirc0.rz(0.006000, qreg_0[1])
subcirc0.u(pi/2,0.249000,-0.951000, qreg_2[1])
subcirc0.rz(-0.650000, qreg_2[1])
subcirc0.u(pi/2,-0.535000,-0.421000, qreg_0[0])
subcirc0.u(pi/2,-0.169000,-0.288000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.s(qreg_3[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.y(qreg_0[0])
		main_circ.y(qreg_2[0])
		main_circ.u(pi/2,param_5,-0.948000, 0)
		main_circ.y(qreg_2[0])
	with case_1(1):
		main_circ.s(qreg_3[0])
		main_circ.s(0)
		main_circ.y(qreg_0[0])
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(0)
	main_circ.id(1)
with else_1:
	main_circ.y(qreg_3[0])
main_circ.rz(0.462000, 0)
main_circ.u(pi/2,param_4,param_2, qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.y(0)
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(-0.708000, 0)
	main_circ.y(1)
	main_circ.rz(0.433000, qreg_0[0])
	main_circ.rz(param_2, 0)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(1)
		main_circ.y(qreg_2[0])
		main_circ.rz(param_1, qreg_0[0])
		main_circ.y(qreg_0[1])
	with case_1(1):
		main_circ.barrier(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(qreg_2[0])
	main_circ.s(qreg_0[0])
	main_circ.u(pi/2,param_4,param_2, qreg_3[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_4,param_4,0.079000, qreg_0[0])
	main_circ.u(pi/2,0.584000,param_3, 1)
	main_circ.rz(0.833000, qreg_0[1])
	main_circ.s(qreg_3[0])
main_circ.s(qreg_2[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(pi/2,-0.174000,param_5, 0)
main_circ.s(qreg_3[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(1)
	main_circ.u(param_4,param_0,0.856000, qreg_3[0])
	main_circ.y(qreg_2[0])
	main_circ.rz(param_4, qreg_3[0])
	main_circ.y(1)
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(-0.992000, qreg_2[0])
	main_circ.y(1)
	main_circ.y(qreg_2[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.s(qreg_3[0])
		main_circ.s(qreg_0[0])
		main_circ.s(qreg_0[1])
		main_circ.barrier(0)
	with case_1(1):
		main_circ.y(1)
		main_circ.rz(-0.143000, qreg_2[0])
		main_circ.u(param_0,0.486000,param_4, 1)
		main_circ.u(param_4,-0.023000,-0.535000, 0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,param_0,param_3, qreg_0[1])
	main_circ.y(qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(-0.172000, qreg_0[0])
	main_circ.rz(0.081000, qreg_3[0])
with else_1:
	main_circ.s(qreg_2[0])
	main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.504000, param_1: 0.141000, param_2: 0.381000, param_3: -0.397000, param_4: 0.529000, param_5: 0.650000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1384")
