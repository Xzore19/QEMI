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
subcirc0.u(0,0,0.485000, qreg_0[0])
subcirc0.rx(0.760000, qreg_3[0])
subcirc0.u(0,0,-0.478000, qreg_3[0])
subcirc0.h(qreg_0[2])
subcirc0.u(0,0,0.771000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0,0,0.292000, qreg_0[0])
subcirc1.rx(0.382000, qreg_2[1])
subcirc1.u(0,0,-0.678000, qreg_0[0])
subcirc1.h(qreg_2[1])
subcirc1.u(-0.706000,-0.882000,-0.213000, qreg_2[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0.656000,0.543000,0.678000, qreg_0[0])
subcirc2.h(qreg_0[3])
subcirc2.u(0,0,-0.006000, qreg_0[2])
subcirc2.h(qreg_0[3])
subcirc2.h(qreg_0[3])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.h(qreg_0[0])
subcirc3.h(qreg_0[0])
subcirc3.rx(0.041000, qreg_0[2])
subcirc3.rx(0.622000, qreg_0[1])
subcirc3.rx(0.091000, qreg_0[0])

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

main_circ.rx(0.066000, 1)
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.rx(-0.056000, 3)
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc2,[0,2,1,3])
	with case_3(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(0, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc2,[3,2,1,0])
			with else_1:
				main_circ.append(subcirc2,[2,0,3,1])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc3,[3,1,0,2])
main_circ.rx(0.328000, 1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(2, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(-0.072000,-0.039000,param_0, 1)
			main_circ.barrier(0)
		with else_1:
			main_circ.rx(0.084000, 2)
			main_circ.rx(0.407000, 2)
			main_circ.h(0)
			main_circ.u(-0.598000,param_1,param_1, 3)
			main_circ.u(param_3,param_3,0.518000, 2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.h(3)
			main_circ.h(0)
			main_circ.barrier(2)
		with else_1:
			main_circ.u(0,param_1,param_0, 0)
			main_circ.u(0,0,param_3, 2)
			main_circ.rx(0.600000, 3)
			main_circ.h(2)
			main_circ.barrier(2)
main_circ.u(param_0,0.956000,param_3, 3)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(1)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_3,0,param_3, 2)
			main_circ.u(param_0,0,param_2, 0)
			main_circ.h(0)
			main_circ.barrier(2)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.h(0)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.rx(param_1, 0)
				main_circ.h(0)
				main_circ.barrier(1)
bindings = {param_0: 0.361000, param_1: 0.823000, param_2: 0.789000, param_3: -0.375000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "569")
