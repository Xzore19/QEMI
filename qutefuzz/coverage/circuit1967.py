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
subcirc0.u(0.485000,0.314000,-0.344000, qreg_0[3])
subcirc0.u(pi/2,-0.901000,-0.124000, qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0.u(pi/2,0.364000,0.637000, qreg_0[2])
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_0[3])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.007000,-0.154000,0.306000, qreg_0[1])
subcirc1.y(qreg_0[2])
subcirc1.u(-0.364000,-0.505000,-0.570000, qreg_0[3])
subcirc1.u(pi/2,0.199000,0.206000, qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.u(-0.423000,-0.996000,-0.024000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,0.165000,-0.943000, qreg_2[0])
subcirc2.u(pi/2,-0.256000,-0.319000, qreg_2[0])
subcirc2.y(qreg_0[0])
subcirc2.u(0.535000,-0.705000,0.168000, qreg_0[0])
subcirc2.x(qreg_3[0])
subcirc2.u(-0.413000,-0.095000,-0.596000, qreg_0[0])

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

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(3)
		with else_1:
			main_circ.barrier(1)
		main_circ.append(subcirc2,[0,3,1,2])
	with case_2(1):
		main_circ.y(2)
		main_circ.measure(2, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.barrier(2)
			with case_1(1):
				main_circ.u(param_0,param_0,-0.757000, 1)
				main_circ.u(param_1,0.149000,-0.923000, 0)
				main_circ.u(param_0,-0.713000,-0.936000, 0)
				main_circ.y(0)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.u(param_1,param_1,-0.412000, 0)
		main_circ.u(0.410000,param_1,-0.419000, 3)
		main_circ.y(0)
with else_2:
	main_circ.barrier(1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.x(2)
			main_circ.y(2)
			main_circ.y(0)
			main_circ.barrier(0)
		with case_1(1):
			main_circ.id(1)
with else_2:
	main_circ.y(0)
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.x(0)
	with else_1:
		main_circ.u(pi/2,-0.012000,param_1, 2)
	main_circ.x(3)
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(pi/2,-0.153000,0.780000, 3)
			main_circ.u(pi/2,param_0,param_0, 0)
			main_circ.u(param_0,-0.874000,0.343000, 2)
			main_circ.u(param_1,param_0,-0.859000, 2)
		with case_1(1):
			main_circ.x(1)
			main_circ.id(0)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.u(param_1,param_0,param_0, 2)
			main_circ.x(0)
			main_circ.append(subcirc2,[2,0,3,1])
	with case_2(1):
		main_circ.barrier(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.append(subcirc2,[3,0,2,1])
	with else_1:
		main_circ.x(3)
		main_circ.append(subcirc2,[0,1,3,2])
with else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.x(3)
		main_circ.barrier(0)
	with else_1:
		main_circ.u(-0.076000,0.661000,param_0, 0)
		main_circ.y(1)
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.barrier(1)
	main_circ.measure(3, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_1:
		main_circ.u(-0.389000,param_1,param_1, 0)
	with else_1:
		main_circ.id(1)
bindings = {param_0: -0.981000, param_1: -0.501000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1967", "InverseCancellation")
