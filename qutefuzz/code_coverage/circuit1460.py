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
subcirc0.u(0,0,-0.731000, qreg_1[2])
subcirc0.rz(0.842000, qreg_1[1])
subcirc0.ry(0.243000, qreg_1[1])
subcirc0.rz(0.088000, qreg_1[2])
subcirc0.u(0,0,-0.280000, qreg_1[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.144000, qreg_3[0])
subcirc1.u(0,0,0.737000, qreg_0[0])
subcirc1.ry(-0.386000, qreg_0[2])
subcirc1.rx(0.985000, qreg_0[2])
subcirc1.rz(0.439000, qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc1,[2,qreg_0[0],1,0])
	with case_2(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[1,0,qreg_0[0],2])
			with case_1(1):
				main_circ.append(subcirc1,[0,qreg_0[0],1,3])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.rz(0.631000, qreg_0[0])
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.ry(0.758000, qreg_0[0])
			main_circ.rz(param_2, 1)
			main_circ.ry(-0.119000, 1)
			main_circ.append(subcirc1,[0,1,2,qreg_0[0]])
		with case_1(1):
			main_circ.append(subcirc1,[qreg_0[0],1,0,3])
with else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[3,qreg_0[0],1,0])
		with case_1(1):
			main_circ.rz(-0.569000, 2)
			main_circ.rx(0.038000, 3)
			main_circ.append(subcirc1,[3,1,2,0])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(param_0, qreg_0[0])
		main_circ.ry(0.803000, 2)
		main_circ.ry(param_3, 2)
		main_circ.rz(param_1, 2)
		main_circ.rz(-0.740000, qreg_0[0])
with else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(1)
	with else_1:
		main_circ.ry(param_1, 0)
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(1)
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.rz(param_1, 2)
		main_circ.id(1)
	with else_1:
		main_circ.id(0)
bindings = {param_0: 0.296000, param_1: 0.211000, param_2: -0.583000, param_3: 0.558000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1460", "InverseCancellation")
