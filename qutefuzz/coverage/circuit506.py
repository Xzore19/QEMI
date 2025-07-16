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
subcirc0.u(0,0,0.706000, qreg_0[2])
subcirc0.rz(0.279000, qreg_0[2])
subcirc0.u(0,0,0.795000, qreg_0[2])
subcirc0.h(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,0.301000, qreg_0[2])
subcirc1.z(qreg_0[2])
subcirc1.rz(0.748000, qreg_0[2])
subcirc1.rz(-0.526000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.148000, qreg_2[0])
subcirc2.rz(-0.938000, qreg_0[1])
subcirc2.u(0,0,-0.788000, qreg_3[0])
subcirc2.rz(-0.553000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(3)

main_circ = QuantumCircuit(1)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],qreg_0[0],qreg_2[0]])
main_circ.measure(qreg_2[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(0)
	with case_1(1):
		main_circ.rz(param_2, qreg_3[0])
		main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_2[0],qreg_3[0]])
main_circ.append(subcirc1,[qreg_2[0],0,qreg_0[0],qreg_0[1]])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.z(qreg_2[0])
		main_circ.z(0)
		main_circ.h(qreg_0[0])
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.z(qreg_2[0])
		main_circ.u(param_2,param_2,param_2, qreg_2[0])
		main_circ.rz(param_5, qreg_3[0])
		main_circ.h(0)
main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_3[0],0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[qreg_2[0],0,qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],0,qreg_3[0],qreg_0[1]])
with else_1:
	main_circ.rz(param_2, 0)
	main_circ.z(0)
	main_circ.rz(-0.426000, qreg_0[1])
	main_circ.z(qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(qreg_0[0])
	main_circ.h(qreg_0[0])
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(0)
	main_circ.h(qreg_0[1])
	main_circ.rz(param_1, 0)
	main_circ.rz(-0.633000, qreg_3[0])
	main_circ.barrier(qreg_3[0])
with else_1:
	main_circ.u(param_3,0,param_0, 0)
	main_circ.z(qreg_0[0])
	main_circ.u(0,0,param_2, qreg_2[0])
	main_circ.z(qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_2[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(0)
with else_1:
	main_circ.barrier(0)
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_5, qreg_2[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(param_5, qreg_2[0])
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.986000, param_1: -0.134000, param_2: 0.688000, param_3: -0.091000, param_5: -0.230000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "506", "CommutationAnalysis")
