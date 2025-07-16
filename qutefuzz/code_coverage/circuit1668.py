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
subcirc0.u(0,0,-0.219000, qreg_1[1])
subcirc0.h(qreg_1[1])
subcirc0.u(0,0,0.289000, qreg_1[0])
subcirc0.s(qreg_1[0])
subcirc0.u(0,0,0.082000, qreg_1[2])
subcirc0.u(-0.907000,0.673000,0.856000, qreg_1[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.h(qreg_0[0])
subcirc1.u(0,0,0.533000, qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1.u(0,0,-0.337000, qreg_3[0])
subcirc1.h(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_0,0,param_0, 2)
	main_circ.u(0.566000,-0.871000,-0.855000, qreg_0[0])
with else_1:
	main_circ.barrier(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_0[0])
	main_circ.id(3)
with else_1:
	main_circ.id(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_0,param_0,param_1, 2)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(-0.904000,param_1,0.222000, 1)
	main_circ.s(2)
	main_circ.s(1)
with else_1:
	main_circ.h(3)
	main_circ.h(2)
	main_circ.u(0,0,-0.404000, 1)
	main_circ.u(param_1,0,0.594000, 2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(1)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(1)
with else_1:
	main_circ.u(-0.227000,0.132000,-0.800000, 0)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.h(1)
		main_circ.s(1)
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.h(0)
		main_circ.id(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(2)
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.s(1)
	main_circ.u(0,0,-0.348000, 3)
	main_circ.s(qreg_0[0])
	main_circ.h(qreg_0[0])
	main_circ.u(param_1,0,0.591000, 3)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(0,param_0,-0.999000, 3)
	main_circ.u(param_0,0.527000,param_1, 0)
	main_circ.barrier(1)
with else_1:
	main_circ.s(3)
	main_circ.id(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(0,param_1,param_1, qreg_0[0])
	main_circ.barrier(1)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.u(-0.001000,param_0,param_1, 0)
		main_circ.s(2)
		main_circ.h(3)
		main_circ.barrier(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.586000,param_0,param_0, 2)
	main_circ.u(param_1,0.584000,param_1, 1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(0,param_1,param_0, 2)
	main_circ.s(2)
	main_circ.h(2)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_1,param_0,-0.540000, 2)
	main_circ.id(qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_0[0])
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.h(qreg_0[0])
	main_circ.s(0)
	main_circ.id(0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.h(qreg_0[0])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.h(2)
		main_circ.h(qreg_0[0])
		main_circ.u(0,0,param_1, 0)
		main_circ.id(1)
main_circ.s(qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(0)
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.id(qreg_0[0])
main_circ.h(3)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(3)
	with case_1(1):
		main_circ.id(2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.h(qreg_0[0])
	main_circ.h(1)
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.barrier(2)
bindings = {param_0: 0.713000, param_1: -0.991000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1668")
