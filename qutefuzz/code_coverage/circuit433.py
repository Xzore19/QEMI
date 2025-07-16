from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.u(0,0,0.397000, qreg_0[0])
subcirc0.rz(0.750000, qreg_0[3])
subcirc0.rz(0.952000, qreg_0[2])
subcirc0.z(qreg_0[1])
subcirc0.rz(0.472000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cy(qreg_0[2],qreg_0[3])
subcirc1.z(qreg_0[0])
subcirc1.z(qreg_0[2])
subcirc1.u(0,0,0.343000, qreg_0[2])
subcirc1.rz(-0.288000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cy(qreg_0[0],qreg_0[3])
subcirc2.cy(qreg_0[0],qreg_0[2])
subcirc2.rz(-0.446000, qreg_0[0])
subcirc2.cy(qreg_0[1],qreg_0[0])
subcirc2.rz(0.099000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc3.add_register(qreg_1)
# Adding creg resources 
subcirc3.u(0,0,-0.527000, qreg_1[0])
subcirc3.u(0,0,0.817000, qreg_1[2])
subcirc3.rz(0.612000, qreg_1[2])
subcirc3.u(0,0,-0.624000, qreg_1[1])
subcirc3.u(0,0,-0.126000, qreg_1[2])
subcirc3 = subcirc3.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.u(param_0,param_1,-0.649000, 3)
	main_circ.append(subcirc0,[3,1,2,0])
with else_1:
	main_circ.append(subcirc1,[2,1,0,3])
main_circ.measure(2, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(0,param_0,param_1, 0)
		main_circ.barrier(1)
	with case_1(1):
		main_circ.rz(-0.549000, 2)
		main_circ.rz(param_1, 2)
		main_circ.append(subcirc0,[3,1,0,2])
main_circ.measure(2, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.append(subcirc2,[3,2,1,0])
with else_1:
	main_circ.append(subcirc2,[2,3,1,0])
main_circ.u(param_0,0,param_0, 0)
main_circ.measure(1, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.barrier(3)
	with case_1(1):
		main_circ.cy(2,0)
		main_circ.append(subcirc1,[0,1,3,2])
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.append(subcirc0,[1,2,3,0])
main_circ.measure(3, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(0,3)
main_circ.cy(3,1)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.cy(0,3)
	main_circ.cy(2,1)
	main_circ.cy(3,1)
	main_circ.cy(1,0)
	main_circ.cy(0,1)
main_circ.measure(1, creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.barrier(2)
main_circ.measure(2, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[0,2,3,1])
main_circ.rz(0.276000, 2)
main_circ.measure(3, creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.u(0,0,0.101000, 0)
	main_circ.u(param_1,0,param_0, 1)
	main_circ.barrier(2)
with else_1:
	main_circ.barrier(0)
bindings = {param_0: -0.001000, param_1: -0.385000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "433", "OptimizeCliffords")
