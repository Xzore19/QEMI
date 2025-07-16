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
subcirc0.u(-0.430000,0.063000,-0.398000, qreg_0[0])
subcirc0.y(qreg_2[1])
subcirc0.y(qreg_2[0])
subcirc0.y(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.rz(0.550000, qreg_0[2])
subcirc1.u(-0.319000,-0.085000,-0.492000, qreg_0[1])
subcirc1.u(-0.668000,-0.530000,-0.922000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.rz(-0.903000, qreg_2[1])
subcirc2.y(qreg_0[0])
subcirc2.rz(0.492000, qreg_0[1])
subcirc2.x(qreg_2[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.y(qreg_2[0])
subcirc3.rz(-0.829000, qreg_2[1])
subcirc3.u(0.782000,0.789000,-0.161000, qreg_0[1])
subcirc3.x(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(-0.830000,0.560000,-0.851000, qreg_0[0])
subcirc4.x(qreg_0[2])
subcirc4.u(-0.377000,-0.876000,0.643000, qreg_0[0])
subcirc4.x(qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc2,[qreg_0[1],0,qreg_2[0],qreg_0[0]])
with else_1:
	main_circ.id(qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc4,[qreg_2[1],qreg_2[0],qreg_0[0],0,qreg_0[1]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(-0.747000,-0.157000,param_1, 0)
	main_circ.rz(0.002000, qreg_2[1])
	main_circ.append(subcirc4,[qreg_2[0],qreg_0[0],0,qreg_0[1],qreg_2[1]])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.y(qreg_0[0])
	main_circ.append(subcirc2,[qreg_0[0],0,qreg_2[0],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.584000,-0.771000,param_0, qreg_0[1])
	main_circ.x(qreg_2[1])
	main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],0,qreg_2[1]])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[qreg_0[1],qreg_2[1],qreg_0[0],qreg_2[0]])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc2,[qreg_2[0],qreg_2[1],0,qreg_0[0]])
with else_1:
	main_circ.u(param_0,-0.929000,0.003000, qreg_2[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_2[1],0,qreg_0[1],qreg_0[0]])
	with case_1(1):
		main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_2[0],qreg_2[1]])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_2[1])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_2[1],qreg_0[0],qreg_0[1],0])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(qreg_0[0])
with else_1:
	main_circ.u(param_2,param_0,-0.372000, qreg_2[1])
	main_circ.u(0.972000,-0.819000,param_1, qreg_2[0])
main_circ.append(subcirc2,[qreg_0[0],0,qreg_0[1],qreg_2[1]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.rz(param_2, qreg_2[0])
		main_circ.x(0)
		main_circ.append(subcirc4,[0,qreg_0[1],qreg_0[0],qreg_2[0],qreg_2[1]])
	with case_1(1):
		main_circ.id(qreg_0[0])
bindings = {param_0: 0.544000, param_1: -0.647000, param_2: -0.238000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1745")
