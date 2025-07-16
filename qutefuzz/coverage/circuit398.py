from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(pi/2,-0.463000,-0.052000, qreg_3[0])
subcirc0.cz(qreg_2[0],qreg_0[0])
subcirc0.ry(-0.398000, qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.u(pi/2,-0.761000,-0.792000, qreg_2[0])
subcirc0.cz(qreg_3[0],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[3])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.h(qreg_0[2])
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.h(qreg_0[0])
subcirc2.h(qreg_1[1])
subcirc2.cz(qreg_1[0],qreg_0[0])
subcirc2.cz(qreg_1[1],qreg_1[0])
subcirc2.u(pi/2,0.426000,0.914000, qreg_1[1])
subcirc2.ry(0.383000, qreg_1[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.h(qreg_1[1])
subcirc3.ry(-0.147000, qreg_1[0])
subcirc3.h(qreg_1[0])
subcirc3.h(qreg_3[0])
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3.u(pi/2,0.871000,-0.876000, qreg_3[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_2,-0.535000,param_1, 0)
	main_circ.append(subcirc1,[1,0,3,qreg_0[0]])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc3,[0,1,3,qreg_0[0],2])
with else_1:
	main_circ.append(subcirc3,[2,qreg_0[0],qreg_0[1],1,3])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cz(1,qreg_0[1])
		main_circ.append(subcirc2,[3,qreg_0[0],1,2])
	with case_1(1):
		main_circ.u(param_1,param_2,param_2, qreg_0[1])
		main_circ.ry(param_1, 3)
		main_circ.h(2)
		main_circ.append(subcirc0,[2,0,qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(qreg_0[1],0)
with else_1:
	main_circ.cz(1,qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(1,qreg_0[1])
	main_circ.cz(1,qreg_0[1])
	main_circ.ry(param_1, qreg_0[0])
with else_1:
	main_circ.append(subcirc3,[qreg_0[1],1,qreg_0[0],0,3])
bindings = {param_1: 0.753000, param_2: 0.746000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "398")
