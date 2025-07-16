from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rx(-0.107000, qreg_0[1])
subcirc0.u(-0.533000,-0.026000,0.184000, qreg_0[2])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_3[0])
subcirc0.y(qreg_0[1])
subcirc0.u(0.031000,-0.777000,-0.545000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.y(qreg_0[0])
subcirc1.rx(0.881000, qreg_2[1])
subcirc1.u(0.978000,-0.677000,-0.572000, qreg_0[0])
subcirc1.y(qreg_2[1])
subcirc1.u(0.782000,-0.444000,-0.875000, qreg_2[1])
subcirc1.u(0.964000,0.478000,-0.208000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.y(qreg_2[0])
subcirc2.rx(-0.273000, qreg_2[0])
subcirc2.u(-0.764000,-0.796000,0.050000, qreg_2[0])
subcirc2.u(0.662000,0.682000,-0.063000, qreg_0[1])
subcirc2.s(qreg_2[0])
subcirc2.s(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.rx(-0.174000, qreg_0[0])
subcirc3.y(qreg_0[1])
subcirc3.rx(0.152000, qreg_2[0])
subcirc3.s(qreg_0[1])
subcirc3.u(-0.347000,-0.162000,-0.069000, qreg_2[1])
subcirc3.u(-0.504000,0.213000,-0.597000, qreg_2[0])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
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

main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.u(-0.564000,-0.823000,param_2, qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
	with case_1(1):
		main_circ.rx(0.486000, qreg_0[1])
		main_circ.barrier(qreg_0[3])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[3],qreg_0[0]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_2,param_2,param_1, qreg_0[1])
	main_circ.rx(-0.915000, qreg_0[0])
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.y(qreg_0[2])
	main_circ.append(subcirc3,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(0.476000,0.243000,param_1, qreg_0[3])
with else_1:
	main_circ.u(param_1,0.846000,param_0, qreg_0[1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(0.373000,param_1,0.813000, qreg_0[1])
with else_1:
	main_circ.id(qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rx(param_2, qreg_0[2])
	main_circ.rx(param_1, qreg_0[1])
	main_circ.append(subcirc2,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.rx(param_2, qreg_0[0])
	main_circ.barrier(qreg_0[3])
with else_1:
	main_circ.barrier(qreg_0[0])
bindings = {param_0: 0.592000, param_1: 0.987000, param_2: -0.386000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "216")
