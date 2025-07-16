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
subcirc0.x(qreg_0[3])
subcirc0.cz(qreg_0[1],qreg_0[3])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.cz(qreg_0[3],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.x(qreg_0[2])
subcirc1.cz(qreg_0[2],qreg_3[0])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.cz(qreg_0[2],qreg_0[1])
subcirc1.cx(qreg_0[1],qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2.x(qreg_0[2])
subcirc2.x(qreg_0[0])
subcirc2.cx(qreg_3[0],qreg_0[0])
subcirc2.cz(qreg_3[0],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3.cz(qreg_0[1],qreg_2[0])
subcirc3.cz(qreg_2[0],qreg_0[1])
subcirc3.cx(qreg_0[1],qreg_0[0])
subcirc3.u(0.145000,0.765000,-0.104000, qreg_0[1])

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
param_5 = Parameter("param_5")

main_circ.append(subcirc2,[1,2,3,0,qreg_0[0]])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.cz(3,1)
	main_circ.measure(1, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.append(subcirc0,[qreg_0[0],2,0,3])
		with case_2(1):
			main_circ.measure(1, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc3,[0,1,2,3])
				with case_1(1):
					main_circ.x(qreg_0[0])
					main_circ.x(2)
					main_circ.cz(1,2)
					main_circ.append(subcirc2,[2,qreg_0[0],1,3,0])
with else_3:
	main_circ.x(0)
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.cz(qreg_0[0],0)
				main_circ.cx(2,0)
				main_circ.append(subcirc3,[0,3,qreg_0[0],1])
			with else_1:
				main_circ.append(subcirc1,[1,0,2,3])
		with case_2(1):
			main_circ.measure(2, creg_1[0])
			with main_circ.switch(creg_1[0]) as case_1:
				with case_1(0):
					main_circ.u(param_2,param_1,param_2, qreg_0[0])
					main_circ.append(subcirc3,[2,qreg_0[0],1,0])
				with case_1(1):
					main_circ.append(subcirc3,[qreg_0[0],0,1,3])
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)) as else_1:
				main_circ.append(subcirc0,[3,1,0,2])
			with else_1:
				main_circ.barrier(3)
	with case_3(1):
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.x(3)
			main_circ.measure(1, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cx(0,qreg_0[0])
				main_circ.barrier(0)
			main_circ.barrier(1)
		with else_2:
			main_circ.id(3)
		main_circ.barrier(3)
bindings = {param_1: -0.294000, param_2: -0.925000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1747")
