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
subcirc0.ry(-0.632000, qreg_0[2])
subcirc0.ry(0.227000, qreg_0[0])
subcirc0.u(0.404000,0.307000,-0.146000, qreg_3[0])
subcirc0.u(-0.622000,0.508000,-0.035000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_3[0])
subcirc1.s(qreg_3[0])
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.u(-0.744000,-0.027000,0.296000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.append(subcirc0,[qreg_0[0],1,qreg_1[0],qreg_1[1],0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[qreg_0[0],qreg_1[0],0,qreg_1[1],1])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(param_5, qreg_0[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(-0.801000, 0)
	main_circ.s(0)
	main_circ.cy(qreg_1[0],qreg_1[1])
with else_1:
	main_circ.u(-0.200000,param_3,0.359000, 0)
	main_circ.append(subcirc0,[1,qreg_0[0],qreg_1[0],0,qreg_1[1]])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(0.354000, qreg_3[0])
	main_circ.u(-0.149000,param_0,0.673000, qreg_3[0])
	main_circ.ry(0.212000, qreg_3[0])
main_circ.s(qreg_3[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cy(qreg_1[1],qreg_3[0])
	main_circ.ry(0.125000, 1)
	main_circ.cy(qreg_3[0],1)
	main_circ.cy(qreg_1[0],qreg_3[0])
	main_circ.u(0.924000,param_5,param_1, qreg_0[0])
with else_1:
	main_circ.ry(0.433000, qreg_1[0])
	main_circ.u(param_1,param_0,param_2, qreg_0[0])
	main_circ.u(param_2,0.613000,param_2, qreg_0[0])
	main_circ.cy(1,qreg_1[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(0.706000,param_3,0.592000, 1)
		main_circ.cy(qreg_1[1],1)
		main_circ.ry(param_2, qreg_0[0])
		main_circ.cy(qreg_1[0],qreg_0[0])
	with case_1(1):
		main_circ.cy(qreg_3[0],0)
		main_circ.cy(qreg_1[1],0)
		main_circ.cy(qreg_1[1],qreg_0[0])
		main_circ.cy(1,qreg_1[0])
main_circ.measure(qreg_1[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cy(qreg_3[0],qreg_0[0])
	main_circ.cy(0,qreg_0[0])
	main_circ.cy(qreg_3[0],qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(param_5, qreg_0[0])
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.id(1)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(param_2, qreg_1[1])
		main_circ.id(1)
	with case_1(1):
		main_circ.cy(0,qreg_1[1])
		main_circ.cy(qreg_3[0],1)
		main_circ.s(qreg_3[0])
		main_circ.ry(param_0, qreg_3[0])
bindings = {param_0: 0.770000, param_1: 0.767000, param_2: 0.422000, param_3: 0.004000, param_5: -0.007000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "965", "ConsolidateBlocks")
