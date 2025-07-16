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
subcirc0.ry(-0.795000, qreg_0[0])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.cx(qreg_2[1],qreg_0[1])
subcirc0.ry(-0.511000, qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.h(qreg_3[0])
subcirc1.ry(0.846000, qreg_0[1])
subcirc1.ry(-0.453000, qreg_3[0])
subcirc1.rz(0.023000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.518000, qreg_0[0])
subcirc2.rz(0.788000, qreg_0[2])
subcirc2.ry(-0.070000, qreg_0[0])
subcirc2.ry(0.565000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_3[0],qreg_0[2])
subcirc3.rz(-0.903000, qreg_3[0])
subcirc3.cx(qreg_3[0],qreg_0[1])
subcirc3.ry(-0.571000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.rz(param_0, 1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.ry(param_0, 1)
		main_circ.append(subcirc3,[3,0,2,1])
with else_2:
	main_circ.measure(3, creg_0[0])
	with main_circ.switch(creg_0[0]) as case_1:
		with case_1(0):
			main_circ.rz(-0.692000, 1)
			main_circ.id(1)
		with case_1(1):
			main_circ.ry(-0.996000, 2)
			main_circ.rz(param_0, 3)
			main_circ.h(3)
			main_circ.append(subcirc0,[3,2,0,1])
main_circ.h(0)
main_circ.measure(2, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.cx(1,2)
			main_circ.append(subcirc0,[2,3,0,1])
	with case_2(1):
		main_circ.barrier(2)
main_circ.measure(3, creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.cx(2,3)
		main_circ.measure(3, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(0)
				main_circ.append(subcirc0,[3,2,1,0])
			with case_1(1):
				main_circ.id(2)
	with case_2(1):
		main_circ.measure(0, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.barrier(0)
			with case_1(1):
				main_circ.barrier(3)
		main_circ.measure(2, creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.h(3)
				main_circ.cx(1,2)
				main_circ.cx(1,3)
				main_circ.barrier(2)
			with case_1(1):
				main_circ.barrier(2)
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(0)
		with else_1:
			main_circ.h(2)
			main_circ.barrier(0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_2:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.h(3)
		main_circ.h(3)
		main_circ.id(1)
with else_2:
	main_circ.id(3)
main_circ.measure(3, creg_0[0])
with main_circ.switch(creg_0[0]) as case_2:
	with case_2(0):
		main_circ.measure(3, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.h(3)
			main_circ.id(1)
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.append(subcirc3,[2,0,1,3])
		with else_1:
			main_circ.cx(2,0)
			main_circ.append(subcirc0,[3,0,2,1])
	with case_2(1):
		main_circ.measure(2, creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.ry(0.748000, 2)
			main_circ.append(subcirc0,[1,0,3,2])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_1:
		main_circ.rz(param_0, 3)
		main_circ.rz(-0.745000, 2)
	with else_1:
		main_circ.rz(-0.222000, 2)
		main_circ.ry(0.262000, 2)
		main_circ.cx(3,1)
		main_circ.barrier(1)
bindings = {param_0: -0.878000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1628", "Collect1qRuns")
