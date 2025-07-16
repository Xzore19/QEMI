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
subcirc0.u(pi/2,-0.716000,0.643000, qreg_0[0])
subcirc0.x(qreg_1[1])
subcirc0.u(pi/2,0.931000,0.340000, qreg_3[0])
subcirc0.h(qreg_1[1])
subcirc0.u(pi/2,-0.775000,0.582000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0,0,-0.072000, qreg_0[2])
subcirc1.x(qreg_0[2])
subcirc1.x(qreg_0[0])
subcirc1.h(qreg_0[1])
subcirc1.h(qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.h(qreg_2[0])
subcirc2.u(pi/2,-0.097000,-0.272000, qreg_2[0])
subcirc2.u(pi/2,0.166000,0.246000, qreg_1[0])
subcirc2.x(qreg_3[0])
subcirc2.u(0,0,-0.975000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.u(0,0,-0.379000, qreg_3[0])
subcirc3.u(pi/2,-0.421000,0.467000, qreg_3[0])
subcirc3.h(qreg_3[0])
subcirc3.h(qreg_0[2])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.x(qreg_1[0])
subcirc4.x(qreg_0[0])
subcirc4.x(qreg_1[2])
subcirc4.h(qreg_0[0])
subcirc4.h(qreg_1[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(pi/2,0.066000,param_0, 0)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[2,3,1,qreg_0[0]])
	with case_1(1):
		main_circ.u(0,0,param_2, 2)
		main_circ.u(param_1,param_2,param_1, 2)
		main_circ.x(3)
		main_circ.u(pi/2,param_0,0.397000, 2)
main_circ.u(pi/2,param_0,-0.741000, 2)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[3,1,0,2])
	with case_1(1):
		main_circ.h(3)
		main_circ.u(pi/2,0.633000,param_0, 2)
		main_circ.u(param_1,param_1,param_0, 3)
		main_circ.append(subcirc2,[0,qreg_0[0],3,1])
main_circ.u(param_1,0.396000,0.279000, 3)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc4,[3,0,2,1])
main_circ.append(subcirc1,[0,3,1,2])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(3)
	with case_1(1):
		main_circ.h(1)
		main_circ.barrier(3)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc0,[2,0,1,qreg_0[0]])
with else_1:
	main_circ.u(0,param_1,-0.081000, qreg_0[0])
	main_circ.id(2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(2)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_0[0])
	with case_1(1):
		main_circ.id(3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,-0.814000,param_1, qreg_0[0])
with else_1:
	main_circ.u(param_1,param_1,param_1, qreg_0[0])
	main_circ.h(1)
	main_circ.id(1)
bindings = {param_0: 0.694000, param_1: -0.119000, param_2: 0.401000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "885")
