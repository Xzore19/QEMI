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
subcirc0.u(-0.114000,-0.860000,0.502000, qreg_0[0])
subcirc0.ry(-0.833000, qreg_0[1])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_0[1])
subcirc1.u(-0.120000,0.070000,-0.890000, qreg_0[1])
subcirc1.y(qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

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

main_circ.ry(0.806000, 0)
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_2,param_2,param_2, qreg_3[0])
	main_circ.id(qreg_0[1])
main_circ.u(-0.287000,0.231000,param_1, qreg_3[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_0[0])
		main_circ.id(qreg_0[1])
	with case_1(1):
		main_circ.y(qreg_0[1])
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0.759000,-0.402000,param_0, qreg_0[0])
		main_circ.ry(-0.406000, qreg_0[0])
		main_circ.ry(param_1, qreg_0[2])
		main_circ.u(param_1,param_2,param_0, 0)
	with case_1(1):
		main_circ.u(0.602000,0.853000,0.533000, qreg_0[2])
		main_circ.ry(param_2, qreg_0[1])
		main_circ.ry(0.185000, qreg_0[2])
		main_circ.barrier(0)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_0[0])
		main_circ.id(qreg_3[0])
	with case_1(1):
		main_circ.ry(0.241000, qreg_0[1])
		main_circ.z(qreg_0[0])
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_3[0])
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0.284000,param_1,-0.123000, qreg_0[2])
		main_circ.y(qreg_0[1])
		main_circ.u(param_2,-0.558000,0.830000, qreg_0[2])
		main_circ.z(0)
	with case_1(1):
		main_circ.u(-0.716000,0.901000,-0.896000, qreg_0[0])
		main_circ.ry(-0.202000, 0)
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_3[0])
	with case_1(1):
		main_circ.u(-0.083000,-0.135000,param_2, qreg_0[0])
		main_circ.barrier(0)
main_circ.z(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(0)
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.y(0)
	main_circ.ry(param_2, qreg_0[0])
	main_circ.u(0.969000,-0.369000,0.755000, qreg_0[0])
	main_circ.ry(0.542000, qreg_0[2])
	main_circ.ry(-0.146000, qreg_0[0])
with else_1:
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_3[0])
		main_circ.y(qreg_0[2])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.z(qreg_0[1])
		main_circ.u(param_1,param_1,0.121000, qreg_0[2])
		main_circ.ry(-0.116000, qreg_0[2])
		main_circ.z(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.312000, qreg_0[2])
with else_1:
	main_circ.barrier(0)
main_circ.z(0)
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,-0.452000,param_2, qreg_0[1])
		main_circ.barrier(0)
	with case_1(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(0.433000, qreg_0[0])
	main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(qreg_3[0])
with else_1:
	main_circ.z(qreg_0[2])
	main_circ.u(param_0,param_0,param_0, qreg_0[0])
	main_circ.y(qreg_0[2])
	main_circ.barrier(qreg_0[2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(qreg_0[2])
	main_circ.id(0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.u(0.313000,param_0,param_2, qreg_0[0])
		main_circ.z(0)
		main_circ.y(0)
		main_circ.id(0)
bindings = {param_0: 0.204000, param_1: 0.662000, param_2: 0.326000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "753", "CommutativeInverseCancellation")
