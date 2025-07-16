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
subcirc0.ry(-0.445000, qreg_3[0])
subcirc0.rx(0.246000, qreg_0[1])
subcirc0.cx(qreg_0[2],qreg_0[1])
subcirc0.rz(0.353000, qreg_0[1])
subcirc0.rz(-0.131000, qreg_0[1])
subcirc0.ry(0.996000, qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.ry(-0.763000, qreg_0[3])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.cx(qreg_0[3],qreg_0[0])
subcirc1.ry(-0.977000, qreg_0[0])
subcirc1.cx(qreg_0[2],qreg_0[3])
subcirc1.rz(-0.349000, qreg_0[3])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.967000, qreg_0[1])
subcirc2.cx(qreg_0[2],qreg_0[1])
subcirc2.rz(-0.376000, qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_3[0])
subcirc2.ry(0.478000, qreg_0[0])
subcirc2.ry(-0.379000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.cx(qreg_0[1],qreg_2[1])
subcirc3.ry(-0.089000, qreg_0[1])
subcirc3.rx(0.482000, qreg_2[0])
subcirc3.rz(0.352000, qreg_0[0])
subcirc3.rx(-0.867000, qreg_2[1])
subcirc3.cx(qreg_2[1],qreg_2[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cx(qreg_0[2],qreg_0[0])
subcirc4.cx(qreg_0[1],qreg_0[0])
subcirc4.cx(qreg_0[3],qreg_0[2])
subcirc4.rx(-0.071000, qreg_0[1])
subcirc4.cx(qreg_0[1],qreg_0[3])
subcirc4.rz(0.777000, qreg_0[1])

main_circ = QuantumCircuit(2)
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

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.append(subcirc1,[1,qreg_3[0],qreg_0[0],qreg_0[2]])
with else_1:
	main_circ.id(qreg_0[1])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.ry(0.189000, qreg_0[2])
with else_1:
	main_circ.ry(param_0, 1)
	main_circ.ry(param_0, qreg_3[0])
	main_circ.barrier(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],1,qreg_0[0],0])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.id(qreg_0[2])
	with case_1(1):
		main_circ.append(subcirc4,[qreg_0[1],qreg_3[0],qreg_0[0],0])
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_0[1],0])
main_circ.measure(qreg_0[2], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc4,[0,1,qreg_3[0],qreg_0[2]])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc4,[qreg_0[0],1,qreg_0[2],0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(qreg_3[0])
with else_1:
	main_circ.ry(-0.141000, qreg_3[0])
	main_circ.append(subcirc1,[qreg_0[0],1,0,qreg_0[2]])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.append(subcirc1,[qreg_0[0],qreg_0[1],qreg_3[0],1])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.id(qreg_0[1])
with else_1:
	main_circ.id(1)
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(0)
with else_1:
	main_circ.id(qreg_0[2])
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.ry(param_0, qreg_0[2])
with else_1:
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.cx(1,0)
		main_circ.ry(param_1, 1)
		main_circ.id(qreg_0[2])
	with case_1(1):
		main_circ.barrier(qreg_3[0])
bindings = {param_0: 0.030000, param_1: -0.438000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1943", "ResetAfterMeasureSimplification")
