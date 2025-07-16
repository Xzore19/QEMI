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
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_3[0])
subcirc0.u(pi/2,-0.472000,-0.595000, qreg_0[0])
subcirc0.ry(0.359000, qreg_0[2])
subcirc0.ry(-0.419000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(-0.809000, qreg_0[1])
subcirc1.u(pi/2,-0.270000,0.621000, qreg_0[0])
subcirc1.ry(0.230000, qreg_2[1])
subcirc1.h(qreg_2[1])
subcirc1.u(pi/2,0.647000,-0.823000, qreg_2[1])
subcirc1.ry(-0.829000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(pi/2,-0.054000,-0.988000, qreg_0[0])
subcirc2.ry(-0.034000, qreg_2[0])
subcirc2.ry(-0.699000, qreg_2[1])
subcirc2.u(pi/2,-0.636000,-0.547000, qreg_0[0])
subcirc2.ry(0.364000, qreg_2[1])
subcirc2.cy(qreg_0[1],qreg_2[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[2],qreg_0[1])
subcirc3.u(pi/2,0.278000,-0.746000, qreg_0[2])
subcirc3.ry(-0.863000, qreg_0[2])
subcirc3.u(pi/2,-0.933000,-0.060000, qreg_0[0])
subcirc3.u(pi/2,-0.425000,-0.283000, qreg_0[2])
subcirc3.h(qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.ry(0.890000, qreg_1[0])
subcirc4.u(pi/2,0.432000,0.528000, qreg_1[1])
subcirc4.cy(qreg_0[0],qreg_1[1])
subcirc4.cy(qreg_1[0],qreg_0[0])
subcirc4.h(qreg_1[0])
subcirc4.ry(0.796000, qreg_1[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc4,[1,qreg_0[1],qreg_2[0],qreg_3[0]])
		with case_1(1):
			main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],1,0])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],1,0,qreg_3[0],qreg_2[0]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc4,[qreg_3[0],qreg_0[1],1,qreg_0[0]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc0,[qreg_3[0],1,qreg_0[0],qreg_0[1],0])
	with case_2(1):
		main_circ.measure(qreg_2[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc3,[qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
		with else_1:
			main_circ.cy(1,qreg_2[0])
			main_circ.cy(qreg_3[0],0)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.cy(qreg_2[0],qreg_3[0])
	with else_1:
		main_circ.cy(qreg_3[0],0)
	main_circ.cy(qreg_0[0],qreg_3[0])
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.cy(0,qreg_2[0])
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(1)
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_3[0])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[1])
	main_circ.barrier(1)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.u(pi/2,param_0,-0.850000, qreg_3[0])
			main_circ.h(1)
			main_circ.id(qreg_3[0])
		with case_1(1):
			main_circ.id(qreg_0[0])
with else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(1)
	with else_1:
		main_circ.barrier(0)
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(qreg_2[0])
	main_circ.measure(qreg_2[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[1])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(0)
		with case_1(1):
			main_circ.barrier(qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(qreg_0[0])
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(qreg_2[0])
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_3[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_0[1])
		with case_1(1):
			main_circ.id(qreg_2[0])
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(0)
	main_circ.id(0)
bindings = {param_0: 0.647000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "436", "OptimizeAnnotated")
