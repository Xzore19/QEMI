from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.ry(0.763000, qreg_0[1])
subcirc0.u(0,0,-0.021000, qreg_0[0])
subcirc0.u(0,0,0.470000, qreg_0[0])
subcirc0.h(qreg_0[1])
subcirc0.y(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.501000, qreg_0[2])
subcirc1.u(0,0,0.160000, qreg_0[3])
subcirc1.ry(-0.903000, qreg_0[0])
subcirc1.ry(-0.850000, qreg_0[0])
subcirc1.u(0,0,-0.043000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.h(qreg_0[0])
subcirc2.h(qreg_1[0])
subcirc2.h(qreg_1[0])
subcirc2.y(qreg_1[1])
subcirc2.ry(-0.613000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[1,0,qreg_1[0],2])
main_circ.y(1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[qreg_0[0],0,3,1])
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0,0,param_0, qreg_1[0])
		main_circ.append(subcirc0,[0,2,3,1])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_0[0],0,3,2])
main_circ.ry(param_2, 0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.y(qreg_1[0])
		main_circ.append(subcirc2,[qreg_0[0],3,qreg_1[0],2])
	with case_1(1):
		main_circ.ry(param_3, qreg_1[0])
		main_circ.append(subcirc1,[qreg_1[0],2,0,1])
main_circ.u(param_2,param_3,0.921000, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc2,[qreg_1[0],0,qreg_0[0],1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],0,1,qreg_1[0]])
	with case_1(1):
		main_circ.u(param_2,param_0,param_1, qreg_1[0])
		main_circ.append(subcirc0,[0,qreg_1[0],1,qreg_0[0]])
main_circ.u(0,0,-0.319000, 2)
main_circ.ry(param_1, 0)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.567000, qreg_1[0])
		main_circ.h(qreg_1[0])
		main_circ.id(qreg_1[0])
	with case_1(1):
		main_circ.id(3)
main_circ.y(1)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0,0,param_0, 2)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_1[0])
	with case_1(1):
		main_circ.id(2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.u(0,0,0.913000, 0)
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.h(qreg_1[0])
	main_circ.id(qreg_0[0])
bindings = {param_0: 0.434000, param_1: 0.715000, param_2: 0.466000, param_3: 0.041000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "884")
