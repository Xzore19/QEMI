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
subcirc0.cy(qreg_0[2],qreg_0[3])
subcirc0.u(0,0,-0.056000, qreg_0[1])
subcirc0.u(0,0,0.661000, qreg_0[0])
subcirc0.cy(qreg_0[1],qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.h(qreg_0[0])
subcirc1.h(qreg_0[1])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.u(0,0,0.996000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(0.771000, qreg_0[2])
subcirc2.h(qreg_0[1])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.rz(-0.986000, qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_3[0]])
with else_1:
	main_circ.u(0,0,param_0, 1)
	main_circ.h(1)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.rz(-0.060000, qreg_0[0])
		main_circ.rz(-0.985000, qreg_0[0])
		main_circ.barrier(1)
	with case_1(1):
		main_circ.append(subcirc2,[1,0,qreg_2[0],qreg_0[1]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0,0,-0.656000, qreg_3[0])
		main_circ.cy(qreg_0[0],qreg_2[0])
		main_circ.id(qreg_3[0])
	with case_1(1):
		main_circ.u(0,param_2,0.823000, qreg_0[1])
		main_circ.rz(-0.874000, 1)
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[0,qreg_0[1],qreg_0[0],1])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],1,qreg_3[0]])
	with case_1(1):
		main_circ.rz(-0.630000, qreg_0[1])
		main_circ.h(qreg_3[0])
		main_circ.append(subcirc2,[0,1,qreg_2[0],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,param_2,0.976000, 1)
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.cy(qreg_0[0],1)
		main_circ.rz(param_0, qreg_0[0])
		main_circ.barrier(qreg_3[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_1,param_0,-0.860000, qreg_2[0])
	main_circ.append(subcirc1,[qreg_2[0],qreg_0[1],1,qreg_3[0]])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cy(qreg_2[0],qreg_0[1])
		main_circ.cy(qreg_3[0],1)
		main_circ.cy(0,qreg_3[0])
		main_circ.cy(0,qreg_0[0])
	with case_1(1):
		main_circ.cy(0,qreg_0[1])
		main_circ.cy(qreg_3[0],1)
		main_circ.cy(qreg_0[1],qreg_2[0])
		main_circ.u(param_0,param_0,-0.931000, 1)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_2[0])
	with case_1(1):
		main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],1,qreg_0[1]])
main_circ.cy(qreg_0[0],qreg_2[0])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.rz(param_2, qreg_0[0])
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.rz(-0.538000, qreg_0[0])
	main_circ.id(qreg_3[0])
bindings = {param_0: 0.685000, param_1: 0.962000, param_2: -0.542000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1665", "ElidePermutations")
