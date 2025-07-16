from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(0,param_2,0.637000, qreg_1[0])
		main_circ.u(param_2,0.308000,param_1, 1)
		main_circ.u(0,param_0,-0.971000, 0)
	with else_1:
		main_circ.u(param_0,-0.659000,param_0, qreg_1[0])
		main_circ.u(param_2,0,param_0, 0)
		main_circ.u(param_1,0,param_0, qreg_1[0])
		main_circ.y(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(2)
			main_circ.u(-0.961000,0.480000,0.248000, 1)
			main_circ.u(param_0,0,param_0, 3)
			main_circ.u(pi/2,param_1,param_1, 0)
		with case_1(1):
			main_circ.u(0.039000,param_2,0.344000, 3)
			main_circ.u(param_1,param_0,-0.325000, qreg_0[0])
			main_circ.u(param_1,param_1,param_1, 0)
			main_circ.u(0,0,param_2, qreg_1[0])
with else_2:
	main_circ.u(param_1,param_1,-0.974000, 0)
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.y(3)
			main_circ.u(pi/2,0.812000,0.694000, qreg_0[0])
			main_circ.u(param_2,0.331000,0.726000, 2)
			main_circ.u(pi/2,0.707000,-0.253000, 1)
		with case_1(1):
			main_circ.u(0,0,param_0, 1)
			main_circ.y(1)
			main_circ.u(param_0,0,0.365000, 2)
			main_circ.u(param_1,0,param_1, 0)
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.u(pi/2,param_0,param_1, qreg_1[0])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0,param_2,param_0, qreg_0[0])
			main_circ.u(pi/2,0.056000,param_2, 1)
			main_circ.y(qreg_1[0])
		with else_1:
			main_circ.u(pi/2,param_0,param_0, qreg_0[0])
			main_circ.u(param_0,0,-0.427000, 0)
			main_circ.u(0.422000,param_1,param_2, 0)
			main_circ.u(param_0,param_2,0.222000, 1)
	with case_2(1):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(0.817000,0.219000,param_0, 0)
			main_circ.y(0)
			main_circ.u(param_2,0.113000,param_1, 2)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(-0.132000,-0.274000,-0.732000, qreg_0[0])
			main_circ.y(qreg_0[0])
			main_circ.u(-0.044000,param_2,param_1, 3)
			main_circ.y(2)
			main_circ.u(-0.013000,param_2,0.252000, 1)
		with else_1:
			main_circ.u(0,0,-0.172000, 3)
			main_circ.u(param_2,0.984000,param_0, qreg_0[0])
main_circ.y(1)
main_circ.u(pi/2,param_0,-0.545000, qreg_1[0])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(pi/2,param_2,-0.951000, qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(0.499000,param_2,0.409000, 1)
		main_circ.u(pi/2,-0.967000,-0.869000, qreg_0[0])
		main_circ.u(param_1,0,0.760000, 0)
	with else_1:
		main_circ.id(1)
bindings = {param_0: -0.519000, param_1: 0.622000, param_2: -0.885000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "391", "CollectCliffords")
