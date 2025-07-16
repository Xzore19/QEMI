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
subcirc0.rx(-0.614000, qreg_1[2])
subcirc0.cy(qreg_1[2],qreg_0[0])
subcirc0.ry(-0.702000, qreg_1[1])
subcirc0.cy(qreg_0[0],qreg_1[2])
subcirc0.cy(qreg_1[2],qreg_1[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(0.496000, qreg_0[1])
subcirc1.ry(0.140000, qreg_3[0])
subcirc1.rz(-0.537000, qreg_0[1])
subcirc1.cy(qreg_0[0],qreg_0[2])
subcirc1.ry(-0.251000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(-0.090000, qreg_0[2])
subcirc2.cy(qreg_0[1],qreg_0[0])
subcirc2.rx(-0.270000, qreg_0[2])
subcirc2.rx(-0.250000, qreg_0[3])
subcirc2.rz(-0.835000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.ry(0.600000, qreg_0[2])
subcirc3.ry(-0.759000, qreg_0[2])
subcirc3.ry(-0.197000, qreg_3[0])
subcirc3.cy(qreg_0[0],qreg_3[0])
subcirc3.rx(-0.912000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(0.947000, qreg_0[1])
subcirc4.rz(0.356000, qreg_0[0])
subcirc4.rx(-0.755000, qreg_0[2])
subcirc4.ry(-0.023000, qreg_0[0])
subcirc4.rz(0.244000, qreg_0[2])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(1)
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

main_circ.append(subcirc4,[qreg_1[2],0,qreg_0[0],qreg_1[0],qreg_1[1]])
main_circ.measure(qreg_1[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_1[2])
		with case_1(1):
			main_circ.cy(qreg_1[1],qreg_1[0])
			main_circ.barrier(qreg_1[2])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rx(param_1, qreg_1[0])
			main_circ.rx(param_1, qreg_0[0])
			main_circ.rz(param_1, qreg_1[1])
			main_circ.rx(param_0, 0)
		with case_1(1):
			main_circ.rx(param_0, 0)
			main_circ.barrier(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.id(qreg_1[1])
	with else_1:
		main_circ.rz(param_0, qreg_1[1])
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.ry(-0.096000, 0)
		main_circ.rx(-0.955000, 0)
		main_circ.barrier(qreg_1[1])
	main_circ.barrier(qreg_1[2])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(0)
	main_circ.rz(-0.522000, qreg_1[2])
main_circ.append(subcirc4,[qreg_1[2],qreg_1[0],qreg_0[0],0,qreg_1[1]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.ry(param_0, qreg_1[0])
			main_circ.barrier(0)
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc4,[0,qreg_0[0],qreg_1[0],qreg_1[2],qreg_1[1]])
		with else_1:
			main_circ.barrier(qreg_1[2])
	with case_2(1):
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.rz(0.801000, qreg_1[2])
			main_circ.append(subcirc4,[qreg_1[0],qreg_1[2],0,qreg_1[1],qreg_0[0]])
main_circ.measure(qreg_1[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(qreg_1[2])
	main_circ.measure(qreg_1[1], creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.id(qreg_0[0])
		with case_1(1):
			main_circ.cy(qreg_0[0],qreg_1[1])
			main_circ.append(subcirc4,[qreg_1[1],qreg_0[0],0,qreg_1[2],qreg_1[0]])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_1[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[1])
			with case_1(1):
				main_circ.barrier(0)
		main_circ.cy(qreg_1[1],qreg_0[0])
		main_circ.measure(qreg_1[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.rx(-0.469000, qreg_1[2])
			main_circ.barrier(qreg_1[0])
		main_circ.barrier(qreg_0[0])
	with case_2(1):
		main_circ.measure(qreg_1[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(qreg_0[0])
		main_circ.barrier(qreg_1[2])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_1[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.ry(-0.806000, qreg_0[0])
		main_circ.cy(qreg_1[2],0)
		main_circ.cy(qreg_0[0],0)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.cy(qreg_1[0],qreg_0[0])
		main_circ.cy(0,qreg_0[0])
	with else_1:
		main_circ.cy(0,qreg_1[1])
with else_2:
	main_circ.cy(qreg_1[0],qreg_1[1])
	main_circ.measure(qreg_1[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cy(0,qreg_0[0])
	with else_1:
		main_circ.cy(0,qreg_1[1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_1[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.cy(qreg_1[2],qreg_1[0])
			main_circ.cy(qreg_0[0],qreg_1[1])
			main_circ.cy(0,qreg_0[0])
			main_circ.cy(qreg_0[0],qreg_1[0])
		with case_1(1):
			main_circ.cy(qreg_0[0],qreg_1[0])
			main_circ.cy(0,qreg_1[2])
			main_circ.barrier(qreg_1[2])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.rx(param_1, 0)
				main_circ.rx(-0.254000, qreg_1[1])
				main_circ.cy(qreg_0[0],0)
				main_circ.id(qreg_1[2])
			with case_1(1):
				main_circ.barrier(qreg_1[1])
		main_circ.barrier(qreg_1[1])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_1[1])
			with case_1(1):
				main_circ.barrier(qreg_1[1])
		main_circ.measure(qreg_1[2], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.id(qreg_1[1])
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(0)
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(0)
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(qreg_1[0])
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.id(0)
			with case_1(1):
				main_circ.id(qreg_1[2])
		main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.329000, param_1: -0.666000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1378")
