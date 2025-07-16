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
subcirc0.ry(-0.011000, qreg_0[0])
subcirc0.u(pi/2,-0.034000,0.406000, qreg_0[2])
subcirc0.rz(-0.956000, qreg_0[2])
subcirc0.s(qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(0.322000, qreg_0[0])
subcirc1.rz(-0.744000, qreg_0[1])
subcirc1.s(qreg_0[1])
subcirc1.u(pi/2,-0.464000,-0.614000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(pi/2,-0.600000,-0.173000, qreg_1[0])
subcirc2.ry(0.195000, qreg_3[0])
subcirc2.u(pi/2,0.943000,0.574000, qreg_3[0])
subcirc2.s(qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.254000,-0.772000, qreg_3[0])
subcirc3.ry(0.229000, qreg_0[2])
subcirc3.ry(-0.011000, qreg_0[0])
subcirc3.s(qreg_0[0])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
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

main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_0,-0.264000,param_3, 2)
		main_circ.ry(param_0, 0)
		main_circ.s(3)
		main_circ.rz(-0.623000, qreg_0[0])
	with case_1(1):
		main_circ.append(subcirc2,[3,1,0,qreg_0[0]])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.rz(-0.240000, 3)
	main_circ.ry(0.365000, 0)
with else_1:
	main_circ.append(subcirc2,[qreg_0[0],2,0,3])
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.761000, 2)
		main_circ.append(subcirc1,[qreg_0[0],3,1,0])
	with case_1(1):
		main_circ.append(subcirc0,[2,1,0,3])
main_circ.s(1)
main_circ.measure(1, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc3,[2,qreg_0[0],3,0])
with else_1:
	main_circ.u(pi/2,-0.692000,0.893000, 2)
	main_circ.rz(0.820000, 0)
	main_circ.s(0)
	main_circ.append(subcirc1,[3,1,2,0])
main_circ.measure(1, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(pi/2,param_0,param_2, 1)
		main_circ.ry(param_0, 1)
		main_circ.append(subcirc0,[3,2,0,qreg_0[0]])
	with case_1(1):
		main_circ.ry(param_2, qreg_0[0])
		main_circ.ry(0.065000, qreg_0[0])
		main_circ.append(subcirc0,[3,1,0,qreg_0[0]])
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.u(param_1,param_1,0.454000, qreg_0[0])
main_circ.rz(param_3, 2)
main_circ.measure(2, creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.append(subcirc2,[qreg_0[0],0,2,1])
with else_1:
	main_circ.id(1)
main_circ.s(2)
bindings = {param_0: -0.911000, param_1: 0.748000, param_2: -0.462000, param_3: 0.306000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "934", "HoareOptimizer")
