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
subcirc0.cx(qreg_0[2],qreg_0[1])
subcirc0.cx(qreg_0[0],qreg_3[0])
subcirc0.z(qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.317000,0.496000,0.137000, qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1.s(qreg_0[0])
subcirc1.u(0.818000,-0.259000,-0.858000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0.784000,-0.676000,0.690000, qreg_0[3])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_0[2])
subcirc2.s(qreg_0[3])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_3[0])
subcirc3.u(-0.881000,-0.983000,-0.376000, qreg_0[1])
subcirc3.s(qreg_0[0])
subcirc3.s(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.z(qreg_1[0])
			main_circ.u(0.389000,param_2,-0.537000, qreg_2[0])
			main_circ.barrier(qreg_3[0])
		with case_1(1):
			main_circ.cx(qreg_2[0],qreg_1[0])
			main_circ.cx(qreg_1[0],qreg_3[0])
			main_circ.cx(qreg_3[0],qreg_0[0])
			main_circ.s(qreg_0[0])
with else_2:
	main_circ.u(-0.795000,param_1,param_2, qreg_1[0])
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.s(qreg_3[0])
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.z(qreg_0[0])
			main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_0[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.s(qreg_2[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.z(qreg_0[0])
			main_circ.id(qreg_2[0])
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_3[0])
		with case_1(1):
			main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.cx(qreg_3[0],qreg_2[0])
	with else_1:
		main_circ.barrier(qreg_1[0])
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(0.681000,-0.585000,param_1, qreg_1[0])
		main_circ.u(param_0,0.060000,-0.735000, qreg_2[0])
		main_circ.cx(qreg_2[0],qreg_3[0])
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.cx(qreg_3[0],qreg_2[0])
	with else_1:
		main_circ.z(qreg_1[0])
		main_circ.u(0.699000,param_3,param_2, qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.cx(qreg_2[0],qreg_1[0])
		main_circ.cx(qreg_3[0],qreg_2[0])
	with else_1:
		main_circ.s(qreg_3[0])
		main_circ.id(qreg_1[0])
	main_circ.s(qreg_0[0])
with else_2:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.s(qreg_3[0])
			main_circ.barrier(qreg_2[0])
		with case_1(1):
			main_circ.id(qreg_2[0])
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.u(param_3,0.659000,param_1, qreg_2[0])
		main_circ.id(qreg_1[0])
	with else_1:
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.barrier(qreg_1[0])
	with else_1:
		main_circ.z(qreg_3[0])
		main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_2[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.z(qreg_0[0])
	with else_1:
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_3[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_3[0])
		with case_1(1):
			main_circ.u(param_1,param_0,-0.409000, qreg_3[0])
			main_circ.cx(qreg_0[0],qreg_1[0])
			main_circ.id(qreg_0[0])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_1[0],qreg_0[0])
			main_circ.z(qreg_0[0])
			main_circ.cx(qreg_2[0],qreg_1[0])
			main_circ.cx(qreg_2[0],qreg_0[0])
		with case_1(1):
			main_circ.cx(qreg_2[0],qreg_3[0])
			main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.id(qreg_3[0])
	with else_1:
		main_circ.z(qreg_2[0])
		main_circ.z(qreg_2[0])
		main_circ.barrier(qreg_1[0])
	main_circ.u(param_1,0.714000,param_2, qreg_2[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_1[0])
		with case_1(1):
			main_circ.cx(qreg_1[0],qreg_0[0])
			main_circ.id(qreg_3[0])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(qreg_2[0],qreg_1[0])
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.u(param_3,param_3,param_2, qreg_3[0])
		main_circ.id(qreg_2[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.s(qreg_1[0])
			main_circ.u(param_1,-0.743000,param_1, qreg_2[0])
			main_circ.u(param_0,0.911000,-0.899000, qreg_0[0])
			main_circ.barrier(qreg_3[0])
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.s(qreg_2[0])
		main_circ.id(qreg_2[0])
bindings = {param_0: 0.228000, param_1: 0.941000, param_2: -0.214000, param_3: 0.045000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "109")
