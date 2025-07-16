from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.z(qreg_0[2])
subcirc0.rz(-0.705000, qreg_0[2])
subcirc0.rz(-0.867000, qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.h(qreg_3[0])
subcirc0.u(0.815000,-0.819000,0.481000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.z(qreg_2[0])
subcirc1.z(qreg_0[0])
subcirc1.rz(-0.225000, qreg_3[0])
subcirc1.u(-0.309000,0.728000,-0.903000, qreg_0[0])
subcirc1.u(-0.344000,0.470000,-0.665000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_3[0])
subcirc2.h(qreg_0[1])
subcirc2.z(qreg_0[0])
subcirc2.h(qreg_0[1])
subcirc2.rz(0.253000, qreg_0[1])
subcirc2.u(0.572000,0.074000,0.217000, qreg_0[0])
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
subcirc3.h(qreg_2[0])
subcirc3.z(qreg_0[1])
subcirc3.h(qreg_2[0])
subcirc3.u(-0.840000,-0.290000,-0.556000, qreg_2[0])
subcirc3.rz(0.323000, qreg_0[0])
subcirc3.h(qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rz(0.624000, qreg_0[1])
subcirc4.z(qreg_3[0])
subcirc4.u(0.439000,-0.954000,-0.077000, qreg_0[1])
subcirc4.rz(0.324000, qreg_3[0])
subcirc4.z(qreg_0[0])
subcirc4.rz(-0.439000, qreg_0[0])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_1,0.928000,-0.181000, 3)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_3:
	with case_3(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc0,[3,0,2,1])
			with else_1:
				main_circ.u(-0.574000,-0.086000,param_0, 2)
				main_circ.append(subcirc0,[1,0,3,2])
	with case_3(1):
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc3,[3,2,1,0])
			with else_1:
				main_circ.append(subcirc3,[1,3,2,0])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(1, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(3, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc0,[2,3,1,0])
				with case_1(1):
					main_circ.id(0)
	with case_3(1):
		main_circ.measure(2, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_2:
			with case_2(0):
				main_circ.measure(1, creg_0[1])
				with main_circ.switch(creg_0[1]) as case_1:
					with case_1(0):
						main_circ.rz(param_1, 3)
						main_circ.barrier(0)
					with case_1(1):
						main_circ.append(subcirc1,[0,2,3,1])
			with case_2(1):
				main_circ.measure(1, creg_0[1])
				with main_circ.if_test((creg_0[1],0)) as else_1:
					main_circ.h(3)
					main_circ.id(0)
				with else_1:
					main_circ.barrier(2)
				main_circ.measure(2, creg_0[0])
				with main_circ.if_test((creg_0[0],0)):
					main_circ.barrier(1)
				main_circ.id(2)
bindings = {param_0: -0.933000, param_1: 0.091000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "1709")
