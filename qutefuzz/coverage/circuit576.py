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
subcirc0.y(qreg_1[1])
subcirc0.rz(-0.858000, qreg_1[0])
subcirc0.u(pi/2,-0.622000,-0.699000, qreg_0[0])
subcirc0.y(qreg_1[0])
subcirc0.rz(-0.928000, qreg_1[1])
subcirc0.y(qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.958000,-0.046000, qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1.y(qreg_0[1])
subcirc1.y(qreg_0[0])
subcirc1.rz(-0.645000, qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.631000,0.770000, qreg_3[0])
subcirc2.s(qreg_0[0])
subcirc2.u(pi/2,-0.992000,0.113000, qreg_0[1])
subcirc2.s(qreg_0[0])
subcirc2.u(pi/2,-0.147000,-0.924000, qreg_3[0])
subcirc2.s(qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_1[1])
subcirc3.rz(-0.180000, qreg_0[0])
subcirc3.rz(-0.663000, qreg_3[0])
subcirc3.s(qreg_0[0])
subcirc3.rz(0.060000, qreg_0[0])
subcirc3.y(qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(0.980000, qreg_0[0])
subcirc4.s(qreg_0[0])
subcirc4.y(qreg_0[0])
subcirc4.u(pi/2,0.482000,0.223000, qreg_0[1])
subcirc4.y(qreg_0[2])
subcirc4.y(qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.s(2)
	main_circ.s(qreg_0[1])
with else_1:
	main_circ.append(subcirc3,[qreg_0[0],1,0,qreg_0[1]])
main_circ.append(subcirc1,[qreg_0[1],0,2,3,qreg_0[0],1])
main_circ.append(subcirc3,[qreg_0[1],2,qreg_0[0],1])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.s(2)
		main_circ.append(subcirc3,[2,qreg_0[0],3,0])
	with case_1(1):
		main_circ.u(param_3,0.305000,-0.326000, 2)
		main_circ.u(pi/2,-0.383000,0.190000, qreg_0[0])
		main_circ.append(subcirc1,[3,2,0,qreg_0[1],qreg_0[0],1])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[1,2,0,qreg_0[1]])
	with case_1(1):
		main_circ.append(subcirc4,[2,qreg_0[0],3,qreg_0[1],0])
main_circ.y(0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[1,2,qreg_0[1],0])
bindings = {param_3: 0.824000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "576")
