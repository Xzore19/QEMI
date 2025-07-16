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
subcirc0.cx(qreg_3[0],qreg_1[0])
subcirc0.u(0,0,-0.879000, qreg_1[0])
subcirc0.cx(qreg_0[0],qreg_1[0])
subcirc0.cx(qreg_3[0],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(-0.035000, qreg_0[3])
subcirc1.rx(0.534000, qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.h(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

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

main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.h(qreg_0[1])
	main_circ.h(qreg_0[2])
	main_circ.rx(param_0, qreg_0[3])
	main_circ.cx(1,qreg_0[0])
	main_circ.cx(1,qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cx(0,qreg_0[1])
with else_1:
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(1)
with else_1:
	main_circ.u(0,0,-0.740000, qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rx(param_2, 1)
with else_1:
	main_circ.h(qreg_0[3])
	main_circ.cx(qreg_0[1],qreg_0[3])
	main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[qreg_0[0],1,0,qreg_0[2]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],0,qreg_0[2]])
	main_circ.rx(0.456000, qreg_0[1])
with else_1:
	main_circ.barrier(0)
main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[3],1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(qreg_0[2])
	main_circ.append(subcirc0,[qreg_0[0],0,1,qreg_0[2]])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(0)
with else_1:
	main_circ.h(qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cx(1,qreg_0[0])
		main_circ.u(0,param_2,0.434000, qreg_0[1])
		main_circ.append(subcirc0,[1,0,qreg_0[1],qreg_0[2]])
	with case_1(1):
		main_circ.cx(qreg_0[0],0)
		main_circ.rx(param_0, qreg_0[3])
		main_circ.h(qreg_0[0])
		main_circ.u(0,param_1,-0.027000, 1)
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[0,1,qreg_0[0],qreg_0[2]])
	with case_1(1):
		main_circ.cx(qreg_0[3],qreg_0[2])
		main_circ.h(0)
		main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(-0.530000, 1)
	main_circ.rx(param_0, qreg_0[1])
	main_circ.append(subcirc0,[1,qreg_0[1],qreg_0[0],qreg_0[2]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(1)
	main_circ.h(qreg_0[1])
	main_circ.u(param_1,0,-0.512000, qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.h(qreg_0[0])
	main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cx(qreg_0[3],qreg_0[1])
bindings = {param_0: 0.098000, param_1: -0.133000, param_2: -0.591000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1679")
