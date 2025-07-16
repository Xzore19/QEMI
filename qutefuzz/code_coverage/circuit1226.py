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
subcirc0.cz(qreg_1[0],qreg_1[1])
subcirc0.rx(-0.377000, qreg_1[2])
subcirc0.u(0,0,-0.538000, qreg_1[1])
subcirc0.z(qreg_1[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,0.191000, qreg_2[0])
subcirc1.cz(qreg_2[0],qreg_0[0])
subcirc1.z(qreg_0[0])
subcirc1.u(0,0,-0.586000, qreg_2[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.z(0)
	main_circ.append(subcirc1,[qreg_0[1],0,2,qreg_0[0]])
with else_1:
	main_circ.append(subcirc0,[2,1,3,qreg_0[0]])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rx(param_1, qreg_0[1])
	main_circ.cz(3,1)
	main_circ.z(0)
	main_circ.append(subcirc1,[1,0,qreg_0[1],2])
main_circ.u(param_1,0,0.069000, qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[2,0,1,3])
	with case_1(1):
		main_circ.rx(0.786000, 2)
		main_circ.append(subcirc1,[0,2,1,qreg_0[1]])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0,0,param_1, qreg_0[0])
		main_circ.u(0,param_1,0.440000, qreg_0[0])
		main_circ.u(0,param_1,param_0, 1)
		main_circ.append(subcirc0,[1,2,qreg_0[1],0])
	with case_1(1):
		main_circ.cz(1,2)
		main_circ.cz(0,qreg_0[1])
		main_circ.cz(2,3)
		main_circ.cz(2,qreg_0[1])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cz(0,qreg_0[1])
	main_circ.append(subcirc1,[0,qreg_0[1],1,2])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(param_0, 3)
		main_circ.id(qreg_0[0])
	with case_1(1):
		main_circ.barrier(qreg_0[1])
bindings = {param_0: 0.781000, param_1: -0.362000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1226", "HoareOptimizer")
