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
subcirc0.h(qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.cz(qreg_0[2],qreg_0[0])
subcirc0.u(0,0,-0.203000, qreg_0[3])
subcirc0.z(qreg_0[3])
subcirc0.cz(qreg_0[0],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cz(qreg_0[0],qreg_1[2])
subcirc1.h(qreg_1[0])
subcirc1.cz(qreg_1[0],qreg_0[0])
subcirc1.u(0,0,-0.848000, qreg_1[2])
subcirc1.cz(qreg_1[2],qreg_1[1])
subcirc1.cz(qreg_0[0],qreg_1[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.cz(qreg_1[0],qreg_1[2])
subcirc2.u(0,0,-0.412000, qreg_1[1])
subcirc2.u(0,0,-0.319000, qreg_1[1])
subcirc2.z(qreg_1[2])
subcirc2.h(qreg_1[0])
subcirc2.h(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_3[0],qreg_0[2])
subcirc3.z(qreg_0[1])
subcirc3.cz(qreg_0[1],qreg_3[0])
subcirc3.h(qreg_0[1])
subcirc3.cz(qreg_3[0],qreg_0[0])
subcirc3.z(qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.z(qreg_0[1])
subcirc4.u(0,0,0.126000, qreg_0[1])
subcirc4.cz(qreg_0[0],qreg_2[1])
subcirc4.u(0,0,-0.783000, qreg_0[1])
subcirc4.cz(qreg_0[1],qreg_2[1])
subcirc4.z(qreg_0[1])

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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.z(1)
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_2:
			with case_2(0):
				main_circ.measure(qreg_0[0], creg_0[0])
				with main_circ.switch(creg_0[0]) as case_1:
					with case_1(0):
						main_circ.u(0,0,param_2, 1)
						main_circ.append(subcirc1,[qreg_3[0],0,1,qreg_0[0]])
					with case_1(1):
						main_circ.append(subcirc1,[qreg_3[0],1,qreg_0[1],qreg_0[0]])
			with case_2(1):
				main_circ.cz(qreg_0[2],qreg_0[0])
				main_circ.measure(0, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.append(subcirc2,[qreg_3[0],qreg_0[2],qreg_0[0],0])
					with case_1(1):
						main_circ.append(subcirc1,[0,qreg_0[2],1,qreg_0[1]])
	with case_3(1):
		main_circ.append(subcirc2,[1,qreg_0[0],0,qreg_3[0]])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.append(subcirc3,[qreg_0[0],1,qreg_3[0],0])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[2], creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.z(0)
		main_circ.measure(qreg_0[1], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc1,[qreg_0[2],0,qreg_3[0],1])
		with else_1:
			main_circ.append(subcirc3,[qreg_0[0],qreg_0[2],0,1])
	with else_2:
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.append(subcirc3,[0,qreg_3[0],qreg_0[2],1])
main_circ.z(qreg_0[2])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(1)
main_circ.cz(qreg_0[2],qreg_0[1])
bindings = {param_2: 0.893000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "393")
