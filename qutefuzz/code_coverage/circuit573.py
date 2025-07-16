from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rz(-0.795000, qreg_0[0])
subcirc0.s(qreg_0[0])
subcirc0.rz(0.535000, qreg_0[0])
subcirc0.s(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.s(qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.z(qreg_0[1])
	main_circ.s(qreg_0[1])
with else_1:
	main_circ.z(qreg_0[1])
	main_circ.s(qreg_0[3])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(0.675000, qreg_0[3])
	main_circ.u(0.333000,0.400000,param_0, qreg_0[3])
	main_circ.z(qreg_0[1])
with else_1:
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(0.384000, qreg_0[3])
	main_circ.barrier(qreg_0[3])
main_circ.u(param_0,-0.255000,param_0, qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_0[3])
		main_circ.u(-0.649000,param_0,0.403000, qreg_0[3])
		main_circ.z(qreg_0[2])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.u(param_0,0.423000,-0.098000, qreg_0[2])
		main_circ.s(qreg_0[1])
		main_circ.barrier(qreg_0[2])
main_circ.s(qreg_0[3])
main_circ.u(param_0,0.791000,0.805000, qreg_0[1])
main_circ.s(qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.s(qreg_0[0])
	main_circ.rz(param_0, qreg_0[1])
with else_1:
	main_circ.rz(param_0, qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(param_0,param_0,param_0, qreg_0[3])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.u(-0.012000,param_0,param_0, qreg_0[2])
		main_circ.z(qreg_0[2])
		main_circ.id(qreg_0[3])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,param_0,param_0, qreg_0[1])
	main_circ.s(qreg_0[3])
with else_1:
	main_circ.rz(0.246000, qreg_0[3])
	main_circ.z(qreg_0[3])
	main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[0])
		main_circ.u(0.569000,param_0,param_0, qreg_0[0])
		main_circ.z(qreg_0[3])
		main_circ.z(qreg_0[1])
	with case_1(1):
		main_circ.z(qreg_0[1])
		main_circ.s(qreg_0[1])
		main_circ.s(qreg_0[2])
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_0, qreg_0[1])
	main_circ.z(qreg_0[1])
	main_circ.rz(0.898000, qreg_0[3])
	main_circ.z(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.s(qreg_0[2])
		main_circ.id(qreg_0[2])
	with case_1(1):
		main_circ.u(param_0,-0.021000,param_0, qreg_0[3])
		main_circ.z(qreg_0[3])
		main_circ.rz(0.414000, qreg_0[0])
		main_circ.s(qreg_0[3])
bindings = {param_0: 0.606000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "573")
