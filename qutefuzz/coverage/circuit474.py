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
subcirc0.u(0,0,-0.982000, qreg_0[1])
subcirc0.rz(0.467000, qreg_0[2])
subcirc0.rz(0.420000, qreg_0[3])
subcirc0.cy(qreg_0[1],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0,0,-0.081000, qreg_0[0])
subcirc1.u(0,0,0.504000, qreg_0[1])
subcirc1.cy(qreg_0[2],qreg_0[1])
subcirc1.rz(0.487000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_3[0],qreg_2[0])
subcirc2.rz(-0.790000, qreg_3[0])
subcirc2.s(qreg_3[0])
subcirc2.rz(0.481000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_0[1])
subcirc3.cy(qreg_0[0],qreg_3[0])
subcirc3.cy(qreg_3[0],qreg_0[1])
subcirc3.u(0,0,0.157000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.u(0,0,0.086000, qreg_1[0])
subcirc4.rz(0.022000, qreg_0[0])
subcirc4.rz(0.746000, qreg_0[0])
subcirc4.u(0,0,0.551000, qreg_1[1])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0],0])
	main_circ.u(0,0,param_1, qreg_0[2])
with else_1:
	main_circ.id(qreg_0[2])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0,0,param_4, qreg_3[0])
		main_circ.rz(0.648000, qreg_0[2])
		main_circ.barrier(0)
	with case_1(1):
		main_circ.rz(param_2, qreg_0[2])
		main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[2])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[2],0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc1,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0],0])
	main_circ.rz(0.965000, 0)
with else_1:
	main_circ.s(qreg_0[2])
	main_circ.u(0,0,param_3, qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_4,0,param_4, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],0,qreg_0[0],qreg_0[1]])
with else_1:
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[1])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],0,qreg_0[1]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(qreg_0[2])
with else_1:
	main_circ.id(qreg_0[2])
main_circ.append(subcirc4,[qreg_0[1],qreg_0[0],0,qreg_0[2],qreg_3[0]])
main_circ.cy(qreg_0[0],qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(0,qreg_0[1])
	main_circ.cy(qreg_0[1],0)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(qreg_3[0],qreg_0[2])
	main_circ.cy(qreg_0[0],0)
	main_circ.cy(qreg_0[0],0)
main_circ.cy(qreg_0[1],qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.barrier(qreg_3[0])
main_circ.u(0,param_3,0.768000, qreg_0[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.s(qreg_3[0])
bindings = {param_1: -0.052000, param_2: 0.954000, param_3: -0.612000, param_4: 0.148000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "474")
