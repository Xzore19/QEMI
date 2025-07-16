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
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0.h(qreg_0[2])
subcirc0.h(qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.rx(-0.304000, qreg_0[0])
subcirc0.rx(-0.068000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.025000, qreg_0[3])
subcirc1.cx(qreg_0[1],qreg_0[3])
subcirc1.h(qreg_0[0])
subcirc1.cy(qreg_0[3],qreg_0[0])
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.rx(0.751000, qreg_0[1])
subcirc2.cy(qreg_2[1],qreg_0[1])
subcirc2.h(qreg_2[0])
subcirc2.cy(qreg_0[0],qreg_2[1])
subcirc2.cy(qreg_2[1],qreg_0[0])
subcirc2.rx(-0.113000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.cx(qreg_1[2],qreg_0[0])
subcirc3.cx(qreg_0[0],qreg_1[0])
subcirc3.cy(qreg_1[1],qreg_1[2])
subcirc3.h(qreg_0[0])
subcirc3.h(qreg_1[2])
subcirc3.h(qreg_1[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cy(qreg_0[0],qreg_0[2])
subcirc4.rx(-0.150000, qreg_0[2])
subcirc4.rx(0.893000, qreg_0[3])
subcirc4.cy(qreg_0[1],qreg_0[0])
subcirc4.cx(qreg_0[1],qreg_0[2])
subcirc4.h(qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.append(subcirc4,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_2[1]])
		with case_2(1):
			main_circ.h(qreg_0[1])
			main_circ.measure(qreg_2[1], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.cy(qreg_0[1],qreg_2[0])
				main_circ.id(qreg_0[1])
			main_circ.h(qreg_0[0])
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.switch(creg_0[1]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[qreg_0[1],qreg_2[1],qreg_0[0],qreg_2[0]])
				with case_1(1):
					main_circ.append(subcirc3,[qreg_2[1],qreg_0[1],qreg_2[0],qreg_0[0]])
with else_3:
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],qreg_2[1],qreg_0[0]])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rx(param_1, qreg_0[1])
			main_circ.id(qreg_2[0])
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.h(qreg_0[1])
				main_circ.append(subcirc1,[qreg_2[1],qreg_0[0],qreg_0[1],qreg_2[0]])
			with case_1(1):
				main_circ.append(subcirc4,[qreg_2[0],qreg_0[1],qreg_0[0],qreg_2[1]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.cx(qreg_2[1],qreg_0[0])
				main_circ.append(subcirc4,[qreg_0[0],qreg_2[0],qreg_2[1],qreg_0[1]])
			with else_1:
				main_circ.id(qreg_2[0])
		with else_2:
			main_circ.measure(qreg_2[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rx(-0.077000, qreg_2[1])
				main_circ.cy(qreg_0[1],qreg_2[0])
				main_circ.id(qreg_0[0])
			with else_1:
				main_circ.id(qreg_2[0])
	with case_3(1):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.append(subcirc3,[qreg_2[1],qreg_0[0],qreg_2[0],qreg_0[1]])
		with else_2:
			main_circ.cx(qreg_0[1],qreg_2[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.cy(qreg_2[1],qreg_2[0])
				main_circ.barrier(qreg_2[0])
			with else_1:
				main_circ.id(qreg_0[1])
			main_circ.measure(qreg_2[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.id(qreg_2[0])
			with else_1:
				main_circ.rx(param_0, qreg_0[1])
				main_circ.id(qreg_2[1])
bindings = {param_0: -0.403000, param_1: 0.298000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1410")
