from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc0.add_register(qreg_1)
# Adding creg resources 
subcirc0.rx(-0.994000, qreg_1[1])
subcirc0.h(qreg_1[1])
subcirc0.u(-0.139000,-0.313000,-0.493000, qreg_1[0])
subcirc0.rx(0.441000, qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[1])
subcirc1.u(0.446000,0.016000,0.191000, qreg_0[0])
subcirc1.x(qreg_0[0])
subcirc1.rx(0.278000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.726000,-0.379000,0.306000, qreg_0[0])
subcirc2.h(qreg_0[0])
subcirc2.x(qreg_0[0])
subcirc2.u(0.816000,0.474000,0.742000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.h(qreg_0[1])
subcirc3.x(qreg_0[2])
subcirc3.u(-0.979000,0.275000,0.889000, qreg_0[1])
subcirc3.x(qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0.797000,0.557000,0.290000, qreg_0[0])
subcirc4.rx(-0.175000, qreg_0[0])
subcirc4.x(qreg_0[0])
subcirc4.x(qreg_3[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.append(subcirc4,[0,2,qreg_0[0],1])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.barrier(1)
	with else_1:
		main_circ.append(subcirc2,[3,1,qreg_0[0],0,2])
main_circ.u(-0.542000,param_2,0.707000, qreg_0[0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.u(-0.637000,param_3,param_2, 2)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(qreg_0[0])
			main_circ.id(0)
		main_circ.id(2)
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc4,[3,1,2,0])
		with else_1:
			main_circ.x(3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.if_test((creg_1[0],0)):
		main_circ.append(subcirc4,[qreg_0[0],3,1,2])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc2,[1,2,3,qreg_0[0],0])
		with case_1(1):
			main_circ.rx(param_0, 2)
			main_circ.id(2)
main_circ.rx(param_3, 0)
main_circ.append(subcirc3,[1,3,2,qreg_0[0]])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.u(param_2,param_0,0.595000, 1)
			main_circ.u(param_3,param_1,-0.629000, qreg_0[0])
			main_circ.append(subcirc2,[3,0,2,qreg_0[0],1])
		with case_1(1):
			main_circ.x(3)
			main_circ.rx(-0.390000, 3)
			main_circ.append(subcirc3,[3,0,2,1])
with else_2:
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc4,[0,2,3,1])
		with case_1(1):
			main_circ.id(qreg_0[0])
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_1:
		with case_1(0):
			main_circ.x(qreg_0[0])
			main_circ.id(2)
		with case_1(1):
			main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.h(2)
			main_circ.id(0)
		with case_1(1):
			main_circ.id(3)
	main_circ.u(param_0,param_3,0.570000, qreg_0[0])
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(qreg_0[0])
	main_circ.id(0)
with else_2:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.id(2)
	main_circ.barrier(qreg_0[0])
bindings = {param_0: -0.093000, param_1: -0.738000, param_2: -0.307000, param_3: -0.820000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1970", "CommutativeCancellation")
