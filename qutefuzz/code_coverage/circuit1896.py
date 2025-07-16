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
subcirc0.cy(qreg_0[2],qreg_3[0])
subcirc0.cy(qreg_0[1],qreg_3[0])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.rx(0.454000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
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

main_circ.measure(qreg_0[3], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.append(subcirc0,[qreg_0[3],1,0,qreg_0[0],qreg_0[1],qreg_0[2]])
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(-0.013000,-0.436000,param_5, 1)
			main_circ.s(1)
			main_circ.s(qreg_0[3])
			main_circ.s(qreg_0[3])
	with else_2:
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(param_3,param_4,param_5, qreg_0[1])
			main_circ.cy(1,qreg_0[3])
			main_circ.u(param_4,0.889000,0.096000, qreg_0[0])
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(param_3,param_5,param_1, qreg_0[0])
			main_circ.rx(param_5, qreg_0[0])
			main_circ.cy(qreg_0[3],qreg_0[2])
			main_circ.u(-0.876000,param_2,-0.783000, 1)
		with else_1:
			main_circ.cy(qreg_0[2],qreg_0[0])
			main_circ.cy(qreg_0[0],qreg_0[1])
			main_circ.rx(param_2, 1)
with else_3:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rx(0.462000, 1)
		with else_1:
			main_circ.cy(qreg_0[2],1)
			main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[0],qreg_0[3],1,qreg_0[1]])
	with else_2:
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cy(qreg_0[0],qreg_0[1])
			main_circ.append(subcirc0,[qreg_0[2],0,qreg_0[0],qreg_0[3],qreg_0[1],1])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(0.148000,param_0,param_0, qreg_0[1])
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[3], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.rx(0.899000, qreg_0[1])
				main_circ.u(0.527000,param_5,param_4, qreg_0[2])
				main_circ.cy(qreg_0[3],1)
				main_circ.rx(param_2, qreg_0[1])
			with case_1(1):
				main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],0,qreg_0[2],qreg_0[3],1])
	with else_2:
		main_circ.rx(0.991000, 0)
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_3,-0.261000,param_2, qreg_0[1])
				main_circ.rx(param_1, qreg_0[1])
				main_circ.rx(param_0, qreg_0[0])
		with else_2:
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.append(subcirc0,[0,1,qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
	with case_3(1):
		main_circ.s(0)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_2:
			main_circ.cy(qreg_0[1],qreg_0[3])
		with else_2:
			main_circ.measure(qreg_0[2], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.rx(0.540000, 1)
				main_circ.append(subcirc0,[qreg_0[2],1,qreg_0[1],0,qreg_0[3],qreg_0[0]])
			with else_1:
				main_circ.barrier(qreg_0[3])
bindings = {param_0: -0.459000, param_1: -0.592000, param_2: -0.765000, param_3: -0.188000, param_4: -0.041000, param_5: 0.283000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1896", "OptimizeCliffords")
