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
subcirc0.u(-0.405000,-0.332000,-0.326000, qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.u(0.603000,0.049000,-0.370000, qreg_2[0])
subcirc0.cz(qreg_2[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_3[0])
subcirc1.u(0,0,0.095000, qreg_2[0])
subcirc1.cy(qreg_0[1],qreg_0[0])
subcirc1.u(0,0,-0.439000, qreg_0[0])

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

main_circ.cz(3,0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.cy(1,2)
main_circ.u(0,param_1,param_0, 3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(-0.227000,param_0,0.594000, 3)
			main_circ.u(-0.962000,param_3,-0.377000, 1)
			main_circ.cy(0,3)
			main_circ.cz(1,0)
		with case_1(1):
			main_circ.id(0)
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc1,[0,2,3,1])
with else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_2,0.182000,-0.645000, 2)
		main_circ.cz(2,3)
		main_circ.u(param_2,0,param_1, 2)
		main_circ.cz(2,0)
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(param_1,0,param_1, 1)
			main_circ.barrier(1)
		with case_1(1):
			main_circ.u(0,param_3,param_1, 1)
			main_circ.barrier(3)
main_circ.cz(1,3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(1)
		with case_1(1):
			main_circ.cy(3,1)
			main_circ.u(param_2,0,-0.357000, 0)
			main_circ.cy(3,2)
			main_circ.u(param_0,0,param_2, 2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(0)
		with case_1(1):
			main_circ.append(subcirc1,[3,0,1,2])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.u(param_2,param_2,-0.003000, 3)
			main_circ.u(0,0,param_3, 0)
			main_circ.append(subcirc1,[2,0,1,3])
		with case_1(1):
			main_circ.u(param_2,0,-0.942000, 3)
			main_circ.cy(1,0)
			main_circ.u(param_0,0.636000,-0.790000, 1)
			main_circ.cy(2,0)
with else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(0,param_3,param_1, 2)
			main_circ.cz(1,2)
			main_circ.cz(0,2)
			main_circ.append(subcirc1,[3,0,1,2])
		with case_1(1):
			main_circ.u(0,0,param_1, 3)
			main_circ.u(0.168000,param_0,param_1, 1)
			main_circ.u(param_3,0,-0.918000, 3)
			main_circ.u(-0.683000,param_3,0.574000, 3)
bindings = {param_0: 0.478000, param_1: -0.624000, param_2: -0.941000, param_3: -0.863000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "488", "Collect1qRuns")
