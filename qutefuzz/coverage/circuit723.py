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
subcirc0.x(qreg_3[0])
subcirc0.cz(qreg_0[0],qreg_3[0])
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_3[0])
subcirc0.x(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cz(qreg_0[1],qreg_2[1])
subcirc1.u(0.491000,0.227000,-0.632000, qreg_0[1])
subcirc1.rz(0.622000, qreg_2[0])
subcirc1.x(qreg_2[1])
subcirc1.rz(0.664000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.450000,0.470000,-0.743000, qreg_0[2])
subcirc2.x(qreg_0[2])
subcirc2.u(-0.890000,-0.967000,-0.193000, qreg_0[2])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.x(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.x(qreg_2[1])
subcirc3.cz(qreg_0[1],qreg_2[0])
subcirc3.cz(qreg_2[1],qreg_0[0])
subcirc3.cz(qreg_0[1],qreg_0[0])
subcirc3.x(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.x(qreg_0[1])
subcirc4.u(0.636000,0.120000,0.766000, qreg_0[0])
subcirc4.rz(-0.573000, qreg_2[0])
subcirc4.rz(-0.137000, qreg_0[1])
subcirc4.cz(qreg_0[1],qreg_0[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(0,qreg_0[0])
	main_circ.append(subcirc2,[0,qreg_0[0],qreg_1[0],qreg_1[2]])
with else_1:
	main_circ.u(0.189000,param_3,0.590000, qreg_1[2])
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_1[2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.id(0)
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(qreg_1[2])
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.id(qreg_0[0])
with else_1:
	main_circ.barrier(qreg_1[1])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(qreg_0[0])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.id(0)
	with case_1(1):
		main_circ.id(qreg_1[0])
main_circ.measure(qreg_1[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(qreg_1[0])
with else_1:
	main_circ.x(qreg_0[0])
	main_circ.cz(qreg_1[2],0)
	main_circ.cz(qreg_1[0],0)
	main_circ.cz(qreg_0[0],0)
	main_circ.id(qreg_0[0])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_0[0],qreg_1[1])
main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc4,[qreg_1[2],qreg_1[0],0,qreg_1[1]])
main_circ.measure(qreg_1[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[qreg_1[2],0,qreg_1[1],qreg_1[0]])
	with case_1(1):
		main_circ.u(0.786000,0.520000,param_1, qreg_1[2])
		main_circ.append(subcirc2,[qreg_0[0],qreg_1[1],qreg_1[2],qreg_1[0]])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc4,[qreg_1[1],qreg_0[0],0,qreg_1[2]])
	with case_1(1):
		main_circ.cz(qreg_1[1],0)
		main_circ.cz(0,qreg_1[1])
		main_circ.cz(0,qreg_1[0])
		main_circ.append(subcirc4,[qreg_1[1],qreg_0[0],qreg_1[2],0])
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(0.611000,param_2,0.179000, qreg_0[0])
	main_circ.x(qreg_1[2])
	main_circ.barrier(qreg_1[2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_1[0])
main_circ.rz(0.683000, qreg_1[2])
main_circ.measure(qreg_1[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.x(0)
		main_circ.barrier(qreg_1[0])
	with case_1(1):
		main_circ.barrier(qreg_1[1])
bindings = {param_1: 0.449000, param_2: 0.322000, param_3: -0.985000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "723")
