from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.u(0,0,-0.480000, qreg_2[0])
subcirc0.u(0,0,-0.802000, qreg_2[0])
subcirc0.rz(0.213000, qreg_2[0])
subcirc0.u(pi/2,0.197000,-0.122000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[0])
subcirc1.x(qreg_0[1])
subcirc1.u(0,0,0.215000, qreg_0[2])
subcirc1.u(0,0,0.882000, qreg_0[0])

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

main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(0,param_0,param_1, 1)
		main_circ.rz(-0.375000, 1)
		main_circ.u(param_1,0,-0.264000, 0)
		main_circ.u(0,0,-0.564000, 0)
with else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.x(0)
			main_circ.append(subcirc1,[0,2,1,3])
		with case_1(1):
			main_circ.rz(0.107000, 3)
			main_circ.rz(0.927000, 0)
			main_circ.u(0,param_0,param_1, 1)
			main_circ.u(0,0,param_1, 1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[0,3,1,2])
		with case_1(1):
			main_circ.rz(0.705000, 3)
			main_circ.id(0)
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_0,param_1,0.727000, 3)
			main_circ.u(pi/2,param_0,param_1, 1)
			main_circ.barrier(0)
		with case_1(1):
			main_circ.u(param_0,0.354000,param_1, 2)
			main_circ.u(param_1,param_1,0.892000, 0)
			main_circ.append(subcirc1,[2,0,3,1])
main_circ.rz(param_1, 2)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.u(0,param_1,param_1, 0)
				main_circ.append(subcirc1,[2,1,0,3])
			with case_1(1):
				main_circ.rz(0.837000, 2)
				main_circ.u(param_0,param_0,0.383000, 1)
				main_circ.rz(-0.915000, 1)
				main_circ.append(subcirc1,[3,2,1,0])
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(param_1,0,param_1, 1)
		with else_1:
			main_circ.x(0)
			main_circ.barrier(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_1,-0.896000,0.178000, 1)
				main_circ.u(param_1,0,param_0, 2)
				main_circ.x(1)
				main_circ.u(0,param_0,param_0, 0)
			with case_1(1):
				main_circ.u(0,0,-0.319000, 2)
				main_circ.rz(param_1, 2)
				main_circ.rz(param_0, 3)
				main_circ.u(0,param_1,0.727000, 3)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.x(3)
		main_circ.u(param_1,0.719000,0.219000, 0)
	main_circ.u(param_0,param_0,param_1, 0)
main_circ.append(subcirc1,[1,2,3,0])
bindings = {param_0: 0.904000, param_1: 0.178000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1738", "ConsolidateBlocks")
