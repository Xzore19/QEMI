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
subcirc0.h(qreg_3[0])
subcirc0.cx(qreg_0[1],qreg_2[0])
subcirc0.h(qreg_0[1])
subcirc0.h(qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(pi/2,0.971000,param_2, 2)
	main_circ.append(subcirc0,[0,3,1,2])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cx(3,1)
	main_circ.h(1)
	main_circ.h(0)
	main_circ.rz(0.397000, 1)
	main_circ.h(1)
main_circ.rz(param_0, 3)
main_circ.h(3)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(0.202000, 1)
		main_circ.h(3)
		main_circ.append(subcirc0,[2,0,3,1])
	with case_1(1):
		main_circ.cx(0,3)
		main_circ.cx(2,0)
		main_circ.append(subcirc0,[3,2,0,1])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc0,[3,0,1,2])
with else_1:
	main_circ.cx(2,3)
	main_circ.h(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.h(3)
	main_circ.u(param_2,param_1,param_1, 0)
	main_circ.rz(-0.005000, 2)
	main_circ.cx(3,0)
main_circ.rz(param_1, 1)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.h(2)
	main_circ.u(pi/2,-0.363000,param_0, 3)
main_circ.u(pi/2,0.227000,param_1, 3)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc0,[0,3,1,2])
with else_1:
	main_circ.cx(0,3)
	main_circ.cx(0,1)
	main_circ.cx(0,2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(3,2)
	main_circ.cx(2,0)
	main_circ.cx(2,0)
	main_circ.cx(2,0)
with else_1:
	main_circ.h(2)
	main_circ.cx(0,1)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.rz(param_2, 1)
	main_circ.rz(-0.674000, 2)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(param_2, 3)
	main_circ.h(3)
with else_1:
	main_circ.barrier(1)
main_circ.u(pi/2,0.865000,param_1, 1)
main_circ.u(pi/2,0.026000,0.960000, 0)
bindings = {param_0: 0.304000, param_1: 0.341000, param_2: 0.554000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "421", "RemoveFinalReset")
