from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.y(qreg_1[2])
subcirc0.ry(0.003000, qreg_1[2])
subcirc0.ry(-0.548000, qreg_0[0])
subcirc0.s(qreg_1[1])
subcirc0.y(qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0.317000,-0.525000,0.930000, qreg_0[0])
subcirc1.s(qreg_2[1])
subcirc1.y(qreg_0[0])
subcirc1.u(0.220000,-0.630000,-0.602000, qreg_0[1])
subcirc1.u(-0.911000,0.498000,-0.579000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.ry(-0.220000, qreg_1[0])
subcirc2.y(qreg_1[0])
subcirc2.y(qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.ry(-0.160000, qreg_0[3])
subcirc3.y(qreg_0[2])
subcirc3.u(0.816000,-0.506000,-0.498000, qreg_0[2])
subcirc3.y(qreg_0[2])
subcirc3.u(0.213000,-0.394000,-0.558000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.ry(-0.429000, qreg_2[0])
subcirc4.s(qreg_2[1])
subcirc4.u(0.185000,0.286000,0.909000, qreg_2[1])
subcirc4.s(qreg_0[1])
subcirc4.u(0.975000,-0.066000,0.782000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(2)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(qreg_1[0])
	main_circ.append(subcirc0,[0,qreg_0[0],qreg_3[0],qreg_1[1]])
with else_1:
	main_circ.y(qreg_1[0])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,param_4,-0.059000, qreg_3[0])
		main_circ.append(subcirc2,[0,qreg_1[0],1,qreg_3[0]])
	with case_1(1):
		main_circ.append(subcirc1,[0,qreg_0[0],qreg_1[0],qreg_3[0]])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_3[0],0])
with else_1:
	main_circ.ry(0.321000, qreg_1[1])
	main_circ.y(qreg_1[0])
	main_circ.s(qreg_0[0])
main_circ.append(subcirc1,[qreg_3[0],0,qreg_0[0],qreg_1[1]])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_3[0])
	main_circ.s(qreg_1[1])
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.append(subcirc1,[qreg_1[0],qreg_1[1],0,qreg_0[0]])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(-0.447000,param_3,-0.005000, 1)
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.barrier(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.582000, 0)
with else_1:
	main_circ.barrier(0)
bindings = {param_1: 0.009000, param_3: -0.040000, param_4: 0.196000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "557", "Optimize1qGatesSimpleCommutation")
