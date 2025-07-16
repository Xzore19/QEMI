from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.s(qreg_1[0])
subcirc0.z(qreg_0[0])
subcirc0.s(qreg_1[0])
subcirc0.u(pi/2,0.483000,0.426000, qreg_0[0])
subcirc0.z(qreg_1[1])
subcirc0.s(qreg_1[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[2],qreg_0[1])
subcirc1.u(pi/2,0.999000,-0.397000, qreg_0[1])
subcirc1.cz(qreg_0[1],qreg_0[3])
subcirc1.cz(qreg_0[0],qreg_0[3])
subcirc1.z(qreg_0[2])
subcirc1.cz(qreg_0[3],qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.683000,-0.729000, qreg_0[2])
subcirc2.s(qreg_0[2])
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.s(qreg_0[0])
subcirc2.z(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.s(qreg_1[1])
subcirc3.cz(qreg_1[2],qreg_1[0])
subcirc3.cz(qreg_1[1],qreg_1[0])
subcirc3.z(qreg_1[2])
subcirc3.z(qreg_0[0])
subcirc3.z(qreg_1[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
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
param_4 = Parameter("param_4")

main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[1],qreg_0[3])
		main_circ.barrier(qreg_0[2])
	with case_1(1):
		main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(qreg_0[3],qreg_0[0])
	main_circ.z(0)
with else_1:
	main_circ.s(0)
	main_circ.append(subcirc2,[qreg_0[1],0,qreg_0[3],qreg_0[2]])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cz(qreg_0[3],qreg_0[2])
		main_circ.cz(0,qreg_0[2])
		main_circ.id(qreg_0[2])
	with case_1(1):
		main_circ.s(qreg_0[0])
		main_circ.id(qreg_0[3])
main_circ.u(pi/2,-0.950000,param_3, qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(0)
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(qreg_0[2],qreg_0[1])
	main_circ.u(param_1,-0.215000,param_4, 0)
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(qreg_0[2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(0)
	main_circ.cz(0,qreg_0[0])
	main_circ.s(0)
	main_circ.barrier(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(qreg_0[0],0)
	main_circ.s(qreg_0[1])
	main_circ.append(subcirc2,[0,qreg_0[2],qreg_0[3],qreg_0[1]])
with else_1:
	main_circ.cz(qreg_0[2],0)
main_circ.measure(qreg_0[3], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(qreg_0[1])
	main_circ.cz(qreg_0[2],qreg_0[0])
	main_circ.cz(qreg_0[0],0)
	main_circ.z(qreg_0[3])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(0,qreg_0[2])
with else_1:
	main_circ.barrier(qreg_0[2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.z(qreg_0[0])
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.id(qreg_0[2])
bindings = {param_1: 0.753000, param_3: 0.385000, param_4: -0.165000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1847", "OptimizeCliffords")
