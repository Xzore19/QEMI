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
subcirc0.y(qreg_0[0])
subcirc0.u(0,0,-0.273000, qreg_0[3])
subcirc0.z(qreg_0[2])
subcirc0.u(0,0,0.441000, qreg_0[0])
subcirc0.z(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[0])
subcirc1.u(pi/2,-0.974000,-0.175000, qreg_2[0])
subcirc1.z(qreg_0[0])
subcirc1.u(0,0,0.531000, qreg_1[0])
subcirc1.u(pi/2,0.775000,-0.880000, qreg_0[0])
subcirc1.z(qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.u(0,0,-0.699000, qreg_0[0])
subcirc2.u(0,0,0.238000, qreg_2[1])
subcirc2.z(qreg_2[1])
subcirc2.u(pi/2,0.353000,-0.655000, qreg_0[1])
subcirc2.y(qreg_2[0])
subcirc2.u(pi/2,0.148000,0.073000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.z(qreg_0[0])
subcirc3.u(pi/2,0.143000,-0.151000, qreg_0[3])
subcirc3.z(qreg_0[3])
subcirc3.u(pi/2,0.562000,-0.770000, qreg_0[0])
subcirc3.u(pi/2,0.192000,-0.598000, qreg_0[0])
subcirc3.y(qreg_0[3])
subcirc3 = subcirc3.to_gate().control(2)

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

main_circ.append(subcirc2,[0,3,2,1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.u(pi/2,-0.444000,param_0, 0)
	main_circ.append(subcirc0,[0,1,qreg_0[0],3,2])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.barrier(2)
with else_1:
	main_circ.append(subcirc2,[2,qreg_0[0],3,0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc0,[3,qreg_0[0],0,2,1])
with else_1:
	main_circ.append(subcirc0,[0,qreg_0[0],3,1,2])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.z(1)
	main_circ.u(0,0,param_0, 2)
	main_circ.u(param_0,param_1,param_1, 2)
	main_circ.z(1)
with else_1:
	main_circ.y(qreg_0[0])
	main_circ.z(2)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],1,0,2,3])
	with case_1(1):
		main_circ.append(subcirc1,[3,1,qreg_0[0],0])
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,-0.850000,-0.331000, 2)
		main_circ.u(0,param_0,param_0, 0)
		main_circ.u(pi/2,param_0,param_0, 3)
		main_circ.append(subcirc0,[0,1,3,qreg_0[0],2])
	with case_1(1):
		main_circ.u(0,param_0,param_0, qreg_0[0])
		main_circ.barrier(0)
bindings = {param_0: -0.066000, param_1: -0.123000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1637", "ConsolidateBlocks")
