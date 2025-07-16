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
subcirc0.rz(-0.278000, qreg_0[3])
subcirc0.u(0.864000,-0.088000,0.716000, qreg_0[3])
subcirc0.u(pi/2,-0.820000,-0.234000, qreg_0[3])
subcirc0.u(pi/2,0.778000,-0.961000, qreg_0[1])
subcirc0.u(pi/2,-0.070000,-0.509000, qreg_0[0])
subcirc0.x(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(pi/2,-0.744000,-0.202000, qreg_0[0])
subcirc1.u(pi/2,-0.711000,0.834000, qreg_0[3])
subcirc1.x(qreg_0[2])
subcirc1.u(0.810000,0.180000,-0.235000, qreg_0[0])
subcirc1.u(pi/2,-0.060000,0.322000, qreg_0[0])
subcirc1.u(0.369000,-0.288000,-0.654000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(1)

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

main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.x(2)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.u(-0.853000,-0.461000,0.057000, qreg_0[0])
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.append(subcirc1,[2,3,1,0,qreg_0[0]])
			with else_1:
				main_circ.barrier(3)
		with else_2:
			main_circ.measure(3, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.barrier(qreg_0[0])
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.u(param_0,0.769000,param_1, 0)
				main_circ.append(subcirc1,[2,1,3,qreg_0[0],0])
	with case_3(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc1,[2,0,3,1,qreg_0[0]])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.x(qreg_0[0])
				main_circ.rz(0.825000, 0)
				main_circ.append(subcirc1,[2,qreg_0[0],0,3,1])
		with case_2(1):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.x(3)
				main_circ.append(subcirc1,[0,3,1,2,qreg_0[0]])
with else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(param_0,param_0,-0.861000, 3)
			main_circ.rz(param_0, 3)
			main_circ.u(param_1,-0.374000,param_0, 0)
			main_circ.u(param_0,param_0,-0.585000, 0)
		with else_1:
			main_circ.u(param_1,0.934000,-0.581000, 3)
			main_circ.u(pi/2,0.225000,param_0, qreg_0[0])
			main_circ.append(subcirc1,[2,3,1,qreg_0[0],0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(3, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.x(1)
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rz(param_1, 1)
			main_circ.u(-0.361000,0.657000,param_0, 1)
			main_circ.barrier(3)
		with else_1:
			main_circ.rz(param_1, 1)
			main_circ.rz(param_1, 1)
			main_circ.u(param_1,param_0,-0.266000, qreg_0[0])
			main_circ.rz(param_1, 2)
	with else_2:
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(param_1,-0.017000,0.465000, 0)
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rz(param_0, 3)
		with else_1:
			main_circ.id(2)
main_circ.u(pi/2,0.959000,-0.572000, 3)
bindings = {param_0: -0.373000, param_1: 0.698000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "516")
