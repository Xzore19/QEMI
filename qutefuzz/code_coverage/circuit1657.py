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
subcirc0.ry(-0.609000, qreg_2[0])
subcirc0.rx(-0.325000, qreg_2[1])
subcirc0.y(qreg_0[1])
subcirc0.y(qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.526000, qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1.y(qreg_0[0])
subcirc1.z(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[1])
subcirc2.ry(0.674000, qreg_0[1])
subcirc2.ry(0.076000, qreg_0[1])
subcirc2.ry(-0.338000, qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.ry(-0.151000, qreg_0[1])
subcirc3.z(qreg_0[1])
subcirc3.ry(-0.076000, qreg_0[0])
subcirc3.z(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.z(0)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.y(0)
				main_circ.append(subcirc0,[3,1,2,0])
			with case_1(1):
				main_circ.append(subcirc0,[0,2,3,1])
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(0)
		main_circ.measure(3, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.y(0)
				main_circ.ry(param_0, 0)
				main_circ.y(2)
				main_circ.barrier(1)
			with case_1(1):
				main_circ.z(3)
				main_circ.rx(param_0, 3)
				main_circ.barrier(0)
main_circ.rx(param_0, 3)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(1, creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.z(0)
				main_circ.ry(0.729000, 2)
				main_circ.y(3)
				main_circ.id(3)
			with case_1(1):
				main_circ.append(subcirc0,[3,2,1,0])
	with case_2(1):
		main_circ.measure(1, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.append(subcirc1,[3,2,1,0])
			with case_1(1):
				main_circ.z(0)
				main_circ.barrier(0)
main_circ.y(3)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.z(2)
		main_circ.append(subcirc1,[0,1,3,2])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.barrier(2)
		with case_1(1):
			main_circ.append(subcirc0,[2,0,1,3])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(0)
main_circ.rx(0.610000, 2)
main_circ.y(3)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.z(1)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(2, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.barrier(2)
	with else_1:
		main_circ.ry(0.681000, 3)
		main_circ.ry(param_0, 0)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.measure(3, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.rx(-0.954000, 2)
			main_circ.barrier(2)
		with case_1(1):
			main_circ.rx(0.207000, 0)
			main_circ.barrier(0)
	main_circ.id(3)
with else_2:
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)) as else_1:
		main_circ.id(0)
	with else_1:
		main_circ.id(2)
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.barrier(3)
		with case_1(1):
			main_circ.id(3)
	main_circ.measure(1, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.id(1)
	main_circ.measure(2, creg_0[1])
	with main_circ.switch(creg_0[1]) as case_1:
		with case_1(0):
			main_circ.id(3)
		with case_1(1):
			main_circ.barrier(0)
	main_circ.barrier(3)
bindings = {param_0: -0.642000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1657", "RemoveFinalReset")
