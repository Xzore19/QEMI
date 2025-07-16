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
subcirc0.ry(0.907000, qreg_3[0])
subcirc0.ry(0.331000, qreg_3[0])
subcirc0.ry(-0.472000, qreg_0[1])
subcirc0.ry(0.998000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.996000, qreg_0[1])
subcirc1.ry(-0.789000, qreg_2[0])
subcirc1.x(qreg_3[0])
subcirc1.x(qreg_2[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.751000, qreg_1[1])
subcirc2.x(qreg_0[0])
subcirc2.u(0,0,0.224000, qreg_3[0])
subcirc2.u(pi/2,-0.410000,-0.752000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.ry(0.084000, qreg_0[2])
subcirc3.ry(-0.410000, qreg_0[0])
subcirc3.ry(-0.396000, qreg_0[0])
subcirc3.u(0,0,0.091000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.x(1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[0,1,2,3])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(pi/2,param_0,param_0, 3)
	main_circ.x(1)
	main_circ.x(3)
	main_circ.x(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(1)
	main_circ.x(0)
	main_circ.x(2)
	main_circ.id(0)
with else_1:
	main_circ.append(subcirc3,[0,1,2,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_3,param_1,param_4, 1)
	main_circ.append(subcirc3,[1,0,2,3])
with else_1:
	main_circ.append(subcirc0,[1,3,0,2])
	main_circ.append(subcirc0,[3,1,0,2])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(param_2,param_1,param_0, 2)
	main_circ.append(subcirc0,[0,1,2,3])
with else_1:
	main_circ.ry(param_1, 1)
	main_circ.u(pi/2,param_4,-0.800000, 3)
	main_circ.x(1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,-0.050000,0.210000, 3)
		main_circ.ry(param_2, 1)
		main_circ.append(subcirc0,[1,2,0,3])
	with case_1(1):
		main_circ.append(subcirc3,[0,1,2,3])
main_circ.append(subcirc0,[3,1,0,2])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(3)
	main_circ.u(param_2,param_4,0.021000, 3)
	main_circ.append(subcirc0,[1,0,3,2])
bindings = {param_0: -0.653000, param_1: 0.111000, param_2: -0.333000, param_3: 0.110000, param_4: -0.701000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "121")
