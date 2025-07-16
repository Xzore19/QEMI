from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_3[0],qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_2[0])
subcirc0.u(pi/2,-0.989000,0.894000, qreg_0[0])
subcirc0.u(0.530000,-0.320000,0.929000, qreg_3[0])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.u(pi/2,0.130000,0.301000, qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,-0.539000,0.248000, qreg_0[1])
subcirc1.u(-0.122000,0.276000,-0.117000, qreg_0[2])
subcirc1.u(0.856000,-0.824000,-0.728000, qreg_0[0])
subcirc1.u(pi/2,-0.593000,-0.553000, qreg_3[0])
subcirc1.u(0,0,0.683000, qreg_0[1])
subcirc1.u(0.417000,0.337000,0.680000, qreg_3[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.u(pi/2,param_1,param_0, qreg_0[0])
		main_circ.cy(qreg_0[0],1)
		main_circ.u(0,param_1,-0.675000, qreg_0[0])
		main_circ.u(param_1,0.536000,0.218000, qreg_3[0])
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.cy(0,qreg_3[0])
		main_circ.u(param_1,0.422000,param_0, 0)
		main_circ.u(pi/2,0.076000,-0.579000, qreg_0[2])
		main_circ.cy(1,qreg_3[0])
with else_2:
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(param_1,0.428000,param_0, qreg_0[1])
		main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],1,qreg_3[0]])
	with else_1:
		main_circ.append(subcirc0,[qreg_3[0],qreg_0[0],0,qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.append(subcirc0,[qreg_3[0],1,qreg_0[2],qreg_0[0],0])
with else_2:
	main_circ.u(pi/2,param_0,param_0, qreg_3[0])
main_circ.u(pi/2,-0.679000,param_0, qreg_0[2])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(0.316000,param_1,0.845000, 0)
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(pi/2,-0.884000,0.863000, qreg_0[0])
				main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],1,qreg_0[0],0])
			with case_1(1):
				main_circ.cy(qreg_0[0],qreg_0[1])
				main_circ.cy(qreg_0[2],1)
				main_circ.cy(0,1)
				main_circ.u(param_0,0,param_1, qreg_3[0])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.u(pi/2,0.582000,0.130000, qreg_3[0])
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.u(param_0,param_0,param_1, qreg_3[0])
			main_circ.u(param_1,param_1,param_1, 0)
			main_circ.u(pi/2,0.740000,-0.723000, qreg_0[2])
		with else_1:
			main_circ.u(0.266000,0.321000,0.442000, 0)
			main_circ.u(param_1,-0.049000,param_1, qreg_0[2])
			main_circ.u(param_1,0.784000,0.348000, qreg_0[2])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_0,param_1,param_0, 0)
			main_circ.u(pi/2,param_1,0.725000, qreg_0[2])
			main_circ.cy(qreg_0[2],qreg_3[0])
			main_circ.barrier(qreg_0[0])
		with case_1(1):
			main_circ.id(qreg_0[1])
bindings = {param_0: -0.586000, param_1: -0.272000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "209")
