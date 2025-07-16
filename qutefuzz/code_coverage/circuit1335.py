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
subcirc0.x(qreg_0[2])
subcirc0.ry(-0.359000, qreg_0[1])
subcirc0.x(qreg_0[2])
subcirc0.y(qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

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
subcirc1.y(qreg_0[0])
subcirc1.y(qreg_1[0])
subcirc1.x(qreg_0[0])
subcirc1.ry(0.057000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[1])
subcirc2.x(qreg_0[3])
subcirc2.s(qreg_0[0])
subcirc2.y(qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.x(qreg_1[1])
subcirc3.x(qreg_0[0])
subcirc3.y(qreg_0[0])
subcirc3.s(qreg_1[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.s(qreg_1[0])
subcirc4.ry(0.310000, qreg_1[0])
subcirc4.y(qreg_1[1])
subcirc4.x(qreg_1[2])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(2)
	main_circ.barrier(3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.x(3)
	main_circ.append(subcirc1,[2,1,0,3])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.barrier(3)
	with case_1(1):
		main_circ.append(subcirc1,[1,0,2,3])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.y(1)
	main_circ.append(subcirc1,[3,0,2,1])
with else_1:
	main_circ.y(2)
main_circ.append(subcirc2,[3,0,1,2])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(1)
	with case_1(1):
		main_circ.id(3)
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.ry(param_5, 3)
	main_circ.id(1)
main_circ.measure(3, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.y(0)
		main_circ.barrier(0)
	with case_1(1):
		main_circ.append(subcirc1,[3,2,0,1])
main_circ.ry(-0.304000, 1)
main_circ.y(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(param_5, 2)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(0)
with else_1:
	main_circ.ry(0.322000, 0)
	main_circ.append(subcirc1,[0,2,1,3])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(-0.426000, 2)
	main_circ.ry(-0.344000, 2)
	main_circ.append(subcirc2,[0,1,2,3])
with else_1:
	main_circ.append(subcirc1,[1,0,3,2])
	main_circ.append(subcirc2,[2,1,3,0])
main_circ.s(1)
main_circ.x(1)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(2)
with else_1:
	main_circ.y(1)
	main_circ.id(2)
main_circ.s(0)
main_circ.ry(0.839000, 3)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.x(3)
	main_circ.y(2)
	main_circ.id(1)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.ry(param_5, 2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(0)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(0)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(1)
main_circ.measure(3, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.barrier(3)
main_circ.x(0)
bindings = {param_5: -0.083000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1335", "Collect2qBlocks")
