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
subcirc0.y(qreg_0[0])
subcirc0.u(pi/2,0.468000,-0.647000, qreg_0[2])
subcirc0.rx(-0.284000, qreg_0[3])
subcirc0.y(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.216000,0.595000, qreg_0[0])
subcirc1.u(pi/2,0.052000,-0.010000, qreg_3[0])
subcirc1.u(0,0,0.004000, qreg_0[0])
subcirc1.y(qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.y(2)
	main_circ.append(subcirc1,[2,0,3,1])
with else_1:
	main_circ.rx(0.522000, 1)
	main_circ.y(1)
	main_circ.append(subcirc1,[0,1,3,2])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0,param_3,0.498000, 3)
	main_circ.append(subcirc1,[2,3,0,1])
with else_1:
	main_circ.u(param_6,0,param_1, 0)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[0,3,1,2])
	main_circ.y(1)
with else_1:
	main_circ.append(subcirc1,[2,3,0,1])
main_circ.rx(-0.419000, 1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0,param_4,0.557000, 1)
	main_circ.barrier(3)
with else_1:
	main_circ.rx(param_0, 1)
	main_circ.y(0)
	main_circ.rx(-0.219000, 2)
	main_circ.u(param_2,param_1,-0.745000, 1)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_5,-0.982000,-0.894000, 0)
	main_circ.append(subcirc1,[0,2,1,3])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(3)
with else_1:
	main_circ.u(param_6,param_3,0.578000, 0)
	main_circ.u(pi/2,param_5,param_3, 1)
	main_circ.u(param_4,param_5,0.291000, 0)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc1,[0,3,1,2])
with else_1:
	main_circ.y(3)
	main_circ.append(subcirc1,[3,1,2,0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_5,-0.580000,0.164000, 1)
	main_circ.u(pi/2,0.794000,0.413000, 2)
	main_circ.u(param_0,-0.877000,param_6, 1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(pi/2,-0.935000,param_5, 1)
	main_circ.u(param_3,param_3,0.333000, 1)
	main_circ.u(param_0,param_3,-0.016000, 1)
	main_circ.u(param_4,param_4,-0.004000, 1)
with else_1:
	main_circ.u(pi/2,param_0,param_4, 0)
	main_circ.id(0)
main_circ.u(param_3,param_6,0.424000, 1)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(2)
	with case_1(1):
		main_circ.u(0,0,param_5, 2)
		main_circ.id(3)
bindings = {param_0: 0.499000, param_1: -0.450000, param_2: -0.770000, param_3: -0.787000, param_4: 0.023000, param_5: 0.170000, param_6: -0.023000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "14", "CollectCliffords")
