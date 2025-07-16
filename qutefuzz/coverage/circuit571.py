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
subcirc0.h(qreg_1[0])
subcirc0.u(0.619000,-0.308000,0.351000, qreg_1[0])
subcirc0.u(-0.116000,-0.050000,-0.693000, qreg_0[0])
subcirc0.u(-0.294000,-0.736000,-0.491000, qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(3,0)
				main_circ.append(subcirc0,[3,0,2,1])
			with case_1(1):
				main_circ.cy(0,1)
				main_circ.ry(param_0, 2)
				main_circ.ry(param_0, 2)
				main_circ.append(subcirc0,[2,1,0,3])
	with case_2(1):
		main_circ.ry(0.636000, 1)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc0,[0,2,1,3])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc0,[1,0,3,2])
	with case_2(1):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.h(3)
			main_circ.cy(2,1)
			main_circ.cy(2,0)
			main_circ.ry(param_0, 1)
		with else_1:
			main_circ.ry(0.832000, 0)
			main_circ.h(0)
			main_circ.cy(3,1)
			main_circ.cy(1,0)
			main_circ.h(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(2, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.h(3)
			main_circ.ry(param_0, 3)
			main_circ.ry(-0.191000, 0)
			main_circ.append(subcirc0,[0,3,1,2])
		with case_1(1):
			main_circ.cy(1,3)
			main_circ.cy(2,1)
			main_circ.cy(3,0)
			main_circ.cy(3,1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(2,3)
				main_circ.cy(2,3)
				main_circ.cy(0,1)
				main_circ.cy(0,1)
			with case_1(1):
				main_circ.cy(3,2)
				main_circ.h(3)
				main_circ.u(param_0,param_0,0.413000, 1)
				main_circ.barrier(1)
	with case_2(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.id(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(1)
		main_circ.barrier(3)
bindings = {param_0: -0.912000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "571", "TemplateOptimization")
