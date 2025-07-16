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
subcirc0.u(pi/2,0.080000,-0.932000, qreg_3[0])
subcirc0.u(pi/2,-0.484000,0.910000, qreg_2[0])
subcirc0.ry(1.000000, qreg_0[0])
subcirc0.y(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(-0.739000, qreg_0[1])
subcirc1.y(qreg_0[3])
subcirc1.ry(-0.664000, qreg_0[2])
subcirc1.ry(-0.441000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(qreg_0[0])
	main_circ.u(pi/2,0.291000,0.290000, qreg_1[0])
with else_1:
	main_circ.append(subcirc1,[1,0,3,qreg_0[0]])
	main_circ.y(qreg_0[0])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[0,1,qreg_0[0],2])
main_circ.z(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,param_0,param_0, 1)
with else_1:
	main_circ.id(1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(-0.321000, 3)
	main_circ.ry(-0.851000, qreg_1[0])
with else_1:
	main_circ.append(subcirc1,[0,qreg_1[0],qreg_0[0],1])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.z(2)
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[2,0,qreg_0[0],qreg_1[0]])
	with case_1(1):
		main_circ.ry(-0.635000, 2)
		main_circ.z(0)
		main_circ.u(param_0,-0.217000,0.402000, qreg_1[0])
		main_circ.y(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[3,0,1,2])
with else_1:
	main_circ.u(pi/2,param_0,0.018000, 3)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(param_0, 3)
with else_1:
	main_circ.y(2)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.z(2)
	main_circ.u(param_0,-0.895000,-0.655000, qreg_1[0])
	main_circ.z(2)
	main_circ.y(0)
with else_1:
	main_circ.z(qreg_1[0])
main_circ.measure(qreg_1[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.y(qreg_0[0])
	main_circ.y(qreg_0[0])
	main_circ.barrier(1)
bindings = {param_0: -0.693000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1011", "CommutationAnalysis")
