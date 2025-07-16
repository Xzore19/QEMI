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
subcirc0.u(-0.823000,-0.889000,-0.611000, qreg_2[1])
subcirc0.cz(qreg_2[1],qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0.cz(qreg_2[0],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[3],qreg_0[0])
subcirc1.u(0.177000,-0.902000,-0.975000, qreg_0[3])
subcirc1.z(qreg_0[3])
subcirc1.s(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.s(qreg_0[0])
subcirc2.s(qreg_0[2])
subcirc2.cz(qreg_0[3],qreg_0[1])
subcirc2.cz(qreg_0[0],qreg_0[1])

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

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.append(subcirc1,[0,qreg_0[0],2,1])
with else_4:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.u(0.454000,param_2,-0.594000, 0)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.append(subcirc1,[qreg_0[0],1,2,3])
			with case_2(1):
				main_circ.measure(0, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.append(subcirc2,[1,qreg_0[0],3,2])
				with else_1:
					main_circ.append(subcirc2,[qreg_0[0],0,3,2])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_4:
	main_circ.measure(0, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_3:
		with case_3(0):
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_2:
				main_circ.s(3)
				main_circ.measure(3, creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(param_2,param_1,0.572000, 0)
						main_circ.cz(qreg_0[0],3)
						main_circ.s(0)
						main_circ.append(subcirc1,[qreg_0[0],0,2,3])
					with case_1(1):
						main_circ.cz(qreg_0[0],1)
						main_circ.z(3)
						main_circ.cz(0,3)
						main_circ.s(3)
			with else_2:
				main_circ.measure(3, creg_0[0])
				with main_circ.if_test((creg_0[0],0)) as else_1:
					main_circ.cz(qreg_0[0],2)
					main_circ.append(subcirc1,[0,2,3,1])
				with else_1:
					main_circ.z(qreg_0[0])
					main_circ.append(subcirc1,[0,3,qreg_0[0],2])
		with case_3(1):
			main_circ.measure(0, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.cz(1,3)
				main_circ.measure(3, creg_1[0])
				with main_circ.if_test((creg_1[0],0)):
					main_circ.cz(0,2)
					main_circ.cz(0,3)
					main_circ.cz(2,0)
					main_circ.append(subcirc1,[qreg_0[0],2,3,1])
with else_4:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(3, creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_2:
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.z(0)
				main_circ.cz(2,1)
				main_circ.u(0.292000,-0.234000,0.272000, qreg_0[0])
				main_circ.append(subcirc0,[2,qreg_0[0],1,3])
		with else_2:
			main_circ.id(1)
main_circ.z(2)
bindings = {param_1: -0.869000, param_2: -0.727000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "828")
