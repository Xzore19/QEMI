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
subcirc0.u(-0.211000,0.036000,0.447000, qreg_0[0])
subcirc0.u(pi/2,0.183000,-0.124000, qreg_2[1])
subcirc0.cx(qreg_2[1],qreg_2[0])
subcirc0.u(0.676000,0.991000,0.528000, qreg_2[1])
subcirc0.cx(qreg_2[0],qreg_0[0])
subcirc0.u(pi/2,0.194000,-0.422000, qreg_2[1])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cx(qreg_1[1],qreg_0[0])
subcirc1.cx(qreg_1[0],qreg_1[1])
subcirc1.u(pi/2,-0.240000,0.248000, qreg_1[0])
subcirc1.cx(qreg_1[0],qreg_1[2])
subcirc1.ry(0.441000, qreg_1[0])
subcirc1.u(pi/2,-0.052000,-0.052000, qreg_1[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(-0.335000,-0.452000,0.162000, qreg_0[3])
subcirc2.u(pi/2,-0.004000,0.820000, qreg_0[1])
subcirc2.ry(0.579000, qreg_0[3])
subcirc2.ry(-0.115000, qreg_0[2])
subcirc2.u(-0.543000,0.119000,-0.757000, qreg_0[1])
subcirc2.ry(-0.621000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.u(0.014000,-0.441000,-0.935000, qreg_0[0])
subcirc3.u(-0.623000,0.617000,0.160000, qreg_0[1])
subcirc3.u(0.008000,-0.811000,-0.408000, qreg_2[0])
subcirc3.u(pi/2,0.339000,-0.338000, qreg_2[1])
subcirc3.u(-0.687000,0.977000,-0.067000, qreg_2[1])
subcirc3.u(pi/2,-0.883000,-0.939000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(1)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.u(param_5,0.504000,param_5, qreg_0[1])
		main_circ.barrier(qreg_0[2])
	with else_1:
		main_circ.id(qreg_0[2])
with else_2:
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc1,[0,qreg_3[0],qreg_0[0],qreg_0[1]])
		with case_1(1):
			main_circ.u(0.196000,param_2,param_4, qreg_0[1])
			main_circ.id(0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.cx(qreg_0[0],qreg_0[1])
with else_2:
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.cx(0,qreg_3[0])
		main_circ.u(param_1,param_3,-0.817000, qreg_0[0])
		main_circ.ry(param_2, qreg_0[2])
		main_circ.append(subcirc2,[qreg_3[0],qreg_0[2],qreg_0[1],qreg_0[0]])
	with else_1:
		main_circ.id(0)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.u(param_5,param_5,0.851000, qreg_0[2])
			main_circ.append(subcirc2,[qreg_0[0],0,qreg_0[2],qreg_0[1]])
	with case_2(1):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc2,[qreg_0[1],qreg_3[0],qreg_0[2],0])
		with else_1:
			main_circ.append(subcirc1,[qreg_0[1],0,qreg_0[0],qreg_3[0]])
main_circ.measure(qreg_0[1], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.cx(0,qreg_3[0])
			main_circ.cx(qreg_3[0],qreg_0[0])
			main_circ.cx(qreg_0[2],qreg_0[1])
			main_circ.cx(qreg_0[2],qreg_0[0])
		with case_1(1):
			main_circ.cx(qreg_0[2],qreg_0[0])
			main_circ.cx(qreg_0[1],0)
			main_circ.cx(qreg_0[0],0)
			main_circ.cx(qreg_0[1],qreg_0[2])
with else_2:
	main_circ.cx(0,qreg_3[0])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.u(param_5,-0.996000,-0.398000, qreg_0[0])
	main_circ.measure(qreg_0[1], creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(qreg_0[0])
	with else_1:
		main_circ.barrier(0)
	main_circ.measure(0, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(qreg_3[0])
		with case_1(1):
			main_circ.id(0)
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.barrier(qreg_0[2])
	main_circ.id(qreg_3[0])
bindings = {param_1: -0.640000, param_2: -0.627000, param_3: -0.481000, param_4: 0.023000, param_5: -0.919000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1834")
