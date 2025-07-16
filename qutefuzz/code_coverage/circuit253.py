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
subcirc0.u(0.093000,0.519000,-0.672000, qreg_0[1])
subcirc0.u(0.337000,0.264000,0.891000, qreg_0[0])
subcirc0.rz(0.241000, qreg_0[2])
subcirc0.h(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_0[2])
subcirc1.rz(0.047000, qreg_0[2])
subcirc1.u(-0.577000,-0.105000,0.452000, qreg_0[0])
subcirc1.cx(qreg_0[0],qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(-0.783000, qreg_0[2])
subcirc2.rz(-0.231000, qreg_0[0])
subcirc2.cx(qreg_0[3],qreg_0[1])
subcirc2.rz(-0.919000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.745000,-0.378000,-0.011000, qreg_1[1])
subcirc3.rz(0.957000, qreg_1[1])
subcirc3.u(-1.000000,-0.146000,-0.288000, qreg_1[1])
subcirc3.cx(qreg_1[1],qreg_3[0])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
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

main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.h(2)
		main_circ.append(subcirc2,[2,0,1,qreg_1[0],3])
	with else_1:
		main_circ.append(subcirc1,[1,3,2,0])
with else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.h(3)
		main_circ.h(0)
		main_circ.append(subcirc0,[1,0,3,2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_1[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.rz(-0.994000, 1)
		main_circ.append(subcirc3,[0,qreg_0[0],1,3,2])
with else_2:
	main_circ.measure(qreg_0[0], creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc1,[qreg_0[0],0,1,qreg_1[0]])
	with else_1:
		main_circ.h(1)
		main_circ.u(param_1,param_2,-0.311000, 1)
main_circ.h(1)
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.h(1)
			main_circ.rz(param_2, qreg_0[0])
			main_circ.cx(0,2)
			main_circ.cx(1,qreg_1[0])
		with case_1(1):
			main_circ.cx(qreg_1[0],3)
			main_circ.cx(1,qreg_1[0])
			main_circ.cx(3,qreg_0[0])
			main_circ.cx(qreg_1[0],1)
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cx(0,3)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.cx(qreg_1[0],2)
			main_circ.u(param_1,param_0,param_2, 2)
			main_circ.cx(0,qreg_1[0])
			main_circ.h(2)
	with case_2(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_1[0],3)
				main_circ.barrier(3)
			with case_1(1):
				main_circ.id(1)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(0)
		with else_1:
			main_circ.barrier(qreg_1[0])
		main_circ.id(1)
bindings = {param_0: 0.898000, param_1: 0.380000, param_2: 0.253000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "253")
