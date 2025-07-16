from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.z(qreg_0[0])
subcirc0.rx(-0.553000, qreg_0[0])
subcirc0.z(qreg_2[1])
subcirc0.rx(-0.812000, qreg_0[0])
subcirc0.u(pi/2,0.149000,-0.339000, qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.z(qreg_1[1])
main_circ.measure(qreg_1[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(param_3,0.154000,param_5, qreg_1[0])
		main_circ.z(qreg_1[1])
	with else_1:
		main_circ.u(param_2,param_0,param_1, 1)
		main_circ.u(pi/2,param_1,-0.954000, qreg_1[1])
		main_circ.append(subcirc0,[qreg_1[2],0,qreg_1[1],1])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.rx(param_1, 1)
		main_circ.cx(qreg_1[0],0)
		main_circ.cx(qreg_1[0],0)
		main_circ.cx(0,qreg_1[1])
		main_circ.append(subcirc0,[qreg_0[0],1,qreg_1[2],0])
	with else_1:
		main_circ.z(qreg_1[1])
		main_circ.u(pi/2,param_4,param_3, 0)
		main_circ.append(subcirc0,[0,qreg_0[0],qreg_1[1],1])
main_circ.u(param_4,param_1,param_4, qreg_1[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rx(param_1, 0)
		main_circ.cx(1,qreg_1[2])
		main_circ.rx(-0.970000, qreg_1[0])
		main_circ.rx(param_1, 1)
	with else_1:
		main_circ.u(param_4,param_5,-0.020000, 0)
		main_circ.u(pi/2,param_2,-0.020000, qreg_1[2])
		main_circ.cx(qreg_1[1],1)
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cx(qreg_1[2],qreg_1[1])
			main_circ.cx(0,qreg_1[0])
			main_circ.cx(qreg_0[0],qreg_1[2])
			main_circ.cx(qreg_1[2],1)
		with case_1(1):
			main_circ.cx(qreg_1[0],qreg_0[0])
			main_circ.cx(qreg_1[1],qreg_1[0])
			main_circ.cx(1,qreg_1[2])
			main_circ.cx(0,qreg_1[1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cx(0,qreg_0[0])
			main_circ.rx(param_1, qreg_1[0])
			main_circ.rx(param_3, 1)
			main_circ.rx(0.074000, 1)
		with else_1:
			main_circ.barrier(qreg_1[0])
	with case_2(1):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(qreg_1[1])
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.barrier(qreg_1[0])
		main_circ.measure(1, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[0])
			with case_1(1):
				main_circ.id(0)
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_1[0])
		with else_1:
			main_circ.id(1)
		main_circ.barrier(qreg_1[1])
bindings = {param_0: 0.761000, param_1: -0.176000, param_2: -0.721000, param_3: -0.238000, param_4: -0.617000, param_5: 0.421000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "376")
