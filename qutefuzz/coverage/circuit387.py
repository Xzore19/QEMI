from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.u(pi/2,0.287000,0.583000, qreg_0[0])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.rx(-0.491000, qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(0.419000, qreg_0[0])
		main_circ.u(param_3,0.140000,param_5, qreg_0[2])
		main_circ.h(qreg_0[2])
		main_circ.h(qreg_0[2])
	with case_1(1):
		main_circ.rx(-0.355000, qreg_0[1])
		main_circ.x(qreg_0[2])
		main_circ.u(pi/2,param_1,param_5, qreg_0[2])
		main_circ.x(qreg_0[2])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.x(qreg_3[0])
	main_circ.rx(-0.585000, qreg_0[0])
	main_circ.rx(param_2, qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[1])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(qreg_0[1])
	main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_3[0])
	main_circ.u(param_0,param_5,param_2, qreg_0[0])
	main_circ.h(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,param_5,param_2, 0)
	main_circ.x(qreg_0[1])
	main_circ.h(qreg_3[0])
with else_1:
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.rx(0.211000, qreg_3[0])
	main_circ.x(qreg_0[0])
	main_circ.rx(param_0, qreg_0[0])
with else_1:
	main_circ.rx(param_0, qreg_0[0])
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[2])
	with case_1(1):
		main_circ.h(0)
		main_circ.rx(param_0, qreg_0[2])
		main_circ.h(qreg_0[0])
		main_circ.rx(param_1, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(qreg_3[0])
	main_circ.h(qreg_0[0])
	main_circ.rx(0.890000, qreg_3[0])
with else_1:
	main_circ.x(qreg_0[2])
	main_circ.x(qreg_0[2])
	main_circ.rx(0.836000, qreg_0[1])
	main_circ.u(param_4,0.210000,0.425000, qreg_0[2])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.x(qreg_0[1])
	main_circ.rx(-0.898000, qreg_0[0])
with else_1:
	main_circ.u(pi/2,param_3,-0.180000, 0)
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[2])
	with case_1(1):
		main_circ.u(param_0,-0.963000,param_1, qreg_0[0])
		main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.h(0)
	main_circ.h(qreg_0[2])
with else_1:
	main_circ.barrier(qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_0[0])
	main_circ.x(qreg_0[1])
	main_circ.h(qreg_0[2])
	main_circ.h(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(qreg_3[0])
	main_circ.u(pi/2,param_4,param_2, qreg_0[0])
	main_circ.h(qreg_0[1])
	main_circ.rx(param_1, qreg_0[1])
with else_1:
	main_circ.x(qreg_0[2])
	main_circ.rx(-0.806000, qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.h(qreg_3[0])
	main_circ.x(qreg_0[0])
	main_circ.h(qreg_0[0])
main_circ.x(qreg_0[2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rx(0.652000, qreg_0[1])
	main_circ.id(0)
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.u(param_1,param_4,0.366000, 0)
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.x(0)
	main_circ.id(0)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.h(qreg_3[0])
		main_circ.h(qreg_0[0])
		main_circ.id(0)
	with case_1(1):
		main_circ.barrier(qreg_3[0])
bindings = {param_0: 0.383000, param_1: 0.279000, param_2: -0.315000, param_3: -0.675000, param_4: 0.380000, param_5: 0.864000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "387", "Collect1qRuns")
