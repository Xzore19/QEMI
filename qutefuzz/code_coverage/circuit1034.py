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
subcirc0.u(pi/2,-0.195000,0.989000, qreg_3[0])
subcirc0.u(pi/2,0.701000,-0.061000, qreg_0[0])
subcirc0.rx(-0.764000, qreg_3[0])
subcirc0.rx(0.491000, qreg_0[0])
subcirc0.z(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.666000,0.014000, qreg_3[0])
subcirc1.s(qreg_0[1])
subcirc1.s(qreg_0[0])
subcirc1.u(pi/2,0.544000,-0.467000, qreg_3[0])
subcirc1.s(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.rx(-0.905000, qreg_0[1])
subcirc2.s(qreg_0[1])
subcirc2.s(qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc2,[1,2,qreg_0[0],3])
			with case_1(1):
				main_circ.barrier(3)
with else_3:
	main_circ.u(param_0,-0.452000,param_0, qreg_0[0])
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.s(qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.id(qreg_0[0])
				with case_1(1):
					main_circ.append(subcirc2,[3,2,0,qreg_0[0]])
		with case_2(1):
			main_circ.append(subcirc2,[2,1,qreg_0[0],3])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rx(-0.940000, qreg_0[0])
				main_circ.barrier(0)
			with else_1:
				main_circ.z(qreg_0[0])
				main_circ.append(subcirc2,[2,1,qreg_0[0],3])
		with case_2(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc2,[0,3,2,1])
			with else_1:
				main_circ.s(qreg_0[0])
				main_circ.z(qreg_0[0])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.z(qreg_0[0])
			main_circ.append(subcirc0,[2,0,qreg_0[0],1,3])
		with else_1:
			main_circ.id(3)
	with else_2:
		main_circ.id(2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(3)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.s(qreg_0[0])
			main_circ.u(pi/2,-0.737000,0.122000, qreg_0[0])
			main_circ.rx(-0.512000, 0)
			main_circ.barrier(qreg_0[0])
	with else_2:
		main_circ.barrier(qreg_0[0])
	main_circ.id(0)
bindings = {param_0: -0.025000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1034")
