from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.u(pi/2,0.245000,0.986000, qreg_0[1])
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.u(0,0,0.492000, qreg_0[1])
subcirc0.u(0,0,-0.961000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.973000, qreg_2[0])
subcirc1.cz(qreg_0[1],qreg_2[0])
subcirc1.u(pi/2,0.191000,-0.512000, qreg_3[0])
subcirc1.u(0,0,0.423000, qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_0[1])
subcirc2.x(qreg_3[0])
subcirc2.cz(qreg_0[1],qreg_0[0])
subcirc2.cz(qreg_0[2],qreg_0[0])

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
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.append(subcirc2,[qreg_0[0],0,1,2])
main_circ.append(subcirc2,[1,qreg_1[0],3,2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[1,3,2,0,qreg_0[0],qreg_1[0]])
with else_1:
	main_circ.cz(0,3)
	main_circ.append(subcirc2,[1,2,qreg_0[0],3])
main_circ.cz(0,2)
main_circ.append(subcirc0,[1,qreg_0[0],qreg_1[0],3])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[0,1,qreg_0[0],qreg_1[0]])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0,param_5,param_1, 2)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.u(param_3,0,param_5, qreg_1[0])
		main_circ.append(subcirc1,[qreg_1[0],0,1,2,3,qreg_0[0]])
	with case_1(1):
		main_circ.x(3)
		main_circ.u(param_0,0,param_0, qreg_1[0])
		main_circ.cz(qreg_0[0],0)
		main_circ.cz(qreg_0[0],1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc0,[1,3,qreg_0[0],2])
with else_1:
	main_circ.cz(qreg_0[0],2)
	main_circ.cz(qreg_1[0],qreg_0[0])
	main_circ.append(subcirc0,[3,0,qreg_1[0],2])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cz(3,qreg_0[0])
with else_1:
	main_circ.x(3)
main_circ.cz(2,0)
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_1,0.150000,0.719000, 0)
		main_circ.cz(0,1)
		main_circ.cz(2,3)
		main_circ.append(subcirc2,[2,qreg_1[0],3,0])
	with case_1(1):
		main_circ.barrier(qreg_1[0])
main_circ.u(param_5,0,param_0, qreg_0[0])
bindings = {param_0: 0.585000, param_1: 0.243000, param_3: 0.572000, param_5: -0.597000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1555")
