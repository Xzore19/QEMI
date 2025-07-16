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
subcirc0.u(pi/2,-0.711000,-0.789000, qreg_1[1])
subcirc0.u(0,0,-0.793000, qreg_0[0])
subcirc0.u(0,0,0.600000, qreg_1[0])
subcirc0.u(pi/2,0.898000,-0.403000, qreg_1[0])
subcirc0.rz(0.759000, qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,0.108000,-0.947000, qreg_0[1])
subcirc1.rz(0.786000, qreg_0[0])
subcirc1.u(0,0,0.937000, qreg_0[2])
subcirc1.x(qreg_0[3])
subcirc1.x(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

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
subcirc2.u(pi/2,0.946000,-0.727000, qreg_0[0])
subcirc2.x(qreg_3[0])
subcirc2.u(0,0,-0.831000, qreg_2[0])
subcirc2.u(pi/2,0.340000,0.503000, qreg_3[0])
subcirc2.u(pi/2,0.170000,-0.658000, qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
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

main_circ.measure(2, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.append(subcirc2,[2,3,0,1])
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_3,0,-0.128000, 0)
				main_circ.rz(param_1, 1)
				main_circ.id(1)
			with case_1(1):
				main_circ.barrier(0)
		main_circ.u(pi/2,0.782000,-0.010000, 1)
		main_circ.u(0,param_3,-0.722000, 3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.x(1)
with else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.x(3)
			main_circ.u(pi/2,-0.840000,0.218000, 3)
			main_circ.u(0,0,param_1, 2)
			main_circ.barrier(1)
		with case_1(1):
			main_circ.u(pi/2,0.195000,-0.119000, 2)
			main_circ.u(param_0,0,param_0, 1)
			main_circ.barrier(1)
main_circ.rz(param_1, 0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(2, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.rz(-0.542000, 2)
		main_circ.u(0,0,0.239000, 0)
	with else_1:
		main_circ.append(subcirc2,[3,0,2,1])
with else_2:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.append(subcirc0,[0,2,1,3])
	with else_1:
		main_circ.u(pi/2,param_0,-0.577000, 2)
		main_circ.u(pi/2,param_0,0.007000, 0)
		main_circ.u(param_0,param_2,0.188000, 0)
		main_circ.append(subcirc0,[2,1,0,3])
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.rz(param_3, 3)
with else_2:
	main_circ.append(subcirc0,[3,0,1,2])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(2)
main_circ.rz(param_2, 3)
bindings = {param_0: 0.910000, param_1: -0.488000, param_2: 0.145000, param_3: -0.618000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "469")
