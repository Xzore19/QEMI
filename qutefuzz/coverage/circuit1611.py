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
subcirc0.cx(qreg_1[1],qreg_0[0])
subcirc0.rz(0.919000, qreg_0[0])
subcirc0.rz(0.396000, qreg_0[0])
subcirc0.cx(qreg_3[0],qreg_0[0])
subcirc0.cx(qreg_1[0],qreg_3[0])
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
subcirc1.rz(-0.441000, qreg_2[0])
subcirc1.rz(-0.900000, qreg_0[0])
subcirc1.u(-0.707000,-0.868000,-0.280000, qreg_0[1])
subcirc1.rz(0.762000, qreg_3[0])
subcirc1.rz(0.831000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(0)
		with case_1(1):
			main_circ.rx(param_2, qreg_0[2])
			main_circ.u(param_0,-0.507000,-0.836000, qreg_0[2])
			main_circ.u(param_1,-0.868000,0.685000, qreg_0[1])
			main_circ.cx(qreg_0[3],qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[2])
		with case_1(1):
			main_circ.cx(qreg_0[1],qreg_0[2])
			main_circ.append(subcirc1,[0,qreg_0[2],1,qreg_0[1],qreg_0[0],qreg_0[3]])
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(-0.308000,param_2,-0.159000, qreg_0[2])
			main_circ.rx(-0.344000, 1)
			main_circ.cx(0,qreg_0[0])
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.rz(-0.286000, qreg_0[1])
			main_circ.rx(-0.165000, qreg_0[3])
			main_circ.rx(param_1, qreg_0[1])
			main_circ.rz(-0.084000, qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rx(-0.297000, qreg_0[0])
		main_circ.append(subcirc1,[0,qreg_0[1],qreg_0[2],1,qreg_0[0],qreg_0[3]])
with else_2:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_1, qreg_0[2])
			main_circ.rx(-0.982000, 1)
			main_circ.append(subcirc1,[0,1,qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2]])
		with case_1(1):
			main_circ.append(subcirc1,[qreg_0[2],qreg_0[1],qreg_0[3],1,0,qreg_0[0]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(-0.982000,param_2,param_2, 1)
			main_circ.cx(qreg_0[0],qreg_0[3])
			main_circ.rz(0.848000, 1)
			main_circ.cx(0,qreg_0[2])
		with case_1(1):
			main_circ.cx(qreg_0[3],0)
			main_circ.cx(qreg_0[0],qreg_0[3])
			main_circ.cx(1,qreg_0[0])
			main_circ.cx(qreg_0[0],0)
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cx(qreg_0[1],qreg_0[3])
		main_circ.cx(qreg_0[0],qreg_0[3])
		main_circ.cx(qreg_0[1],qreg_0[0])
		main_circ.cx(qreg_0[2],1)
		main_circ.cx(qreg_0[1],qreg_0[3])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(0,qreg_0[0])
		main_circ.barrier(1)
	with else_1:
		main_circ.barrier(1)
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(param_0, qreg_0[3])
			main_circ.rz(param_0, qreg_0[1])
			main_circ.rz(param_2, 1)
			main_circ.rx(0.618000, qreg_0[3])
			main_circ.barrier(qreg_0[3])
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.id(qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.barrier(qreg_0[3])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[3])
			with case_1(1):
				main_circ.barrier(1)
		main_circ.barrier(0)
bindings = {param_0: 0.768000, param_1: 0.170000, param_2: 0.624000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1611", "ResetAfterMeasureSimplification")
