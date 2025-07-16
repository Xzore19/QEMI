from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.cz(qreg_1[2],qreg_1[0])
subcirc0.cx(qreg_1[2],qreg_1[0])
subcirc0.rx(0.231000, qreg_1[1])
subcirc0.cz(qreg_1[1],qreg_1[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.rx(0.870000, qreg_0[3])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.050000, qreg_0[1])
subcirc2.cx(qreg_0[1],qreg_0[2])
subcirc2.cx(qreg_3[0],qreg_0[2])
subcirc2.cz(qreg_3[0],qreg_0[2])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rx(0.231000, qreg_0[2])
subcirc3.z(qreg_3[0])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.z(qreg_0[2])
subcirc4.rx(0.657000, qreg_3[0])
subcirc4.z(qreg_0[2])
subcirc4.cz(qreg_0[0],qreg_0[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc2,[1,qreg_0[0],2,3])
			with case_1(1):
				main_circ.cz(1,0)
				main_circ.barrier(2)
	with case_2(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.z(1)
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.z(3)
				main_circ.cx(1,3)
				main_circ.cx(1,0)
				main_circ.id(1)
	with case_2(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.cz(3,2)
				main_circ.append(subcirc2,[qreg_0[0],0,3,1])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(3)
main_circ.cx(qreg_0[0],0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(1)
	with else_1:
		main_circ.rx(param_1, 1)
		main_circ.barrier(3)
main_circ.z(2)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.z(0)
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.z(qreg_0[0])
		main_circ.rx(0.102000, qreg_0[0])
		main_circ.rx(-0.818000, 2)
		main_circ.cx(0,3)
		main_circ.id(0)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.cx(1,2)
			main_circ.z(2)
			main_circ.append(subcirc2,[0,2,3,1])
	with case_2(1):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(1,2)
				main_circ.id(2)
			with case_1(1):
				main_circ.cx(0,qreg_0[0])
				main_circ.id(3)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cz(qreg_0[0],3)
			main_circ.append(subcirc1,[3,qreg_0[0],2,0,1])
		with else_1:
			main_circ.rx(-0.786000, qreg_0[0])
			main_circ.id(qreg_0[0])
main_circ.append(subcirc2,[1,3,qreg_0[0],2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc2,[2,3,qreg_0[0],0])
		with case_1(1):
			main_circ.cx(0,1)
			main_circ.id(3)
with else_2:
	main_circ.id(0)
main_circ.cz(3,1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.rx(0.227000, 0)
			main_circ.cx(qreg_0[0],2)
			main_circ.z(qreg_0[0])
			main_circ.append(subcirc2,[2,3,qreg_0[0],0])
		with case_1(1):
			main_circ.id(qreg_0[0])
with else_2:
	main_circ.z(2)
	main_circ.z(1)
bindings = {param_1: -0.691000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1766", "ElidePermutations")
