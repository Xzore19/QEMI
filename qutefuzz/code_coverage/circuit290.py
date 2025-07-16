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
subcirc0.z(qreg_0[0])
subcirc0.cy(qreg_0[0],qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_2[1])
subcirc0.rz(0.691000, qreg_0[0])
subcirc0.rz(-0.563000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(-0.600000, qreg_1[0])
subcirc1.z(qreg_3[0])
subcirc1.rz(-0.301000, qreg_0[0])
subcirc1.cy(qreg_0[0],qreg_3[0])
subcirc1.rz(-0.535000, qreg_2[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(0.679000, qreg_0[3])
subcirc2.ry(0.601000, qreg_0[2])
subcirc2.cy(qreg_0[1],qreg_0[3])
subcirc2.rz(-0.320000, qreg_0[0])
subcirc2.z(qreg_0[3])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.ry(0.097000, qreg_0[1])
subcirc3.cy(qreg_0[1],qreg_0[0])
subcirc3.z(qreg_0[3])
subcirc3.z(qreg_0[2])
subcirc3.rz(0.928000, qreg_0[0])

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

main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.measure(qreg_0[2], creg_0[1])
		with main_circ.switch(creg_0[1]) as case_1:
			with case_1(0):
				main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],qreg_0[2]])
			with case_1(1):
				main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
with else_3:
	main_circ.measure(qreg_0[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.ry(-0.940000, qreg_0[1])
			main_circ.cy(0,qreg_0[2])
			main_circ.append(subcirc3,[qreg_0[1],qreg_3[0],0,qreg_0[0]])
		with else_1:
			main_circ.cy(qreg_0[0],qreg_0[2])
			main_circ.ry(-0.167000, qreg_3[0])
			main_circ.cy(qreg_3[0],qreg_0[0])
			main_circ.z(qreg_0[0])
main_circ.append(subcirc1,[qreg_0[2],qreg_3[0],0,qreg_0[0]])
main_circ.measure(qreg_0[2], creg_0[1])
with main_circ.switch(creg_0[1]) as case_3:
	with case_3(0):
		main_circ.z(qreg_3[0])
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.measure(qreg_0[2], creg_0[1])
			with main_circ.if_test((creg_0[1],0)) as else_1:
				main_circ.rz(param_0, qreg_0[0])
				main_circ.append(subcirc0,[0,qreg_0[0],qreg_0[1],qreg_3[0]])
			with else_1:
				main_circ.barrier(0)
	with case_3(1):
		main_circ.z(qreg_0[1])
		main_circ.measure(qreg_0[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.measure(qreg_0[1], creg_0[0])
			with main_circ.switch(creg_0[0]) as case_1:
				with case_1(0):
					main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
				with case_1(1):
					main_circ.cy(qreg_0[1],qreg_0[2])
					main_circ.cy(qreg_0[1],0)
					main_circ.z(qreg_0[0])
					main_circ.cy(0,qreg_3[0])
main_circ.ry(param_0, qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_3:
	main_circ.measure(0, creg_0[0])
	with main_circ.if_test((creg_0[0],0)) as else_2:
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)) as else_1:
			main_circ.rz(-0.189000, qreg_0[1])
		with else_1:
			main_circ.id(qreg_3[0])
		main_circ.measure(0, creg_0[1])
		with main_circ.if_test((creg_0[1],0)):
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_0[1], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.z(0)
			main_circ.ry(param_0, 0)
			main_circ.rz(param_0, qreg_3[0])
		main_circ.barrier(qreg_0[2])
	with else_2:
		main_circ.measure(qreg_0[2], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.ry(-0.449000, 0)
			main_circ.id(qreg_3[0])
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.id(qreg_3[0])
		with else_1:
			main_circ.id(0)
		main_circ.measure(qreg_3[0], creg_0[0])
		with main_circ.if_test((creg_0[0],0)):
			main_circ.id(qreg_0[2])
		main_circ.id(qreg_0[1])
with else_3:
	main_circ.id(0)
bindings = {param_0: 0.929000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "290")
