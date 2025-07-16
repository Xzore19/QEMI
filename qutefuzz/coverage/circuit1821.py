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
subcirc0.x(qreg_0[1])
subcirc0.u(pi/2,-0.257000,0.171000, qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_2[0])
subcirc0.cy(qreg_0[1],qreg_3[0])
subcirc0.u(pi/2,0.419000,0.389000, qreg_0[0])
subcirc0.x(qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.x(qreg_0[3])
subcirc1.z(qreg_0[2])
subcirc1.x(qreg_0[3])
subcirc1.z(qreg_0[2])
subcirc1.x(qreg_0[1])
subcirc1.u(pi/2,-0.553000,-0.841000, qreg_0[2])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.x(qreg_0[1])
subcirc2.x(qreg_3[0])
subcirc2.x(qreg_0[2])
subcirc2.z(qreg_0[2])
subcirc2.x(qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc3.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(pi/2,0.023000,0.052000, qreg_2[0])
subcirc3.z(qreg_3[0])
subcirc3.z(qreg_0[0])
subcirc3.cy(qreg_0[1],qreg_3[0])
subcirc3.z(qreg_3[0])
subcirc3.z(qreg_3[0])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.z(qreg_0[0])
subcirc4.cy(qreg_1[1],qreg_0[0])
subcirc4.z(qreg_1[0])
subcirc4.z(qreg_3[0])
subcirc4.u(pi/2,-0.306000,-0.251000, qreg_0[0])
subcirc4.z(qreg_1[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc4,[3,2,qreg_1[0],qreg_0[0],0,1])
	with case_1(1):
		main_circ.append(subcirc2,[1,qreg_0[0],3,qreg_1[0],0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.u(param_0,param_0,param_0, 2)
	main_circ.append(subcirc4,[0,2,qreg_0[0],3,qreg_1[0],1])
main_circ.measure(1, creg_1[0])
with main_circ.switch(creg_1[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc4,[2,1,0,qreg_0[0],qreg_1[0],3])
	with case_1(1):
		main_circ.append(subcirc4,[0,3,2,qreg_0[0],qreg_1[0],1])
main_circ.measure(0, creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_1[0])
with else_1:
	main_circ.barrier(2)
main_circ.measure(1, creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_0[0])
main_circ.measure(0, creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.append(subcirc0,[1,qreg_1[0],0,3,2])
	with case_1(1):
		main_circ.u(pi/2,param_0,param_0, 1)
		main_circ.cy(qreg_1[0],0)
		main_circ.cy(3,qreg_1[0])
		main_circ.cy(3,1)
main_circ.measure(qreg_0[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.cy(1,3)
	main_circ.cy(qreg_1[0],qreg_0[0])
	main_circ.cy(2,qreg_0[0])
	main_circ.cy(2,0)
	main_circ.cy(0,2)
with else_1:
	main_circ.u(pi/2,param_0,param_0, qreg_0[0])
	main_circ.append(subcirc0,[0,qreg_0[0],qreg_1[0],3,2])
bindings = {param_0: -0.404000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "1821", "CXCancellation")
