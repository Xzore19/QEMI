from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(param_1, qreg_1[1])
	main_circ.h(qreg_1[1])
with else_1:
	main_circ.u(pi/2,param_3,param_3, qreg_1[0])
	main_circ.h(qreg_3[0])
	main_circ.ry(param_3, qreg_0[0])
	main_circ.u(pi/2,0.962000,-0.008000, qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,0,param_0, qreg_0[0])
		main_circ.u(param_2,param_0,-0.471000, qreg_3[0])
		main_circ.h(0)
		main_circ.u(pi/2,param_3,param_1, qreg_0[0])
	with case_1(1):
		main_circ.u(param_1,param_3,param_1, qreg_3[0])
		main_circ.h(0)
		main_circ.ry(-0.967000, 0)
		main_circ.h(qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(qreg_1[1])
with else_1:
	main_circ.h(qreg_3[0])
	main_circ.u(0,0,param_3, qreg_0[0])
	main_circ.u(param_0,param_1,param_1, qreg_0[0])
	main_circ.u(pi/2,0.239000,param_1, qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(param_3, qreg_3[0])
	main_circ.ry(param_3, qreg_1[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0,param_3,0.084000, qreg_3[0])
	main_circ.u(0,param_2,0.699000, qreg_1[1])
	main_circ.u(param_3,param_0,-0.459000, 0)
	main_circ.h(qreg_1[1])
	main_circ.ry(param_0, 0)
with else_1:
	main_circ.u(param_1,-0.895000,param_2, qreg_0[0])
	main_circ.u(0,0,-0.848000, 0)
	main_circ.u(param_1,param_2,param_0, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(param_1, qreg_3[0])
	main_circ.u(param_1,0,-0.778000, qreg_1[1])
	main_circ.u(0,0,param_3, qreg_0[0])
	main_circ.u(0,0,param_1, qreg_1[0])
	main_circ.u(pi/2,-0.779000,0.192000, qreg_3[0])
with else_1:
	main_circ.h(qreg_1[1])
	main_circ.ry(-0.660000, qreg_3[0])
	main_circ.u(param_1,0,0.817000, qreg_1[1])
	main_circ.ry(-0.188000, 0)
	main_circ.u(param_1,0,param_0, 0)
main_circ.ry(param_0, qreg_1[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,param_0,-0.740000, qreg_1[1])
		main_circ.ry(param_2, qreg_1[1])
		main_circ.ry(-0.400000, qreg_1[1])
		main_circ.u(param_2,param_0,0.563000, qreg_0[0])
	with case_1(1):
		main_circ.h(qreg_1[1])
		main_circ.u(pi/2,param_3,0.768000, qreg_3[0])
		main_circ.u(0,param_0,-0.186000, 0)
		main_circ.ry(-0.996000, qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,0.573000,param_0, qreg_3[0])
	main_circ.u(param_2,param_3,param_2, qreg_0[0])
	main_circ.u(pi/2,param_2,param_3, qreg_3[0])
	main_circ.ry(param_1, qreg_3[0])
	main_circ.barrier(qreg_1[0])
with else_1:
	main_circ.barrier(qreg_3[0])
bindings = {param_0: -0.931000, param_1: 0.959000, param_2: 0.653000, param_3: 0.483000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1289")
