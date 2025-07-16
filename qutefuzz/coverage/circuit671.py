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
subcirc0.u(0.400000,0.323000,0.930000, qreg_0[0])
subcirc0.z(qreg_0[3])
subcirc0.u(pi/2,0.419000,-0.247000, qreg_0[3])
subcirc0.u(pi/2,-0.322000,-0.296000, qreg_0[3])
subcirc0.u(pi/2,-0.509000,0.747000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_3[0],qreg_0[0])
subcirc1.cx(qreg_3[0],qreg_0[1])
subcirc1.cx(qreg_0[2],qreg_0[1])
subcirc1.u(pi/2,-0.187000,0.684000, qreg_0[1])
subcirc1.u(pi/2,-0.706000,-0.698000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_3[0])
subcirc2.u(pi/2,-0.553000,0.343000, qreg_1[1])
subcirc2.z(qreg_3[0])
subcirc2.u(pi/2,0.934000,-0.885000, qreg_3[0])
subcirc2.u(pi/2,-0.705000,0.747000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.316000,0.787000, qreg_0[0])
subcirc3.z(qreg_0[2])
subcirc3.u(-0.541000,0.048000,0.670000, qreg_0[2])
subcirc3.cx(qreg_0[2],qreg_0[0])
subcirc3.cx(qreg_0[2],qreg_3[0])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
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

main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(qreg_0[1], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_3[0],0])
		with case_1(1):
			main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],0,qreg_0[0]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[0,qreg_3[0],qreg_0[2],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.measure(qreg_3[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.z(0)
		main_circ.z(qreg_0[0])
		main_circ.z(qreg_3[0])
		main_circ.append(subcirc3,[qreg_3[0],qreg_0[2],0,qreg_0[1]])
main_circ.measure(0, creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_1[0])
		with main_circ.switch(creg_1[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[qreg_0[1],qreg_3[0],qreg_0[2],0])
			with case_1(1):
				main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],0,qreg_0[0]])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_2,-0.764000,0.957000, qreg_3[0])
				main_circ.u(param_0,0.805000,param_2, qreg_0[0])
				main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
			with case_1(1):
				main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cx(0,qreg_0[2])
		with else_1:
			main_circ.cx(0,qreg_0[1])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.cx(qreg_3[0],qreg_0[2])
				main_circ.cx(qreg_0[1],qreg_0[2])
				main_circ.cx(qreg_3[0],qreg_0[2])
				main_circ.cx(qreg_0[2],qreg_3[0])
			with case_1(1):
				main_circ.cx(qreg_0[2],qreg_0[1])
				main_circ.cx(qreg_0[2],qreg_0[1])
				main_circ.cx(0,qreg_3[0])
				main_circ.cx(0,qreg_0[2])
	with case_2(1):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.cx(qreg_3[0],0)
		with else_1:
			main_circ.cx(qreg_0[0],qreg_0[2])
			main_circ.cx(qreg_0[0],qreg_0[1])
			main_circ.id(qreg_0[2])
		main_circ.measure(qreg_0[1], creg_1[0])
		with main_circ.if_test((creg_1[0],0)) as else_1:
			main_circ.cx(0,qreg_0[0])
			main_circ.barrier(qreg_0[0])
		with else_1:
			main_circ.id(qreg_3[0])
bindings = {param_0: -0.947000, param_2: -0.062000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "671", "ResetAfterMeasureSimplification")
