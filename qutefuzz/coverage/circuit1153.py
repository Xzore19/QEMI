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

main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.h(0)
		main_circ.x(1)
		main_circ.u(0.581000,param_2,param_0, 0)
		main_circ.u(0.345000,-0.474000,-0.018000, 1)
	with case_1(1):
		main_circ.rx(-0.650000, 3)
		main_circ.x(1)
		main_circ.h(2)
		main_circ.u(param_2,-0.265000,0.587000, 1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(1)
	main_circ.h(1)
	main_circ.h(1)
	main_circ.x(3)
	main_circ.x(3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(0)
with else_1:
	main_circ.h(2)
	main_circ.rx(0.922000, 2)
	main_circ.u(0.757000,0.508000,-0.476000, 2)
main_circ.rx(-0.023000, 3)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rx(param_1, 0)
		main_circ.u(param_0,param_2,0.164000, 0)
		main_circ.h(2)
		main_circ.h(2)
	with case_1(1):
		main_circ.rx(0.896000, 1)
		main_circ.rx(param_1, 2)
		main_circ.x(1)
		main_circ.u(0.887000,param_1,-0.295000, 3)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0.529000,param_1,0.283000, 2)
		main_circ.x(2)
		main_circ.u(param_2,0.081000,-0.062000, 2)
		main_circ.u(-0.710000,0.139000,-0.458000, 2)
	with case_1(1):
		main_circ.h(2)
		main_circ.h(1)
		main_circ.x(1)
		main_circ.x(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(-0.742000, 2)
	main_circ.rx(param_2, 0)
	main_circ.u(0.742000,param_2,param_1, 0)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.x(0)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(0)
		main_circ.u(param_0,0.417000,-0.390000, 0)
		main_circ.x(3)
		main_circ.h(1)
	with case_1(1):
		main_circ.h(1)
		main_circ.h(0)
		main_circ.barrier(1)
bindings = {param_0: 0.245000, param_1: -0.101000, param_2: 0.138000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1153")
