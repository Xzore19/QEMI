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
subcirc0.u(0,0,-0.505000, qreg_2[0])
subcirc0.u(0,0,0.990000, qreg_0[0])
subcirc0.h(qreg_0[1])
subcirc0.y(qreg_2[0])
subcirc0.rz(-0.507000, qreg_2[1])
subcirc0.y(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.rz(-0.972000, qreg_1[1])
subcirc1.y(qreg_1[0])
subcirc1.u(0,0,-0.904000, qreg_1[0])
subcirc1.rz(0.952000, qreg_1[2])
subcirc1.rz(-0.675000, qreg_1[0])
subcirc1.y(qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,0.264000, qreg_2[0])
subcirc2.h(qreg_0[1])
subcirc2.u(0,0,-0.395000, qreg_3[0])
subcirc2.u(0,0,-0.537000, qreg_2[0])
subcirc2.y(qreg_0[0])
subcirc2.h(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_0[2])
subcirc3.u(0,0,0.172000, qreg_0[0])
subcirc3.rz(-0.046000, qreg_0[2])
subcirc3.y(qreg_3[0])
subcirc3.u(0,0,-0.470000, qreg_0[1])
subcirc3.h(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
with else_2:
	main_circ.measure(qreg_0[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.rz(param_0, qreg_0[0])
		main_circ.append(subcirc1,[qreg_0[2],qreg_0[3],0,qreg_0[1]])
	with else_1:
		main_circ.append(subcirc1,[0,qreg_0[3],qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],0,qreg_0[1]])
	with else_1:
		main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.u(0,param_2,0.305000, qreg_0[2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.u(param_2,0,param_3, qreg_0[2])
		main_circ.barrier(qreg_0[2])
	with else_1:
		main_circ.h(qreg_0[0])
		main_circ.y(0)
		main_circ.u(0,0,param_0, qreg_0[3])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[qreg_0[0],0,qreg_0[3],qreg_0[1]])
		with case_1(1):
			main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
with else_2:
	main_circ.measure(qreg_0[3], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.y(qreg_0[3])
		main_circ.u(param_4,0,param_2, qreg_0[0])
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.id(qreg_0[1])
	main_circ.barrier(qreg_0[2])
bindings = {param_0: -0.713000, param_2: 0.573000, param_3: 0.164000, param_4: -0.586000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "520", "RemoveDiagonalGatesBeforeMeasure")
