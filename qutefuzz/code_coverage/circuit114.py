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
subcirc0.u(0,0,-0.269000, qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.u(pi/2,-0.081000,-0.504000, qreg_2[1])
subcirc0.cx(qreg_0[1],qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_3[0])
subcirc1.u(pi/2,0.587000,-0.787000, qreg_0[1])
subcirc1.u(pi/2,0.082000,0.691000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,-0.537000, qreg_0[1])
subcirc2.u(0,0,0.533000, qreg_0[2])
subcirc2.z(qreg_0[3])
subcirc2.u(pi/2,-0.878000,-0.845000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(0)
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

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[0],qreg_3[0]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_3[0])
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.u(pi/2,param_1,param_0, qreg_3[0])
		main_circ.cx(qreg_0[1],qreg_2[0])
		main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_0[1])
		main_circ.cx(qreg_2[0],qreg_0[1])
		main_circ.z(qreg_3[0])
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.u(pi/2,0.686000,param_1, qreg_0[1])
		main_circ.barrier(qreg_3[0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_2[0]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_2[0])
main_circ.u(param_1,param_1,param_0, qreg_2[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],qreg_2[0],qreg_3[0]])
with else_1:
	main_circ.barrier(qreg_2[0])
main_circ.z(qreg_3[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(qreg_2[0])
	main_circ.z(qreg_2[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.z(qreg_2[0])
	main_circ.u(0,0,0.026000, qreg_0[1])
	main_circ.z(qreg_3[0])
with else_1:
	main_circ.z(qreg_3[0])
	main_circ.u(0,param_0,0.691000, qreg_0[0])
main_circ.cx(qreg_2[0],qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_3[0]])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(0,param_0,0.737000, qreg_0[1])
	main_circ.u(param_1,param_1,-0.209000, qreg_2[0])
	main_circ.append(subcirc0,[qreg_0[0],qreg_3[0],qreg_0[1],qreg_2[0]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cx(qreg_0[1],qreg_2[0])
		main_circ.cx(qreg_0[1],qreg_2[0])
		main_circ.cx(qreg_3[0],qreg_0[0])
		main_circ.cx(qreg_3[0],qreg_2[0])
	with case_1(1):
		main_circ.cx(qreg_3[0],qreg_0[1])
		main_circ.cx(qreg_3[0],qreg_2[0])
		main_circ.cx(qreg_0[0],qreg_3[0])
		main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_3[0],qreg_0[1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(qreg_2[0])
with else_1:
	main_circ.barrier(qreg_0[0])
main_circ.cx(qreg_3[0],qreg_0[1])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,0,param_0, qreg_0[0])
		main_circ.u(pi/2,-0.833000,param_1, qreg_2[0])
		main_circ.u(param_1,param_0,-0.133000, qreg_0[1])
		main_circ.u(param_1,0,-0.762000, qreg_0[1])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.493000, param_1: -0.621000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "114", "InverseCancellation")
