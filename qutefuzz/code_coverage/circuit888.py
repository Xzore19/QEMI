from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.x(qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.s(qreg_3[0])
subcirc0.s(qreg_3[0])
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
subcirc1.u(-0.708000,0.789000,0.838000, qreg_3[0])
subcirc1.s(qreg_0[0])
subcirc1.u(-0.196000,0.505000,-0.278000, qreg_3[0])
subcirc1.x(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.x(qreg_1[0])
subcirc2.u(0.496000,0.002000,0.772000, qreg_1[1])
subcirc2.u(0.589000,0.815000,-0.799000, qreg_1[0])
subcirc2.x(qreg_1[0])
subcirc2 = subcirc2.to_gate().control(3)

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

main_circ.x(2)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_1,0.826000,param_0, 2)
	main_circ.x(1)
with else_1:
	main_circ.id(1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(0)
main_circ.rx(param_2, 3)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rx(param_0, 2)
main_circ.s(3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.s(1)
	main_circ.id(1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rx(param_2, 1)
	main_circ.rx(param_2, 1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.x(3)
	main_circ.s(0)
	main_circ.s(3)
	main_circ.rx(param_0, 2)
	main_circ.id(1)
with else_1:
	main_circ.rx(-0.254000, 2)
	main_circ.x(1)
	main_circ.id(2)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(3)
	with case_1(1):
		main_circ.id(1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.x(3)
	main_circ.x(0)
with else_1:
	main_circ.barrier(2)
main_circ.u(param_2,param_0,param_2, 0)
main_circ.rx(0.671000, 1)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.x(1)
	main_circ.u(0.689000,-0.147000,param_0, 1)
	main_circ.s(2)
	main_circ.x(2)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(3)
	with case_1(1):
		main_circ.u(param_0,0.680000,0.135000, 3)
		main_circ.barrier(2)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(2)
	with case_1(1):
		main_circ.id(1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(2)
	main_circ.u(0.699000,-0.332000,param_0, 0)
	main_circ.s(3)
with else_1:
	main_circ.barrier(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,-0.369000,param_2, 3)
	main_circ.rx(0.890000, 3)
with else_1:
	main_circ.barrier(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.s(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(1)
	main_circ.id(2)
with else_1:
	main_circ.s(3)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0.558000,param_0,param_0, 2)
		main_circ.barrier(0)
	with case_1(1):
		main_circ.id(3)
main_circ.x(0)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(0.187000, 0)
	main_circ.barrier(1)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.x(3)
	main_circ.rx(param_1, 2)
	main_circ.barrier(3)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(-0.157000,param_2,0.559000, 3)
	main_circ.id(1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(2)
with else_1:
	main_circ.id(3)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rx(-0.200000, 3)
		main_circ.s(3)
		main_circ.barrier(2)
	with case_1(1):
		main_circ.barrier(3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(3)
	with case_1(1):
		main_circ.s(1)
		main_circ.u(0.533000,0.127000,-0.629000, 3)
		main_circ.u(param_1,0.667000,0.190000, 1)
		main_circ.x(3)
main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(2)
	with case_1(1):
		main_circ.id(0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(2)
		main_circ.id(2)
	with case_1(1):
		main_circ.rx(0.252000, 2)
		main_circ.x(1)
		main_circ.id(2)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(2)
	with case_1(1):
		main_circ.u(-0.790000,0.398000,-0.843000, 2)
		main_circ.barrier(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(param_2, 1)
	main_circ.s(1)
	main_circ.id(0)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(-0.317000,-0.335000,param_2, 3)
		main_circ.s(1)
		main_circ.rx(param_1, 0)
		main_circ.s(2)
	with case_1(1):
		main_circ.x(2)
		main_circ.id(1)
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.x(1)
		main_circ.barrier(0)
	with case_1(1):
		main_circ.barrier(1)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(0)
		main_circ.x(3)
		main_circ.barrier(0)
	with case_1(1):
		main_circ.barrier(2)
bindings = {param_0: 0.315000, param_1: 0.426000, param_2: 0.075000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "888")
