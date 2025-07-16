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
subcirc0.u(0.941000,-0.670000,0.037000, qreg_0[0])
subcirc0.s(qreg_1[1])
subcirc0.z(qreg_1[0])
subcirc0.s(qreg_3[0])
subcirc0.z(qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.426000,0.950000,0.577000, qreg_2[0])
subcirc1.z(qreg_1[0])
subcirc1.u(0.686000,0.996000,-0.554000, qreg_0[0])
subcirc1.z(qreg_2[0])
subcirc1.z(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[1])
subcirc2.s(qreg_0[3])
subcirc2.u(-0.897000,0.572000,0.221000, qreg_0[2])
subcirc2.cz(qreg_0[3],qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

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

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,param_1,param_1, qreg_0[0])
		main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
	with case_1(1):
		main_circ.append(subcirc0,[qreg_3[0],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_0[2],0)
	main_circ.z(qreg_0[1])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_3[0])
	main_circ.u(-0.554000,param_1,-0.282000, qreg_3[0])
with else_1:
	main_circ.z(qreg_3[0])
	main_circ.barrier(qreg_0[1])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,param_0,param_0, qreg_0[2])
		main_circ.append(subcirc0,[0,qreg_0[2],qreg_3[0],qreg_0[0]])
	with case_1(1):
		main_circ.s(qreg_3[0])
		main_circ.append(subcirc1,[qreg_0[1],qreg_3[0],0,qreg_0[0]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.s(qreg_0[1])
with else_1:
	main_circ.cz(qreg_0[1],0)
	main_circ.append(subcirc1,[qreg_0[2],0,qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(qreg_0[0],qreg_0[1])
	main_circ.cz(0,qreg_0[1])
main_circ.cz(qreg_0[2],0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_0[1],qreg_0[0])
	main_circ.cz(qreg_0[2],0)
	main_circ.cz(qreg_0[2],qreg_0[1])
	main_circ.cz(0,qreg_0[0])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cz(qreg_3[0],qreg_0[2])
	main_circ.barrier(qreg_3[0])
with else_1:
	main_circ.id(qreg_3[0])
bindings = {param_0: 0.567000, param_1: 0.668000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1221", "RemoveResetInZeroState")
