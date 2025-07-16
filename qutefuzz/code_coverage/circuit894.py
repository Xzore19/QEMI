from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(-0.215000,1.000000,-0.938000, qreg_2[1])
subcirc0.u(0,0,0.164000, qreg_2[0])
subcirc0.cz(qreg_0[1],qreg_2[1])
subcirc0.u(0,0,-0.669000, qreg_2[0])
subcirc0.u(0.955000,0.760000,0.321000, qreg_0[1])
subcirc0.cz(qreg_2[1],qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cz(qreg_0[2],qreg_3[0])
subcirc1.u(0,0,0.797000, qreg_0[0])
subcirc1.u(0,0,0.379000, qreg_0[1])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.u(0,0,-0.307000, qreg_0[0])
subcirc1.u(0,0,-0.567000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(-0.369000, qreg_0[2])
subcirc2.u(-0.005000,-0.796000,0.875000, qreg_0[3])
subcirc2.u(0.781000,-0.901000,0.651000, qreg_0[0])
subcirc2.rz(0.769000, qreg_0[3])
subcirc2.u(0,0,-0.864000, qreg_0[3])
subcirc2.cz(qreg_0[3],qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_0[0],qreg_3[0])
subcirc3.rz(1.000000, qreg_3[0])
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3.u(0,0,0.401000, qreg_0[1])
subcirc3.u(0.012000,-0.872000,-0.288000, qreg_0[0])
subcirc3.rz(-0.143000, qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc4.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0,0,-0.035000, qreg_3[0])
subcirc4.rz(0.387000, qreg_1[0])
subcirc4.rz(-0.985000, qreg_0[0])
subcirc4.u(0,0,0.934000, qreg_1[0])
subcirc4.u(0.033000,-0.054000,0.834000, qreg_1[0])
subcirc4.rz(0.667000, qreg_1[0])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[3],1])
		with case_1(1):
			main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],qreg_0[0],0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc4,[qreg_0[3],0,qreg_0[0],1,qreg_0[1]])
	with case_2(1):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.rz(-0.636000, qreg_0[0])
			main_circ.u(param_0,0,param_1, qreg_0[0])
			main_circ.append(subcirc3,[1,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_0[3], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.u(-0.560000,param_1,-0.240000, qreg_0[2])
		main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],1,qreg_0[2]])
	with else_1:
		main_circ.cz(1,qreg_0[0])
		main_circ.cz(qreg_0[1],qreg_0[3])
with else_2:
	main_circ.cz(qreg_0[2],0)
main_circ.cz(0,qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.id(0)
	main_circ.measure(qreg_0[3], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.rz(-0.837000, qreg_0[0])
			main_circ.id(1)
		with case_1(1):
			main_circ.id(0)
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(qreg_0[0])
	with else_1:
		main_circ.u(param_0,0.992000,0.233000, qreg_0[1])
	main_circ.barrier(qreg_0[3])
main_circ.cz(qreg_0[0],1)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(qreg_0[1])
		with else_1:
			main_circ.u(0,param_1,param_1, qreg_0[3])
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(1)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.rz(param_1, qreg_0[3])
				main_circ.id(0)
			with case_1(1):
				main_circ.barrier(qreg_0[2])
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.id(qreg_0[3])
			with case_1(1):
				main_circ.barrier(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_0[1])
		with else_1:
			main_circ.barrier(1)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.barrier(1)
		with else_1:
			main_circ.barrier(qreg_0[0])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[3], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(1)
		main_circ.barrier(0)
	with case_2(1):
		main_circ.barrier(qreg_0[2])
bindings = {param_0: 0.927000, param_1: -0.241000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "894", "TemplateOptimization")
