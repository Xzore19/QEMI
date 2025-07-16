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
subcirc0.ry(0.526000, qreg_0[1])
subcirc0.ry(-0.971000, qreg_3[0])
subcirc0.x(qreg_0[2])
subcirc0.u(0.133000,-0.433000,-0.606000, qreg_0[0])
subcirc0.u(0.102000,0.667000,0.593000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.x(qreg_2[0])
subcirc1.s(qreg_0[1])
subcirc1.x(qreg_2[0])
subcirc1.x(qreg_2[0])
subcirc1.ry(0.159000, qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.s(qreg_3[0])
subcirc2.s(qreg_0[2])
subcirc2.x(qreg_0[1])
subcirc2.s(qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc3.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(0.102000, qreg_1[0])
subcirc3.u(0.317000,-0.599000,-0.810000, qreg_3[0])
subcirc3.u(-0.948000,-0.493000,0.177000, qreg_0[0])
subcirc3.s(qreg_3[0])
subcirc3.ry(-0.174000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.x(3)
				main_circ.append(subcirc1,[2,1,0,3])
			with case_1(1):
				main_circ.s(3)
				main_circ.append(subcirc1,[qreg_0[0],0,3,2])
	with case_2(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc3,[qreg_0[0],2,0,1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.x(0)
		main_circ.append(subcirc1,[3,1,0,2])
	with else_1:
		main_circ.barrier(qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.append(subcirc3,[0,3,qreg_0[0],1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(param_0,param_0,0.304000, 3)
		main_circ.append(subcirc3,[1,3,0,2])
	with else_1:
		main_circ.s(2)
		main_circ.ry(param_0, 0)
		main_circ.u(param_0,-0.297000,-0.668000, 1)
		main_circ.x(3)
		main_circ.ry(param_0, 2)
with else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(-0.491000,param_0,-0.432000, qreg_0[0])
			main_circ.append(subcirc3,[2,qreg_0[0],0,3])
		with case_1(1):
			main_circ.append(subcirc1,[0,2,3,qreg_0[0]])
bindings = {param_0: 0.282000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1670", "Optimize1qGates")
