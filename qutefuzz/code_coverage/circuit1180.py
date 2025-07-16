from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(pi/2,-0.162000,0.017000, qreg_2[0])
subcirc0.h(qreg_2[0])
subcirc0.y(qreg_0[0])
subcirc0.u(pi/2,0.371000,0.846000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,0.568000,-0.800000, qreg_0[1])
subcirc1.y(qreg_0[3])
subcirc1.y(qreg_0[2])
subcirc1.u(-0.576000,0.591000,0.281000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[2])
subcirc2.h(qreg_0[2])
subcirc2.y(qreg_0[1])
subcirc2.h(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.725000,0.480000, qreg_0[1])
subcirc3.y(qreg_0[0])
subcirc3.u(pi/2,-0.886000,0.009000, qreg_0[1])
subcirc3.u(pi/2,0.647000,0.209000, qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.h(qreg_3[0])
subcirc4.u(pi/2,0.781000,-0.611000, qreg_0[1])
subcirc4.u(pi/2,0.909000,-0.450000, qreg_3[0])
subcirc4.h(qreg_2[0])
subcirc4 = subcirc4.to_gate().control(3)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc3,[qreg_2[0],qreg_1[0],qreg_0[0],qreg_2[1]])
with else_1:
	main_circ.id(0)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_2[0],qreg_2[1],qreg_0[0],0,qreg_1[0]])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.y(qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(0)
	main_circ.append(subcirc2,[qreg_0[0],qreg_1[0],0,qreg_2[1],qreg_2[0]])
with else_1:
	main_circ.barrier(qreg_0[0])
main_circ.y(qreg_2[1])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(qreg_1[0])
with else_1:
	main_circ.y(qreg_2[1])
	main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.h(qreg_0[0])
		main_circ.u(param_1,param_1,-0.290000, qreg_1[0])
		main_circ.u(param_2,0.620000,param_0, 0)
		main_circ.append(subcirc3,[qreg_0[0],qreg_2[0],qreg_1[0],qreg_2[1]])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(qreg_2[1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,param_1,0.639000, qreg_2[1])
		main_circ.id(qreg_1[0])
	with case_1(1):
		main_circ.id(qreg_2[1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_2[0])
	with case_1(1):
		main_circ.y(0)
		main_circ.append(subcirc2,[qreg_2[1],qreg_2[0],qreg_1[0],qreg_0[0],0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.u(param_3,0.097000,param_3, 0)
		main_circ.id(qreg_2[1])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc3,[qreg_2[1],qreg_0[0],qreg_1[0],qreg_2[0]])
with else_1:
	main_circ.y(qreg_0[0])
	main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(0)
	main_circ.append(subcirc3,[qreg_0[0],qreg_2[1],0,qreg_1[0]])
with else_1:
	main_circ.id(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0.427000,param_0,-0.964000, qreg_2[1])
	main_circ.y(qreg_1[0])
	main_circ.u(param_0,0.327000,param_1, qreg_2[1])
	main_circ.append(subcirc3,[0,qreg_2[1],qreg_2[0],qreg_1[0]])
with else_1:
	main_circ.barrier(qreg_2[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(qreg_2[1])
	with case_1(1):
		main_circ.id(qreg_2[0])
main_circ.measure(qreg_2[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(qreg_2[0])
with else_1:
	main_circ.h(qreg_2[1])
	main_circ.id(0)
bindings = {param_0: 0.925000, param_1: -0.146000, param_2: 0.962000, param_3: -0.354000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1180")
