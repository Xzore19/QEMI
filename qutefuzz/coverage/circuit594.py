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
subcirc0.z(qreg_3[0])
subcirc0.z(qreg_2[0])
subcirc0.z(qreg_0[0])
subcirc0.ry(-0.114000, qreg_0[1])
subcirc0.h(qreg_0[0])
subcirc0.h(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[1])
subcirc1.h(qreg_0[1])
subcirc1.h(qreg_0[2])
subcirc1.ry(-0.739000, qreg_0[1])
subcirc1.u(0,0,-0.665000, qreg_0[0])
subcirc1.ry(0.577000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc2.add_register(qreg_1)
# Adding creg resources 
subcirc2.u(0,0,-0.856000, qreg_0[0])
subcirc2.h(qreg_1[2])
subcirc2.u(0,0,-0.283000, qreg_1[0])
subcirc2.z(qreg_1[0])
subcirc2.ry(-0.909000, qreg_1[2])
subcirc2.u(0,0,0.323000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(0,0,0.803000, qreg_0[2])
subcirc3.h(qreg_0[2])
subcirc3.ry(-0.536000, qreg_0[2])
subcirc3.u(0,0,-0.441000, qreg_0[2])
subcirc3.u(0,0,0.843000, qreg_0[2])
subcirc3.u(0,0,0.133000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(0.674000, qreg_3[0])
subcirc4.u(0,0,-0.428000, qreg_3[0])
subcirc4.h(qreg_3[0])
subcirc4.u(0,0,0.925000, qreg_3[0])
subcirc4.ry(-0.973000, qreg_0[2])
subcirc4.z(qreg_0[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.ry(-0.779000, 0)
		main_circ.append(subcirc1,[qreg_3[0],qreg_0[1],qreg_2[0],qreg_0[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_2:
	with case_2(0):
		main_circ.measure(qreg_3[0], creg_0[1])
		with main_circ.if_test((creg_0[1],0)) as else_1:
			main_circ.append(subcirc0,[qreg_2[0],0,qreg_0[1],qreg_3[0],qreg_0[0]])
		with else_1:
			main_circ.append(subcirc4,[qreg_0[1],0,qreg_3[0],qreg_2[0]])
	with case_2(1):
		main_circ.measure(qreg_2[0], creg_0[0])
		with main_circ.switch(creg_0[0]) as case_1:
			with case_1(0):
				main_circ.u(param_1,param_1,param_1, qreg_2[0])
				main_circ.h(qreg_2[0])
				main_circ.z(qreg_0[0])
				main_circ.z(qreg_2[0])
			with case_1(1):
				main_circ.z(0)
				main_circ.z(qreg_2[0])
				main_circ.ry(param_1, qreg_3[0])
				main_circ.h(qreg_0[1])
main_circ.append(subcirc4,[qreg_0[1],0,qreg_0[0],qreg_3[0]])
main_circ.append(subcirc3,[qreg_0[0],0,qreg_3[0],qreg_2[0],qreg_0[1]])
main_circ.u(0,param_0,-0.274000, qreg_3[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_2:
	main_circ.z(qreg_0[0])
	main_circ.id(qreg_3[0])
with else_2:
	main_circ.measure(qreg_2[0], creg_0[0])
	with main_circ.if_test((creg_0[0],0)):
		main_circ.barrier(0)
	main_circ.measure(0, creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.z(qreg_3[0])
		main_circ.id(0)
	main_circ.measure(qreg_3[0], creg_0[1])
	with main_circ.if_test((creg_0[1],0)):
		main_circ.z(qreg_3[0])
		main_circ.h(qreg_0[0])
	main_circ.id(qreg_0[0])
main_circ.h(qreg_0[1])
main_circ.u(0,0,-0.373000, qreg_2[0])
bindings = {param_0: 0.790000, param_1: 0.996000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "594", "CollectMultiQBlocks")
