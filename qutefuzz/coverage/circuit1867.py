from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

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

main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,param_0,param_1, 1)
		main_circ.u(param_2,param_0,param_1, 1)
		main_circ.u(param_1,-0.046000,param_2, 2)
		main_circ.u(pi/2,0.019000,param_0, 2)
	with case_1(1):
		main_circ.cz(1,2)
		main_circ.cz(3,2)
		main_circ.z(3)
		main_circ.cz(3,2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(3,1)
	main_circ.h(2)
	main_circ.cz(2,0)
	main_circ.cz(2,3)
	main_circ.cz(0,1)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,-0.748000,param_0, 1)
		main_circ.z(0)
		main_circ.h(0)
		main_circ.h(0)
	with case_1(1):
		main_circ.z(2)
		main_circ.z(0)
		main_circ.z(0)
		main_circ.cz(3,2)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.h(3)
		main_circ.z(0)
		main_circ.h(3)
		main_circ.u(pi/2,param_1,-0.144000, 3)
	with case_1(1):
		main_circ.cz(1,2)
		main_circ.z(1)
		main_circ.h(3)
		main_circ.z(2)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.z(2)
		main_circ.cz(0,2)
		main_circ.h(2)
		main_circ.cz(2,0)
	with case_1(1):
		main_circ.h(2)
		main_circ.z(3)
		main_circ.h(0)
		main_circ.z(0)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,param_2,0.735000, 2)
		main_circ.h(3)
		main_circ.h(0)
		main_circ.z(2)
	with case_1(1):
		main_circ.cz(2,0)
		main_circ.cz(2,3)
		main_circ.cz(0,1)
		main_circ.cz(0,3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(0,1)
	main_circ.cz(2,0)
	main_circ.cz(3,1)
	main_circ.u(param_1,0.950000,-0.088000, 1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(0)
	main_circ.h(3)
	main_circ.h(1)
	main_circ.z(3)
	main_circ.u(param_2,-0.533000,-0.766000, 0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_2,-0.990000,param_2, 0)
	main_circ.u(param_2,0.250000,param_0, 0)
	main_circ.z(0)
	main_circ.u(param_1,param_0,0.878000, 2)
	main_circ.barrier(2)
bindings = {param_0: 0.525000, param_1: -0.634000, param_2: -0.522000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1867")
