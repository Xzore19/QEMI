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
subcirc0.u(pi/2,-0.644000,0.720000, qreg_2[0])
subcirc0.y(qreg_0[0])
subcirc0.u(0,0,0.061000, qreg_0[0])
subcirc0.y(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,0.350000, qreg_0[1])
subcirc1.u(pi/2,0.249000,-0.019000, qreg_0[1])
subcirc1.u(pi/2,-0.034000,0.972000, qreg_0[0])
subcirc1.ry(-0.632000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.249000, qreg_3[0])
subcirc2.u(0,0,-0.983000, qreg_0[2])
subcirc2.u(0,0,-0.752000, qreg_0[2])
subcirc2.u(pi/2,-0.433000,-0.302000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(pi/2,param_2,-0.070000, qreg_0[0])
		main_circ.u(param_0,-0.427000,-0.328000, qreg_0[0])
		main_circ.append(subcirc0,[0,2,qreg_0[0],3])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc2,[0,qreg_0[0],2,1,3])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(3)
			main_circ.y(1)
			main_circ.u(param_0,0.244000,param_1, 2)
			main_circ.append(subcirc2,[1,qreg_0[0],2,0,3])
		with case_1(1):
			main_circ.u(param_1,param_0,param_1, qreg_0[0])
			main_circ.append(subcirc1,[1,qreg_0[0],0,2])
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(pi/2,-0.748000,param_1, 0)
	with else_1:
		main_circ.u(param_1,0,param_1, 0)
		main_circ.y(3)
		main_circ.append(subcirc0,[3,2,1,qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.y(0)
		main_circ.ry(param_2, qreg_0[0])
	with else_1:
		main_circ.ry(-0.812000, 2)
		main_circ.u(param_1,param_0,-0.117000, 0)
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(-0.203000, 1)
			main_circ.u(param_2,param_1,0.225000, 0)
			main_circ.ry(0.839000, 3)
			main_circ.append(subcirc1,[1,2,0,3])
		with case_1(1):
			main_circ.append(subcirc0,[qreg_0[0],3,1,2])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc1,[2,3,qreg_0[0],0])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_1,0,param_2, 3)
		main_circ.y(1)
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc2,[3,1,0,qreg_0[0],2])
	with else_1:
		main_circ.append(subcirc2,[2,3,qreg_0[0],0,1])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.ry(param_0, 0)
		main_circ.u(pi/2,0.452000,param_0, 2)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(3)
	with else_1:
		main_circ.barrier(3)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(2)
	with else_1:
		main_circ.id(0)
	main_circ.id(1)
bindings = {param_0: -0.127000, param_1: -0.169000, param_2: -0.659000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1661", "ResetAfterMeasureSimplification")
