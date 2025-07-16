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
subcirc0.rz(0.261000, qreg_1[1])
subcirc0.rz(0.611000, qreg_3[0])
subcirc0.h(qreg_3[0])
subcirc0.h(qreg_1[0])
subcirc0.u(0.402000,0.720000,-0.078000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.160000, qreg_0[0])
subcirc1.rz(-0.608000, qreg_0[3])
subcirc1.rz(-0.136000, qreg_0[1])
subcirc1.h(qreg_0[0])
subcirc1.u(pi/2,0.681000,0.160000, qreg_0[1])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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
param_6 = Parameter("param_6")

main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_2[0]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rz(-0.633000, qreg_0[0])
		main_circ.u(pi/2,param_3,0.780000, qreg_0[1])
		main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_2[0]])
	with case_1(1):
		main_circ.rz(0.304000, qreg_0[1])
		main_circ.rz(-0.650000, qreg_2[0])
		main_circ.rz(param_0, qreg_3[0])
		main_circ.u(param_5,param_4,0.945000, qreg_0[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc1,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_3[0]])
with else_1:
	main_circ.u(param_6,-0.877000,param_6, qreg_2[0])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,param_2,param_5, qreg_2[0])
	main_circ.u(-0.195000,param_0,0.700000, qreg_2[0])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_3[0]])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(qreg_0[0])
	main_circ.u(param_5,param_3,param_2, qreg_2[0])
	main_circ.u(pi/2,-0.344000,0.491000, qreg_0[0])
	main_circ.u(param_4,-0.241000,param_3, qreg_3[0])
	main_circ.u(param_4,param_6,param_0, qreg_2[0])
with else_1:
	main_circ.rz(0.506000, qreg_3[0])
	main_circ.h(qreg_3[0])
	main_circ.rz(-0.789000, qreg_3[0])
	main_circ.u(-0.997000,-0.722000,param_0, qreg_0[1])
main_circ.measure(qreg_2[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.h(qreg_3[0])
	main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_2[0]])
with else_1:
	main_circ.rz(0.757000, qreg_0[0])
main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_2[0],qreg_0[0]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_3[0]])
	with case_1(1):
		main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.541000, param_2: -0.857000, param_3: 0.828000, param_4: 0.868000, param_5: -0.570000, param_6: 0.021000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1331", "Collect1qRuns")
