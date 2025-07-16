from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.cz(qreg_0[3],qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.cz(qreg_0[0],qreg_0[3])
subcirc0.u(0.353000,-0.293000,-0.522000, qreg_0[1])
subcirc0.rz(-0.537000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(-0.379000,-0.160000,-0.026000, qreg_0[3])
subcirc1.rz(0.552000, qreg_0[3])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.142000, qreg_0[1])
subcirc2.y(qreg_0[1])
subcirc2.u(-0.885000,-0.141000,0.593000, qreg_0[0])
subcirc2.rz(-0.989000, qreg_3[0])
subcirc2.cz(qreg_3[0],qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc2,[qreg_2[0],0,qreg_3[0],qreg_0[0]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(0,qreg_0[0])
	main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],qreg_0[0],qreg_2[0],1])
with else_1:
	main_circ.append(subcirc1,[qreg_3[0],1,0,qreg_2[0],qreg_1[0]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.y(qreg_1[0])
		main_circ.cz(qreg_3[0],qreg_0[0])
		main_circ.u(-0.161000,0.476000,0.560000, qreg_3[0])
		main_circ.append(subcirc2,[qreg_2[0],qreg_1[0],qreg_3[0],0])
	with case_1(1):
		main_circ.u(param_2,-0.088000,param_1, qreg_2[0])
		main_circ.append(subcirc1,[0,qreg_3[0],1,qreg_0[0],qreg_2[0]])
main_circ.rz(param_0, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_2[0],1])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(-0.575000,1.000000,-0.496000, qreg_2[0])
	main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],0,qreg_3[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(1,qreg_2[0])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(0,qreg_2[0])
	main_circ.cz(qreg_1[0],1)
	main_circ.rz(param_2, qreg_2[0])
with else_1:
	main_circ.append(subcirc2,[qreg_3[0],qreg_2[0],0,1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[qreg_0[0],1,0,qreg_2[0],qreg_3[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(1,qreg_3[0])
	main_circ.id(qreg_1[0])
with else_1:
	main_circ.barrier(qreg_2[0])
bindings = {param_0: 0.167000, param_1: 0.544000, param_2: -0.770000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1850", "OptimizeAnnotated")
