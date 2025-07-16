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
subcirc0.u(pi/2,0.855000,-0.758000, qreg_0[0])
subcirc0.u(pi/2,-0.793000,0.183000, qreg_3[0])
subcirc0.s(qreg_3[0])
subcirc0.rz(-0.957000, qreg_3[0])
subcirc0.u(pi/2,-0.933000,-0.541000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[0])
subcirc1.u(pi/2,-0.800000,0.931000, qreg_0[2])
subcirc1.rz(0.403000, qreg_0[3])
subcirc1.rz(-0.094000, qreg_0[2])
subcirc1.u(pi/2,-0.702000,-0.274000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
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

main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.s(2)
			main_circ.measure(qreg_0[1], creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.id(0)
				with case_1(1):
					main_circ.rz(0.461000, qreg_0[0])
					main_circ.s(2)
					main_circ.id(2)
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(param_2,-0.880000,0.849000, 1)
				main_circ.append(subcirc1,[2,0,3,qreg_0[0]])
			with else_1:
				main_circ.rx(param_2, 2)
		with case_2(1):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.u(pi/2,param_1,param_1, qreg_0[1])
				main_circ.u(param_0,param_2,param_0, 0)
				main_circ.s(qreg_0[0])
				main_circ.s(0)
			with else_1:
				main_circ.s(qreg_0[1])
				main_circ.rz(0.503000, 3)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.rz(0.871000, 1)
					main_circ.rx(param_0, qreg_0[1])
					main_circ.append(subcirc1,[1,qreg_0[0],3,qreg_0[1]])
				with case_1(1):
					main_circ.u(param_2,param_2,param_1, 2)
					main_circ.u(param_1,0.238000,-0.317000, 3)
					main_circ.id(0)
		with case_2(1):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.append(subcirc1,[0,qreg_0[1],2,3])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.append(subcirc1,[3,1,qreg_0[1],qreg_0[0]])
	with else_2:
		main_circ.barrier(2)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_3:
	with case_3(0):
		main_circ.id(qreg_0[0])
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.append(subcirc1,[3,qreg_0[0],1,0])
		with else_2:
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.rx(param_0, 3)
					main_circ.s(1)
					main_circ.u(param_0,param_0,param_1, 1)
					main_circ.rz(param_1, 2)
				with case_1(1):
					main_circ.u(param_1,-0.289000,-0.458000, 2)
					main_circ.id(qreg_0[1])
bindings = {param_0: -0.957000, param_1: -0.603000, param_2: 0.970000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "215", "ResetAfterMeasureSimplification")
