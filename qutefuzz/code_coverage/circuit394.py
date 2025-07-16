from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc0.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.z(qreg_1[1])
subcirc0.rz(0.817000, qreg_1[0])
subcirc0.cx(qreg_0[0],qreg_1[1])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc1.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.076000, qreg_0[0])
subcirc1.x(qreg_1[1])
subcirc1.cx(qreg_1[0],qreg_1[1])
subcirc1.cx(qreg_3[0],qreg_1[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rz(0.624000, qreg_0[1])
subcirc2.x(qreg_0[1])
subcirc2.z(qreg_0[3])
subcirc2.x(qreg_0[0])
subcirc2 = subcirc2.to_gate().control(1)

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

main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(3)
with else_1:
	main_circ.append(subcirc0,[2,qreg_0[0],0,3])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rz(param_0, qreg_0[0])
	main_circ.x(qreg_0[0])
main_circ.x(3)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc2,[2,qreg_0[0],3,0,1])
with else_1:
	main_circ.barrier(3)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rz(-0.148000, qreg_0[0])
	main_circ.rz(param_3, 3)
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cx(1,3)
	main_circ.z(0)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(-0.900000, 0)
	main_circ.cx(qreg_0[0],2)
with else_1:
	main_circ.rz(0.781000, 3)
	main_circ.x(1)
	main_circ.rz(param_1, 3)
	main_circ.append(subcirc2,[3,1,2,0,qreg_0[0]])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.rz(-0.394000, 1)
	main_circ.id(2)
with else_1:
	main_circ.append(subcirc0,[qreg_0[0],2,0,1])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.cx(2,1)
	main_circ.cx(3,0)
	main_circ.cx(0,1)
	main_circ.cx(1,qreg_0[0])
with else_1:
	main_circ.cx(qreg_0[0],3)
	main_circ.cx(qreg_0[0],3)
	main_circ.cx(1,0)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cx(3,qreg_0[0])
	main_circ.append(subcirc0,[0,qreg_0[0],2,3])
with else_1:
	main_circ.id(3)
bindings = {param_0: -0.156000, param_1: 0.754000, param_3: -0.986000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "394", "ConsolidateBlocks")
