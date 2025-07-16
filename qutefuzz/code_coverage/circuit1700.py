from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.y(qreg_1[0])
subcirc0.u(pi/2,0.900000,0.271000, qreg_3[0])
subcirc0.cz(qreg_1[1],qreg_3[0])
subcirc0.y(qreg_1[0])
subcirc0.u(pi/2,-0.931000,0.697000, qreg_0[0])
subcirc0.y(qreg_1[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[2])
subcirc1.ry(-0.060000, qreg_0[1])
subcirc1.u(pi/2,0.075000,0.400000, qreg_0[3])
subcirc1.u(pi/2,0.365000,0.470000, qreg_0[1])
subcirc1.cz(qreg_0[2],qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.u(pi/2,-0.510000,-0.436000, qreg_0[1])
subcirc2.cz(qreg_0[1],qreg_2[0])
subcirc2.cz(qreg_2[1],qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_2[0])
subcirc2.u(pi/2,0.895000,0.073000, qreg_2[1])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.u(param_1,0.085000,-0.163000, qreg_0[3])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(-0.655000, qreg_0[3])
	main_circ.ry(param_2, qreg_0[3])
	main_circ.id(0)
with else_1:
	main_circ.cz(qreg_0[0],qreg_0[2])
	main_circ.cz(0,qreg_0[3])
main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[0],qreg_0[3]])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(qreg_0[1],qreg_0[2])
	main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[0],0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_0[2])
with else_1:
	main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[2])
main_circ.u(param_0,0.019000,param_0, qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(0)
with else_1:
	main_circ.id(qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(-0.822000, 0)
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.y(0)
	main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.ry(0.038000, qreg_0[2])
		main_circ.id(qreg_0[3])
main_circ.cz(qreg_0[3],qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(0)
	main_circ.ry(-0.820000, qreg_0[2])
	main_circ.cz(qreg_0[3],0)
with else_1:
	main_circ.append(subcirc1,[qreg_0[0],qreg_0[3],qreg_0[1],0])
main_circ.cz(qreg_0[2],0)
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(param_1, qreg_0[2])
	main_circ.ry(param_0, qreg_0[1])
	main_circ.cz(qreg_0[0],qreg_0[3])
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(qreg_0[3])
with else_1:
	main_circ.append(subcirc1,[0,qreg_0[2],qreg_0[1],qreg_0[3]])
main_circ.cz(qreg_0[1],qreg_0[0])
bindings = {param_0: -0.066000, param_1: 0.994000, param_2: 0.082000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1700", "RemoveFinalReset")
