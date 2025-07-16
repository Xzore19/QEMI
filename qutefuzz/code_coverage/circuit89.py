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
subcirc0.x(qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.u(-0.009000,-0.245000,0.018000, qreg_0[1])
subcirc0.u(pi/2,-0.780000,0.979000, qreg_3[0])
subcirc0.u(pi/2,0.068000,-0.401000, qreg_3[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.u(-0.992000,-0.870000,-0.356000, qreg_0[3])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.u(-0.547000,-0.712000,-0.660000, qreg_0[3])
subcirc1.u(pi/2,0.195000,0.866000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.x(qreg_0[3])
subcirc2.u(0.292000,-0.800000,-0.261000, qreg_0[3])
subcirc2.cz(qreg_0[1],qreg_0[2])
subcirc2.x(qreg_0[1])
subcirc2.x(qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cz(qreg_2[1],qreg_0[1])
subcirc3.u(pi/2,-0.474000,0.380000, qreg_0[1])
subcirc3.u(0.075000,-0.385000,-0.278000, qreg_2[1])
subcirc3.u(pi/2,-0.665000,0.986000, qreg_0[1])
subcirc3.u(pi/2,-0.424000,-0.950000, qreg_2[0])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.append(subcirc0,[3,qreg_0[0],2,1])
		with else_1:
			main_circ.u(param_1,param_2,0.611000, qreg_0[0])
with else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(qreg_0[0], creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.append(subcirc2,[qreg_1[0],qreg_0[0],1,0,2,3])
			with else_1:
				main_circ.x(qreg_1[0])
				main_circ.append(subcirc0,[1,qreg_0[0],qreg_1[0],2])
		with case_2(1):
			main_circ.append(subcirc0,[0,qreg_1[0],qreg_0[0],1])
main_circ.append(subcirc1,[0,2,3,1])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_1[0])
	with main_circ.if_test((creg_1[0],0)) as else_2:
		main_circ.measure(qreg_1[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.append(subcirc2,[1,2,qreg_1[0],3,qreg_0[0],0])
		with else_1:
			main_circ.append(subcirc1,[3,qreg_0[0],1,qreg_1[0]])
	with else_2:
		main_circ.measure(3, creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.cz(3,1)
				main_circ.cz(qreg_1[0],2)
				main_circ.cz(2,1)
				main_circ.cz(qreg_1[0],2)
			with case_1(1):
				main_circ.cz(1,2)
				main_circ.cz(2,3)
				main_circ.cz(2,1)
				main_circ.cz(qreg_1[0],2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.cz(3,qreg_1[0])
					main_circ.cz(3,qreg_1[0])
					main_circ.cz(qreg_0[0],2)
					main_circ.barrier(0)
				with case_1(1):
					main_circ.id(qreg_1[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.barrier(1)
			with else_1:
				main_circ.barrier(1)
			main_circ.barrier(qreg_0[0])
		with case_2(1):
			main_circ.barrier(qreg_1[0])
with else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.barrier(qreg_0[0])
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(1)
		main_circ.barrier(qreg_0[0])
	main_circ.barrier(3)
bindings = {param_1: -0.305000, param_2: 0.653000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "89", "TemplateOptimization")
