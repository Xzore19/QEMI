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
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.z(qreg_0[2])
subcirc0.rz(-0.386000, qreg_0[1])
subcirc0.u(0,0,0.521000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cz(qreg_2[0],qreg_2[1])
subcirc1.rz(0.824000, qreg_2[0])
subcirc1.cz(qreg_0[1],qreg_2[0])
subcirc1.cz(qreg_2[1],qreg_0[1])
subcirc1.u(0,0,0.206000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.u(0,0,0.129000, qreg_0[1])
subcirc2.cz(qreg_2[0],qreg_0[0])
subcirc2.z(qreg_2[0])
subcirc2.rz(0.916000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[0],qreg_0[2])
subcirc3.cz(qreg_0[3],qreg_0[0])
subcirc3.rz(-0.420000, qreg_0[1])
subcirc3.u(0,0,-0.361000, qreg_0[3])
subcirc3.cz(qreg_0[1],qreg_0[2])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_2[1]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc3,[qreg_2[1],qreg_0[0],qreg_2[0],qreg_0[1]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(param_0, qreg_2[1])
	main_circ.rz(param_0, qreg_2[1])
	main_circ.id(qreg_2[0])
with else_1:
	main_circ.u(0,param_0,param_0, qreg_0[0])
	main_circ.barrier(qreg_2[1])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_2[1],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],qreg_2[1],qreg_0[0]])
	with case_1(1):
		main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_0[1],qreg_2[1]])
main_circ.measure(qreg_2[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_2[0])
	with case_1(1):
		main_circ.id(qreg_2[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[1],qreg_2[0])
		main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_2[1],qreg_0[1]])
	with case_1(1):
		main_circ.u(0,param_0,param_0, qreg_2[0])
		main_circ.cz(qreg_0[1],qreg_2[1])
		main_circ.cz(qreg_0[0],qreg_0[1])
		main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_2[0],qreg_2[1])
		main_circ.cz(qreg_0[0],qreg_2[1])
		main_circ.cz(qreg_2[1],qreg_0[1])
		main_circ.cz(qreg_2[0],qreg_2[1])
	with case_1(1):
		main_circ.id(qreg_0[1])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rz(-0.539000, qreg_0[0])
	main_circ.id(qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_2[1])
with else_1:
	main_circ.id(qreg_0[1])
main_circ.u(param_0,0,0.455000, qreg_0[1])
main_circ.cz(qreg_2[0],qreg_0[0])
bindings = {param_0: -0.779000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "940", "ResetAfterMeasureSimplification")
