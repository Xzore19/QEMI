from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.s(qreg_2[0])
subcirc0.s(qreg_3[0])
subcirc0.ry(0.020000, qreg_2[0])
subcirc0.ry(-0.776000, qreg_1[0])
subcirc0.y(qreg_3[0])
subcirc0.rx(-0.048000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.ry(0.198000, qreg_0[0])
subcirc1.y(qreg_1[0])
subcirc1.rx(0.652000, qreg_1[2])
subcirc1.s(qreg_0[0])
subcirc1.ry(0.483000, qreg_1[2])
subcirc1.ry(-0.735000, qreg_1[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.y(qreg_0[0])
subcirc2.s(qreg_0[1])
subcirc2.y(qreg_0[0])
subcirc2.s(qreg_0[1])
subcirc2.s(qreg_0[1])
subcirc2.y(qreg_0[3])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_0[0])
subcirc3.rx(-0.450000, qreg_0[0])
subcirc3.s(qreg_0[2])
subcirc3.s(qreg_0[2])
subcirc3.y(qreg_0[0])
subcirc3.y(qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.y(qreg_0[1])
subcirc4.rx(0.427000, qreg_3[0])
subcirc4.ry(0.706000, qreg_0[2])
subcirc4.y(qreg_0[0])
subcirc4.s(qreg_3[0])
subcirc4.ry(-0.961000, qreg_0[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(1)
with else_1:
	main_circ.id(3)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(1)
with else_1:
	main_circ.barrier(0)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(1)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.y(0)
		main_circ.rx(param_1, 1)
		main_circ.append(subcirc2,[2,3,1,0])
	with case_1(1):
		main_circ.id(3)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.ry(param_0, 2)
	main_circ.barrier(2)
with else_1:
	main_circ.rx(param_1, 3)
	main_circ.s(3)
	main_circ.y(2)
	main_circ.append(subcirc2,[2,3,1,0])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.id(1)
	with case_1(1):
		main_circ.id(3)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.id(1)
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[1,0,2,3])
	with case_1(1):
		main_circ.ry(param_0, 2)
		main_circ.id(3)
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(2)
	with case_1(1):
		main_circ.s(3)
		main_circ.append(subcirc2,[2,3,1,0])
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.s(1)
	main_circ.y(0)
	main_circ.y(3)
	main_circ.id(0)
with else_1:
	main_circ.barrier(2)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(2)
with else_1:
	main_circ.rx(param_0, 3)
	main_circ.s(0)
	main_circ.id(0)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(3)
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(2)
with else_1:
	main_circ.y(0)
	main_circ.barrier(0)
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.barrier(2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.y(3)
	main_circ.append(subcirc2,[0,2,3,1])
with else_1:
	main_circ.rx(param_0, 2)
	main_circ.barrier(0)
bindings = {param_0: 0.141000, param_1: 0.138000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "265")
