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
subcirc0.rz(-0.893000, qreg_0[2])
subcirc0.ry(0.813000, qreg_0[1])
subcirc0.u(0,0,-0.723000, qreg_0[2])
subcirc0.rx(-0.933000, qreg_0[0])
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
subcirc1.u(0,0,-0.829000, qreg_0[0])
subcirc1.rx(-0.867000, qreg_3[0])
subcirc1.u(0,0,0.019000, qreg_3[0])
subcirc1.ry(-0.409000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.ry(-0.986000, qreg_0[3])
subcirc2.rz(-0.520000, qreg_0[0])
subcirc2.rx(-0.128000, qreg_0[1])
subcirc2.rz(-0.452000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.ry(-0.182000, qreg_0[0])
subcirc3.rz(-0.761000, qreg_0[0])
subcirc3.rx(0.433000, qreg_0[1])
subcirc3.rz(0.674000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(0.005000, qreg_2[0])
subcirc4.ry(-0.051000, qreg_0[0])
subcirc4.u(0,0,-0.079000, qreg_0[0])
subcirc4.ry(0.640000, qreg_0[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.append(subcirc4,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
	with case_3(1):
		main_circ.rz(-0.224000, qreg_0[3])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(-0.680000, qreg_0[1])
				main_circ.barrier(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.u(0,0,param_2, qreg_0[1])
			main_circ.measure(qreg_0[3], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.u(param_3,0,param_3, qreg_0[0])
					main_circ.append(subcirc4,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
				with case_1(1):
					main_circ.ry(param_3, qreg_0[2])
					main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[3], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.u(param_1,param_2,0.602000, qreg_0[1])
			main_circ.ry(0.866000, qreg_0[1])
		main_circ.rx(param_2, qreg_0[2])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[3])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(0,param_1,param_3, qreg_0[0])
				main_circ.append(subcirc2,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
			with case_1(1):
				main_circ.id(qreg_0[0])
	with else_2:
		main_circ.ry(param_3, qreg_0[2])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_0[3],qreg_0[2]])
		with else_1:
			main_circ.u(param_1,0,param_2, qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.id(qreg_0[1])
	with case_3(1):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.ry(param_2, qreg_0[2])
				main_circ.barrier(qreg_0[2])
			with case_2(1):
				main_circ.measure(qreg_0[1], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.barrier(qreg_0[0])
				main_circ.measure(qreg_0[0], creg_1[0])
				with main_circ.switch(creg_1[0]) as case_1:
					with case_1(0):
						main_circ.u(param_0,0,0.899000, qreg_0[2])
						main_circ.ry(-0.213000, qreg_0[1])
						main_circ.barrier(qreg_0[0])
					with case_1(1):
						main_circ.id(qreg_0[2])
				main_circ.measure(qreg_0[3], creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.u(0,param_3,param_2, qreg_0[0])
					main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.id(qreg_0[1])
with else_3:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.ry(param_2, qreg_0[3])
				main_circ.ry(-0.269000, qreg_0[3])
			with else_1:
				main_circ.rx(param_3, qreg_0[2])
				main_circ.id(qreg_0[3])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[1])
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.id(qreg_0[3])
			main_circ.id(qreg_0[2])
		with case_2(1):
			main_circ.ry(0.667000, qreg_0[1])
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rz(param_2, qreg_0[3])
			main_circ.measure(qreg_0[2], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.barrier(qreg_0[3])
			main_circ.barrier(qreg_0[1])
main_circ.rz(param_3, qreg_0[2])
bindings = {param_0: 0.246000, param_1: -0.091000, param_2: -0.892000, param_3: -0.389000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1799", "ResetAfterMeasureSimplification")
