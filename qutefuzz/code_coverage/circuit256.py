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
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.ry(0.342000, qreg_2[1])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_2[1])
subcirc0.s(qreg_2[0])
subcirc0.cx(qreg_0[0],qreg_2[1])

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

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_3:
	main_circ.measure(3, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(1, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.ry(-0.858000, 1)
					main_circ.rx(param_3, 2)
					main_circ.append(subcirc0,[0,2,1,qreg_0[0]])
				with case_1(1):
					main_circ.s(0)
					main_circ.cx(1,qreg_0[0])
					main_circ.rx(-0.403000, 2)
					main_circ.rx(-0.626000, 0)
		with case_2(1):
			main_circ.measure(3, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.s(0)
			main_circ.append(subcirc0,[3,qreg_0[0],2,0])
with else_3:
	main_circ.s(1)
	main_circ.measure(2, creg_1[0])
	with main_circ.switch(creg_1[0]) as case_2:
		with case_2(0):
			main_circ.measure(2, creg_1[0])
			with main_circ.if_test((creg_1[0],0)):
				main_circ.ry(param_2, 3)
				main_circ.s(qreg_0[0])
				main_circ.cx(qreg_0[0],3)
				main_circ.append(subcirc0,[0,2,3,qreg_0[0]])
		with case_2(1):
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.ry(-0.130000, 0)
			main_circ.measure(1, creg_0[0])
			with main_circ.if_test((creg_0[0],0)):
				main_circ.rx(param_2, 0)
				main_circ.rx(0.876000, qreg_0[0])
			main_circ.measure(0, creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc0,[0,1,qreg_0[0],3])
				with case_1(1):
					main_circ.cx(qreg_0[0],1)
					main_circ.cx(1,3)
					main_circ.cx(2,0)
					main_circ.barrier(2)
main_circ.rx(0.023000, qreg_0[0])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_3:
	main_circ.cx(0,1)
with else_3:
	main_circ.measure(2, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.rx(param_1, 1)
		main_circ.ry(0.352000, 3)
		main_circ.measure(0, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.cx(0,1)
			main_circ.barrier(qreg_0[0])
	with else_2:
		main_circ.measure(qreg_0[0], creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.barrier(2)
		main_circ.measure(0, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.id(3)
		with else_1:
			main_circ.barrier(2)
		main_circ.measure(1, creg_1[0])
		with main_circ.if_test((creg_1[0],0)):
			main_circ.id(1)
		main_circ.id(0)
bindings = {param_1: -0.245000, param_2: 0.003000, param_3: 0.029000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "256", "CommutativeInverseCancellation")
