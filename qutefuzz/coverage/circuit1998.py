from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.y(qreg_0[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_2[0])
subcirc0.cy(qreg_2[0],qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

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
param_2 = Parameter("param_2")

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cy(3,qreg_0[0])
				main_circ.y(2)
				main_circ.cz(3,qreg_0[0])
				main_circ.cz(1,3)
			with case_1(1):
				main_circ.y(0)
				main_circ.y(qreg_0[0])
				main_circ.y(qreg_0[0])
				main_circ.y(2)
	with else_2:
		main_circ.cx(qreg_0[0],3)
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc0,[qreg_0[0],0,2,1,3])
		with else_1:
			main_circ.y(1)
			main_circ.y(0)
			main_circ.cx(qreg_0[0],0)
			main_circ.y(qreg_0[0])
with else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.cx(qreg_0[0],3)
		main_circ.cx(0,1)
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.y(1)
				main_circ.cy(qreg_0[0],1)
				main_circ.cx(1,qreg_0[0])
				main_circ.cx(qreg_0[0],0)
			with case_1(1):
				main_circ.cy(2,0)
				main_circ.append(subcirc0,[2,3,1,0,qreg_0[0]])
	with else_2:
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.y(3)
			main_circ.y(0)
		with else_1:
			main_circ.cx(2,1)
			main_circ.cz(qreg_0[0],1)
			main_circ.cz(2,qreg_0[0])
			main_circ.cy(1,2)
			main_circ.cy(3,0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(qreg_0[0],1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.y(1)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.cz(3,qreg_0[0])
					main_circ.cy(0,qreg_0[0])
					main_circ.cx(1,2)
					main_circ.cz(2,0)
				with case_1(1):
					main_circ.append(subcirc0,[0,1,qreg_0[0],3,2])
		with else_2:
			main_circ.id(0)
	with case_3(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(0)
			with else_1:
				main_circ.barrier(2)
			main_circ.id(2)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(3, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.barrier(2)
				with case_1(1):
					main_circ.barrier(2)
			main_circ.measure(1, creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.id(2)
				with case_1(1):
					main_circ.barrier(qreg_0[0])
			main_circ.barrier(1)
		main_circ.barrier(1)
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1998", "CollectMultiQBlocks")
