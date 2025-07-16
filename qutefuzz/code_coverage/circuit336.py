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
subcirc0.ry(0.895000, qreg_0[1])
subcirc0.ry(-0.709000, qreg_0[1])
subcirc0.u(pi/2,0.685000,0.622000, qreg_0[1])
subcirc0.rx(-0.914000, qreg_0[0])
subcirc0.rx(0.218000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[2])
subcirc1.ry(-0.376000, qreg_0[2])
subcirc1.z(qreg_0[1])
subcirc1.rx(0.684000, qreg_0[2])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.z(qreg_0[1])
subcirc2.u(pi/2,-0.398000,-0.928000, qreg_3[0])
subcirc2.z(qreg_0[2])
subcirc2.ry(0.058000, qreg_0[1])
subcirc2.u(pi/2,-0.839000,-0.686000, qreg_0[1])
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
subcirc3.u(pi/2,-0.116000,0.671000, qreg_0[0])
subcirc3.u(pi/2,-0.414000,0.245000, qreg_0[0])
subcirc3.rx(-0.344000, qreg_3[0])
subcirc3.rx(-0.833000, qreg_0[0])
subcirc3.ry(-0.543000, qreg_2[0])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.z(qreg_1[0])
subcirc4.u(pi/2,0.173000,0.983000, qreg_0[0])
subcirc4.ry(-0.157000, qreg_0[0])
subcirc4.ry(0.672000, qreg_1[2])
subcirc4.z(qreg_1[2])

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.measure(qreg_1[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.append(subcirc2,[0,qreg_1[0],qreg_3[0],qreg_0[0],qreg_1[1]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.if_test((creg_0[0],0)):
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_1[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.ry(0.959000, 0)
		main_circ.rx(param_0, qreg_1[1])
		main_circ.z(qreg_3[0])
		main_circ.append(subcirc1,[0,qreg_1[0],qreg_3[0],qreg_0[0]])
	with case_1(1):
		main_circ.id(qreg_1[1])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.z(qreg_3[0])
	main_circ.append(subcirc1,[0,qreg_0[0],qreg_1[1],qreg_3[0]])
with else_1:
	main_circ.z(qreg_0[0])
	main_circ.barrier(qreg_0[0])
main_circ.measure(0, creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc2,[0,qreg_1[0],qreg_0[0],qreg_3[0],qreg_1[1]])
	with case_1(1):
		main_circ.barrier(qreg_1[0])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.u(param_4,0.653000,-0.007000, 0)
		main_circ.z(0)
		main_circ.id(0)
	with case_1(1):
		main_circ.id(qreg_1[0])
main_circ.u(pi/2,0.986000,-0.263000, qreg_3[0])
main_circ.u(pi/2,param_0,-0.941000, qreg_1[0])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.switch(creg_0[1]) as case_1:
	with case_1(0):
		main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],qreg_0[0],0])
	with case_1(1):
		main_circ.append(subcirc4,[qreg_3[0],0,qreg_0[0],qreg_1[0]])
main_circ.measure(qreg_0[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)) as else_1:
	main_circ.barrier(0)
with else_1:
	main_circ.u(param_3,0.178000,0.522000, qreg_1[1])
	main_circ.rx(1.000000, qreg_1[1])
	main_circ.append(subcirc2,[qreg_1[0],0,qreg_1[1],qreg_3[0],qreg_0[0]])
main_circ.measure(qreg_3[0], creg_0[1])
with main_circ.if_test((creg_0[1],0)):
	main_circ.z(0)
	main_circ.id(0)
bindings = {param_0: -0.079000, param_3: -0.483000, param_4: -0.295000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_on_simulator(main_circ, "336")
