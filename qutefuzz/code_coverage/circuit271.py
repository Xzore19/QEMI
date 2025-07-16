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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.y(qreg_0[2])
subcirc0.cy(qreg_0[1],qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(0.530000, qreg_0[1])
subcirc1.cy(qreg_0[3],qreg_0[2])
subcirc1.cy(qreg_0[2],qreg_0[0])
subcirc1.y(qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cy(qreg_0[3],qreg_0[2])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.cx(qreg_0[0],qreg_0[3])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_3[0])
subcirc3.ry(-0.259000, qreg_0[2])
subcirc3.ry(-0.965000, qreg_3[0])
subcirc3.ry(-0.104000, qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cx(qreg_3[0],qreg_2[0])
subcirc4.cy(qreg_2[0],qreg_0[0])
subcirc4.cy(qreg_3[0],qreg_0[0])
subcirc4.cy(qreg_2[0],qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

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
param_4 = Parameter("param_4")

main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.cx(qreg_3[0],qreg_0[2])
	main_circ.cx(0,qreg_0[1])
	main_circ.y(qreg_3[0])
	main_circ.append(subcirc3,[qreg_0[2],qreg_0[0],0,qreg_3[0]])
with else_1:
	main_circ.cx(0,qreg_0[2])
	main_circ.y(qreg_3[0])
	main_circ.id(0)
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cx(qreg_3[0],qreg_0[2])
	main_circ.cx(qreg_0[2],qreg_0[1])
	main_circ.append(subcirc3,[qreg_3[0],qreg_0[0],qreg_0[1],0])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cx(0,qreg_0[2])
	main_circ.cx(qreg_3[0],qreg_0[1])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc1,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1],0])
	main_circ.append(subcirc3,[qreg_0[2],qreg_3[0],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_0[2], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc4,[qreg_0[2],0,qreg_0[0],qreg_3[0],qreg_0[1]])
	with case_1(1):
		main_circ.cy(qreg_3[0],qreg_0[1])
		main_circ.ry(-0.504000, qreg_0[1])
		main_circ.y(qreg_3[0])
		main_circ.id(0)
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.y(qreg_0[1])
	main_circ.append(subcirc1,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0],0])
main_circ.measure(0, creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.cy(qreg_3[0],qreg_0[2])
	main_circ.y(qreg_0[1])
	main_circ.cx(qreg_0[2],qreg_0[1])
	main_circ.cy(0,qreg_0[0])
	main_circ.barrier(qreg_0[2])
main_circ.y(qreg_3[0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "271", "OptimizeCliffords")
