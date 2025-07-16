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
subcirc0.u(pi/2,0.159000,0.593000, qreg_2[0])
subcirc0.y(qreg_0[1])
subcirc0.u(0,0,0.148000, qreg_0[1])
subcirc0.cz(qreg_0[1],qreg_3[0])
subcirc0.cz(qreg_0[0],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[2],qreg_0[0])
subcirc1.y(qreg_3[0])
subcirc1.u(pi/2,0.868000,-0.839000, qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.u(pi/2,-0.061000,-0.773000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0,0,0.023000, qreg_0[0])
subcirc2.y(qreg_0[3])
subcirc2.cz(qreg_0[3],qreg_0[2])
subcirc2.u(0,0,-0.967000, qreg_0[1])
subcirc2.u(pi/2,-0.890000,0.192000, qreg_0[3])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(pi/2,-0.560000,-0.576000, qreg_0[3])
subcirc3.y(qreg_0[2])
subcirc3.y(qreg_0[2])
subcirc3.u(0,0,0.511000, qreg_0[3])
subcirc3.cz(qreg_0[1],qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.y(qreg_1[2])
subcirc4.u(pi/2,0.285000,-0.253000, qreg_1[1])
subcirc4.u(0,0,-0.110000, qreg_1[2])
subcirc4.y(qreg_1[0])
subcirc4.u(0,0,0.356000, qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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

main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0,param_2,param_3, qreg_0[0])
		main_circ.append(subcirc1,[1,qreg_0[0],2,0,3])
	with case_1(1):
		main_circ.append(subcirc4,[3,0,2,1])
main_circ.append(subcirc3,[3,qreg_0[0],2,1])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_1,-0.269000,0.530000, 3)
with else_1:
	main_circ.u(pi/2,0.408000,param_1, 0)
	main_circ.u(pi/2,-0.675000,0.175000, 0)
	main_circ.append(subcirc1,[2,1,3,0,qreg_0[0]])
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cz(2,3)
	main_circ.cz(1,0)
	main_circ.append(subcirc3,[0,3,2,1])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_0[0],0,1,2,3])
	with case_1(1):
		main_circ.cz(0,1)
		main_circ.cz(1,3)
		main_circ.cz(3,2)
		main_circ.cz(1,0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(0,0,param_2, qreg_0[0])
		main_circ.append(subcirc0,[2,3,0,1,qreg_0[0]])
	with case_1(1):
		main_circ.barrier(1)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,0,param_2, qreg_0[0])
		main_circ.cz(1,2)
		main_circ.u(param_0,0,param_2, 2)
		main_circ.id(3)
	with case_1(1):
		main_circ.id(1)
bindings = {param_0: 0.568000, param_1: -0.914000, param_2: 0.190000, param_3: 0.025000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "818")
