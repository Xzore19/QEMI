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
subcirc0.rx(-0.224000, qreg_0[0])
subcirc0.rx(-0.472000, qreg_0[1])
subcirc0.cz(qreg_3[0],qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc1.add_register(qreg_1)
# Adding creg resources 
subcirc1.cz(qreg_1[1],qreg_1[2])
subcirc1.z(qreg_1[0])
subcirc1.rx(0.710000, qreg_1[0])
subcirc1.z(qreg_1[0])
subcirc1.cz(qreg_1[1],qreg_1[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(-0.997000, qreg_0[1])
subcirc2.cz(qreg_0[2],qreg_0[0])
subcirc2.cz(qreg_0[0],qreg_0[2])
subcirc2.cz(qreg_0[3],qreg_0[1])
subcirc2.z(qreg_0[3])

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
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc2,[0,3,qreg_0[0],2])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc0,[qreg_0[0],1,2,0,3])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.rx(param_4, 3)
		main_circ.append(subcirc2,[0,3,qreg_0[0],2])
	with case_1(1):
		main_circ.x(3)
		main_circ.rx(0.377000, 3)
		main_circ.z(3)
		main_circ.rx(-0.684000, qreg_0[0])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.z(qreg_0[0])
	main_circ.rx(param_1, 2)
	main_circ.append(subcirc0,[3,1,0,2,qreg_0[0]])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cz(0,2)
	main_circ.z(3)
	main_circ.append(subcirc2,[3,qreg_0[0],0,2])
with else_1:
	main_circ.append(subcirc0,[qreg_0[0],2,0,3,1])
main_circ.append(subcirc2,[1,0,3,2])
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.cz(qreg_0[0],0)
	main_circ.z(2)
	main_circ.cz(qreg_0[0],3)
main_circ.measure(0, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rx(0.913000, 2)
	main_circ.x(2)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.x(0)
	main_circ.z(1)
	main_circ.append(subcirc0,[1,3,0,qreg_0[0],2])
with else_1:
	main_circ.z(2)
	main_circ.id(2)
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.rx(-0.055000, 2)
	main_circ.id(2)
bindings = {param_1: -0.241000, param_4: -0.077000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "484", "OptimizeAnnotated")
