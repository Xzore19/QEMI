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
subcirc0.u(-0.635000,-0.107000,0.576000, qreg_0[2])
subcirc0.u(pi/2,-0.191000,-0.952000, qreg_0[0])
subcirc0.x(qreg_3[0])
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_3[0])
subcirc1.x(qreg_0[0])
subcirc1.u(-0.027000,0.556000,-0.092000, qreg_0[1])
subcirc1.u(-0.015000,-0.417000,0.351000, qreg_3[0])
subcirc1.x(qreg_0[1])
subcirc1.u(pi/2,-0.156000,-0.337000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.354000,-0.530000, qreg_0[0])
subcirc2.u(pi/2,0.686000,0.102000, qreg_0[1])
subcirc2.u(pi/2,-0.086000,0.785000, qreg_0[1])
subcirc2.ry(-0.233000, qreg_3[0])
subcirc2.u(pi/2,-0.900000,0.702000, qreg_0[2])
subcirc2.u(pi/2,-0.663000,-0.064000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
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
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_2, 2)
		main_circ.u(pi/2,param_4,0.136000, 1)
		main_circ.ry(0.065000, 1)
		main_circ.u(param_6,0.942000,param_7, 2)
	with case_1(1):
		main_circ.barrier(3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(3)
	main_circ.id(3)
with else_1:
	main_circ.ry(-0.159000, 0)
	main_circ.id(1)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_7,-0.294000,param_1, 0)
		main_circ.barrier(0)
	with case_1(1):
		main_circ.id(2)
main_circ.u(param_1,param_1,param_3, 3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.369000,param_4,param_5, 3)
	main_circ.barrier(2)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0.586000,param_6,0.913000, 2)
		main_circ.u(param_6,-0.719000,0.169000, 1)
		main_circ.ry(-0.015000, 2)
		main_circ.ry(param_0, 0)
	with case_1(1):
		main_circ.u(-0.518000,-0.104000,param_5, 1)
		main_circ.barrier(1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(2)
with else_1:
	main_circ.barrier(3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_2,0.020000,-0.759000, 2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(-0.032000,-0.998000,-0.198000, 2)
	main_circ.x(1)
	main_circ.barrier(2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(1)
main_circ.ry(-0.239000, 1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(1)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.x(3)
		main_circ.u(param_2,-0.897000,param_4, 3)
		main_circ.id(0)
	with case_1(1):
		main_circ.id(0)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.x(1)
		main_circ.ry(0.244000, 3)
		main_circ.x(3)
		main_circ.u(pi/2,0.069000,param_0, 1)
	with case_1(1):
		main_circ.ry(0.604000, 2)
		main_circ.u(param_3,-0.982000,0.531000, 0)
		main_circ.id(3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_1,param_3,param_4, 1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(0.804000,-0.841000,param_3, 1)
	main_circ.x(2)
	main_circ.barrier(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(0.881000, 0)
	main_circ.x(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,-0.189000,param_2, 1)
	main_circ.barrier(1)
with else_1:
	main_circ.id(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.366000,-0.164000,-0.256000, 3)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(2)
		main_circ.u(param_7,param_3,-0.677000, 1)
		main_circ.u(-0.447000,param_1,param_0, 0)
		main_circ.barrier(2)
	with case_1(1):
		main_circ.ry(-0.495000, 2)
		main_circ.barrier(3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,-0.890000,0.452000, 3)
	main_circ.x(0)
	main_circ.u(param_6,-0.382000,0.463000, 1)
	main_circ.barrier(2)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_5, 3)
		main_circ.u(param_6,param_2,param_4, 1)
		main_circ.u(0.175000,-0.300000,-0.815000, 1)
		main_circ.barrier(3)
	with case_1(1):
		main_circ.u(param_4,0.894000,0.026000, 2)
		main_circ.id(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(-0.319000,param_1,param_1, 2)
	main_circ.id(1)
with else_1:
	main_circ.u(pi/2,param_4,param_3, 2)
	main_circ.u(-0.163000,param_0,param_2, 1)
	main_circ.ry(0.082000, 2)
	main_circ.id(1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(2)
	with case_1(1):
		main_circ.barrier(2)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,-0.152000,param_6, 3)
		main_circ.ry(param_2, 1)
		main_circ.x(1)
		main_circ.barrier(0)
	with case_1(1):
		main_circ.id(1)
bindings = {param_0: 0.157000, param_1: -0.862000, param_2: 0.528000, param_3: -0.641000, param_4: 0.644000, param_5: -0.750000, param_6: 0.767000, param_7: 0.003000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "904")
