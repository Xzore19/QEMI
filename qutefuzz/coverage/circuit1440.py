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
subcirc0.u(0,0,0.348000, qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.u(0,0,0.357000, qreg_0[0])
subcirc0.cz(qreg_2[1],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.z(qreg_0[1])
subcirc1.cz(qreg_2[1],qreg_2[0])
subcirc1.u(0,0,-0.063000, qreg_2[0])
subcirc1.cy(qreg_0[0],qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cy(qreg_0[1],qreg_2[0])
subcirc2.u(0,0,0.238000, qreg_2[0])
subcirc2.cy(qreg_2[1],qreg_0[0])
subcirc2.z(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cy(qreg_0[3],qreg_0[1])
subcirc3.cz(qreg_0[1],qreg_0[2])
subcirc3.u(0,0,-0.625000, qreg_0[3])
subcirc3.u(0,0,0.379000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(2)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")
param_7 = Parameter("param_7")

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.barrier(2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_0[0])
	main_circ.barrier(2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[1,3,0,qreg_0[0]])
	with case_1(1):
		main_circ.u(param_7,0,param_1, 0)
		main_circ.cz(1,0)
		main_circ.z(1)
		main_circ.cy(1,qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[0],1)
		main_circ.barrier(3)
	with case_1(1):
		main_circ.id(3)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.cy(1,2)
		main_circ.barrier(3)
	with case_1(1):
		main_circ.cy(2,0)
		main_circ.cz(qreg_0[0],2)
		main_circ.u(0,param_0,0.432000, 2)
		main_circ.cy(2,qreg_0[0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(2)
	main_circ.u(0,param_1,param_4, 0)
	main_circ.cy(1,3)
	main_circ.cz(3,0)
	main_circ.barrier(0)
with else_1:
	main_circ.z(0)
	main_circ.z(0)
	main_circ.cy(0,2)
	main_circ.cz(qreg_0[0],0)
	main_circ.u(param_6,param_1,param_5, qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.z(3)
		main_circ.u(0,param_3,param_6, 2)
		main_circ.id(qreg_0[0])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(2)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc1,[0,1,2,qreg_0[0]])
	main_circ.barrier(2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[2,1,0,qreg_0[0]])
	main_circ.cy(2,3)
with else_1:
	main_circ.barrier(2)
main_circ.cy(qreg_0[0],0)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc1,[0,3,2,qreg_0[0]])
	main_circ.cy(1,3)
with else_1:
	main_circ.id(0)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(3,1)
	main_circ.cy(2,3)
	main_circ.id(0)
with else_1:
	main_circ.id(2)
bindings = {param_0: 0.216000, param_1: -0.129000, param_3: 0.120000, param_4: -0.013000, param_5: 0.372000, param_6: 0.621000, param_7: -0.006000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1440", "NormalizeRXAngle")
