from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cx(qreg_0[1],qreg_2[0])
subcirc0.rz(-0.387000, qreg_0[0])
subcirc0.rz(0.057000, qreg_2[0])
subcirc0.rz(0.974000, qreg_2[0])
subcirc0.cx(qreg_2[0],qreg_0[1])
subcirc0.x(qreg_2[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cx(qreg_0[1],qreg_0[0])
subcirc1.rz(-0.540000, qreg_2[0])
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.u(-0.288000,-0.307000,-0.299000, qreg_0[0])
subcirc1.cx(qreg_2[0],qreg_0[1])
subcirc1.rz(-0.545000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(0.615000, qreg_0[0])
subcirc2.cx(qreg_1[1],qreg_3[0])
subcirc2.u(-0.345000,0.990000,0.154000, qreg_1[1])
subcirc2.x(qreg_1[1])
subcirc2.rz(-0.952000, qreg_0[0])
subcirc2.u(-0.069000,0.909000,-0.991000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.cx(qreg_0[1],qreg_0[2])
subcirc3.cx(qreg_3[0],qreg_0[1])
subcirc3.cx(qreg_0[1],qreg_0[0])
subcirc3.cx(qreg_3[0],qreg_0[2])
subcirc3.u(-0.226000,0.267000,-0.475000, qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc4.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cx(qreg_0[0],qreg_0[1])
subcirc4.x(qreg_0[0])
subcirc4.cx(qreg_3[0],qreg_0[1])
subcirc4.rz(0.684000, qreg_0[0])
subcirc4.cx(qreg_0[1],qreg_3[0])
subcirc4.u(-0.981000,-0.409000,0.434000, qreg_2[0])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.rz(-0.577000, qreg_0[1])
	main_circ.append(subcirc3,[qreg_3[0],qreg_2[0],qreg_0[1],qreg_0[0]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.x(qreg_3[0])
		main_circ.u(0.036000,param_0,-0.236000, qreg_3[0])
		main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_2[0],qreg_3[0]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(param_1,param_3,-0.292000, qreg_3[0])
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.rz(param_1, qreg_3[0])
	main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_2[0]])
main_circ.measure(qreg_0[1], creg_0[0])
with main_circ.if_test((creg_0[0],0)) as else_1:
	main_circ.id(qreg_2[0])
with else_1:
	main_circ.barrier(qreg_2[0])
main_circ.measure(qreg_3[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)):
	main_circ.id(qreg_3[0])
main_circ.measure(qreg_0[1], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.barrier(qreg_0[0])
with else_1:
	main_circ.id(qreg_2[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.measure(qreg_3[0], creg_0[0])
with main_circ.switch(creg_0[0]) as case_1:
	with case_1(0):
		main_circ.u(param_2,-0.597000,0.170000, qreg_0[0])
		main_circ.cx(qreg_0[0],qreg_2[0])
		main_circ.barrier(qreg_3[0])
	with case_1(1):
		main_circ.append(subcirc3,[qreg_3[0],qreg_0[1],qreg_2[0],qreg_0[0]])
main_circ.measure(qreg_2[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.rz(param_0, qreg_0[1])
	main_circ.id(qreg_3[0])
with else_1:
	main_circ.rz(param_1, qreg_0[0])
	main_circ.id(qreg_0[0])
main_circ.measure(qreg_0[0], creg_1[0])
with main_circ.if_test((creg_1[0],0)) as else_1:
	main_circ.u(0.204000,0.476000,param_3, qreg_0[1])
	main_circ.barrier(qreg_0[1])
with else_1:
	main_circ.id(qreg_0[0])
bindings = {param_0: 0.323000, param_1: -0.163000, param_2: -0.933000, param_3: -0.367000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_pass_on_simulator(main_circ, "19", "InverseCancellation")
