from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0.936000,-0.273000,0.219000, 1)
with else_1:
	main_circ.u(param_2,-0.186000,param_2, 3)
	main_circ.u(0.643000,param_2,param_0, 1)
	main_circ.x(1)
	main_circ.z(2)
main_circ.x(2)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.x(0)
		main_circ.u(0,0,param_1, 2)
		main_circ.z(1)
		main_circ.z(3)
	with case_1(1):
		main_circ.u(param_1,param_1,param_3, 2)
		main_circ.u(-0.769000,param_1,0.971000, 0)
		main_circ.u(-0.978000,0.232000,param_4, 1)
		main_circ.u(param_0,param_2,0.322000, 1)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(2)
	main_circ.u(0,param_2,param_0, 1)
	main_circ.u(param_1,param_1,0.160000, 0)
	main_circ.z(2)
	main_circ.u(0.844000,param_4,param_4, 0)
with else_1:
	main_circ.z(3)
	main_circ.u(param_4,param_1,param_2, 2)
	main_circ.u(param_2,-0.933000,0.730000, 2)
	main_circ.u(0,0,0.076000, 1)
	main_circ.u(0.863000,param_0,param_2, 2)
main_circ.z(2)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0,0,0.884000, 0)
	main_circ.x(1)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(1)
		main_circ.x(1)
		main_circ.u(0,0,0.603000, 0)
		main_circ.z(0)
	with case_1(1):
		main_circ.u(param_5,0,-0.425000, 3)
		main_circ.u(param_4,param_5,param_5, 3)
		main_circ.u(param_0,0,param_2, 1)
		main_circ.u(0,0,param_1, 1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_4,-0.245000,-0.304000, 0)
	main_circ.x(3)
	main_circ.x(2)
	main_circ.u(param_4,0.095000,param_1, 0)
	main_circ.u(param_2,param_2,param_4, 3)
with else_1:
	main_circ.u(0,0,param_4, 3)
	main_circ.z(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(-0.093000,-0.649000,0.348000, 1)
	main_circ.u(0.451000,-0.049000,param_3, 3)
	main_circ.u(0.484000,0.307000,0.596000, 2)
with else_1:
	main_circ.u(0,0,param_1, 2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0,0,param_1, 0)
	main_circ.z(2)
with else_1:
	main_circ.u(param_0,param_4,0.536000, 0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(1)
with else_1:
	main_circ.x(0)
	main_circ.u(param_5,param_0,0.027000, 2)
main_circ.x(1)
main_circ.z(0)
main_circ.x(1)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_3,-0.725000,param_2, 3)
	main_circ.z(2)
	main_circ.id(2)
bindings = {param_0: -0.235000, param_1: 0.507000, param_2: -0.927000, param_3: 0.038000, param_4: 0.092000, param_5: -0.772000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "481", "ElidePermutations")
