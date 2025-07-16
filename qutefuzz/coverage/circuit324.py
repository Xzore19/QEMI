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
subcirc0.x(qreg_3[0])
subcirc0.y(qreg_0[1])
subcirc0.rz(-0.832000, qreg_0[0])
subcirc0.x(qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rz(0.709000, qreg_0[3])
subcirc1.x(qreg_0[1])
subcirc1.y(qreg_0[0])
subcirc1.u(0,0,0.731000, qreg_0[2])
subcirc1.x(qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.y(qreg_3[0])
subcirc2.x(qreg_3[0])
subcirc2.u(0,0,-0.014000, qreg_0[1])
subcirc2.rz(0.234000, qreg_3[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(-0.175000, qreg_0[3])
subcirc3.y(qreg_0[3])
subcirc3.y(qreg_0[2])
subcirc3.rz(-0.075000, qreg_0[2])
subcirc3.x(qreg_0[2])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(1, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(3, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.rz(param_0, 3)
			main_circ.append(subcirc2,[1,2,qreg_0[0],3])
		with else_1:
			main_circ.append(subcirc1,[3,2,1,0])
	with else_2:
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.append(subcirc1,[qreg_0[0],0,3,1])
with else_3:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_2:
		main_circ.barrier(0)
	with else_2:
		main_circ.id(3)
	main_circ.measure(qreg_0[0], creg_0[0])
	with main_circ.switch(creg_0[0]) as case_2:
		with case_2(0):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)) as else_1:
				main_circ.append(subcirc1,[3,2,0,1])
			with else_1:
				main_circ.append(subcirc1,[2,1,0,3])
		with case_2(1):
			main_circ.rz(0.846000, qreg_0[0])
			main_circ.measure(2, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.x(0)
				main_circ.rz(0.519000, 2)
				main_circ.rz(param_0, qreg_0[0])
main_circ.append(subcirc3,[2,0,qreg_0[0],3])
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.measure(qreg_0[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_2:
			main_circ.measure(2, creg_0[1])
			with main_circ.if_test((creg_0[1],0)):
				main_circ.y(2)
		with else_2:
			main_circ.measure(qreg_0[0], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.x(qreg_0[0])
					main_circ.rz(param_3, 0)
					main_circ.x(3)
					main_circ.append(subcirc3,[0,1,qreg_0[0],2])
				with case_1(1):
					main_circ.y(0)
					main_circ.y(0)
					main_circ.barrier(3)
	with case_3(1):
		main_circ.id(1)
bindings = {param_0: -0.430000, param_3: -0.641000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "324", "TemplateOptimization")
