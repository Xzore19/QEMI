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
subcirc0.s(qreg_0[2])
subcirc0.cx(qreg_0[2],qreg_0[3])
subcirc0.s(qreg_0[0])
subcirc0.u(0,0,0.294000, qreg_0[0])
subcirc0.s(qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.u(0,0,-0.774000, qreg_0[0])
subcirc1.u(0,0,-0.500000, qreg_0[0])
subcirc1.u(0,0,-0.814000, qreg_0[3])
subcirc1.rz(0.832000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cx(qreg_2[0],qreg_0[0])
subcirc2.u(0,0,-0.745000, qreg_0[1])
subcirc2.u(0,0,-0.350000, qreg_0[1])
subcirc2.rz(0.942000, qreg_2[0])
subcirc2.u(0,0,0.511000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.rz(-0.933000, qreg_3[0])
subcirc3.s(qreg_0[1])
subcirc3.rz(-0.042000, qreg_2[0])
subcirc3.s(qreg_3[0])
subcirc3.s(qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cx(qreg_0[0],qreg_0[2])
subcirc4.s(qreg_0[0])
subcirc4.u(0,0,-0.692000, qreg_0[2])
subcirc4.cx(qreg_0[0],qreg_3[0])
subcirc4.rz(0.780000, qreg_3[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc0,[qreg_1[1],qreg_1[0],qreg_0[0],0])
	with else_1:
		main_circ.u(0,0,param_1, qreg_1[1])
		main_circ.append(subcirc4,[0,qreg_1[0],qreg_3[0],qreg_0[0]])
with else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(param_0,param_2,0.253000, qreg_1[0])
		main_circ.rz(param_1, qreg_1[0])
		main_circ.s(qreg_3[0])
		main_circ.append(subcirc4,[qreg_3[0],qreg_1[1],qreg_1[0],qreg_0[0]])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.rz(-0.839000, 0)
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc4,[qreg_1[0],qreg_3[0],qreg_0[0],0])
		with case_1(1):
			main_circ.append(subcirc4,[qreg_1[1],qreg_3[0],qreg_1[0],qreg_0[0]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rz(param_0, qreg_0[0])
		main_circ.rz(param_0, qreg_0[0])
		main_circ.rz(0.293000, qreg_1[1])
	with else_1:
		main_circ.cx(qreg_0[0],qreg_1[0])
		main_circ.cx(qreg_0[0],qreg_1[1])
		main_circ.cx(qreg_0[0],qreg_1[0])
		main_circ.cx(qreg_1[0],qreg_1[1])
		main_circ.cx(0,qreg_3[0])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.u(0,0,param_3, qreg_1[1])
		with else_1:
			main_circ.append(subcirc4,[qreg_0[0],qreg_1[1],qreg_3[0],0])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rz(-0.928000, qreg_1[0])
			main_circ.id(0)
		with else_1:
			main_circ.barrier(qreg_3[0])
		main_circ.measure(qreg_1[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(qreg_0[0])
			with case_1(1):
				main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_1[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rz(-0.831000, 0)
		with else_1:
			main_circ.u(param_0,0,param_0, qreg_1[0])
			main_circ.s(qreg_0[0])
bindings = {param_0: -0.485000, param_1: -0.186000, param_2: 0.345000, param_3: -0.180000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "220")
