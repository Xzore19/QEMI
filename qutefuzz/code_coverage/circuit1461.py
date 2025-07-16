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
subcirc0.rz(-0.003000, qreg_0[0])
subcirc0.u(pi/2,0.355000,0.191000, qreg_0[1])
subcirc0.z(qreg_0[2])
subcirc0.rz(-0.037000, qreg_0[3])
subcirc0.z(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,0.756000, qreg_2[1])
subcirc1.rz(-0.992000, qreg_0[0])
subcirc1.u(0,0,0.580000, qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.rz(-0.595000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.z(qreg_0[0])
subcirc2.rz(-0.548000, qreg_0[1])
subcirc2.rz(0.205000, qreg_0[1])
subcirc2.z(qreg_0[0])
subcirc2.z(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.u(pi/2,0.700000,0.466000, qreg_0[0])
subcirc3.z(qreg_0[0])
subcirc3.u(0,0,-0.781000, qreg_1[2])
subcirc3.u(pi/2,0.625000,0.233000, qreg_0[0])
subcirc3.rz(-0.462000, qreg_1[2])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(pi/2,-0.234000,0.348000, qreg_0[0])
subcirc4.u(0,0,0.837000, qreg_3[0])
subcirc4.z(qreg_0[2])
subcirc4.u(pi/2,0.948000,0.029000, qreg_3[0])
subcirc4.rz(0.497000, qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
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
param_3 = Parameter("param_3")

main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc3,[qreg_0[0],qreg_2[0],0,qreg_3[0],qreg_1[0]])
with else_1:
	main_circ.append(subcirc4,[qreg_0[0],qreg_1[0],0,qreg_2[0]])
main_circ.u(param_1,param_3,0.203000, qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc3,[qreg_2[0],0,qreg_3[0],qreg_1[0],qreg_0[0]])
	with case_1(1):
		main_circ.rz(-0.422000, qreg_0[0])
		main_circ.rz(param_2, qreg_2[0])
		main_circ.barrier(qreg_0[0])
main_circ.rz(param_0, qreg_3[0])
main_circ.u(param_2,param_1,0.339000, qreg_3[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_2[0])
	with case_1(1):
		main_circ.append(subcirc4,[qreg_3[0],qreg_0[0],0,qreg_2[0]])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_2, qreg_0[0])
	main_circ.z(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(0)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc3,[0,qreg_3[0],qreg_1[0],qreg_2[0],qreg_0[0]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],qreg_2[0],0,qreg_3[0]])
with else_1:
	main_circ.u(pi/2,param_0,param_0, 0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_2[0])
		main_circ.id(0)
	with case_1(1):
		main_circ.append(subcirc1,[qreg_1[0],qreg_3[0],qreg_2[0],qreg_0[0]])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.z(0)
with else_1:
	main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.barrier(0)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(param_1, qreg_1[0])
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_1[0])
	with case_1(1):
		main_circ.u(param_0,0,-0.938000, 0)
		main_circ.barrier(qreg_1[0])
bindings = {param_0: 0.767000, param_1: 0.455000, param_2: 0.526000, param_3: -0.917000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1461")
