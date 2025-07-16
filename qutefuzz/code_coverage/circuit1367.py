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
subcirc0.rz(-0.980000, qreg_3[0])
subcirc0.u(-0.052000,0.486000,0.412000, qreg_0[0])
subcirc0.rz(0.917000, qreg_3[0])
subcirc0.u(0.294000,0.172000,-0.772000, qreg_0[1])
subcirc0.rz(-0.671000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cy(qreg_1[0],qreg_0[0])
subcirc1.cy(qreg_2[1],qreg_1[0])
subcirc1.u(0.030000,0.522000,0.255000, qreg_0[0])
subcirc1.rz(0.689000, qreg_2[1])
subcirc1.cy(qreg_2[1],qreg_2[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.141000, qreg_0[0])
subcirc2.u(0.457000,-0.124000,-0.311000, qreg_3[0])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_1[0])
subcirc2.u(-0.251000,0.136000,-0.455000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_0[0])
subcirc3.cy(qreg_0[1],qreg_2[1])
subcirc3.z(qreg_2[0])
subcirc3.z(qreg_2[1])
subcirc3.u(0.866000,-0.328000,0.010000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

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

main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.z(1)
		main_circ.u(0.767000,0.857000,-0.428000, 3)
		main_circ.append(subcirc0,[1,0,2,qreg_0[0]])
	with case_1(1):
		main_circ.id(3)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[0,2,3,1,qreg_0[0]])
	with case_1(1):
		main_circ.id(1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[0,3,qreg_0[0],1,2])
with else_1:
	main_circ.cy(2,0)
	main_circ.append(subcirc1,[0,2,qreg_0[0],3,1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cy(3,qreg_0[0])
		main_circ.barrier(0)
	with case_1(1):
		main_circ.cy(0,1)
		main_circ.u(-0.574000,param_0,param_1, 1)
		main_circ.append(subcirc1,[2,1,0,3,qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[1,0,qreg_0[0],2])
main_circ.z(qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[1,qreg_0[0],3,2,0])
	with case_1(1):
		main_circ.append(subcirc2,[0,qreg_0[0],1,3])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.id(2)
main_circ.rz(param_1, qreg_0[0])
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.rz(-0.369000, 1)
		main_circ.id(1)
bindings = {param_0: -0.661000, param_1: -0.034000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1367", "OptimizeCliffords")
